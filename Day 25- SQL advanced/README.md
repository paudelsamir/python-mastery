# Advanced SQL with MySQL: Detailed Notes

## 1. Complex JOIN Operations

Beyond INNER JOIN, MySQL supports other types of JOINs:

- LEFT JOIN: Returns all records from the left table and matched records from the right table
- RIGHT JOIN: Returns all records from the right table and matched records from the left table
- FULL OUTER JOIN: Returns all records when there's a match in either left or right table (simulated in MySQL)
- CROSS JOIN: Returns the Cartesian product of both tables

Example of LEFT JOIN:
```sql
SELECT customers.name, orders.order_id
FROM customers
LEFT JOIN orders ON customers.customer_id = orders.customer_id;
```

## 2. Advanced Subqueries

Subqueries can be used in various parts of a SQL statement:

- In the SELECT clause (scalar subquery)
- In the FROM clause (derived table)
- In the WHERE clause (correlated subquery)

Example of a correlated subquery:
```sql
SELECT employee_name, salary
FROM employees e1
WHERE salary > (
    SELECT AVG(salary)
    FROM employees e2
    WHERE e1.department = e2.department
);
```

## 3. UNION, INTERSECT, and EXCEPT Operations

- UNION: Combines result sets of two or more SELECT statements
- INTERSECT: Returns rows that are common to both SELECT statements (simulated in MySQL)
- EXCEPT: Returns rows from the first SELECT statement that aren't in the second (simulated in MySQL)

Example of UNION:
```sql
SELECT product_name FROM products
UNION
SELECT service_name FROM services;
```

## 4. Window Functions

Window functions perform calculations across a set of rows that are related to the current row.

Common window functions: ROW_NUMBER(), RANK(), DENSE_RANK(), LAG(), LEAD()

Example:
```sql
SELECT 
    employee_name,
    salary,
    ROW_NUMBER() OVER (ORDER BY salary DESC) as salary_rank
FROM employees;
```

## 5. Common Table Expressions (CTEs)

CTEs provide a way to write auxiliary statements for use in a larger query.

Example:
```sql
WITH high_value_orders AS (
    SELECT customer_id, SUM(total_amount) as total_spent
    FROM orders
    GROUP BY customer_id
    HAVING SUM(total_amount) > 10000
)
SELECT c.customer_name, hvo.total_spent
FROM customers c
JOIN high_value_orders hvo ON c.customer_id = hvo.customer_id;
```

## 6. Recursive Queries

Recursive CTEs allow you to reference the CTE itself within its own definition.

Example (generating a sequence):
```sql
WITH RECURSIVE sequence(n) AS (
    SELECT 1
    UNION ALL
    SELECT n + 1 FROM sequence WHERE n < 10
)
SELECT * FROM sequence;
```

## 7. Stored Procedures and Functions

Stored procedures are prepared SQL code that you can save and reuse.

Example of creating a stored procedure:
```sql
DELIMITER //
CREATE PROCEDURE GetEmployeesByDepartment(IN dept_name VARCHAR(50))
BEGIN
    SELECT * FROM employees WHERE department = dept_name;
END //
DELIMITER ;

-- To call the procedure:
CALL GetEmployeesByDepartment('Sales');
```

## 8. Triggers and Events

Triggers are database operations that are automatically performed when a specified database event occurs.

Example of creating a trigger:
```sql
CREATE TRIGGER before_employee_update 
    BEFORE UPDATE ON employees
    FOR EACH ROW 
BEGIN
    IF NEW.salary < OLD.salary THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Salary cannot be reduced';
    END IF;
END;
```

## 9. Transactions and ACID Properties

Transactions group a set of tasks into a single execution unit. ACID ensures reliability in transaction processing:

- Atomicity: All operations in a transaction succeed or they all fail
- Consistency: Database remains in a consistent state before and after transaction
- Isolation: Concurrent execution of transactions results in a system state that would be obtained if transactions were executed serially
- Durability: Once a transaction has been committed, it will remain so

Example:
```sql
START TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE account_id = 123;
UPDATE accounts SET balance = balance + 100 WHERE account_id = 456;
COMMIT;
```

## 10. Views

Views are virtual tables based on the result of a SELECT statement.

Example:
```sql
CREATE VIEW high_salary_employees AS
SELECT * FROM employees WHERE salary > 100000;

-- Using the view
SELECT * FROM high_salary_employees;
```

## 11. Indexing and Query Optimization

Indexes improve the speed of data retrieval operations on database tables.

Example of creating an index:
```sql
CREATE INDEX idx_last_name ON employees(last_name);
```

Query optimization involves structuring queries to improve performance, often using EXPLAIN to analyze query execution plans.

## 12. Full-text Search

Full-text search allows you to search for words and phrases in text columns.

Example:
```sql
CREATE FULLTEXT INDEX idx_article_content ON articles(content);

SELECT * FROM articles
WHERE MATCH(content) AGAINST('database optimization' IN NATURAL LANGUAGE MODE);
```

## 13. Partitioning

Partitioning allows you to divide large tables into smaller, more manageable parts.

Example:
```sql
CREATE TABLE sales (
    id INT,
    sale_date DATE,
    amount DECIMAL(10,2)
)
PARTITION BY RANGE (YEAR(sale_date)) (
    PARTITION p0 VALUES LESS THAN (2020),
    PARTITION p1 VALUES LESS THAN (2021),
    PARTITION p2 VALUES LESS THAN (2022),
    PARTITION p3 VALUES LESS THAN MAXVALUE
);
```

## 14. JSON Data Type and Operations

MySQL provides native JSON data type support and functions to work with JSON data.

Example:
```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    user_info JSON
);

INSERT INTO users (id, user_info) VALUES (1, '{"name": "John", "age": 30, "city": "New York"}');

SELECT id, JSON_EXTRACT(user_info, '$.name') AS name
FROM users;
```

