import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('food_log.db')

# Create a cursor object
cursor = conn.cursor()


# Function to display table data
def display_table_data(table_name, header, query):
    cursor.execute(query)
    rows = cursor.fetchall()

    if rows:
        print(f"\nContents of {table_name} Table")
        print(header)
        print("-" * len(header))
        for row in rows:
            print(row)
    else:
        print(f"No data available in {table_name} table.")


# Query to display data from the food table
display_table_data(
    "food",
    f"{'ID':<5} {'Name':<20} {'Protein':<10} {'Carbohydrates':<15} {'Fat':<5} {'Calories':<10}",
    "SELECT * FROM food;"
)

# Query to display data from the log_date table
display_table_data(
    "log_date",
    f"{'ID':<5} {'Entry Date':<20}",
    "SELECT * FROM log_date;"
)

# Query to display data from the food_date table
display_table_data(
    "food_date",
    f"{'Food ID':<10} {'Log Date ID':<10}",
    "SELECT * FROM food_date;"
)

# Close the connection
conn.close()
