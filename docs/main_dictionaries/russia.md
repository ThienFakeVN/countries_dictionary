# Russia dictionary
The Russian Federation dictionary (`countries_dictionary/russia.py`), which contains dictionaries of the country's federal subjects and their information.

## Structure
Each key in the `RUSSIA` constant has 7 items:
```python
RUSSIA = {
    "Adygea": {
        "federal district": "Southern",
        "economic region": "North Caucasus",
        "landlocked": True,
        "capital/administrative centre": "Maykop",
        "area": 7792.0,
        "population": 501038,
        "ISO 3166-2:RU": "RU-AD",
    },
    # ...
}
```

- `"federal district"`: The federal district of the federal subject, type: `str`, `NoneType` (for Russian-occupied regions in Ukraine after the 2022 invasion)

- `"economic region"`: The economic region of the federal subject, type: `str`, `NoneType` (for Russian-occupied regions in Ukraine after the 2022 invasion)

- `"landlocked"`: Whether the federal subject is landlocked or not, type: `bool`

- `"capital/administrative centre"`: The capital of the federal subject if it is a republic, the administrative centre of the federal subject otherwise, type: `str`

- `"area"`: Area (in square kilometre) of the federal subject, type: `float`

- `"population"`: Population of the federal subject, type: `int`

- `"ISO 3166-2:RU"`: Subdivision codes of ISO 3166-2's entry for Russia, type: `str`, `NoneType` (for all Russian-occupied regions in Ukraine during the Russo-Ukrainian war)

## Usage example
```python
from countries_dictionary.russia import RUSSIA

# Prints the administrative centre of a krai
print(RUSSIA["Primorsky Krai"]["capital/administrative centre"])

# Checks if the two federal subjects are in the same federal district
print(RUSSIA["Tuva"]["federal district"] == RUSSIA["Altai Republic"]["federal district"])

# Creates the list of all federal subjects
list_of_federal_subjects = list(RUSSIA.keys())
print(list_of_federal_subjects)
```
