-- Advanced SQL Example Script

-- Create a database for an e-commerce platform
CREATE DATABASE IF NOT EXISTS advanced_ecommerce;
USE advanced_ecommerce;

-- Create tables with various constraints and relationships
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    registration_date DATE,
    last_login TIMESTAMP
);

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    description TEXT,
    price DECIMAL(10, 2),
    stock INT,
    category ENUM('Electronics', 'Clothing', 'Books', 'Home & Garden')
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending',
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT,
    price_at_time DECIMAL(10, 2),
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create an index on the products table
CREATE INDEX idx_product_category ON products(category);

-- Insert sample data
INSERT INTO customers (first_name, last_name, email, registration_date) VALUES
('John', 'Doe', 'john@example.com', '2023-01-15'),
('Jane', 'Smith', 'jane@example.com', '2023-02-20'),
('Alice', 'Johnson', 'alice@example.com', '2023-03-10');

INSERT INTO products (name, description, price, stock, category) VALUES
('Smartphone', 'Latest model smartphone', 699.99, 50, 'Electronics'),
('T-shirt', 'Cotton t-shirt', 19.99, 100, 'Clothing'),
('SQL Guide', 'Comprehensive SQL guide', 39.99, 30, 'Books'),
('Garden Chair', 'Outdoor furniture', 59.99, 20, 'Home & Garden');

INSERT INTO orders (customer_id, order_date) VALUES
(1, '2023-04-01 10:00:00'),
(2, '2023-04-02 11:30:00'),
(3, '2023-04-03 09:15:00');

INSERT INTO order_items (order_id, product_id, quantity, price_at_time) VALUES
(1, 1, 1, 699.99),
(1, 2, 2, 19.99),
(2, 3, 1, 39.99),
(3, 4, 1, 59.99);

-- Create a view for order summaries
CREATE VIEW order_summary AS
SELECT 
    o.order_id,
    c.first_name,
    c.last_name,
    o.order_date,
    SUM(oi.quantity * oi.price_at_time) AS total_amount
FROM 
    orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY 
    o.order_id;

-- Create a stored procedure to get top selling products
DELIMITER //
CREATE PROCEDURE GetTopSellingProducts(IN top_n INT)
BEGIN
    SELECT 
        p.name,
        SUM(oi.quantity) AS total_sold
    FROM 
        products p
    JOIN order_items oi ON p.product_id = oi.product_id
    GROUP BY 
        p.product_id
    ORDER BY 
        total_sold DESC
    LIMIT top_n;
END //
DELIMITER ;

-- Create a trigger to update stock after an order
DELIMITER //
CREATE TRIGGER after_order_insert
AFTER INSERT ON order_items
FOR EACH ROW
BEGIN
    UPDATE products
    SET stock = stock - NEW.quantity
    WHERE product_id = NEW.product_id;
END //
DELIMITER ;

-- Perform some advanced queries

-- 1. Complex JOIN with subquery and window function
SELECT 
    c.first_name,
    c.last_name,
    o.order_id,
    o.order_date,
    p.name AS product_name,
    oi.quantity,
    ROW_NUMBER() OVER (PARTITION BY c.customer_id ORDER BY o.order_date) AS order_sequence
FROM 
    customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
WHERE 
    o.order_date > (SELECT AVG(order_date) FROM orders);

-- 2. Common Table Expression (CTE) with aggregation
WITH CustomerSpending AS (
    SELECT 
        c.customer_id,
        c.first_name,
        c.last_name,
        SUM(oi.quantity * oi.price_at_time) AS total_spent
    FROM 
        customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN order_items oi ON o.order_id = oi.order_id
    GROUP BY 
        c.customer_id
)
SELECT 
    cs.first_name,
    cs.last_name,
    cs.total_spent,
    AVG(cs.total_spent) OVER () AS avg_customer_spending
FROM 
    CustomerSpending cs
WHERE 
    cs.total_spent > (SELECT AVG(total_spent) FROM CustomerSpending);

-- 3. Full-text search (first, create a FULLTEXT index)
ALTER TABLE products ADD FULLTEXT(name, description);

-- Now perform a full-text search
SELECT 
    name,
    description
FROM 
    products
WHERE 
    MATCH(name, description) AGAINST('smartphone electronics' IN NATURAL LANGUAGE MODE);

-- 4. JSON operations (assuming MySQL 5.7+)
ALTER TABLE customers ADD COLUMN preferences JSON;

UPDATE customers 
SET preferences = '{"favorite_categories": ["Electronics", "Books"], "newsletter": true}'
WHERE customer_id = 1;

SELECT 
    customer_id,
    first_name,
    JSON_EXTRACT(preferences, '$.favorite_categories') AS favorite_categories
FROM 
    customers
WHERE 
    JSON_EXTRACT(preferences, '$.newsletter') = TRUE;

-- 5. Recursive CTE (example: creating a number sequence)
WITH RECURSIVE NumberSequence AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1 FROM NumberSequence WHERE n < 10
)
SELECT * FROM NumberSequence;

-- Call the stored procedure
CALL GetTopSellingProducts(3);

-- Demonstrate a transaction
START TRANSACTION;

INSERT INTO orders (customer_id, order_date) VALUES (1, NOW());
SET @last_order_id = LAST_INSERT_ID();
INSERT INTO order_items (order_id, product_id, quantity, price_at_time)
VALUES (@last_order_id, 1, 1, (SELECT price FROM products WHERE product_id = 1));

-- Check if stock is available
SET @available_stock = (SELECT stock FROM products WHERE product_id = 1);
IF @available_stock >= 1 THEN
    COMMIT;
ELSE
    ROLLBACK;
END IF;

-- Show the results of our operations
SELECT * FROM order_summary;
SELECT * FROM products WHERE product_id = 1;

-- Clean up (comment out if you want to keep the database and data)
-- DROP DATABASE advanced_ecommerce;