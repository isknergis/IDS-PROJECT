from scapy.all import IP,TCP

def detec_anomaly(paket):
	if paket.haslayer(TCP):
		tcp_layer=paket[TCP]
		if tcp_layer.flags=="S": #sadece SYN varsa
			print(f"[ALERT] SYN taraması tespit edildi! IP: {paket[IP].src}")

#[ALERT], uyarı vermek için kullanılan bir metin ifadesidir. Genellikle şüpheli veya anormal bir durum olduğunda ekrana yazdırılır.
