-- Displays the top 3 cities by average temperature during July and August, descending.
-- Average the values of months 7 and 8 per city and keep the top 3
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month = 7 OR month = 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
