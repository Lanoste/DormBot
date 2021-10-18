from config import TOKEN
import logging
import KeyBoard as kb
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

#Общие команды
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("Привет, выбери что тебе необходимо!", reply_markup=kb.greet_kb)

#Выбор чего нужно
@dp.message_handler(lambda message: message.text == "💼 Услуги 💼")
async def choice_service(message: types.Message):
    await message.answer("Хорошо")
    await message.answer("Что тебе нужно? Выбери")

@dp.message_handler(lambda message: message.text == "🍫 Товары 🍫")
async def choice_goods(message: types.Message):
    await message.answer("Отличный выбор!")
    await message.answer("Выбери, как ты хочешь купить товар", reply_markup=kb.kb_foh)

#Выбор продолжения если Товары
@dp.message_handler(lambda message: message.text == "🍫 Категории товаров 🍫")
async def goods(message: types.Message):
    await message.answer("Выбери, что тебе нужно", reply_markup=kb.kb_food)

@dp.message_handler(lambda message: message.text == "💃 Конкретный продавец 🕺")
async def human(message: types.Message):
    await message.answer("Ладно, вот тебе список")
    await message.answer("Выбери, того у кого ты хочешь купить, и отправь мне его номер")

#Выбор продолжения если Категории товаров

if __name__ == '__main__':
    executor.start_polling(dp)

