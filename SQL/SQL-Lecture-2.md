# SQL Lecture 2 (AGRIGATE FUNCTIONS)

- DELETE RECORD
- DISTINCT
- TOP, COUNT, AS, MAX, MIN
- Retrieving Data from Other DATABASE

### STEP 1 Creating EmployeeData Table

```sql
CREATE TABLE EmployeeData 
(
EmployeeId int, 
FirstName varchar(50),
LastName varchar(50),
Age int,
Gender varchar(50),
City varchar(50),
Job varchar(50),
Salaray numeric
)
```

### STEP 2 Insering Values in EmployeeData Table

```sql
INSERT INTO EmployeeData (EmployeeId, FirstName, LastName, Age, Gender, City, Job, Salaray)
VALUES 
(1, 'John', 'Doe', 30, 'Male', 'New York', 'Manager', 5000),
(2, 'Jane', 'Smith', 25, 'Female', 'London', 'Assistant', 2500),
(3, 'Michael', 'Johnson', 35, 'Male', 'Chicago', 'Analyst', 4000),
(4, 'Emily', 'Davis', 28, 'Female', 'Los Angeles', 'Developer', 4500),
(5, 'Robert', 'Wilson', 32, 'Male', 'Paris', 'Manager', 5500),
(6, 'Samantha', 'Lee', 27, 'Female', 'Tokyo', 'Assistant', 2800),
(7, 'David', 'Brown', 40, 'Male', 'Berlin', 'Analyst', 3800),
(8, 'Jennifer', 'Miller', 24, 'Female', 'Sydney', 'Developer', 4200),
(9, 'Matthew', 'Anderson', 33, 'Male', 'Toronto', 'Manager', 5200),
(10, 'Sarah', 'Wilson', 29, 'Female', 'Melbourne', 'Assistant', 2600)
```

### STEP 3 Different Function

1. **Top**

It will return top values like TOP 5 will return top 5 records ( rows ).

```sql
SELECT TOP 5 FirstName, LastName FROM EmployeeData
```

1. **DISTINCT** 

DISTINCT returns all unique values in the specified column.

```sql
SELECT DISTINCT(Age) FROM EmployeeData
```

1. **COUNT**

It counts the number of values

```sql
SELECT COUNT(LastName) FROM EmployeeData
```

1. **AS**

It can be used to give the name to the resulting column

```sql
SELECT COUNT(LastName)AS LastNameCount FROM EmployeeData
```

1. **MIN, MAX & AVG**

```sql
SELECT MAX(Salaray) FROM EmployeeData
SELECT MIN(Salaray) FROM EmployeeData
SELECT AVG(Salaray) FROM EmployeeData
```

### **STEP 4 Retrieving Data from Other DATABASE**

If we are in the SQLtutorial database and want to see everything in another database like Testdb then we will use such a query.

```sql
SELECT * FROM Testdb.dbo.EmployeeData
```
