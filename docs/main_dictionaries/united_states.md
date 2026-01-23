# United States dictionary
The United States of America dictionary (`countries_dictionary/united_states.py`), which contains dictionaries of the country's states, federal district, inhabited territories and their information.

## Structure
Each key in the `UNITED_STATES` constant has 7 items:
```python
UNITED_STATES = {
    "Alabama": {
        "capital": "Montgomery",
        "date of ratification/establishment/acquisition": "1819.12.14",
        "landlocked": False,
        "area": 135767.0,
        "population": 5024279,
        "Representatives": 7,
        "ISO 3166-2:US": "US-AL",
    },
    # ...
}
```

- `"capital"`: The capital of the state or inhabited territory, type: `str`, `None` (for the federal district)

- `"date of ratification/establishment/acquisition"`: Date (format: YYYY.MM.DD) of ratification of the state, establishment of the federal district or acquisition of inhabited territory, type: `str`

- `"landlocked"`: Whether the state, federal district or inhabited territory is landlocked or not, type: `bool`

- `"area"`: Area (in square kilometre) of the state, federal district or inhabited territory, type: `float`

- `"population"`: Population of the state, federal district or inhabited territory, type: `int`

- `"Representatives"`: Number of Representatives of the state, federal district or inhabited territory, type: `int`

- `"ISO 3166-2:US"`: Subdivision codes of ISO 3166-2's entry for the United States, type: `str`

## Usage example
```python
from countries_dictionary.united_states import UNITED_STATES

# Prints the capital of a state
print(UNITED_STATES["Ohio"]["capital"])

# Compares the numbers of Representatives of two states
print(UNITED_STATES["California"]["Representatives"] > UNITED_STATES["Texas"]["Representatives"])
print(UNITED_STATES["California"]["Representatives"] == UNITED_STATES["Texas"]["Representatives"])
print(UNITED_STATES["California"]["Representatives"] < UNITED_STATES["Texas"]["Representatives"])

# Creates the list of all states
list_of_states = list(UNITED_STATES.keys())
print(list_of_states)
```
