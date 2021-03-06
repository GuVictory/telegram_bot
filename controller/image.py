import telebot
import logging
import config
import os
from PIL import Image, ImageFilter
bot = config.BOT


@bot.message_handler(func=lambda message: True, content_types=['photo'])
def image_command(message):
    config.LOGGER.log(
        logging.INFO, f'image from id: {message.from_user.id}')

    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)

    with open(file_info.file_path, 'wb') as new_file:
        new_file.write(downloaded_file)
        img = Image.open('./' + file_info.file_path)
        # TODO Сделать модуль для работы с изображениями, чтобы создавать рандомные изменения
        formated_img = img.convert('L')
        formated_img.save(file_info.file_path, 'png')

    with open(file_info.file_path, 'rb') as new_file:
        bot.send_photo(message.chat.id, new_file)
        os.remove(file_info.file_path)
