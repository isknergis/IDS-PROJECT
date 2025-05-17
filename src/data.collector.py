import pandas as pd
from scapy.all import sniff, IP, TCP

data_list = []

def collect_data(paket):
    if paket.haslayer(IP) and paket.haslayer(TCP):
        data_list.append({
            "src_ip": paket[IP].src,
            "dst_ip": paket[IP].dst,
            "dst_port": paket[TCP].dport,
            "syn_flag": 1 if paket[TCP].flags == 'S' else 0
        })

        if len(data_list) >= 10:  # Veri setini oluştur
            df = pd.DataFrame(data_list)
            df.to_csv("network_data.csv", index=False)
            print("Veri seti kaydedildi!")
            data_list.clear()

sniff(filter="tcp", prn=collect_data, store=False)
