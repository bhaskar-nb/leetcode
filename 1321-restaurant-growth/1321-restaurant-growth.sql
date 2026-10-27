WITH main AS
(
SELECT 
    visited_on,
    SUM(amount) AS amount
FROM customer
GROUP BY visited_on
)
,rolling_totals AS 
(
SELECT 
    visited_on,
    SUM(amount) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
    ROUND((SUM(amount) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) / 7), 2) AS average_amount
FROM main
)
SELECT 
    visited_on,
    amount,
    average_amount
FROM rolling_totals
WHERE visited_on >= 
(SELECT DATE_ADD(MIN(visited_on), INTERVAL 6 DAY) FROM customer)