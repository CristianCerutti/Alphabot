import requests
import time as tempo_time
#/api/v1/motors/left?pwm=x&time=t
#/api/v1/motors/right?pwm=y&time=t
#/api/v1/motors/both?pwmL=x&pwmR=y&time=t
def main():
    try:
        while True:
            tempo_time.sleep(0.3) #tempo per evitare che vada troppo veloce
            r = requests.get('http://192.168.0.129:5000/api/v1/sensors/obstacles')  
            r = r.json()
            destra = r["right"] #1 c'è 0 non c'è
            sinistra = r["left"]

            while int(destra) == 0 and int(sinistra) == 0: #non ci sono ostacoli, quindi va diritto
                r = requests.get('http://192.168.0.129:5000/api/v1/sensors/obstacles')  
                r = r.json()
                destra = r["right"] #1 c'è 0 non c'è
                sinistra = r["left"]
                pwmL = 36 #la sinistra va un po più veloce della destra perché il nostro alphabot pendeva a destra
                pwmR = 35
                time = 0.2
                r = requests.get(f'http://192.168.0.129:5000/api/v1/motors/both?pwmL={pwmL}&time={time}&pwmR={pwmR}')

            while int(destra) == 0 and int(sinistra) == 1:  #ostacolo sulla sinistra
                r = requests.get('http://192.168.0.129:5000/api/v1/sensors/obstacles')  
                r = r.json()
                destra = r["right"] #1 c'è 0 non c'è
                sinistra = r["left"]
                pwmL = 33
                pwmR = 0
                time = 0.3
                r = requests.get(f'http://192.168.0.129:5000/api/v1/motors/both?pwmL={pwmL}&time={time}&pwmR={pwmR}')

            while int(destra) == 1 and int(sinistra) == 0: #ostacolo sulla destra
                r = requests.get('http://192.168.0.129:5000/api/v1/sensors/obstacles')  
                r = r.json()
                destra = r["right"] #1 c'è 0 non c'è
                sinistra = r["left"]
                pwmL = 0
                pwmR = 33
                time = 0.3
                r = requests.get(f'http://192.168.0.129:5000/api/v1/motors/both?pwmL={pwmL}&time={time}&pwmR={pwmR}')
            
            while int(destra) == 1 and int(sinistra) == 1: #ha un ostacolo davanti a se
                r = requests.get('http://192.168.0.129:5000/api/v1/sensors/obstacles')  
                r = r.json()
                destra = r["right"] #1 c'è 0 non c'è
                sinistra = r["left"]
                pwmL = 31
                pwmR = 0
                time = 0.3  
                r = requests.get(f'http://192.168.0.129:5000/api/v1/motors/both?pwmL={pwmL}&time={time}&pwmR={pwmR}') #va prima adestra
                time = 0.3
                pwm = 33
                r = requests.get(f'http://192.168.0.129:5000/api/v1/motors/back?pwm={pwm}&time={time}') #va indietro
                r = requests.get('http://192.168.0.129:5000/api/v1/sensors/obstacles')  
                r = r.json()
                destra = r["right"] #1 c'è 0 non c'è
                sinistra = r["left"]

                if int(destra) == 0 and int(sinistra) == 0: #se non trova ostacoli può continuare ad andare diritto
                    break;
                    
                elif int(destra) == 1 and int(sinistra) == 1: #se c'è ancora un ostacolo significa che deve girarsi dall'altra parte
                    r = requests.get('http://192.168.0.129:5000/api/v1/sensors/obstacles')  
                    r = r.json()
                    destra = r["right"] #1 c'è 0 non c'è
                    sinistra = r["left"]
                    pwmL = 0
                    pwmR = 33
                    time = 0.8
                    r = requests.get(f'http://192.168.0.129:5000/api/v1/motors/both?pwmL={pwmL}&time={time}&pwmR={pwmR}')

    except KeyboardInterrupt: #finisce il programma quando si interrompe il terminale
        print("programma finito")


if __name__ == "__main__":
    main()