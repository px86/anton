"""Send a quote to user."""

# This script is scheduled by cron.

import os
import telebot
from utils import get_quote

api_key = os.getenv("API_KEY")
user_id = os.getenv("USER_ID")

bot = telebot.TeleBot(api_key)
bot.send_message(user_id, get_quote())
