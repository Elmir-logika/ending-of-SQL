from models import add_products, add_customers, add_orders
from queries import execute_query

def user_interface():
    while True:
        print("1. Додати продукти")
        print("2. Додати клієнтів")
        print("3. Додати замовлення")
        print("4. Сумарний обсяг продажів")
        print("5. Кількість замовлень на кожного клієнта")
        print("6. Середній чек замовлення")
        print("7. Найбільш популярна категорія товарів")
        print("8. Загальна кількість товарів кожної категорії")
        print("9. Оновити ціни на смартфони")
        print("10. Вихід")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            add_products()
        elif choice == '2':
            add_customers()
        elif choice == '3':
            add_orders()
        elif choice == '4':
            result = execute_query('''
                SELECT SUM(p.price * o.quantity) AS total_sales
                FROM orders o
                JOIN products p ON o.product_id = p.product_id;
            ''')
            print(result)
        elif choice == '5':
            result = execute_query('''
                SELECT c.first_name, c.last_name, COUNT(o.order_id) AS order_count
                FROM customers c
                JOIN orders o ON c.customer_id = o.customer_id
                GROUP BY c.customer_id;
            ''')
            print(result)
        elif choice == '6':
            result = execute_query('''
                SELECT AVG(p.price * o.quantity) AS average_order_value
                FROM orders o
                JOIN products p ON o.product_id = p.product_id;
            ''')
            print(result)
        elif choice == '7':
            result = execute_query('''
                SELECT p.category, COUNT(o.order_id) AS order_count
                FROM orders o
                JOIN products p ON o.product_id = p.product_id
                GROUP BY p.category
                ORDER BY order_count DESC
                LIMIT 1;
            ''')
            print(result)
        elif choice == '8':
            result = execute_query('''
                SELECT category, COUNT(product_id) AS product_count
                FROM products
                GROUP BY category;
            ''')
            print(result)
        elif choice == '9':
            conn = get_db_connection() # Підключення до бази даних 
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE products
                SET price = price * 1.10
                WHERE category = 'смартфони';
            ''')
            conn.commit()
            conn.close()
            print("Ціни на смартфони оновлено.")
        elif choice == '10':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")



