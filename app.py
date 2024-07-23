from flask import Flask, request, render_template, jsonify
import test_run_prism

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    input_data = request.json
    
    model = input_data.get("model")
    properties = input_data.get("properties")
    constants = input_data.get("constants")
    
    result = test_run_prism.run_prism(model, properties, constants)
    
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
