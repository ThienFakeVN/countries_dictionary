# Main Unrecognised states dictionary
The main non-United Nations states dictionary (`countries_dictionary/unrecognised_states/__init__.py`), which includes such states and their information.

## Structure
The `UNRECOGNISED_STATES` constant has the same structure with the `COUNTRIES` constants of the main Countries dictionary, having these items in each key:
```python
UNRECOGNISED_STATES = {
    "Cook Islands": {
        "formal name": "Cook Islands",
        "motto": None,
        "continents": "Oceania",
        "landlocked": False,
        "area": 236.0,
        "land area": 236.0,
        "population": 15040,
        "official languages": ["English", "Cook Islands Māori", "Pukapukan"],
        "official religion": None,
        "nominal GDP": 384000000,
        "HDI": 0,
        "ISO 3166-1": {"alpha-2": "CK", "alpha-3": "COK", "numeric": "184"},
    },
    # ...
}
```

- `"formal name"`: Formal name of the state, type: `str`

- `"motto"`: Motto of the state (in English), type: `str`, `None` (if the state has no motto)

- `"continents"`: Continent(s) of the state’s mainland, type: `str`, `list` (if there are more than one continent)

- `"landlocked"`: Whether the state is landlocked or not, type: `bool`

- `"area"`: Area (in square kilometre) of the state, type: `float`

- `"land area"`: Land area (in square kilometre) of the state, type: `float`

- `"population"`: Population of the state, type: `int`

- `"official languages"`: Official language(s) of the state, type: `str`, `list` (if there are more than one language)

- `"official religion"`: Official religion of the state, type: `str`, `None` (if the state has no official religion)

- `"nominal GDP"`: Nominal gross domestic product of the state, type: `int`

- `"HDI"`: Human Development Index of the state, type: `float`

- `"ISO 3166-1"`: ISO 3166-1 alpha-2, alpha-3 and numeric codes of the state, type: `dict`

## Usage example
```python
from countries_dictionary.unrecognised_states import UNRECOGNISED_STATES

# Prints the formal name of a state
print(UNRECOGNISED_STATES["Transnistria"]["formal name"])

# Compares the population of two states
print(UNRECOGNISED_STATES["Abkhazia"]["population"] > UNRECOGNISED_STATES["South Ossetia"]["population"])
print(UNRECOGNISED_STATES["Abkhazia"]["population"] == UNRECOGNISED_STATES["South Ossetia"]["population"])
print(UNRECOGNISED_STATES["Abkhazia"]["population"] < UNRECOGNISED_STATES["South Ossetia"]["population"])

# Creates the list of all states
list_of_countries_i_mean_states = list(UNRECOGNISED_STATES.keys())
print(list_of_countries_i_mean_states)
```
<!--Yep i'm to lazy to add any other example lol-->
