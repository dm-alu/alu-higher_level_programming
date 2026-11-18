# python-object_relational_mapping

Project about connecting Python to a MySQL database, first with the
`MySQLdb` module and then with the `SQLAlchemy` ORM.

## Requirements

- Ubuntu 20.04 LTS, Python 3.8.5
- MySQLdb 2.0.x and SQLAlchemy 1.4.x
- Code style: pycodestyle 2.7.*
- Scripts take the MySQL user, password and database name as arguments
  and connect to a MySQL server on localhost, port 3306

## MySQLdb scripts

| File | Description |
| ---- | ----------- |
| `0-select_states.py` | Lists all states of `hbtn_0e_0_usa` |
| `1-filter_states.py` | Lists the states starting with `N` |
| `2-my_filter_states.py` | Lists the states matching an argument (uses `format`) |
| `3-my_safe_filter_states.py` | Same as above, safe from SQL injection |
| `4-cities_by_state.py` | Lists all cities with their state in `hbtn_0e_4_usa` |
| `5-filter_cities.py` | Lists the cities of a state given as argument |

## SQLAlchemy scripts

| File | Description |
| ---- | ----------- |
| `model_state.py` | `State` class linked to the table `states` |
| `7-model_state_fetch_all.py` | Lists all `State` objects |
| `8-model_state_fetch_first.py` | Prints the first `State` object |
| `9-model_state_filter_a.py` | Lists the states containing the letter `a` |
| `10-model_state_my_get.py` | Prints the id of the state with the given name |
| `11-model_state_insert.py` | Adds the state `Louisiana` |
| `12-model_state_update_id_2.py` | Renames the state with id 2 to `New Mexico` |
| `13-model_state_delete_a.py` | Deletes the states containing the letter `a` |
| `model_city.py` | `City` class linked to the table `cities` |
| `14-model_city_fetch_by_state.py` | Prints all cities with their state name |
| `relationship_state.py` | `State` class with the `cities` relationship |
| `relationship_city.py` | `City` class with the `state` reference |
| `100-relationship_states_cities.py` | Creates `California` with `San Francisco` |
| `101-relationship_states_cities_list.py` | Lists states and their cities (one query) |
| `102-relationship_cities_states_list.py` | Lists cities and their state (one query) |

## Usage



