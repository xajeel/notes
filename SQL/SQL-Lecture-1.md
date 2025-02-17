# SQL Lecture 1 (CREATION & MANIPULATION)

- Creating Database
- Creating Tables
- Inserting Vales in Tabale
- Updating values in Table
- ALTER TABLE
- TRUNCATE TABLE
- DROP TABLE

```sql
-- Creating a customer Database

CREATE DATABASE testdb;

-- Creating customer table

CREATE TABLE customer 
(
	"ID" INT NOT NULL,
	"Name" varchar(50) NOT NULL,
	"Age" INT NOT NULL,
	"City" char(50) NOT NULL,
	"Salary" numeric
)

--Insert values of attributes in the customer table

INSERT INTO customer ("ID", "Name", "Age", "City", "Salary")
VALUES 
(4, 'John Doe', 30, 'New York', 5000),
(5, 'Jane Smith', 28, 'Los Angeles', 6000),
(6, 'Michael Johnson', 35, 'Chicago', 5500),
(7, 'Emily Williams', 32, 'San Francisco', 5200),
(8, 'David Brown', 27, 'Seattle', 4800);
(9, 'David', 32, 'San Francisco', 10000),
(10, 'Jane Brown', 25, 'New York', 5000);

-- Updating Salary values in Customer

UPDATE customer 
SET "Salary" = 2000 WHERE "ID" = 2;

-- Altering Table

ALTER TABLE customer
ADD "Job_Title" VARCHAR(50);

ALTER TABLE customer
ALTER COLUMN "Job_Title" CHAR(50); 
(-- If the existing data in the column does not match with 
the new data type then it can cause problems)

ALTER TABLE customer
DROP COLUMN "Job_Title";

-- Truncate Table will delete all the data in a table

TRUNCATE TABLE customer

-- Dropping / Deleting table

DROP TABLE customer
IMMEDIATE;

-- Selecting Everything in the customer

SELECT * FROM customer

```
