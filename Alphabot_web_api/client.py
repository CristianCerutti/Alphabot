import requests

#/api/v1/motors/left?pwm=x&time=t
#/api/v1/motors/right?pwm=y&time=t
#/api/v1/motors/both?pwmL=x&pwmR=y&time=t
def main():
    scelta = input("inserire una scelta: ")
    if int(scelta == 0):
        try:
            while True:
                r = requests.get('http://192.168.0.129:5000/api/v1/sensors/obstacles')  
                r = r.json()
                print(r)
        except:
            print("hai sbagliato")
    elif int(scelta) == 1:
        try:
            pwm = input("inserire il pwm")
            time = input("inserire il tempo")
            r = requests.get(f'http://192.168.0.129:5000/api/v1/motors/right?pwm={pwm}&time={time}')  
            r = r.json()
            print(r)
        except:
            print("hai sbagliato")
    elif int(scelta) == 2:
        try:
            pwm = input("inserire il pwm")
            time = input("inserire il tempo")
            r = requests.get(f'http://192.168.0.129:5000/api/v1/motors/left?pwm={pwm}&time={time}')  
            r = r.json()
            print(r)
        except:
            print("hai sbagliato")
    elif int(scelta) == 3:
        try:
            pwmL = input("inserire il pwm di sinistra")
            pwmR = input("inserire il pwm di destra")
            time = input("inserire il tempo")
            r = requests.get(f'http://192.168.0.129:5000/api/v1/motors/both?pwmL={pwmL}&time={time}&pwmR={pwmR}')  
            r = r.json()
            print(r)
        except:
            print("hai sbagliato")

if __name__ == "__main__":
    main()