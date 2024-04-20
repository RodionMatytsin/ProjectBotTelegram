import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from config import TOKEN


bot = telebot.TeleBot(TOKEN)
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Hello'))
keyboard.add(KeyboardButton('Bye'))
keyboard.add(KeyboardButton('Uwu'))


@bot.message_handler(commands=['help', 'start'])
def send_welcome(m):
    bot.send_message(m.chat.id, 'Я бот!', reply_markup=keyboard)


@bot.message_handler(regexp=r'hello\.*')
def say_hello(m):
    bot.send_message(m.chat.id, 'Hello!')


@bot.message_handler(regexp=r'uwu\.*')
def say_uwu(m):
    bot.send_message(m.chat.id, 'Uwu!')


@bot.message_handler(func=lambda s: 'Bye' in s.text)
def echo_message(m):
    bot.send_message(m.chat.id, 'Bye!')


#-----------------------Эхло бот------------------------Начало
# @bot.message_handler(commands=['help', 'start'])
# def send_welcome(m):
#    bot.send_message(m.chat.id, 'Я бот!')
#
#
# @bot.message_handler(content_types=['text'])
# def echo_message(m):
#    bot.send_message(m.chat.id, m.text)
#-----------------------Эхло бот------------------------Конец


bot.infinity_polling()
