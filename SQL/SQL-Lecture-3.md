# SQL Lecture 3(WHERE STATEMENT)

- WHERE Statment
- NOT EQUAL TO
- Greater than & Less Than
- AND, OR, LIKE, NULL, NOT NULL, IN, BETWEEN

## STEP 1: WHERE Statment

WHERE statement is used to filter in SQL.

```sql
SELECT * FROM EmployeeData
WHERE FirstName = 'Sarah'
```

### STEP 2: Other Operators with WHERE statement

1. **Is not Equal <>**

```sql
SELECT * FROM EmployeeData
WHERE FirstName <> 'Sarah'
```

1. **Greater & Less than**

```sql
-- Graeter than
SELECT * FROM EmployeeData
WHERE Age > 30

-- Graeter than Equal to
SELECT * FROM EmployeeData
WHERE Age >= 30

-- Less than
SELECT * FROM EmployeeData
WHERE Age < 30

-- Less than Equal to
SELECT * FROM EmployeeData
WHERE Age =< 30
```

1. **AND**

AND operator means we will get output when both conditions are TRUE

```sql
SELECT * FROM EmployeeData
WHERE Age = 30 AND Gender = 'Male'
```

1. **OR**

OR operator means we will get output when any one of the conditions is TRUE

```sql
SELECT * FROM EmployeeData
WHERE Age = 30 OR Gender = 'Male'
```

1. **LIKE**

LIKE operator is used when we want results related to a specific letter or symbol.

For example, if we want to check whose last names start with ‘s’ then we will use LIKE.

```sql
SELECT * FROM EmployeeData
WHERE LastName LIKE '%S'
```

If we want to check if there is ‘s’ anywhere in anybody's name then

```sql
SELECT * FROM EmployeeData
WHERE LastName LIKE '%S%'
```

If we want to look for the Last Name which starts with ‘S’ and has ‘O’ in it then we will use

```sql
SELECT * FROM EmployeeData
WHERE LastName LIKE 'S%o%'
```

1. **NULL % NOT NULL**

To see if there is any NULL or not

1. **IN** 

With IN we can search for different things at the same time

```sql
SELECT * FROM EmployeeData
WHERE FirstName IN ('Jane','Emily')
```

1. **BETWEEN**

```sql
SELECT * FROM EmployeeData
WHERE firstName BETWEEN 'Jane' AND 'Emily'
```
