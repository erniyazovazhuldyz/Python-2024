import psycopg2

def connect_to_database():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="laura11111"
    )
    return conn

def query_with_pagination(table_name, limit, offset):
    conn = connect_to_database()
    cursor = conn.cursor()

    try:
        query = f"SELECT * FROM {table_name} LIMIT %s OFFSET %s"
        cursor.execute(query, (limit, offset))
        
        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except psycopg2.Error as e:
        print("Error querying data:", e)

    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    table_name = input("Enter table name: ")
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))
    query_with_pagination(table_name, limit, offset)
