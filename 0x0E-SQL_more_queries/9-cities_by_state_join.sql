-- script that lists all cities contained in the database hbtn_0d_usa.
SELECT ct.id ,ct.name ,stat.name
FROM cities AS ct
LEFT JOIN states AS stat
ON ct.state_id = stat.id
ORDER BY ct.id;
