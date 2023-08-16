-- script that creates the MySQL server user user_0d_1.
-- user_0d_1 should have all privileges on your MySQL server
-- The user_0d_1 password should be set to user_0d_1_pwd
CREATE USER IF NOT EXISTS 'user user_0d_1'@'localhost'

-- Used to create password for the user                                         
IDENTIFIED BY 'user_0d_1_pwd';                                                  

-- Have full control over the databases & tables                                
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

