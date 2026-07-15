import asyncio
from aiogram import  Bot , Dispatcher
from  aiogram.filters import  CommandStart,Command
from  aiogram.types import  Message,ReplyKeyboardMarkup,KeyboardButton
from dotenv import load_dotenv
import os
load_dotenv()


Token = os.getenv("API")
bot = Bot(token=Token)
dp = Dispatcher()


aaaa = ReplyKeyboardMarkup(
    keyboard=[
        [ KeyboardButton(text='Tel number 📞'),KeyboardButton(text='Kanallar ')],

    ],
    resize_keyboard=True
)

@dp.message(CommandStart)
async def startt(message: Message):
    await message.answer('Assalawma Aleykum!')
async def main():

    print("bot iske qosildi ✅")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
