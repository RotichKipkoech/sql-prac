import sqlite3

# Establish a connection to the SQLite database
# Create a cursor to interact with the database
class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    # Create 'Restaurants' table if it doesn't exist
    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Restaurants (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        ''')

        # Create 'Customers' table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Customers (
                id INTEGER PRIMARY KEY,
                given_name TEXT NOT NULL,
                family_name TEXT NOT NULL
            )
        ''')

        # Create 'Reviews' table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Reviews (
                id INTEGER PRIMARY KEY,
                customer_id INTEGER,
                restaurant_id INTEGER,
                rating INTEGER,
                FOREIGN KEY (customer_id) REFERENCES Customers(id),
                FOREIGN KEY (restaurant_id) REFERENCES Restaurants(id)
            )
        ''')

        # Commit the changes to the database
        self.conn.commit()

        # Insert a new restaurant into the 'Restaurants' table
    def insert_restaurant(self, name):
        self.cursor.execute('INSERT INTO Restaurants (name) VALUES (?)', (name,))
        self.conn.commit()

        # Insert a new customer into the 'Customers' table
    def insert_customer(self, given_name, family_name):
        self.cursor.execute('INSERT INTO Customers (given_name, family_name) VALUES (?, ?)', (given_name, family_name))
        self.conn.commit()

        # Insert a new review into the 'Reviews' table
    def insert_review(self, customer_id, restaurant_id, rating):
        self.cursor.execute('INSERT INTO Reviews (customer_id, restaurant_id, rating) VALUES (?, ?, ?)', (customer_id, restaurant_id, rating))
        self.conn.commit()

        # Close the database connection
    def close(self):
        self.conn.close()

# Usage
# Create a new instance of the Database class and specify the database name
db = Database("yelp_database.db")
db.create_tables()

# Insert restaurant records
db.insert_restaurant("Icecream Prestige")
db.insert_restaurant("Nyama Zone")

# Insert customer records
db.insert_customer("Kennedy", "Rotich")
db.insert_customer("Layerson", "Maingi")

# Insert review records
db.insert_review(customer_id=1, restaurant_id=1, rating=4)
db.insert_review(customer_id=1, restaurant_id=2, rating=5)
db.insert_review(customer_id=2, restaurant_id=1, rating=3)

# Close the database connection
db.close()
