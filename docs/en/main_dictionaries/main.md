# Main Countries dictionary
The main United Nations' members and observers dictionary, consists of countries and their information.

## Structure
Each key in the `COUNTRIES` constant has 12 items:
```python
COUNTRIES = {
    "Afghanistan": {
        "formal name": "Islamic Emirate of Afghanistan",
        "motto": "There is no god but God; Muhammad is the messenger of God",
        "continents": "Asia",
        "landlocked": True,
        "area": 652864.0,
        "land area": 652230.0,
        "population": 43844000,
        "official languages": ["Dari", "Pashto"],
        "official religion": "Sunni Islam",
        "nominal GDP": 16417000000,
        "HDI": 0.496,
        "PwrIndx": 2.7342,
        "ISO 3166-1": {"alpha-2": "AF", "alpha-3": "AFG", "numeric": "004"},
    },
    # ...
}
```

- `"formal name"`: Formal name of the country, type: `str`

- `"motto"`: Motto of the country (in English), type: `str`, `None` (if the country has no motto)

- `"continents"`: Continent(s) of the country’s mainland, type: `str`, `list` (if there are more than one continent)

- `"landlocked"`: Whether the country is landlocked or not, type: `bool`

- `"area"`: Area (in square kilometre) of the country, type: `float`

- `"land area"`: Land area (in square kilometre) of the country, type: `float`

- `"population"`: Population of the country, type: `int`

- `"official languages"`: Official language(s) of the country, type: `str`, `list` (if there are more than one language)

- `"official religion"`: Official religion of the country, type: `str`, `None` (if the country has no official religion)

- `"nominal GDP"`: Nominal gross domestic product of the country, type: `int`

- `"HDI"`: Human Development Index of the country, type: `float`, `None` (if the country is not measured)

- `"PwrIndx"`: Power Index (acordding to Global Firepower) of the country, type: `float`, `None` (if the country is not measured)

- `"ISO 3166-1"`: ISO 3166-1 alpha-2, alpha-3 and numeric codes of the country, type: `dict`

## Usage example
```python
from countries_dictionary import COUNTRIES

# Prints the formal name of a country
print(COUNTRIES["Vietnam"]["formal name"])

# Compares the population of two countries
print(COUNTRIES["North Korea"]["population"] > COUNTRIES["South Korea"]["population"])
print(COUNTRIES["North Korea"]["population"] == COUNTRIES["South Korea"]["population"])
print(COUNTRIES["North Korea"]["population"] < COUNTRIES["South Korea"]["population"])

# Creates the list of all countries
list_of_countries = list(COUNTRIES.keys())
print(list_of_countries)
```
