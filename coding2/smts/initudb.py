import sqlite3

# Connect to (or create) the database file
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create the users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    uid INTEGER UNIQUE NOT NULL
)
''')

# Commit and close
conn.commit()
conn.close()

print("Database and table created successfully.")
