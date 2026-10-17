SELECT 
    e.name AS employee
FROM employee e
JOIN employee t
ON e.managerId = t.id
WHERE e.salary > t.salary