import os

def run_prism(model, properties, constants):
    prism_dir = "C:/Program Files/prism-4.8.1/bin"
    prism_model_file = "C:/prismtest/prism.pm"
    properties_file = "C:/prismtest/properties.pctl"
    
    # Escrever arquivos de modelo e propriedades
    with open(prism_model_file, "w") as file:
        file.write(model)
    
    with open(properties_file, "w") as file:
        file.write(properties)
    
    # Executar PRISM com os arquivos gerados
    os.chdir(prism_dir)
    command = f"prism {prism_model_file} {properties_file} -sim -const {constants}"
    returned_value = os.popen(command).read()
    
    return format_prism_output(returned_value)

def format_prism_output(output):
    result = {}
    lines = output.split('\n')
    result['header'] = lines[0]
    result['version'] = lines[1]
    result['date'] = lines[2]
    result['hostname'] = lines[3]
    result['memory_limits'] = lines[4]
    result['command_line'] = lines[5]
    
    parsing_model_index = output.index("Parsing model file")
    result['model_file'] = output[parsing_model_index:parsing_model_index + 100]  # ajuste o comprimento conforme necessário

    parsing_properties_index = output.index("Parsing properties file")
    result['properties_file'] = output[parsing_properties_index:parsing_properties_index + 100]  # ajuste o comprimento conforme necessário

    result['simulation'] = output[output.index("Simulating"):]

    return result
