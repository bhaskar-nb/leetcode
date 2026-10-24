WITH main AS 
(
    SELECT 
        e.employee_id
    FROM employees e
    LEFT JOIN employees m
    ON e.manager_id = m.employee_id
    WHERE e.salary < 30000 
        AND e.manager_id IS NOT NULL
        AND m.employee_id IS NULL 
)
SELECT 
    employee_id
FROM main
ORDER BY employee_id