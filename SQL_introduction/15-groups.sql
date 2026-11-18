-- Lists the number of records with the same score in the table second_table.
-- Count the records per score, with the biggest groups first
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
