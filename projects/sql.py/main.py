import sqlite3
import matplotlib.pyplot as plt

# Function to create the database and table
def create_table():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS data
                 (id INTEGER PRIMARY KEY, value INTEGER)''')
    conn.commit()
    conn.close()

# Function to insert data into the database
def insert_data(value):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("INSERT INTO data (value) VALUES (?)", (value,))
    conn.commit()
    conn.close()

# Function to fetch data from the database
def fetch_data():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM data")
    data = c.fetchall()
    conn.close()
    return data

# Function to visualize the data
def visualize_data(data):
    values = [x[1] for x in data]
    plt.plot(values)
    plt.xlabel('Games')
    plt.ylabel('Cubes Gained')
    plt.title('Marvel Snap Cubes')
    plt.show()

# Main function
def main():
    create_table()

    # Input data
    while True:
        value = input("Enter a value (or 'q' to quit): ")
        if value.lower() == 'q':
            break
        insert_data(int(value))

    # Fetch and visualize data
    data = fetch_data()
    visualize_data(data)

if __name__ == "__main__":
    main()
