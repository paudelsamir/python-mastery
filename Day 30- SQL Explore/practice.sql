-- Create a database for an online bookstore
CREATE DATABASE online_bookstore;

-- Use the newly created database
USE online_bookstore;

-- Create a table for authors
CREATE TABLE authors (
    author_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birth_date DATE
);

-- Create a table for books
CREATE TABLE books (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    author_id INT,
    publication_date DATE,
    price DECIMAL(10, 2),
    stock INT,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

-- Insert some sample data into the authors table
INSERT INTO authors (first_name, last_name, birth_date)
VALUES 
    ('Jane', 'Austen', '1775-12-16'),
    ('George', 'Orwell', '1903-06-25'),
    ('J.K.', 'Rowling', '1965-07-31');

-- Insert some sample data into the books table
INSERT INTO books (title, author_id, publication_date, price, stock)
VALUES 
    ('Pride and Prejudice', 1, '1813-01-28', 12.99, 50),
    ('1984', 2, '1949-06-08', 10.99, 75),
    ('Harry Potter and the Philosopher''s Stone', 3, '1997-06-26', 15.99, 100),
    ('Emma', 1, '1815-12-23', 11.99, 30);

-- Basic SELECT with WHERE clause and ORDER BY
-- Retrieve all books priced under $15, ordered by price
SELECT title, price
FROM books
WHERE price < 15
ORDER BY price;

-- Using JOIN to combine data from two tables
-- List all books with their authors' full names
SELECT 
    b.title,
    CONCAT(a.first_name, ' ', a.last_name) AS author_name,
    b.publication_date
FROM 
    books b
INNER JOIN 
    authors a ON b.author_id = a.author_id;

-- Subquery example
-- Find books that are priced higher than the average book price
SELECT title, price
FROM books
WHERE price > (SELECT AVG(price) FROM books);

-- Aggregate functions with GROUP BY and HAVING
-- Count the number of books by each author, but only for authors with more than one book
SELECT 
    a.author_id,
    CONCAT(a.first_name, ' ', a.last_name) AS author_name,
    COUNT(*) AS book_count
FROM 
    authors a
INNER JOIN 
    books b ON a.author_id = b.author_id
GROUP BY 
    a.author_id
HAVING 
    COUNT(*) > 1;

-- UPDATE statement to change the price of a book
UPDATE books
SET price = 13.99
WHERE title = 'Pride and Prejudice';

-- Using a transaction to ensure data integrity when performing multiple operations
START TRANSACTION;

-- Decrease the stock of a book (simulating a sale)
UPDATE books
SET stock = stock - 1
WHERE book_id = 1;

-- Insert a record into a sales table (assuming we had one)
-- INSERT INTO sales (book_id, sale_date, quantity) VALUES (1, CURDATE(), 1);

-- If everything is okay, commit the transaction
COMMIT;
-- If there was an error, you would use ROLLBACK instead of COMMIT

-- Using LIMIT to get the top 3 most expensive books
SELECT title, price
FROM books
ORDER BY price DESC
LIMIT 3;

-- Demonstrating NULL handling
-- Let's assume some books might not have a publication date
ALTER TABLE books MODIFY COLUMN publication_date DATE NULL;

INSERT INTO books (title, author_id, price, stock)
VALUES ('Unpublished Manuscript', 3, 0, 1);

-- Find all books without a publication date
SELECT title
FROM books
WHERE publication_date IS NULL;

-- Using string functions
-- Get the year from the publication date and the length of the title
SELECT 
    title,
    YEAR(publication_date) AS pub_year,
    LENGTH(title) AS title_length
FROM 
    books
WHERE 
    publication_date IS NOT NULL;

-- Demonstrate the use of aggregate functions
SELECT 
    COUNT(*) AS total_books,
    AVG(price) AS average_price,
    MIN(price) AS cheapest_book,
    MAX(price) AS most_expensive_book,
    SUM(stock) AS total_stock
FROM 
    books;