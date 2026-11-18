-- Lists the score and name of all records of second_table with a score >= 10, top first.
-- Select the best records ordered by score in descending order
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
