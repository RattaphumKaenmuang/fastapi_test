const URL = "http://127.0.0.1:8000"

async function makeAPICall() {
    const result = await fetch(URL);
    result.json().then(data => {
        console.log(data);

        var table = document.createElement('table');

        // Create table header
        var thead = document.createElement('thead');
        var headerRow = document.createElement('tr');
        ['Name', 'Age'].forEach(headerText => {
            var th = document.createElement('th');
            th.appendChild(document.createTextNode(headerText));
            headerRow.appendChild(th);
        });
        thead.appendChild(headerRow);
        table.appendChild(thead);

        // Create table body
        var tbody = document.createElement('tbody');
        data.forEach(student => {
            var row = document.createElement('tr');
            [student.name, student.age].forEach(text => {
                var td = document.createElement('td');
                td.appendChild(document.createTextNode(text));
                row.appendChild(td);
            });
            tbody.appendChild(row);
        });
        table.appendChild(tbody);

        // Append the table to the document body
        document.body.appendChild(table);
    })
}

makeAPICall();