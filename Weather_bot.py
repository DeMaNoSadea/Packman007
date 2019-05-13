import telebot
from telebot import apihelper
import requests
import json

bot = telebot.TeleBot("714421706:AAGKaDy366JAGJWKixyIQ7Mwaf_cBJedxX0")
apihelper.proxy = {'https': 'socks5h://localhost:9050'}


@bot.message_handler(commands=['start', 'help', 'get_weather', 'get_me'])
def handle_start_help(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Hello! I am WBot. How can i help you?")

    elif message.text == "/help":
        bot.send_message(message.from_user.id, """I can do 3 command: 
1) /start - вывод приветственного сообщения
2) /get_weather - получение и вывод температуры из выбраного города
3) /get_me - вывод id пользователя""")

    elif message.text == "/get_weather":
        bot.send_message(message.chat.id, "Please, type the name of your city!")
        bot.register_next_step_handler(message, temp)

    elif message.text == "/get_me":
        bot.send_message(message.from_user.id, message.from_user.id)


def temp(message):
    city = message.text
    City = dict(json.loads(str((requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&APPID=e5c0f593f4d3d55b91b74e9be0e532a6').text))))
    temp = round(City.get('main').get('temp'), 1)
    bot.send_message(message.chat.id, f"{temp}" + " " + u"\u2103")


bot.polling(none_stop=True, interval=1
