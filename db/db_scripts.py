from config import db, cursor

def create_tables():
    cursor.execute(''' 
CREATE TABLE IF NOT EXISTS users(
                   user_id INTEGER NOT NULL,
                   first_name TEXT NOT NULL,
                   last_name TEXT,
                   username TEXT,
                   chat_id INTEGER NOT NULL,
                   first_login INTEGER NOT NULL,
                   last_login INTEGER NOT NULL,
                   email TEXT,
                   phone TEXT 

)
 ''' )
    db.commit()

    cursor.execute('''
CREATE TABLE IF NOT EXISTS categories(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT
                   )
                         ''')
    db.commit()

    cursor.execute(''' 
CREATE TABLE IF NOT EXISTS products(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    description TEXT,
                    category_id INTEGER,
                    price INTEGER,
                    photo TEXT,
                    FOREIGN KEY (category_id) REFERENCES categories (id) ON DELETE CASCADE     
)
''')
    db.commit()


    cursor.execute('''
CREATE TABLE IF NOT EXISTS stocks(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    description TEXT,
                    products TEXT
                    
)
''')
    db.commit()

    cursor.execute(''' 
CREATE TABLE IF NOT EXISTS cart(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    product_id INTEGER,
                    FOREIGN KEY (product_id) REFERENCES products (id) ON DELETE CASCADE
)
''')
    db.commit()