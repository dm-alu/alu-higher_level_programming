-- Creates the table unique_id where id has the default value 1 and is unique.
-- Create unique_id if it is missing
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
