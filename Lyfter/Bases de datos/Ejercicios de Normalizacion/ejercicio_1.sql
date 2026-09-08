CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(50),
    PhoneNumber VARCHAR(15)
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    Address VARCHAR(100),
    Deliverytime DATETIME,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

CREATE TABLE Product (
    ProductID INT PRIMARY KEY,
    Name VARCHAR(50),
    Price DECIMAL(10, 2)
);

CREATE TABLE Order_Item (
    OrderItemID INTEGER PRIMARY KEY AUTOINCREMENT, 
    OrderID INT,
    ProductID INT,
    Quantity INT,
    SpecialRequest VARCHAR(255),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);

INSERT INTO Customer (CustomerID, Name, PhoneNumber) VALUES
    (1, 'Alice', '123-456-7890'),
    (2, 'Bob', '987-654-3210'),
    (3, 'Claire', '555-123-4567');

INSERT INTO Product (ProductID, Name, Price) VALUES
    (101, 'Cheeseburger', 8.00),
    (102, 'Fries', 3.00),
    (103, 'Pizza', 12.00),
    (105, 'Salad', 6.00),
    (106, 'Water', 1.00);

INSERT INTO Orders (OrderID, CustomerID, Address, Deliverytime) VALUES
    (1, 1, '123 Main St', '18:00:00'),
    (2, 2, '456 Elm St', '19:30:00'),
    (3, 3, '789 Oak St', '12:00:00'),
    (4, 3, '464 Georgia St', '17:00:00');

INSERT INTO Order_Item (OrderID, ProductID, Quantity, SpecialRequest)
VALUES
    (1, 101, 2, 'No onions'),
    (1, 102, 1, 'Extra ketchup'),
    (2, 103, 1, 'Extra cheese'),
    (2, 102, 2, 'None'),
    (3, 105, 1, 'No croutons'),
    (4, 106, 1, 'None');

SELECT * FROM Customer;
SELECT * FROM Orders;
SELECT * FROM Product;
SELECT * FROM Order_Item;