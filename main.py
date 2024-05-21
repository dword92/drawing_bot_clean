from aiogram import Bot, Dispatcher
from core.basic import get_start, get_message
from aiogram.filters import Command
from core.commands import set_commands
import asyncio
import logging
from core.db import close_database_connection

TOKEN = ''
ADMIN_ID = ''


async def start_bot(bot: Bot):
    await set_commands(bot)
    # await bot.send_message(ADMIN_ID, text='Bot started', disable_notification=True)


# async def stop_bot(bot: Bot):
# await bot.send_message(ADMIN_ID, text='Bot stopped', disable_notification=True)


async def start():
    #logging.basicConfig(level=logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    bot = Bot(token=TOKEN, parse_mode='HTML')
    dp = Dispatcher()
    dp.startup.register(start_bot)
    # dp.shutdown.register(stop_bot)
    dp.message.register(get_start, Command(commands=['start']))
    dp.message.register(get_message)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        close_database_connection()


if __name__ == '__main__':
    asyncio.run(start())
