from telebot import types



start_keyboard = types.InlineKeyboardMarkup(row_width=1)
choose_products_btn = types.InlineKeyboardButton("Выбрать товары", callback_data="choose_products_btn")
about_us_btn = types.InlineKeyboardButton("Все о нас!", callback_data="about_us_btn")
stocks_btn = types.InlineKeyboardButton("Акции и скидки!", callback_data="stocks_btn")
start_keyboard.add(choose_products_btn, about_us_btn, stocks_btn)

