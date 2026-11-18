-- Lists all the cities of California of the database hbtn_0d_usa, using a subquery.
-- Select the cities whose state id is the one of California
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id;
