import telebot
import config
import pyjokes
import logging

bot = config.BOT
# Handle /start, /help, /joke


@bot.message_handler(commands=['start'])
def start_message(message):
    config.LOGGER.log(
        logging.INFO, f'start chat with id: {message.from_user.id}')
    bot.send_message(
        message.chat.id, f'Hi, {message.from_user.username}!\nWrite /help to see some commands...')


@bot.message_handler(commands=['help'])
def command_help(message):
    config.LOGGER.log(logging.INFO, f'help to id: {message.from_user.id}')
    bot.reply_to(
        message, "Hello, did someone call for help?\nHere are some commands:\n/joke - random joke for you")


@bot.message_handler(commands=['joke'])
def command_joke(message):
    config.LOGGER.log(logging.INFO, f'send joke to id: {message.from_user.id}')
    bot.send_message(message.chat.id, pyjokes.get_joke(category='all'))
