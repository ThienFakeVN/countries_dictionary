# Vietnam dictionary
The Socialist Republic of Vietnam dictionary, which contains dictionaries of the country's provinces and municipalities and their information.

## Structure
Each key in the `VIETNAM` constant has 6 items:
```py
VIETNAM = {
    "Hanoi": {
        "region": "Red River Delta",
        "landlocked": True,
        "administrative centre": "Hoàn Kiếm ward",
        "area": 3359.84,
        "population": 8807523,
        "ISO 3166-2:VN": "VN-HN",
    },
    # ...
}
```

- `"region"`: The former region of the province or municipality <!-- it used to be common; now it still is but...-->, type: `str`

- `"landlocked"`: Whether the province or municipality is landlocked or not, type: `bool`

- `"administrative centre"`: The administrative centre of the province or municipality, type: `str`

- `"area"`: Area (in square kilometre) of the province or municipality, type: `float`

- `"population"`: Population of the province or municipality, type: `int`

- `"ISO 3166-2:VN"`: Subdivision codes of ISO 3166-2's entry for Vietnam, type: `str`

## Usage example
```python
from countries_dictionary import VIETNAM

# Prints the population of a province
print(VIETNAM["Ho Chi Minh City"]["population"])

# Checks if the two provinces are in the same region
print(VIETNAM["Nghệ An province"]["region"] == VIETNAM["Hà Tĩnh province"]["region"])

# Creates the list of all provinces
list_of_provinces = list(VIETNAM.keys())
print(list_of_provinces)
```
