# Perus SELECT harjoituksia

Lähde: https://www.w3resource.com/sqlite-exercises/sqlite-basic-simple-exercises.php

1. Write a query to display the names (first_name, last_name) using alias name "First Name", "Last Name" (employees)
```SQL
SELECT first_name AS "First Name", last_name AS "Last Name" FROM employees;
```


2. Write a query to get unique department ID from employee table.
```SQL
SELECT DISTINCT department_id FROM employees;
```


3. Write a query to get all employee details from the employee table order by first name, descending.
```SQL
SELECT * FROM employees ORDER BY first_name DESC;
```


4. Write a query to get the names (first_name, last_name), salary and PF of all the employees (PF is calculated as 12% of salary).
```SQL
SELECT first_name, last_name, salary, salary * .12 AS PF FROM employees;
```


5. Write a query to get the employee ID, names (first_name, last_name), salary in ascending order of salary.
```SQL
SELECT employee_id, first_name, last_name, salary from employees ORDER BY salary;
```


6. Write a query to get the total salaries payable to employees.
```SQL
SELECT SUM(salary) FROM employees;
```


7. Write a query to get the maximum and minimum salary from employees table.
```SQL
SELECT MAX(salary), MIN(salary) FROM employees;
```


8. Write a query to get the average salary and number of employees in the employees table.
```SQL
SELECT AVG(salary), COUNT(*) FROM employees;
```


9. Write a query to get the number of employees working with the company.
```SQL
SELECT COUNT(*) FROM employees;
```


10. Write a query to get the number of jobs available in the employees table.
```SQL
SELECT COUNT(DISTINCT job_id) FROM employees;
```


11. Write a query get all first name from employees table in upper case.
```SQL
SELECT UPPER(first_name) FROM employees;
```


12. Write a query to get the first 3 characters of first name from employees table.
```SQL
SELECT SUBSTRING(first_name,1,3) FROM employees;
```


13. Write a query to calculate 171*214+625.
```SQL
SELECT 171*214+625 AS 'Result';
```


14. Write a query to get the full names (for example Ellen Abel, Sundar Ande etc.) of all the employees from employees table.
```SQL
SELECT first_name || ' ' || last_name AS 'Employee Name' FROM employees;
```


15. Write a query to get first name from employees table after removing white spaces from both side.
```SQL
SELECT TRIM(first_name) FROM employees;
```


16. Write a query to get the length of the employee names (first_name, last_name) from employees table.
```SQL
SELECT first_name, last_name, LENGTH(first_name)+LENGTH(last_name) AS 'Length of  Names' FROM employees;
```


17. Write a query to select first 10 records from a table.
```SQL
SELECT employee_id, first_name FROM employees LIMIT 10;
```


18. Write a query to get monthly salary (round 2 decimal places) of each and every employee
```SQL
SELECT first_name, last_name, ROUND(salary/12,2) AS 'Monthly Salary' FROM employees;
```


19. Write a query to get the average salary and number of employees working the department 90.
```SQL
SELECT AVG(salary),count(*) 
FROM employees 
WHERE department_id = 90;
```


20.  Write a query to get the highest, lowest, sum, and average salary of all employees.
```SQL
SELECT ROUND(MAX(salary),0) AS "Maximum", ROUND(MIN(salary),0) AS "Minimum", 
ROUND(SUM(salary),0) AS "Sum", ROUND(AVG(salary),0) AS "Average"
FROM employees;
```


21. Write a query to get the difference between the highest and lowest salaries.
```SQL
SELECT MAX(salary) - MIN(salary) DIFFERENCE
FROM employees;
```
