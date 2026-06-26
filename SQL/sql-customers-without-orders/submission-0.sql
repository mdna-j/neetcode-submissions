-- Write your query below
SELECT c.name AS name
FROM Customers c
LEFT JOIN Orders o ON c.id = o.customer_id
WHERE o.customer_id IS NULL;
