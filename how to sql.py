from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogra.filters import Command
import sqlite3 
import asyncio

bot = Bot(token = '') #здесь свой токен 
dp = Dispatcher()

connection = sqlite3.connect('users.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users(
  username TEXT,
  id INT
)
''')

@dp.message(Command('start'))
async def start(msg : Message):
  cursor.execute('INSERT INTO users VALUES (?, ?)', (msg.from_user.username, msg.from_user.id))
  connection.commit()
async def main():
  await dp.start_polling(bot)

asyncio.run(main())
