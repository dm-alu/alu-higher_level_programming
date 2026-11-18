-- Creates the table id_not_null where id has the default value 1.
-- Create id_not_null if it is missing
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
