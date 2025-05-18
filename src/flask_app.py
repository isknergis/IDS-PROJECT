from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
import time
import threading  # 📌 Çoklu işlem desteği ekliyoruz!

app = Flask(__name__)
socketio = SocketIO(app)  # 📌 WebSocket desteğini aktif ediyoruz!

@app.route("/")
def index():
    return render_template("index.html")  # 📌 Ana sayfayı çağırıyoruz

@app.route("/logs")
def get_logs():
    logs = [
        {"ip": "192.168.1.15", "status": "Suspicious"},
        {"ip": "10.0.0.5", "status": "Normal"},
    ]
    return jsonify(logs)

# 📌 Gerçek zamanlı logları gönderme fonksiyonu
def send_live_logs():
    count = 1
    while True:
        log_data = {"ip": f"192.168.1.{count}", "status": "Suspicious" if count % 2 == 0 else "Normal"}
        print(f"Emitting log: {log_data}")  # ✅ Terminalde logları görebileceğiz!
        socketio.emit("new_log", log_data)  # 🔗 Yeni logu WebSocket üzerinden gönderiyoruz!
        count += 1
        time.sleep(5)  # ⏳ Her 5 saniyede bir yeni log yolluyoruz

if __name__ == "__main__":
    threading.Thread(target=send_live_logs).start()  # 🚀 Log fonksiyonunu başlatıyoruz!
    socketio.run(app, debug=True)  # 📌 Flask-SocketIO başlatılıyor!
