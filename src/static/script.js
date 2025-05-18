var ctx = document.getElementById("logChart").getContext("2d");
var logChart = new Chart(ctx, {
    type: "line",
    data: {
        labels: [],
        datasets: [{
            label: "Şüpheli Aktivite",
            borderColor: "red",
            backgroundColor: "rgba(255, 0, 0, 0.2)",
            data: [],
        }]
    },
    options: {
        responsive: true,
    }
});

// 📌 WebSocket bağlantısını başlat
var socket = io("http://127.0.0.1:5000");

// 📌 WebSocket bağlanınca mesaj ver
socket.on("connect", function() {
    console.log("Sunucuya başarıyla bağlandı!");
});

// 📌 Bağlantı koparsa otomatik tekrar bağlan
socket.on("disconnect", function() {
    console.log("Bağlantı koptu, yeniden bağlanıyor...");
    setTimeout(() => {
        socket.connect();
    }, 3000);
});

// 📌 Yeni log geldiğinde tabloyu ve grafiği güncelle
socket.on("new_log", function(data) {
    console.log("Yeni log alındı!", data);

    let now = new Date().toLocaleTimeString();
    let table = document.getElementById("log-table");
    let row = `<tr><td>${data.ip}</td><td>${data.status}</td><td>${now}</td></tr>`;
    table.innerHTML += row;

    logChart.data.labels.push(now);
    logChart.data.datasets[0].data.push(data.status === "Suspicious" ? 1 : 0);
    logChart.update();
});
