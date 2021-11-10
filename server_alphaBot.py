import socket as sck
import AlphaBot
import time
#import threading
import sqlite3
s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
s.bind(('0.0.0.0', 24000))
s.listen()
conn, addr = s.accept()
bot = AlphaBot.AlphaBot()
con = sqlite3.connect("db_movimenti.db")
cur = con.cursor()
#SE DA ERRORE RIMETTERE CAST A INT NELLA CLASSE ALPHABOT
while True:  
    mess = conn.recv(4096).decode()
    cont = -1
    for row in cur.execute("SELECT * FROM movimento").fetchall():
        if row[0] == mess:
            lista_comandi = row[1].split(",") 
    print(lista_comandi)   
    for comando in lista_comandi:  #["w", 3, "s", 5]
        cont += 1
        if comando == "w":
            bot.time_forward(lista_comandi[cont+1])
            print("avanti")
        if comando.lower() == "s":
            bot.time_backward(lista_comandi[cont+1])
            print("indietro")
        if comando.lower() == "d":
            bot.time_right(lista_comandi[cont+1])
            print("destra")
        if comando.lower() == "a":
            bot.time_left(lista_comandi[cont+1])
            print("sinistra")
s.close()
con.close()