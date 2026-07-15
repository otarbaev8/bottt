# import asyncio
# from aiogram import  Bot , Dispatcher
# from  aiogram.filters import  CommandStart,Command
# from  aiogram.types import  Message,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
# from dotenv import load_dotenv
# import os
# load_dotenv()
#
#
# Token = os.getenv("API")
# bot = Bot(token=Token)
# dp = Dispatcher()
#
# @dp.message(CommandStart)
# async def startt(message: Message):
#     await message.answer('Assalawma Aleykum!')
#
#
# aaaa = ReplyKeyboardMarkup(
#     keyboard=[
#         [ KeyboardButton(text='Tel number 📞'),KeyboardButton(text='Kanallar')],
#
#     ],
#     resize_keyboard=True
# )
# @dp.message(CommandStart())
# async def  start(a:Message):
#     await a.answer(f"Assalawma aleykum", reply_markup=aaaa)
#
# @dp.message()
# async def menular(message:Message):
#     t = message.text
#     if t =='Tel number 📞':
#         await message.answer("+998 99 999 99 99")
#     elif t =='Kanallar':
#         await message.answer("https://t.me/FUTGOAL")
#
#
# async def main():
#     print("bot iske qosildi ✅")
#     await dp.start_polling(bot)
#
# if __name__ == '__main__':
#     asyncio.run(main())
#
#
#
#
#






import  asyncio
from aiogram import  Bot, Dispatcher
from  aiogram.filters import  CommandStart,Command
from aiogram.types import ( Message,ReplyKeyboardMarkup,KeyboardButton)
from dotenv import load_dotenv
import os
load_dotenv()


Token = os.getenv("API")
bot = Bot(token=Token)
dp = Dispatcher()


# reply keyboards
aaa = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='kanallar 🔈'), KeyboardButton(text='Tel number 📞')],
        [KeyboardButton(text='Settings ⚙️')],
    ],
    resize_keyboard=True
)










@dp.message(CommandStart())
async def  start(a:Message):
    await a.answer(f"Assalawma aleykum", reply_markup=aaa)


@dp.message()
async def menular(message:Message):
    t = message.text
    if t =='kanallar 🔈':
        await message.answer("https://t.me/FUTGOAL")
    elif t =='Tel number 📞':
        await message.answer("+998 99 999 99 99")



async def main():
    print('bot iske qosildi')
    await  dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
