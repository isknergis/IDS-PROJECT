from scapy.all import IP, TCP, ICMP,ARP

def analyze_packet(paket):
	if paket.haslayer(IP):
		print(f"Kaynak IP: {paket[IP].src},Hedef IP: {paket[IP].dst}") # hedef IP -> paketin hangi cihaza yönlendirildiğini gösterir.
		
	if paket.haslayer(TCP):
		print(f"TCP Port : {paket[TCP].dport}") #hedef port()Destination port-> Bir paketin hangi servise veya uygulamaya gitmesi gerektiğini gösterir.
	if paket.haslayer(ARP): # ARP paketlerindeki hedef IP yi belirtir. Paketin hedeflediği ağ cihazını bulmak için kullanılır.
		print(f"ARP isteği : {paket[ARP].psrc} -> {paket[ARP].pdst}")
	if paket.haslayer(ICMP):#Ping vb mesaj türünü belirtir. ICMP-> Hata raporlama ve ağ iletişimi için kullanılan protokol. TCP veya UDP gibi veri taşımaz. Ağda bağlantı sorunlarını teşhis etmek ve yönlendirme bilgilerini sağlamak için kullanılır.
		print(f"ICMP paketi : {paket[ICMP].type}")


#Scapy’de / işareti, katmanları birleştirmek için kullanılır. Bir ağ paketinde farklı protokol katmanlarını üst üste eklemek için kullanılır.
#paket = Ether() / IP(dst="192.168.1.1") / TCP(dport=443) / Raw(load="Merhaba!")
