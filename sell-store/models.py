from database import get_db_connection

def add_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    products = [
        (1, 'iPhone', 'смартфони', 999.99),
        (2, 'Samsung Galaxy', 'смартфони', 849.99),
        (3, 'MacBook Air', 'ноутбуки', 1199.99),
        (4, 'Dell TV', 'ноутбуки', 999.99),
        (5, 'iPad', 'планшети', 799.99)
    ]
    cursor.executemany('INSERT INTO products VALUES (?, ?, ?, ?)', products)
    conn.commit()
    conn.close()

def add_customers():
    conn = get_db_connection()
    cursor = conn.cursor()
    customers = [
        (1, 'Олександр', 'Коваленко', 'alex@example.com'),
        (2, 'Марія', 'Шевченко', 'mari@example.com'),
        (3, 'Андрій', 'Петренко', 'andreu@example.com'),
        (4, 'Максим', 'Івфанович', 'maxim@example.com'),
        (5, 'Вікторія', 'Сидоренко', 'vika@example.com')
    ]
    cursor.executemany('INSERT INTO customers VALUES (?, ?, ?, ?)', customers)
    conn.commit()
    conn.close()

def add_orders():
    conn = get_db_connection()
    cursor = conn.cursor()
    orders = [
        (1, 1, 1, 2, '2024-06-01'),
        (2, 2, 2, 1, '2024-06-02'),
        (3, 3, 3, 1, '2024-06-03'),
        (4, 4, 4, 3, '2024-06-04'),
        (5, 5, 5, 1, '2024-06-05')
    ]
    cursor.executemany('INSERT INTO orders VALUES (?, ?, ?, ?, ?)', orders)
    conn.commit()
    conn.close()


