-- Write your query below
SELECT s.name FROM sales_person s 
WHERE NOT EXISTS (
    SELECT 1
    FROM orders o JOIN company c
    ON c.com_id=o.com_id 
    WHERE o.sales_id = s.sales_id
      AND c.name = 'CRIMSON'
);