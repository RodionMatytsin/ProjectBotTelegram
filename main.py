import telebot
import requests
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from config import TOKEN, URL_WEATHER_API


bot = telebot.TeleBot(TOKEN)
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Получить погоду', request_location=True))
keyboard.add(KeyboardButton('О проекте'))


def get_weather(lat, lon):
    try:
        params = {'lat': lat, 'lon': lon, 'appid': '969b064b9491469659432a63c4d0c476', 'units': 'metric', 'lang': 'ru'}
        return requests.get(url=URL_WEATHER_API, params=params).json()
    except Exception as e:
        print(f'Ошибка при получении данных о погоде: {e}')
        return None


@bot.message_handler(commands=['start'])
def send_welcome(m):
    bot.send_message(m.chat.id, 'Отправь мне свое местоположение и я отправлю тебе погоду.', reply_markup=keyboard)


@bot.message_handler(content_types=['location'])
def send_weather(m):
    data = get_weather(m.location.latitude, m.location.longitude)
    if data is not None and "name" in data and "weather" in data and len(data["weather"]) > 0:
        msg = f'Погода в: {data["name"]}\n' \
              f'☁ {data["weather"][0]["description"].capitalize()}\n' \
              f'🌡️ Температура {data["main"]["temp"]}°С\n' \
              f'🌡️ Ощущается {data["main"]["feels_like"]}°С\n' \
              f'💧️ Влажность {data["main"]["humidity"]}%.'
        bot.send_message(m.chat.id, msg, reply_markup=keyboard)
    else:
        text = 'К сожалению, сейчас у меня возникли проблемы с получением данных о погоде. Попробуйте позже.'
        bot.send_message(m.chat.id, text)


@bot.message_handler(regexp='О проекте')
def send_about(m):
    bot.send_message(m.chat.id, 'Этот ТГ бот предназначен для получения текущей погоды.')


bot.infinity_polling()