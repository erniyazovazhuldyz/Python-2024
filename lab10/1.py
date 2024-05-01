import psycopg2
import csv

def connect_to_database():
    conn = psycopg2.connect(
        host="localhost",
        database="suppliers",
        user="postgres",
        password="laura11111"
    )
    return conn


def insert_from_csv(filename, cursor, conn):
    try:
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader, None)  
            if header is None:
                print("CSV file is empty.")
                return
            for row in csv_reader:
                cursor.execute("INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)", row)
        conn.commit()
        print("Data inserted from CSV file successfully.")
    except IOError as e:
        print(f"Error reading CSV file: {e}")

def insert_from_console(cursor, conn):
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    cursor.execute("INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)", (first_name, last_name, phone))
    conn.commit()
    print("Data inserted from console successfully.")

def update_data(username, new_phone, cursor, conn):
    cursor.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s OR last_name = %s", (new_phone, username, username))
    conn.commit()
    print("Data updated successfully.")

def query_data(filter_type, filter_value, cursor):
    if filter_type == 'first_name':
        cursor.execute("SELECT * FROM phonebook WHERE first_name = %s", (filter_value,))
    elif filter_type == 'last_name':
        cursor.execute("SELECT * FROM phonebook WHERE last_name = %s", (filter_value,))
    elif filter_type == 'phone':
        cursor.execute("SELECT * FROM phonebook WHERE phone = %s", (filter_value,))
    else:
        print("Invalid filter type.")
        return

    result = cursor.fetchall()
    if result:
        for row in result:
            print(row)
    else:
        print("No matching records found.")

def delete_data(filter_type, filter_value, cursor, conn):
    if filter_type == 'first_name':
        cursor.execute("DELETE FROM phonebook WHERE first_name = %s", (filter_value,))
    elif filter_type == 'last_name':
        cursor.execute("DELETE FROM phonebook WHERE last_name = %s", (filter_value,))
    elif filter_type == 'phone':
        cursor.execute("DELETE FROM phonebook WHERE phone = %s", (filter_value,))
    else:
        print("Invalid filter type.")
        return

    conn.commit()
    print("Data deleted successfully.")

def execute_functions():
    conn = connect_to_database()
    cursor = conn.cursor()
    operation = input("Enter operation (insert/update/query/delete): ").lower()

    if operation == 'insert':
        insert_from_console(cursor, conn)
    elif operation == 'update':
        username = input("Enter username to update: ")
        new_phone = input("Enter new phone number: ")
        update_data(username, new_phone, cursor, conn)
    elif operation == 'query':
        filter_type = input("Enter filter type (first_name/last_name/phone): ")
        filter_value = input(f"Enter {filter_type}: ")
        query_data(filter_type, filter_value, cursor)
    elif operation == 'delete':
        filter_type = input("Enter filter type (first_name/last_name/phone): ")
        filter_value = input(f"Enter {filter_type}: ")
        delete_data(filter_type, filter_value, cursor, conn)
    else:
        print("Invalid operation.")
    
    cursor.close()
    conn.close()

execute_functions()
