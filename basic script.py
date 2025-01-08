# Import necessary libraries
import sqlite3
import pandas as pd

# Create an in-memory SQLite database (or connect to an existing database file)
connection = sqlite3.connect(':memory:')  # Use ':memory:' for a temporary in-memory database

# Create a cursor object to interact with the database
cursor = connection.cursor()
# nnw
# Create a sample table and insert data
cursor.execute('''
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    gpa REAL
)
''')

# Insert sample data into the table
students_data = [
    (1, 'Alice', 3.8),
    (2, 'Bob', 3.5),
    (3, 'Charlie', 3.9),
]
cursor.executemany('INSERT INTO students VALUES (?, ?, ?)', students_data)
connection.commit()

# Run a SQL query to retrieve the data
query = "SELECT * FROM students WHERE gpa > 3.5"
df = pd.read_sql_query(query, connection)

# Display the query results
print("Students with GPA > 3.5:")
print(df)
# nnw
# Close the database connection
connection.close()
