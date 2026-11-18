-- Creates the table force_name where name can not be null.
-- Create force_name if it is missing
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
