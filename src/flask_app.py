from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # 📌 Bu satır ana sayfayı gösterecek!

@app.route("/logs")
def get_logs():
    logs = [
        {"ip": "192.168.1.15", "status": "Suspicious"},
        {"ip": "10.0.0.5", "status": "Normal"},
    ]
    return jsonify(logs)

if __name__ == "__main__":
    app.run(debug=True)
