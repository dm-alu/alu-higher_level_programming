-- Creates a table called first_table in the current database without failing if it exists.
-- Create first_table if it is missing
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
