
import sqlite3

def create_community_table():
    try:
        conn = sqlite3.connect('database/community.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS community (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            message TEXT,
                            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                        )''')
        conn.commit()
        print("Community table created successfully.")
    except Exception as e:
        print(f"Error creating table: {e}")
    finally:
        conn.close()

def add_message(name, message):
    try:
        conn = sqlite3.connect('database/community.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO community (name, message) VALUES (?, ?)', (name, message))
        conn.commit()
        print("Message added to the community.")
    except Exception as e:
        print(f"Error adding message: {e}")
    finally:
        conn.close()

def view_messages():
    try:
        conn = sqlite3.connect('database/community.db')
        cursor = conn.cursor()
        cursor.execute('SELECT name, message, timestamp FROM community ORDER BY timestamp DESC')
        messages = cursor.fetchall()
        for msg in messages:
            print(f"{msg[2]} - {msg[0]}: {msg[1]}")
    except Exception as e:
        print(f"Error fetching messages: {e}")
    finally:
        conn.close()

if __name__ == '__main__':
    create_community_table()
    while True:
        print("1. Add Message\n2. View Messages\n3. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            name = input("Enter your name: ")
            message = input("Enter your message: ")
            add_message(name, message)
        elif choice == '2':
            view_messages()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
