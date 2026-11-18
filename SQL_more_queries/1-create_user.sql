-- Creates the MySQL server user user_0d_1 with all privileges and the password user_0d_1_pwd.
-- Create the user if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Give the user all privileges on the server
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
