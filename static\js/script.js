document.getElementById('modelForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const model = document.getElementById('model').value;
    const properties = document.getElementById('properties').value;
    const constants = document.getElementById('constants').value;
    
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
            document.getElementById('result').textContent = 'Error: ' + data.error;
        } else {
            document.getElementById('result').textContent = data.result;
        }
    })
    .catch(error => console.error('Error:', error));
});
