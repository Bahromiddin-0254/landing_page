from bot import dp
from aiogram.utils.markdown import text,bold,italic
from aiogram.types import ParseMode, Message
from aiogram import *
from aiogram.types import InputFile,InputMediaAudio,InputMediaPhoto,InputMediaVideo,InputMediaAnimation,InputMediaDocument
import logging
import requests
import math
from aiogram import Bot, Dispatcher, executor, types
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Salom men @bahromiddinsblog kanalining murojaatlar uchun botiman.")

#aiogram string filter

@dp.message_handler(commands=['namoz'])
async def namaz_times(message: types.Message):
    res=requests.get("https://api.pray.zone/v2/times/today.json?city=asaka-uz").json()['results']['datetime'][0]['times']
    
    await message.reply(text("Bomdod: ",res['Fajr'],"\nPeshin: ",res['Dhuhr'],"\nAsr: ",res['Asr'],"\nShom: ",res['Maghrib'],"\nXufton: ",res['Isha']))

@dp.message_handler()
async def my_message_handler(message: types.Message):
    res=requests.get(" https://v6.exchangerate-api.com/v6/2f8af6b87e1be600497a0ea3/pair/USD/UZS").json()['conversion_rate']
    print(res)
    try:
        response=str(round(float(message.text)*res))+" so'm"
    except:
        response= "xato kiritildi"
    await message.reply(response)
