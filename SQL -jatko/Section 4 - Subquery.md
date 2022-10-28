# Subquery

Lähde: https://www.w3resource.com/sqlite-exercises/sqlite-subquery-exercises.php

1. Write a query to find the names (first_name, last_name) and salaries of the employees who have a higher salary than the employee whose last_name='Bull'.
```SQL
SELECT first_name, last_name, salary 
FROM employees 
WHERE salary > (SELECT salary FROM employees WHERE last_name='Bull');
```


2. Write a query to find the names (first_name, last_name) of all employees who works in the IT department.
```SQL
SELECT first_name, last_name 
FROM employees 
WHERE department_id IN (SELECT department_id FROM departments WHERE depart_name='IT');
```


3. Write a query to find the names (first_name, last_name) of the employees who have a manager who works for a department based in the United States.
```SQL
SELECT first_name, last_name FROM employees 
WHERE manager_id IN (
    SELECT employee_id FROM employees 
    WHERE department_id IN (
        SELECT department_id FROM departments 
        WHERE location_id IN (select location_id from locations where country_id='US')
    )
);
```


4. Write a query to find the names (first_name, last_name) of the employees who are managers.
```SQL
SELECT first_name, last_name 
FROM employees 
WHERE employee_id IN (SELECT manager_id FROM employees);
```


5. Write a query to find the names (first_name, last_name), the salary of the employees whose salary is greater than the average salary.
```SQL
SELECT first_name, last_name, salary FROM employees 
WHERE salary > (SELECT AVG(salary) FROM employees);
```


6. Write a query to find the names (first_name, last_name), the salary of the employees whose salary is equal to the minimum salary for their job grade.
```SQL
SELECT first_name, last_name, salary 
FROM employees 
WHERE salary = (SELECT min_salary FROM jobs WHERE employees.job_id = jobs.job_id);
```


7.  Write a query to find the names (first_name, last_name), the salary of the employees who earn more than the average salary and who works in any of the IT departments.
```SQL
SELECT first_name,last_name,salary 
FROM employees
WHERE department_id IN (
    SELECT department_id
    FROM departments
    WHERE depart_name LIKE 'IT%'
) AND salary > (
    SELECT avg(salary)
    FROM employees
);
```


8.  Write a query to find the names (first_name, last_name), the salary of the employees who earn more than Mr. Bell.
```SQL
SELECT first_name, last_name, salary
FROM employees
WHERE salary>(SELECT salary FROM employees WHERE last_name='Bell');
```


9.  Write a query to find the names (first_name, last_name), the salary of the employees who earn the same salary as the minimum salary of the employees.
```SQL
SELECT * FROM employees 
WHERE salary = (SELECT MIN(salary) FROM employees);
```


10.  Write a query to find the names (first_name, last_name) of the employees who are not supervisors.
```SQL
SELECT first_name, last_name, salary 
FROM employees 
WHERE employee_id NOT IN (
    SELECT manager_id FROM departments WHERE manager_id <> ''
);
```


11.  Write a query to display the employee ID, first name, last names, salary of all employees whose salary is above average for their departments.
```SQL
SELECT employee_id, first_name 
FROM employees AS A 
WHERE salary > 
( SELECT AVG(salary) FROM employees WHERE department_id = A.department_id);
```


12.  Write a query to select last 10 records from a table. This 10 records should be ordered by employee_id.
```SQL
SELECT * FROM (
SELECT * FROM employees ORDER BY employee_id DESC LIMIT 10)
ORDER BY employee_id ASC;
```


13.  Write a query to list department number, name for all the departments in which there are no employees in the department.
```SQL
SELECT department_id, department_name FROM departments 
WHERE department_id 
NOT IN (select DISTINCT(department_id) FROM employees);
```
