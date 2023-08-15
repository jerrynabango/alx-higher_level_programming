-- script converts hbtn_0c_0 db to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
--convert all of the following to UTF8:
-- Database hbtn_0c_0
-- Table first_table
-- Field name in first_table
USE `hbtn_0c_0`
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

