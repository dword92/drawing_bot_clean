from aiogram import Bot
from aiogram.types import Message, FSInputFile
from draw_img import image_draw
from core.processing import format_numbers
from core.db import add_user_to_database, increment_request_count
from core.save_request import save_request_to_file
import logging
import os
import asyncio


put = ""


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'<b>Привет, {message.from_user.first_name}!</b>')
    user_id = message.from_user.id
    add_user_to_database(user_id)


async def get_message(message: Message, bot: Bot):
    logging.basicConfig(level=logging.DEBUG)
    parts = message.text.split()

    if len(parts) != 4:
        await bot.send_message(message.from_user.id, 'Введи данные согласно формату!')
        return
    summa, name, surname_initial, phone = parts

    if not summa.isdigit() or int(summa) < 100 or int(summa) > 99999:
        await bot.send_message(message.from_user.id, 'Недопустимая сумма!')
        return
    formatted_num1 = format(int(summa), ',d').replace(',', ' ')
    summa = formatted_num1
    user_id = message.from_user.id
    increment_request_count(user_id)
    user_text = message.text
    save_request_to_file(user_id, user_text)
    await bot.send_message(message.from_user.id, 'Ожидай...')
    format_numbers(phone)
    image_draw(summa, name, surname_initial, phone=format_numbers(phone))
    await bot.send_document(message.from_user.id, FSInputFile(put))
    await asyncio.sleep(5)
    os.remove(put)
