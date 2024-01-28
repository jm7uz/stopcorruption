from aiogram import Bot,Dispatcher
from data.config import BOT_TOKEN
# Import Database Class
from utils.db_api.sqlite import Database
from aiogram.fsm.storage.memory import MemoryStorage
bot=Bot(token=BOT_TOKEN,parse_mode='HTML')
dp=Dispatcher(storage=MemoryStorage())
# Create database file
db = Database(path_to_db='data/main.db')
