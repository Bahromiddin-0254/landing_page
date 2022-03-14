from aiogram.utils.markdown import text,bold,italic
from aiogram.types import ParseMode, Message
from aiogram import *
from aiogram.types import InputFile,InputMediaAudio,InputMediaPhoto,InputMediaVideo,InputMediaAnimation,InputMediaDocument
import logging

from aiogram import Bot, Dispatcher, executor, types
logging.basicConfig(level=logging.INFO)
import environ
# Initialize bot and dispatcher

env=environ.Env()
environ.Env.read_env()

API_TOKEN = env.str('API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

    
if __name__ == '__main__':
    from handler.personal_start import dp
    executor.start_polling(dp, skip_updates=True)