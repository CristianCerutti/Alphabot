from flask import Flask, render_template, redirect, url_for, request, make_response, jsonify
from datetime import date, datetime
import RPi.GPIO as GPIO
from re import U
import time as tmps
import sqlite3
import string
import random
from AlphaBot import AlphaBot

#/api/v1/sensors/obstacles
#{"left": 0 non c'è ostacolo 1 c'è ostacolo, "right": 0 non c'è ostacolo 1 c'è ostacolo}

app = Flask(__name__)
bot = AlphaBot()

@app.route('/api/v1/sensors/obstacles', methods =['GET', 'POST'])
def generale():
  
    DR = 16
    DL = 19

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(DR,GPIO.IN,GPIO.PUD_UP)
    GPIO.setup(DL,GPIO.IN,GPIO.PUD_UP)

    try:
        while True:
            DR_status = GPIO.input(DR)
            DL_status = GPIO.input(DL)
            result = {}
            if((DL_status == 1) and (DR_status == 1)):
                result = {"left": 0, "right": 0} #no ostacoli
                print("no ostacoli ")
                return jsonify(result)

            elif((DL_status == 1) and (DR_status == 0)): #1 non c'è, 0 c'è
                result = {"left": 0, "right": 1} #ostacolo sulla destra
                print("sulla destra")
                return jsonify(result)
                
            elif((DL_status == 0) and (DR_status == 1)):
                result = {"left": 1, "right": 0}  #ostacolo sulla sinistra
                print("sulla sinistra ")
                return jsonify(result)

            elif((DL_status == 0) and (DR_status == 0)):
                result = {"left": 1, "right": 1}  #ostacolo su entrambi i sensori
                print("su entrambi ")
                return jsonify(result)

    except KeyboardInterrupt:
        GPIO.cleanup();

#?pwm=x&time=t
@app.route('/api/v1/motors/left', methods =['GET', 'POST'])
def left():
    try:
        if 'pwm' in request.args and 'time' in request.args:
            pwm = float(request.args['pwm'])
            time = float(request.args['time'])
            bot.time_left(time, pwm)
            return "1"
        else:
            return "0"  #1 c'è errore
    except:
        return "0"
    
@app.route('/api/v1/motors/right', methods =['GET', 'POST'])
def right():
    try:
        if 'pwm' in request.args and 'time' in request.args:
            pwm = float(request.args['pwm'])
            time = float(request.args['time'])
            bot.time_right(time, pwm)
            return "1"
        else:
            return "0"
    except:
        return "0"

@app.route('/api/v1/motors/both', methods =['GET', 'POST'])
def both():
    try:
        if 'pwmL' in request.args and 'time' in request.args and 'pwmR' in request.args :
            pwmL = float(request.args['pwmL'])
            pwmR = float(request.args['pwmR'])
            time = float(request.args['time'])
            bot.time_forward(time, pwmL, pwmR)
            return "1"
        else:
            return "0"
    except:
        return "0"

@app.route('/api/v1/motors/back', methods =['GET', 'POST'])
def back():
    try:
        if 'pwm' in request.args and 'time' in request.args:
            pwm = float(request.args['pwm'])
            time = float(request.args['time'])
            bot.time_backward(time, pwm)
            return "1"
        else:
            return "0"
    except:
        return "0"

if __name__== "__main__":
    app.run(debug=True, host="192.168.0.129") #, host='192.168.0.129'