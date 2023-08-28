import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Restaurants (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Customers (
                id INTEGER PRIMARY KEY,
                given_name TEXT NOT NULL,
                family_name TEXT NOT NULL
            )
        ''')

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

        self.conn.commit()

    def insert_restaurant(self, name):
        self.cursor.execute('INSERT INTO Restaurants (name) VALUES (?)', (name,))
        self.conn.commit()

    def insert_customer(self, given_name, family_name):
        self.cursor.execute('INSERT INTO Customers (given_name, family_name) VALUES (?, ?)', (given_name, family_name))
        self.conn.commit()

    def insert_review(self, customer_id, restaurant_id, rating):
        self.cursor.execute('INSERT INTO Reviews (customer_id, restaurant_id, rating) VALUES (?, ?, ?)', (customer_id, restaurant_id, rating))
        self.conn.commit()

    #methods for querying data 

    def close(self):
        self.conn.close()

# Usage
db = Database("yelp_database.db")
db.create_tables()

db.insert_restaurant("Icecream Prestige")
db.insert_restaurant("Nyama Zone")

db.insert_customer("Kennedy", "Rotich")
db.insert_customer("Layerson", "Maingi")

db.insert_review(customer_id=1, restaurant_id=1, rating=4)
db.insert_review(customer_id=1, restaurant_id=2, rating=5)
db.insert_review(customer_id=2, restaurant_id=1, rating=3)

db.close()
