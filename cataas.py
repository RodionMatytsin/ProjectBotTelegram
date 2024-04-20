import telebot
import requests
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from config import TOKEN, URL


bot = telebot.TeleBot(TOKEN)
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Котика'))


def get_cat():
    return requests.get(URL).content


@bot.message_handler(commands=['help', 'start'])
def send_welcome(m):
    bot.send_message(m.chat.id, 'Я котик!', reply_markup=keyboard)


@bot.message_handler(regexp='кот')
def cat_image_message(m):
    bot.send_photo(m.chat.id, get_cat())


bot.infinity_polling()
