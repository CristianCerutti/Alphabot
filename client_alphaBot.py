#client pc, robot server, robot che si muove
#w "muove sopra", s "muove indietro", d "muove a destra", a "muove a"
import socket as sck

s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
s.connect(('192.168.0.126', 24000))
while True:
    istruzione = input("inserire un comando: ") #comando,durata
    s.sendall(istruzione.encode())
s.close()