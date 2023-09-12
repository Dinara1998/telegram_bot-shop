from config import bot
from art import tprint
from colorama import Fore
from hendlers import main_hendlers
from db import db_scripts


db_scripts.create_tables()

main_hendlers.registar_main_message_handlers()

print(Fore.GREEN + "BOT started")


bot.infinity_polling()

print(Fore.RED + "BOT closed")
