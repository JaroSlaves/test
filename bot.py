import asyncio
import logging

from aiogram import Bot, Dispatcher,F
from config import token
from untitles.handlers import router

bot = Bot(token=token)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')