import sqlite3

def init_user_order_db():
    conn = sqlite3.connect('database.sql')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS userOrder (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT,
            phone_number TEXT,
            address TEXT,
            post_address TEXT)
    ''')
    conn.commit()
    cursor.close()
    conn.close()

def init_product_db():
    conn = sqlite3.connect('products.sql')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prod_name TEXT,
            description TEXT,
            price TEXT)
    ''')
    # cursor.execute('DROP TABLE IF EXISTS Products')
    conn.commit()
    cursor.close()
    conn.close()
