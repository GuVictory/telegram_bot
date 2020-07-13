import telebot
import logging
import config

bot = config.BOT


@bot.message_handler(content_types=['text'])
def send_text(message):
    if not message.text.startswith('/'):
        config.LOGGER.log(
            logging.INFO, f'message from id: {message.from_user.id}')
        bot.send_message(message.chat.id, message.text)
