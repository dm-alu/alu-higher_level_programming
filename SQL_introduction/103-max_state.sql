-- Displays the max temperature of each state, ordered by state name.
-- Take the maximum value per state
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
