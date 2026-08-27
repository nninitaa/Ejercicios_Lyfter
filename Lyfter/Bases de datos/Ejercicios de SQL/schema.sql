CREATE TABLE invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_number VARCHAR(50) NOT NULL UNIQUE,
    buyer_email VARCHAR(100) NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE invoices ADD phone_number VARCHAR(20);
ALTER TABLE invoices ADD employee_code VARCHAR(50);

INSERT INTO invoices (invoice_number, buyer_email, total_amount, phone_number, employee_code, purchase_date) VALUES
('INV001', 'customer1@example.com', 434000, '1234567890', 'EMP001', '2023-01-01'),
('INV002', 'customer2@example.com', 870000, '0987654321', 'EMP002', '2023-01-02'),
('INV003', 'customer3@example.com', 115000, '1122334455', 'EMP003', '2023-01-03');

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    entry_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    brand VARCHAR(100),
    stock_available INTEGER DEFAULT 0,
    code BIGINT UNIQUE
);

CREATE TABLE products_per_invoice (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    unit_price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (invoice_id) REFERENCES invoices(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

INSERT INTO products_per_invoice (invoice_id, product_id, quantity, unit_price) VALUES
(1, 1, 2, 150000),
(1, 2, 1, 134000),
(2, 3, 3, 190000),
(2, 4, 1, 290000),
(3, 5, 5, 23000);

CREATE TABLE shopping_carts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    buyer_email VARCHAR(100) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE cart_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cart_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY (cart_id) REFERENCES shopping_carts(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

INSERT INTO products (name, price, brand, stock_available, code) VALUES
('Laptop', 150000, 'BrandA', 10, 1001),
('Smartphone', 134000, 'BrandB', 20, 1002),
('Headphones', 190000, 'BrandC', 15, 1003),
('Monitor', 290000, 'BrandD', 5, 1004),
('Keyboard', 23000, 'BrandE', 25, 1005);

SELECT * FROM products;

SELECT * FROM products WHERE price > 50000;

SELECT * FROM products_per_invoice WHERE product_id = 3;

SELECT
    product_id,
    SUM(quantity) AS total_quantity,
    SUM(quantity * unit_price) AS total_price
FROM products_per_invoice
GROUP BY product_id;

SELECT * FROM invoices ORDER BY buyer_email = 'customer1@example.com';

SELECT * FROM invoices ORDER BY total_amount DESC;

SELECT * FROM invoices WHERE invoice_number = 'INV001';