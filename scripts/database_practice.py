import sqlite3
import os

# Create a database file (like creating an Excel file)
db_file = "my_books.db"

# Connect to it
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create a table (like creating a sheet in Excel with columns)
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    rating INTEGER,
    date_read TEXT
)
""")

print("=" * 60)
print("BOOKS DATABASE")
print("=" * 60)

# Add some sample data
cursor.execute("INSERT INTO books (title, author, rating, date_read) VALUES (?, ?, ?, ?)",
               ("Red rising", "Pierce Brown", 5, "2026-01-15"))
cursor.execute("INSERT INTO books (title, author, rating, date_read) VALUES (?, ?, ?, ?)",
               ("The giver", "Lois Lowry", 4, "2026-02-03"))

# Save changes
conn.commit()

# Read all data back
cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()

print("\n📚 Your Books Collection:\n")
for row in rows:
    print(f"   {row[1]} by {row[2]} - ⭐ {row[3]}/5 - Read on {row[4]}")

# Close the connection
conn.close()

print("\n✅ Database saved to:", db_file)
print("=" * 60)
