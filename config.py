import os
import sys
import telebot
import logging
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BOT_TOCKEN = os.getenv("bot_tocken")
BOT = telebot.TeleBot(BOT_TOCKEN)
LOGGER = telebot.logger

LOGGER.setLevel(logging.INFO)  # or use logging.INFO
