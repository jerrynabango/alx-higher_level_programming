Creating Users, previliges, joins and db design
# JOINS: ombine data from two or more tables based on related columns. Joins allow you to retrieve data from multiple tables and create a single result set.
# Types of joins are:
	* JOIN or INNER JOIN
	* LEFT JOIN or LEFT OUTER JOIN
	* RIGHT JOIN or RIGHT OUTER JOIN
	* FULL OUTER JOIN
# IDENTIFIED BY: Used to create passwords
# GRANT ALL: Used to provide control or permissions for users

# PRIMARY KEY: set of columns in a database table that uniquely identifies each record in the table. It enforces the integrity of the data by ensuring that each row in the table has a distinct identifier. Primary keys are used to uniquely identify records and are crucial for maintaining data consistency and for creating relationships between tables. Every table in a database should have a primary key. The primary key also serves as the basis for creating foreign key relationships with other tables.

# FOREIGN KEY: set of columns in a table that establishes a link between the data in two tables. It creates a relationship between the referencing table (child table) and the referenced table (parent table). The foreign key in the child table refers to the primary key in the parent table. This relationship enforces referential integrity, ensuring that data in the child table corresponds to data in the parent table.
