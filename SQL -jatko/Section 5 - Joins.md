# Joins

Lähde: https://www.w3resource.com/sqlite-exercises/sqlite-join-exercises.php

1. Write a query to find the addresses (location_id, street_address, city, state_province, country_name) of all the departments. Hint : Use NATURAL JOIN.
```SQL
SELECT location_id, street_address, city, state_province, country_name
FROM locations
NATURAL JOIN countries;
```


2. Write a query to find the names (first_name, last name), department ID and the name of all the employees.
```SQL
SELECT first_name, last_name, department_id, depart_name 
FROM employees
JOIN departments USING (department_id);
```


3. Write a query to find the employee id, name (last_name) along with their manager_id, manager name (last_name).
```SQL
SELECT e.employee_id 'Emp_Id', e.last_name 'Employee', 
m.employee_id 'Mgr_Id', m.last_name 'Manager' 
FROM employees e 
join employees m 
ON (e.manager_id = m.employee_id);
```


4. Write a query to find the names (first_name, last_name) and hire date of the employees who were hired after 'Jones'.
```SQL
SELECT e.first_name, e.last_name, e.hire_date 
FROM employees e 
JOIN employees davies 
ON (davies.last_name = "Jones") 
WHERE davies.hire_date < e.hire_date;
```


5. Write a query to get the department name and number of employees in the department.
```SQL
SELECT depart_name AS 'Department Name', 
COUNT(*) AS 'No of Employees' 
FROM departments 
INNER JOIN employees 
ON employees.department_id = departments.department_id 
GROUP BY departments.department_id, depart_name 
ORDER BY depart_name;
```


6.  Write a query to find the employee ID, job title number of days between ending date and starting date for all jobs in department 90 from job history.
```SQL
SELECT employee_id, job_title, end_date-start_date Days FROM job_history 
NATURAL JOIN jobs 
WHERE department_id=90;
```


7.  Write a query to display the department ID, department name, and manager first name.
```SQL
SELECT d.department_id, d.depart_name, e.manager_id, e.first_name 
FROM departments d 
INNER JOIN employees e 
ON (d.manager_id = e.employee_id);
```


8.  Write a query to display the department name, manager name, and city.
```SQL
SELECT d.depart_name, e.first_name, l.city 
FROM departments d 
JOIN employees e 
ON (d.manager_id = e.employee_id) 
JOIN locations l USING (location_id);
```


9.  Write a query to display the job title and average salary of employees.
```SQL
SELECT job_title, AVG(salary) 
FROM employees 
NATURAL JOIN jobs 
GROUP BY job_title;
```


10.  Write a query to to display job title, employee name, and the difference between the salary of the employee and minimum salary for the job.
```SQL
SELECT job_title, first_name, salary-min_salary 'Salary - Min_Salary' 
FROM employees 
NATURAL JOIN jobs;
```


11.  Write a query to display the job history that was done by any employee who is currently drawing more than 10000 of salary.
```SQL
SELECT jh.* FROM job_history jh 
JOIN employees e 
ON (jh.employee_id = e.employee_id) 
WHERE salary > 10000;
```
