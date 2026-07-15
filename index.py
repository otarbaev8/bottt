import asyncio
from aiogram import  Bot , Dispatcher
from  aiogram.filters import  CommandStart,Command
from  aiogram.types import  Message,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
import os
load_dotenv()


Token = os.getenv("API")
bot = Bot(token=Token)
dp = Dispatcher()


menu=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Katalog')],
        [KeyboardButton(text='Sebet')],
    ],
    resize_keyboard=True
 )
catalog = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text="iPhone 15 — 12 000 000 so'm", callback_data="iphone")],
    [InlineKeyboardButton(text="Samsung S24 — 9 500 000 so'm", callback_data="samsung")],
    [InlineKeyboardButton(text="AirPods Pro — 2 500 000 so'm", callback_data="airpods")],
])





aaaa = ReplyKeyboardMarkup(
    keyboard=[
        [ KeyboardButton(text='Tel number 📞'),KeyboardButton(text='Kanallar ')],

    ],
    resize_keyboard=True
)

nnn = ReplyKeyboardMarkup(
    keyboard=[
        [ KeyboardButton(text='settings ⚙ '), KeyboardButton(text='observer ')],
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Assalawma aleykum\nMenyuda tanlan!",reply_markup=menu)

@dp.message()
async def catalogg(message:Message):
    t=message.text
    if t=='Katalog':
        await message.answer('Onimler kestesi',reply_markup=catalog)


async def main():

    print("bot iske qosildi ✅")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


