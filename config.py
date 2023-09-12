import telebot
import sqlite3

bot = telebot.TeleBot("6555758045:AAGpg_6UDdU19zMEuNEFAf2HZM05jts-UJ0")

db = sqlite3.connect("db.db", check_same_thread=False)

cursor = db.cursor()