-- script lists number of records with same score in second_table
-- The list should be sorted by the number of records (descending)
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY
number DESC;

