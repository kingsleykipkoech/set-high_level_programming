# Python - Object-Relational Mapping

This project bridges Python and MySQL databases using both MySQLdb (raw SQL)
and SQLAlchemy (ORM). It covers querying, inserting, updating, deleting,
and modeling relationships between tables.

## Files

| File | Description |
|------|-------------|
| `0-select_states.py` | List all states using MySQLdb |
| `1-filter_states.py` | Filter states starting with N |
| `2-my_filter_states.py` | Filter by user input (vulnerable) |
| `3-my_safe_filter_states.py` | SQL injection safe filter |
| `4-cities_by_state.py` | List all cities with state names |
| `5-filter_cities.py` | Cities of a given state |
| `model_state.py` | State class definition (SQLAlchemy) |
| `7-model_state_fetch_all.py` | List all State objects |
| `8-model_state_fetch_first.py` | Print first State |
| `9-model_state_filter_a.py` | States containing letter a |
| `10-model_state_my_get.py` | Get state by name |
| `11-model_state_insert.py` | Add Louisiana |
| `12-model_state_update_id_2.py` | Update state id=2 |
| `13-model_state_delete_a.py` | Delete states with letter a |
| `model_city.py` | City class definition |
| `14-model_city_fetch_by_state.py` | Print cities by state |
| `relationship_state.py` | State with cities relationship |
| `relationship_city.py` | City with state backref |
| `100-relationship_states_cities.py` | Create CA + SF |
| `101-relationship_states_cities_list.py` | List states with cities |
| `102-relationship_cities_states_list.py` | List cities with states |

## Author
Kingsley Kipkoech
