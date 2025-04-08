import sqlite3

def insert_user(username, uid):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO users (username, uid) VALUES (?, ?)", (username, uid))
        conn.commit()
        print(f"User {username} with UID {uid} added successfully.")
    except sqlite3.IntegrityError:
        print("Error: Username or UID already exists.")
    
    conn.close()

def find_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT uid FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    
    conn.close()
    
    return user

def get_users():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    
    conn.close()
    
    return users
