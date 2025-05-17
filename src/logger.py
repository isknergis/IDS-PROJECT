import datetime
def logla(mesaj):

	zaman=datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
	with open ("ids_log.txt", "a") as dosya
:
		dosya.write(f"{zaman} {mesaj}\n")
