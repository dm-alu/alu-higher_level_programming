-- Lists the score and name of the records of second_table that have a name, top score first.
-- Select the records with a name ordered by score in descending order
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
