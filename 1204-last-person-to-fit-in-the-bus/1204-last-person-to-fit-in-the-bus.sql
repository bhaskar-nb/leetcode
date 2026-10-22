WITH main AS(
    SELECT 
        person_name,
        weight,
        turn,
        SUM(weight) OVER(ORDER BY turn) AS total_weight
    FROM queue
    ORDER BY turn ASC
)
SELECT 
    person_name
FROM main
WHERE total_weight <= 1000
ORDER BY turn DESC 
LIMIT 1