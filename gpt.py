from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogra.filters import Command
import asyncio
from openai import OpenAI

client = OpenAI(
    base_url="https://api.aimlapi.com/v1",
    api_key="2784d3f624c5401da4a5a6d1580a3a2f",  
)

print(f"Assistant: {message}")

bot = Bot(token = '') 
dp = Dispatcher()

@dp.message()
async def start(msg : Message):
  response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "You are an AI assistant who knows everything.",
        },
        {
            "role": "user",
            "content": msg.text,
        },
    ],
  )

  res = response.choices[0].message.content
  await msg.answer(res)
async def main():
  await dp.start_polling(bot)

asyncio.run(main())
