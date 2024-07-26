var darkmode = true
function run(){
    const model = editormodel.getValue()
    const properties = editorprop.getValue()
    const constants = document.getElementById("constants").value

    const data = {
        model: model,
        properties: properties,
        constants: constants
    };

    fetch('/process', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            editorterminal.setValue('Error: ' + data.error);
        } else {
            editorterminal.setValue(data.result)
        }
    })
    .catch(error => console.error('Error:', error));
}

function downloadFile(model){
    var text = model ? editormodel.getValue(): editorprop.getValue()
    var filename = model ? "model.pm": "properties.pctl"
    var blob = new Blob([text], {type: "text/plain;charset=utf-8"})
    saveAs(blob, filename)
}

function changeMode(){
    if(darkmode){
        editormodel.setTheme("ace/theme/clouds")
        editorprop.setTheme("ace/theme/clouds")
        document.body.style.backgroundColor = "white"
        document.getElementById("constantsLabel").style.color = "black"
        document.getElementById("buttonmode").innerText = "Dark Mode"
    }
    else{
        editormodel.setTheme("ace/theme/dracula");
        editorprop.setTheme("ace/theme/dracula");
        document.body.style.backgroundColor = "#282a36"
        document.getElementById("constantsLabel").style.color = "white"
        document.getElementById("buttonmode").innerText = "Light Mode"
    }

    darkmode = !darkmode
}