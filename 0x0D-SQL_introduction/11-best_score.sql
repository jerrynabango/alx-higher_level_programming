--  script lists all records with a score >= 10 in second_table of db hbtn_0c_0
-- Results should display both the score and the name (in this order)
-- Records should be ordered by score (top first)
SELECT score, name FROM second_table ORDER BY score >= 10 DESC;

