# Transnistra dictionary
The Pridnestrovian Moldavian Republic dictionary (`countries_dictionary/TRANSNISTRIA/transnistria.py`), which contains dictionaries of the country's raions, municipality and their information.

## Structure
Each key in the `TRANSNISTRIA` constant has 3 items:
```python
TRANSNISTRIA = {
    "Camenca": {
        "administrative centre": "Camenca",
        "area": 434.5,
        "population": 21000,
    },
    # ...
}
```

- `"administrative centre"`: The administrative centre of the raion or municipality, type: `str`

- `"area"`: Area (in square kilometre) of the raion or municipality, type: `float`

- `"population"`: Population of the province or municipality, type: `int`

## Usage example
```python
from countries_dictionary.TRANSNISTRIA.transnistria import TRANSNISTRIA

# Prints the area of a raion
print(TRANSNISTRIA["Rîbnița"]["area"])

# Compares the population of two raions
print(TRANSNISTRIA["Camenca"]["population"] > TRANSNISTRIA["Tiraspol"]["population"])
print(TRANSNISTRIA["Camenca"]["population"] == TRANSNISTRIA["Tiraspol"]["population"])
print(TRANSNISTRIA["Camenca"]["population"] < TRANSNISTRIA["Tiraspol"]["population"])

# Creates the list of all provinces
list_of_raions = list(TRANSNISTRIA.keys())
print(list_of_raions)
```