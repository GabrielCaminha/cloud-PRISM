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
    
    return returned_value
