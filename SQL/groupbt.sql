-- write a query to find avg marks in each city ascending order

SELECT city, avg(marks) as avg_marks
FROM students GROUP BY city
ORDER BY avg_marks ASC;