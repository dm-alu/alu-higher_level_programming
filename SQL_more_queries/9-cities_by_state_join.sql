-- Lists all cities of the database hbtn_0d_usa with the name of their state.
-- Select the city id, the city name and the state name
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id;
