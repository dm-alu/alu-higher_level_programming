-- Displays the average temperature (Fahrenheit) by city, ordered by temperature descending.
-- Compute the average value per city
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
