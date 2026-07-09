# European Union dictionary
The European Union dictionary, consists of EU members and their information.

## Structure
Each key in the `EUROPEAN_UNION` constant has 2 items:
```py
EUROPEAN_UNION = {
    "Austria": {
        "date of accession": "1995.01.01",
        "eurozone": True
    },
    # ...
}
```

- `"date of accession"`: Date of the country acceding to EU, type: `str`

- `"eurozone"`: Whether the country is part of the euro area (also eurozone; i.e. group of countries within EU that have adopted the euro as their primary currency and sole legal tender), type: `bool`

## Usage example
```py
from countries_dictionary import EUROPEAN_UNION

# Prints the date of accession of a country
print(EUROPEAN_UNION["Sweden"]["date of accession"])

# Check if a country is in eurozone or not (yeah just like that)
print(EUROPEAN_UNION["Poland"]["eurozone"])

# Create the list of all EU members
list_of_EU_members = list(EUROPEAN_UNION.keys())
print(list_of_EU_members)
```
