import socket as sck
import AlphaBot
import time
import threading
#select sequenza from movimento where movimento = "movimentoricevuto"
#destra indietro, sinistra avanti, avanti sinistra, indietro destra
s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
s.bind(('0.0.0.0', 10000))
s.listen()
conn, addr = s.accept()
bot = AlphaBot.AlphaBot()
while True:  
    mess = conn.recv(4096).decode()
    if mess.lower() != "f":
        lista_comandi = mess.split(",")
        comando = lista_comandi[0]
        durata = lista_comandi[1]
    if comando.lower() == "w":
        #x = threading.Thread(bot.time_forward(durata))
        #x.start()
        if mess == "f":
            bot.stop()
            #x.join()
        print("avanti")
    if comando.lower() == "s":
        print("indietro")
        bot.time_backward(durata)
    if comando.lower() == "d":
        print("destra")
        bot.time_right(durata)
    if comando.lower() == "a":
        print("sinistra")
        bot.time_left(durata)  
    if comando.lower() == "f":
        print("fermo")
        bot.stop()
s.close()