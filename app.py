from flask import Flask, request, render_template, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    model = data['model']
    properties = data['properties']
    constants = data['constants']

    # Escrever o modelo em um arquivo
    model_file = 'prism.pm'
    with open(model_file, 'w') as f:
        f.write(model)

    # Escrever as propriedades em um arquivo separado
    properties_file = 'properties.pctl'
    with open(properties_file, 'w') as f:
        f.write(properties)

    # Caminho completo para o executável do PRISM
    prism_executable = "C:\Program Files\prism-4.8.1\bin\prism.bat"
    command = f'"{prism_executable}" {model_file} {properties_file} -sim -const {constants}'

    try:
        # Executar o comando PRISM
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        
        # Verificar se há erros
        if result.returncode != 0:
            response = {'error': result.stderr}
        else:
            response = {'result': result.stdout}

    except Exception as e:
        response = {'error': str(e)}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
