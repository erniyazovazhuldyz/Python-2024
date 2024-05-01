import psycopg2

def connect_to_database():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="laura11111"
    )
    return conn

def delete_entry_by_first_name(first_name):
    conn = connect_to_database()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM phonebook WHERE first_name = %s", (first_name,))
    conn.commit()

    if cursor.rowcount > 0:
        print("Entry for '{}' deleted successfully.".format(first_name))
    else:
        print("Entry for '{}' not found.".format(first_name))

    cursor.close()
    conn.close()

def delete_entry_by_phone(phone):
    conn = connect_to_database()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    conn.commit()

    if cursor.rowcount > 0:
        print("Entry with phone number '{}' deleted successfully.".format(phone))
    else:
        print("Entry with phone number '{}' not found.".format(phone))

    cursor.close()
    conn.close()

if __name__ == "__main__":
    first_name = input("Enter first name to delete: ")
    delete_entry_by_first_name(first_name)

    phone = input("Enter phone number to delete: ")
    delete_entry_by_phone(phone)
