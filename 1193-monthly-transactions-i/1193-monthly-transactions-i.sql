SELECT 
    DATE_FORMAT(trans_date,'%Y-%m') AS month,
    country,
    COUNT(*) AS trans_count,
    COUNT(CASE WHEN state = 'approved' THEN 1 END) approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) approved_total_amount
FROM transactions
GROUP BY 
    DATE_FORMAT(trans_date,'%Y-%m'),
    country