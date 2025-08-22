import sqlite3
import csv

# Connect to the SQLite database
conn = sqlite3.connect('clues.db')  # Replace with your actual .db file
cursor = conn.cursor()

# Fetch the results from the newly created table
cursor.execute("SELECT * FROM airdates")
rows = cursor.fetchall()

# Get column names (from cursor.description)
columns = [description[0] for description in cursor.description]

# Write the results to a CSV file
with open('joined_table.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write the column names as the header row
    csv_writer.writerow(columns)
    
    # Write the data rows
    csv_writer.writerows(rows)

# Close the connection
conn.close()

print("The joined table has been written to 'joined_table.csv'")

