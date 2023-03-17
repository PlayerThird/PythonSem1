from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from aiogram.types import Message


bot = Bot(token = "6280050741:AAGERmqenqHqSvv-oPSzUjXPQwg-0mkZjxQ")
dp = Dispatcher(bot)

# @dp.message_handler(commands=['start'])#на команду старт отвечает текст

@dp.message_handler()#отвечает на любое сообщение
async def com_start(message: Message):
    await message.answer(f'{message.from_user.first_name}, сам ты, {message.text}!')





executor.start_polling(dp, skip_updates=True)
