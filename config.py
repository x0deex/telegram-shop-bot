import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN=os.getenv("BOT_TOKEN")
TELEGRAM_ID_CHANEL=os.getenv("TELEGRAM_ID_CHANEL")
if not BOT_TOKEN:
    raise ValueError
if not TELEGRAM_ID_CHANEL:
    raise ValueError