from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

#Кнопки под первую клаву
button_foods = KeyboardButton('🍫 Товары 🍫')
button_services = KeyboardButton('💼 Услуги 💼')

#Кнопки под клаву выбора человека или категории
button_human = KeyboardButton('💃 Конкретный продавец 🕺')
button_idk = KeyboardButton('🍫 Категории товаров 🍫')

#Кнопки под клаву выбора категорий
button_chips = KeyboardButton('Чипсы')
button_chocolate = KeyboardButton('Шоколад и шоколадные батончики')
button_drinks = KeyboardButton('Напитки')
button_noodles = KeyboardButton('Продукты быстрого приготовления')
button_other = KeyboardButton('Другие продукты')
button_other2 = KeyboardButton('Другие товары')

button_nails = KeyboardButton('Маникюр')

#Кнопки под выбор вида напитков
button_energetics = KeyboardButton('Энергетики')
button_juices = KeyboardButton('Соки')
button_soda = KeyboardButton('Газировка')

#Кнопки под выбор  шоколада или батончиков
button_chocolate_bar = KeyboardButton('Шоколадные батончики')
button_chocolate_big = KeyboardButton('Шоколадные плитки')

#Клава первого выбора
greet_kb = ReplyKeyboardMarkup().row(button_foods, button_services)

#Клава выбора человека или категорий товаров
kb_foh = ReplyKeyboardMarkup().row(button_human, button_idk)

#Клава выбора категорий товаров
kb_food = ReplyKeyboardMarkup().row(button_chips, button_chocolate, button_drinks).row(button_noodles, button_other, button_other2)

#Клава под вида напитков
kb_drinks = ReplyKeyboardMarkup().row(button_energetics, button_juices, button_soda)

#Клава под выбор шоколада или батончиков
kb_chocolate= ReplyKeyboardMarkup().row(button_chocolate_bar, button_chocolate_big)

#Клава выбора услуг
kb_services = ReplyKeyboardMarkup().row(button_nails)

