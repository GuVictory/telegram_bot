import telebot
import config
import logging
import controller.router

bot = config.BOT

config.LOGGER.log(logging.INFO, 'start')

if __name__ == '__main__':
    bot.infinity_polling()
