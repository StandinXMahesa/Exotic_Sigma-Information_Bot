# Library
from data_txt import *
import os
import telebot
from telebot import types
from dotenv import load_dotenv

# Load Env
load_dotenv()

# bot
API_KEY = os.getenv('API')
bot = telebot.TeleBot(API_KEY)

# Making Command
lst_command = [
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("help", "Menampilkan Bantuan untuk "),
        types.BotCommand("test", "Тест"),
        types.BotCommand("form", "Форма"),
        types.BotCommand("menu", "Меню"),
    ]
bot.set_my_commands(lst_command)

@bot.message_handler(commands=["start"])
def greet(message):
    bot.reply_to(message,f"{data['start']}")
    
bot.polling()