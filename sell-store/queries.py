from database import get_db_connection

def execute_query(query):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result


