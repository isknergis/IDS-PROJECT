from scapy.all import sniff, IP, TCP

def paket_yakala(paket):
    if paket.haslayer(IP) and paket.haslayer(TCP):
        print(f"IP: {paket[IP].src} → {paket[IP].dst}, Port: {paket[TCP].dport}")

print("IDS başlatıldı...")
sniff(filter="tcp", prn=paket_yakala, store=False)
