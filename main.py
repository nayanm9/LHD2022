from flask import Flask, render_template, request, redirect, url_for
import requests
import os
from cryptography.fernet import Fernet
import sys
sys.path.insert(0, "/home/runner/LHD2022/funcs")
import rps_game
import cc
from custom_random import gen_random_range
from pi import pi, pi_total

app = Flask(__name__,template_folder='static')

@app.route("/") # index page
def index():
    return render_template('index.html')

@app.route("/day1")
def day1():
    api_key_1 = os.environ['KEY1']
    api_key_2 = os.environ['KEY2']
    url = f'https://ip-geolocation.whoisxmlapi.com/api/v1?apiKey={api_key_1}&ipAddress={request.remote_addr}'
    r = requests.get(url)
    j = r.json()
    city = j['location']
    lat = city['lat']
    lng = city['lng']
    final_url =f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lng}&exclude=hourly,daily&appid={api_key_2}"
    r1 = requests.get(final_url)
    j1 = r1.json()
    current = j1["current"]
    pressure = current['pressure']
    humidity = current['humidity']
    wind_speed = current['wind_speed']
    wind_deg = current['wind_deg']
    w = current["weather"]
    for i in w:
        weather = i["main"]
        weather_description = i["description"]
        break
    return render_template('day1.html',weather=weather,weather_description=weather_description,pressure=pressure,humidity=humidity,wind_speed=wind_speed,wind_deg=wind_deg,)

@app.route("/day2")
def day2():
    user_score, comp_score = 0, 0
    return render_template('day2.html',user_score=user_score,comp_score=comp_score)

@app.route("/rps/<value>")
def rps(value):
    user_score  = rps_game.pls_points
    comp_score = rps_game.comps_points
    if value != "":
        result = rps_game.rps1(value)
        print(result)
        return render_template('day2.html',user_score=user_score,comp_score=comp_score, result=result)

@app.route("/day3", methods=["GET","POST"])
def day3():
    if request.method == "POST":
        req = request.form
        choice = req['choice']
        inmessage = req['inmessage']
        inpass = req['key_dn']
        
        if choice != "s":
            if choice == "e":
                key = Fernet.generate_key()
                fernet = Fernet(key)
                data = fernet.encrypt(inmessage.encode())
                return redirect(url_for('formatedtext',key=key,text=data))   
            else:
                fernet = Fernet(inpass)
                data = fernet.decrypt(inmessage.encode()).decode()
                return redirect(url_for('formatedtext',key="Decrypted",text=data))

    return render_template('day3.html')

@app.route("/formatedtext/<key>/<text>")
def formatedtext(key,text):
    return render_template('endn.html',key=key,text=text)

@app.route("/day4", methods=["GET","POST"])
def day4():
    if request.method == "POST":
        req = request.form
        shift = req['shift']
        shift = int(shift)
        choice = req['choice']
        inmessage = req['inmessage']
        if choice != '':
            if shift >=0 and shift <=25:
                if choice == 'e':
                    data = cc.encrypt(inmessage,shift)
                    return redirect(url_for('formatedtext',key=shift,text=data))
                else:
                    data = cc.decrypt(inmessage,shift)
                    return redirect(url_for('formatedtext',key=shift,text=data))
            return redirect(url_for('day4'))
        return redirect(url_for('day4'))
    return render_template('day4.html')

@app.route("/day5", methods=["GET","POST"])
def day5():
    if request.method == "POST":
        req = request.form
        min = req['min']
        max = req['max']
        number = gen_random_range(int(min),int(max))
        return render_template('randnumber.html',number=number)
    return render_template('day5.html')

@app.route("/day6", methods=["GET","POST"])
def day6():
    if request.method == "POST":
        req = request.form
        value = req["value"]
        number = pi(int(value))
        pi_total.clear()
        return render_template('pi.html',number=number)
    return render_template('day6.html')

@app.route("/day7")
def day7():
    return render_template('day7.html')

app.run(host='0.0.0.0', port=8080)