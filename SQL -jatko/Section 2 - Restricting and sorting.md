# Restricting and Sorting Data

Lähde: https://www.w3resource.com/sqlite-exercises/sqlite-restricting-and-sorting-data-exercises.php

1. Write a query to display the names (first_name, last_name) and salary for all employees whose salary is not in the range $10,000 through $15,000.
```SQL
SELECT first_name, last_name, salary
FROM employees
WHERE salary NOT BETWEEN 10000 AND 15000;
```


2. Write a query to display the names (first_name, last_name) and department ID of all employees in departments 30 or 100 in ascending alphabetical order by department ID.
```SQL
SELECT first_name, last_name, department_id
FROM employees
WHERE department_id IN (30, 100)
ORDER BY department_id  ASC;
```


3. Write a query to display the names (first_name, last_name) and salary for all employees whose salary is not in the range $10,000 through $15,000 and are in department 30 or 100.
```SQL
SELECT first_name, last_name, salary, department_id
FROM employees
WHERE salary NOT BETWEEN 10000 AND 15000 
AND department_id IN (30, 100);
```


4. Write a query to display the first_name of all employees who have both an "b" and "c" in their first name.
```SQL
SELECT first_name
FROM employees
WHERE first_name LIKE '%b%'
AND first_name LIKE '%c%';
```


5.  Write a query to display the last name, job, and salary for all employees whose job is that of a Programmer or a Shipping Clerk, and whose salary is not equal to $4,500, $10,000, or $15,000.
```SQL
SELECT last_name, job_id, salary
FROM employees
WHERE job_id IN ('IT_PROG', 'SH_CLERK')
AND salary NOT IN (4500, 10000, 15000);
```


6.  Write a query to display the last names of employees whose names have exactly 6 characters.
```SQL
SELECT last_name 
FROM employees 
WHERE last_name LIKE '______';
```


7.  Write a query to display the last names of employees having 'e' as the third character.
```SQL
SELECT last_name 
FROM employees 
WHERE last_name LIKE '__e%';
```
