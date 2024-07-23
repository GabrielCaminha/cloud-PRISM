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
        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = `
            <h2>PRISM Result</h2>
            <p><strong>Header:</strong> ${data.result.header}</p>
            <p><strong>Version:</strong> ${data.result.version}</p>
            <p><strong>Date:</strong> ${data.result.date}</p>
            <p><strong>Hostname:</strong> ${data.result.hostname}</p>
            <p><strong>Memory Limits:</strong> ${data.result.memory_limits}</p>
            <p><strong>Command Line:</strong> ${data.result.command_line}</p>
            <h3>Model File</h3>
            <pre>${data.result.model_file}</pre>
            <h3>Properties File</h3>
            <pre>${data.result.properties_file}</pre>
            <h3>Simulation</h3>
            <pre>${data.result.simulation}</pre>
        `;
    })
    .catch(error => console.error('Error:', error));
});
