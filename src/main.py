"""Personal telegram bot."""
import os
import telebot
import time
from quotes.utils import get_quote, add_quote


api_key = os.getenv("API_KEY")
user_id = int(os.getenv("USER_ID"))


bot = telebot.TeleBot(api_key)


@bot.message_handler(commands=["start"])
def start(message):
    """Send an acknowledgement message to the user with user_id."""
    if message.from_user.id == user_id:
        bot.send_message(user_id, "Hi")


@bot.message_handler(commands=["quote"])
def quote_send(message):
    """Send a quote to the user."""
    if message.from_user.id == user_id:
        bot.send_message(user_id, get_quote())


@bot.message_handler(commands=["add"])
def quote_add(message):
    """Add a quote to the quotes collection."""
    if message.from_user.id == user_id:
        pass
        # quote = message.text.split(" ")[1].strip()
        # add_quote(quote)
        # bot.send_message(user_id, "quote added")


bot.infinity_polling()
