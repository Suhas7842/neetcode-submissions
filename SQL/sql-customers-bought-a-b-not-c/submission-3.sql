-- Write your query below
SELECT c.customer_id, c.customer_name
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING COUNT(*) FILTER (WHERE o.product_name = 'A') > 0
   AND COUNT(*) FILTER (WHERE o.product_name = 'B') > 0
   AND COUNT(*) FILTER (WHERE o.product_name = 'C') = 0
ORDER BY c.customer_name;