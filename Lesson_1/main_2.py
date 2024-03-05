import asyncio

from aiogram import Bot, Dispatcher
from Lesson_1.app.hendlers import router
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('TOKEN')
bot = Bot(token=token)

dp = Dispatcher()


async def main():
    dp.include_router(router)
    await  dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
