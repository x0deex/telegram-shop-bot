import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import BOT_TOKEN

from app.client import client
from app.database.models import init_models


from aiogram.fsm.storage.redis import RedisStorage
import redis.asyncio as aioredis
from dotenv import load_dotenv
import os


load_dotenv()

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

async def main():
    bot = Bot(token=BOT_TOKEN)

    redis_host=os.getenv("REDIS_HOST", "localhost")
    redis_port=os.getenv("REDIS_PORT", "6379")
    redis_db=os.environ["REDIS_DB"]

    redis=await aioredis.from_url(f"redis://{redis_host}:{redis_port}/{redis_db}")

    dp =  Dispatcher(RedisStorage(redis))
    dp.include_router(client)
    dp.startup.register(on_startup)
    dp.shutdown.register(off_startup)
    await dp.start_polling(bot)

async def on_startup(dispatcher: Dispatcher):
    await init_models()
    logging.info("Bot started up...")

async def off_startup(dispatcher: Dispatcher):
    logging.info("Bot shutting down...")

if __name__ == "__main__":
    try:
        print("Starting up...")
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot Stopped")