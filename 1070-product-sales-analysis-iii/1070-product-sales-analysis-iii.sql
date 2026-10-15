WITH main AS(
SELECT 
    product_id,
    MIN(year) AS first_year
FROM sales
GROUP BY product_id
)
SELECT
    s.product_id,
    m.first_year,
    s.quantity,
    s.price
FROM sales s
JOIN main m
ON s.product_id = m.product_id
    AND s.year = m.first_year