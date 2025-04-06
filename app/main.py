from os import getenv
from dotenv import load_dotenv

import telebot as tb

import settings
from func import get_schedule

load_dotenv()
BOT_TOKEN = settings.BOT_TOKEN

bot = tb.TeleBot(BOT_TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def start(message):
    text = 'Щоб отримати актуальний розклад скористайтеся /schedule'
    bot.reply_to(message, text)


@bot.message_handler(commands=['fetchnew'])
def update_schedule(message):
    get_schedule()
    show_schedule(message)


@bot.message_handler(commands=['schedule'])
def show_schedule(message):
    text = 'Актуальний розклад:'
    bot.send_message(message.chat.id, text)
    img = open('home_schedule.png', 'rb')
    bot.send_photo(message.chat.id, img)
