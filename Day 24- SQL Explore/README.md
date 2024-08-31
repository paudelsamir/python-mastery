
# [Visit the SQL Practice log repository 🚀 ](https://github.com/paudelsamir/sql-log)


## This notes is for revision purpose only, created after learned SQL.


## 1. Introduction to Databases and MySQL

- A database is an organized collection of structured information or data.
- SQL (Structured Query Language) is used to communicate with and manipulate databases.
- MySQL is an open-source relational database management system (RDBMS) that uses SQL.
- Key concepts: tables, rows (records), columns (fields), primary keys.

## 2. Basic SQL Syntax and Structure

- SQL keywords are typically written in ALL CAPS (convention, not required).
- Statements end with a semicolon `;`.
- SQL is not case-sensitive for keywords, but it is for database/table/column names (depending on settings).
- Basic structure: `ACTION on OBJECT`

Example:
```sql
SELECT column_name FROM table_name;
```

## 3. CREATE, USE, and DROP Databases

- CREATE DATABASE: Creates a new database
- USE: Selects a database to work with
- DROP DATABASE: Deletes a database

Examples:
```sql
CREATE DATABASE my_database;
USE my_database;
DROP DATABASE my_database;
```

## 4. CREATE, ALTER, and DROP Tables

- CREATE TABLE: Creates a new table
- ALTER TABLE: Modifies an existing table structure
- DROP TABLE: Deletes a table

Examples:
```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    hire_date DATE
);

ALTER TABLE employees ADD COLUMN salary DECIMAL(10, 2);

DROP TABLE employees;
```

## 5. Data Types in MySQL

Common data types:
- Numeric: INT, TINYINT, BIGINT, FLOAT, DOUBLE, DECIMAL
- String: CHAR, VARCHAR, TEXT
- Date and Time: DATE, TIME, DATETIME, TIMESTAMP
- Boolean: BOOLEAN (TINYINT(1))

## 6. INSERT Statements to Add Data

Used to add new records to a table.

Example:
```sql
INSERT INTO employees (id, name, hire_date)
VALUES (1, 'John Doe', '2023-01-15');
```

## 7. SELECT Statements for Basic Data Retrieval

Retrieves data from one or more tables.

Example:
```sql
SELECT name, hire_date FROM employees;
```

## 8. WHERE Clause for Filtering Data

Specifies conditions that must be met for the rows to be returned.

Example:
```sql
SELECT * FROM employees WHERE hire_date > '2022-01-01';
```

## 9. ORDER BY for Sorting Results

Sorts the result set in ascending (ASC) or descending (DESC) order.

Example:
```sql
SELECT * FROM employees ORDER BY hire_date DESC;
```

## 10. UPDATE and DELETE Statements

UPDATE: Modifies existing records
DELETE: Removes records from a table

Examples:
```sql
UPDATE employees SET salary = 50000 WHERE id = 1;

DELETE FROM employees WHERE id = 1;
```

## 11. Basic Arithmetic Operations in Queries

SQL supports +, -, *, / operations in queries.

Example:
```sql
SELECT name, salary, salary * 1.1 AS increased_salary FROM employees;
```

## 12. Introduction to NULL Values

NULL represents missing or unknown data.

Example:
```sql
SELECT * FROM employees WHERE salary IS NULL;
```

## 13. LIMIT Clause to Restrict Results

Specifies the maximum number of rows to return.

Example:
```sql
SELECT * FROM employees ORDER BY hire_date DESC LIMIT 5;
```

## 14. DISTINCT Keyword to Remove Duplicates

Returns only distinct (different) values.

Example:
```sql
SELECT DISTINCT department FROM employees;
```

## 15. Basic String Functions

Common string functions: CONCAT, SUBSTRING, LENGTH, UPPER, LOWER

Example:
```sql
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM employees;
```

## 16. Simple JOIN Operations (INNER JOIN)

Combines rows from two or more tables based on a related column between them.

Example:
```sql
SELECT employees.name, departments.dept_name
FROM employees
INNER JOIN departments ON employees.dept_id = departments.id;
```

## 17. Basic Aggregate Functions

Common aggregate functions: COUNT, SUM, AVG, MIN, MAX

Example:
```sql
SELECT AVG(salary) AS average_salary FROM employees;
```

## 18. GROUP BY Clause

Groups rows that have the same values in specified columns.

Example:
```sql
SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department;
```

## 19. HAVING Clause for Filtering Grouped Data

Specifies a search condition for a group or an aggregate.

Example:
```sql
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;
```

## 20. Basic Subqueries

A query nested inside another query.

Example:
```sql
SELECT name
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```
