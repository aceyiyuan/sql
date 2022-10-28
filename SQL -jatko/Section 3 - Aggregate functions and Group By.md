# Group by

Lähde: https://www.w3resource.com/sqlite-exercises/sqlite-aggregate-functions-group-by-exercises.php

1.  Write a query to get the number of employees with the same job.
```SQL
SELECT job_id, COUNT(*)
FROM employees
GROUP BY job_id;
```

2. Write a query to find the manager IDs and the salary of the lowest-paid employee for every one of them.
```SQL
SELECT manager_id, MIN(salary)
FROM employees
WHERE manager_id IS NOT NULL
GROUP BY manager_id
ORDER BY MIN(salary) DESC;
```


3.  Write a query to get the department ID and the total salary payable in each department.
```SQL
SELECT department_id, SUM(salary)
FROM employees 
GROUP BY department_id;
```


4.  Write a query to get the average salary for each job ID excluding programmer.
```SQL
SELECT job_id, AVG(salary) 
FROM employees 
WHERE job_id <> 'IT_PROG' 
GROUP BY job_id;
```


5.  Write a query to get the total salary, maximum, minimum, average salary of employees (job ID wise), for department ID 90 only.
```SQL
SELECT job_id, SUM(salary), AVG(salary), MAX(salary), MIN(salary)
FROM employees 
WHERE department_id = '90' 
GROUP BY job_id;
```


6.  Write a query to get the job ID and maximum salary of the employees where maximum salary is greater than or equal to $4000.
```SQL
SELECT job_id, MAX(salary) 
FROM employees 
GROUP BY job_id 
HAVING MAX(salary) >=4000;
```


7.  Write a query to get the average salary for all departments employing more than 10 employees.
```SQL
SELECT job_id, AVG(salary), COUNT(*) 
FROM employees 
GROUP BY department_id
HAVING COUNT(*) > 10;
```
