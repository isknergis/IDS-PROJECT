fetch("/logs")
    .then(response => response.json())
    .then(data => {
        let table = document.getElementById("log-table");
        data.forEach(log => {
            let row = `<tr><td>${log.ip}</td><td>${log.status}</td></tr>`;
            table.innerHTML += row;
        });
    });
