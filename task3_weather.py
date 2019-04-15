# -*- coding: utf-8 -*-
import requests
import json


def weather():
    city = "509820"
    token = "e5c0f593f4d3d55b91b74e9be0e532a6"
    s = requests.get(f"http://api.openweathermap.org/data/2.5/weather?id={city}&units=metric&APPID={token}")
    fo = json.loads(s.text)
    celsii = fo['main']['temp']
    nolic = u'\N{DEGREE SIGN}'
    print("City: ", fo['name'])
    print("temp: ", str(celsii) + nolic + "C")
    print("Wind: ", str(fo['wind']['speed']) + "m/c")
    print("Country: ", fo['sys']['country'])
    return fo


print(weather())

