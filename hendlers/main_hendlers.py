from config import bot, db, cursor
from keyboards import main
from telebot import types

def start(message):
    

    cursor.execute(f"SELECT * FROM users WHERE user_id = {message.from_user.id}")
    user_data = cursor.fetchone()
    if user_data is None:
        
        cursor.execute(f'''INSERT INTO users(user_id, first_name, last_name, username, chat_id, first_login, last_login)
                        VALUES(
                            {message.from_user.id},
                            "{message.from_user.first_name}",
                            "{message.from_user.last_name}",
                            "{message.from_user.username}",
                            {message.chat.id},
                            {message.date},
                            {message.date});''')

        db.commit()
    else:

    
        cursor.execute(f'''UPDATE users SET last_login = {message.date} WHERE user_id ={message.from_user.id}''') 
        db.commit()

    bot.send_message(message.chat.id, text="Добро пожаловать!", reply_markup=main.start_keyboard)

def choose_category(callback):
    cursor.execute("SELECT * FROM categories")
    category = cursor.fetchall()
    print(category)
    categories_kb = types.InlineKeyboardMarkup()


    for id, title in category:
        print(id, title)

        category_btn = types.InlineKeyboardButton(text=title, callback_data=f'category_{id}')
        categories_kb.add(category_btn)
    bot.send_message(callback.message.chat.id, text="Выберите категорию", reply_markup=categories_kb)


def choose_products(callback):
    print(callback.data)

    category_id = int(callback.data.split("_")[1])   # id?
    print(category_id)

    cursor.execute(f''' SELECT id, title, price FROM products WHERE category_id = {category_id} ''')
    products = cursor.fetchall()
    products_kb = types.InlineKeyboardMarkup()

    # [(id, title, price), (id, title, price),(id, title, price),(id, title, price),]
    
    for id, title, price in products:

        products_btn = types.InlineKeyboardButton(text=f'{title} | {price}', callback_data=f'product_{id}')
        products_kb.add(products_btn)
    bot.send_message(callback.message.chat.id, text="Выберите товар", reply_markup=products_kb)

    # product_{id}
    # Сумка | 3000р
    # Сапог 1 шт | 1500р
def send_product_info(callback):
    print(callback.data)

    product_id = int(callback.data.split("_")[1])
    print(product_id)

    cursor.execute(f''' SELECT * FROM products WHERE id={product_id} ''')
    product = cursor.fetchone() # (1, 'Платья', 'арвр', 1, 2000, None)
    print(product)

    bot.send_message(callback.message.chat.id, text=f'''Название: {product[1]}

Описание: {product[2]}
Цена: {product[4]}
''')


    




def registar_main_message_handlers():
    bot.register_message_handler(start, commands=["start"])
    bot.register_callback_query_handler(choose_category, func=lambda callback: callback.data=="choose_products_btn")
    bot.register_callback_query_handler(choose_products, func=lambda callback: "category_" in callback.data)
    bot.register_callback_query_handler(send_product_info, func=lambda callback: "product_" in callback.data)
   

