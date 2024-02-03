import sqlite3
from openpyxl import Workbook

# Connect to the SQLite database
conn = sqlite3.connect('crud_app.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a SQL query to select data from a table
cursor.execute('SELECT * FROM users')

# Fetch the results of the query
rows = cursor.fetchall()

# Close the cursor and the connection
cursor.close()
conn.close()

# Create a new Excel workbook
wb = Workbook()
ws = wb.active

# Write the header row
header = ['user_id', 'name', 'email']  # Replace with your actual column names
ws.append(header)

# Write the data rows
for row in rows:
    ws.append(row)

# Save the Excel file
wb.save('output.xlsx')
