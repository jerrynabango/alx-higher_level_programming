-- script that lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id ,cities.name ,states.name
FROM cities AS cities
LEFT JOIN states AS states
ON states.id = cities.id
ORDER BY cities.id ASC;
