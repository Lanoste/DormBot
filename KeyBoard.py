from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_foods = KeyboardButton('🍫 Товары 🍫')
button_services = KeyboardButton('💼 Услуги 💼')

button_human = KeyboardButton('💃 Конкретный продавец 🕺')
button_idk = KeyboardButton('🍫 Категории товаров 🍫')

button_chips = KeyboardButton(' Снеки ')
button_chocolate = KeyboardButton(' Шоколад ')
button_drinks = KeyboardButton(' Напитки ')
button_noodles = KeyboardButton('Продукты быстрого приготовления ')
button_other = KeyboardButton(' Другое ')
button_nails = KeyboardButton(' Маникюр ')

button_energetics = KeyboardButton(' Энергетики ')
button_juices = KeyboardButton(' Соки ')
button_soda = KeyboardButton(' Газировка ')
button_chocolate_bar = KeyboardButton(' Шоколадные батончики ')
button_chocolate_big = KeyboardButton(' Шоколадные плитки ')


greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_foods)
greet_kb.add(button_services)

kb_foh = ReplyKeyboardMarkup()
kb_foh.add(button_human)
kb_foh.add(button_idk)

kb_food = ReplyKeyboardMarkup().row(button_chips, button_chocolate, button_drinks).row(button_noodles, button_other)


kb_services = ReplyKeyboardMarkup()
kb_services.add(button_nails)