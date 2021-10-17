from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_foods = KeyboardButton('🍫 Продукты 🍫')
button_services = KeyboardButton('💼 Услуги 💼')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_foods)
greet_kb.add(button_services)
