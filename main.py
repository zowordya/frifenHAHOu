import asyncio
from aiogram import Bot, Dispatcher
from handlers import router
from dotenv import load_dotenv
import os
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(router)  # Подключаем роутеры

    print("Бот запущен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
