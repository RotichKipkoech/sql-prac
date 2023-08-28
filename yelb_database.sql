CREATE TABLE Restaurants (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE Customers (
    id INTEGER PRIMARY KEY,
    given_name TEXT NOT NULL,
    family_name TEXT NOT NULL
);

CREATE TABLE Reviews (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    restaurant_id INTEGER,
    rating INTEGER,
    FOREIGN KEY (customer_id) REFERENCES Customers(id),
    FOREIGN KEY (restaurant_id) REFERENCES Restaurants(id)
);
