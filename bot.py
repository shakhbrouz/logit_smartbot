import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers.start import register_start

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

register_start(dp)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())