from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

# the token for the bot is stored in.env file
TOKEN = os.getenv("bot_token")
