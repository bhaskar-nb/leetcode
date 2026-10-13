WITH cte_main AS 
(
    SELECT
        customer_id,
        MIN(order_date) AS first_date
    FROM delivery
    GROUP BY customer_id
)
SELECT 
    ROUND(AVG(d.order_date = d.customer_pref_delivery_date ) * 100, 2) AS immediate_percentage 
FROM cte_main c
JOIN delivery d
ON c.customer_id = d.customer_id
    AND c.first_date = d.order_date