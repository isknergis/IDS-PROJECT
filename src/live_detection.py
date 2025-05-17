import pandas as pd 
import pickle
from scapy.all import sniff, IP, TCP

# Modeli yükle
with open("ids_model.pkl", "rb") as f:
    model = pickle.load(f)

def detect_anomaly(paket):
    if paket.haslayer(IP) and paket.haslayer(TCP):
        data = pd.DataFrame([{ 
            "dst_port": paket[TCP].dport, 
            "syn_flag": 1 if paket[TCP].flags == 'S' else 0 
        }])

        prediction = model.predict(data)

        # 🌟 Tahmin sonucunu ekrana yazdıralım:
        print(f"Prediction sonucu: {prediction[0]}, IP: {paket[IP].src}")

        if prediction[0] == -1:  # Anormal trafikse
            print(f"[ALERT] Şüpheli trafik tespit edildi! IP: {paket[IP].src}")

sniff(filter="tcp", prn=detect_anomaly, store=False)
