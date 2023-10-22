from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from settings import BOT_API_TOKEN


storage = MemoryStorage()
bot = Bot(token=BOT_API_TOKEN)
dp = Dispatcher(storage=storage)