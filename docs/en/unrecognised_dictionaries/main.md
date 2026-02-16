# Main Unrecognised states dictionary
The main non-United Nations states dictionary, consists of such states and their information.

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
        "HDI": None,
        "PwrIndx": .0,
        "ISO 3166-1": {"alpha-2": "CK", "alpha-3": "COK", "numeric": "184"},
    },
    # ...
}
```

## Usage example
```python
from countries_dictionary import UNRECOGNISED_STATES

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
