"""Personal telegram bot."""
import os
import telebot
import time
from multiprocessing import Process
from quotes import get_quote


api_key = os.getenv("API_KEY")
user_id = int(os.getenv("USER_ID"))


def send_quote(interval: int = 60):
    """Send a quote to user, after every interval seconds."""
    bot = telebot.TeleBot(api_key)
    while True:
        bot.send_message(user_id, get_quote())
        time.sleep(interval)


process = Process(target=send_quote, args=(60 * 60 * 24,))
process.start()


bot = telebot.TeleBot(api_key)


@bot.message_handler(commands=["start"])
def start(message):
    """Send an acknowledgement message to the user with user_id."""
    if message.from_user.id == user_id:
        bot.send_message(user_id, "Hi")


@bot.message_handler(commands=["process"])
def process_status(message):
    """Check if the process is still running."""
    global process
    if message.from_user.id == user_id:
        if process.is_alive():
            bot.reply_to(message, "[OK] process is running")
        else:
            bot.reply_to(message, "[ERROR] process is dead!")


bot.infinity_polling()
process.join()
