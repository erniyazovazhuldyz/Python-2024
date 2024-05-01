import psycopg2

def connect_to_database():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="laura11111"
    )
    return conn

def create_table_if_not_exists():
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            phone VARCHAR(20)
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

def insert_from_console():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)", (first_name, last_name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Data inserted successfully.")

def search_phonebook_pattern(pattern):
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE first_name LIKE %s OR last_name LIKE %s OR phone LIKE %s", (f'%{pattern}%', f'%{pattern}%', f'%{pattern}%'))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

create_table_if_not_exists()
insert_from_console()
pattern = 'zhuldyz'
pattern_results = search_phonebook_pattern(pattern)
print(pattern_results)


