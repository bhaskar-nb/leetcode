SELECT 
    e.name
FROM Employee e
JOIN Employee ep
ON e.id = ep.managerId
GROUP BY 
    e.id,
    e.name
HAVING COUNT(ep.managerId) >= 5;