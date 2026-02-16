# Quick functions
Some quick functions that may help you in your code.

## Quick function
`quick_function()`, returns one of the dictionaries depends on the `dictionary` parameter and modify it depends on the `addition` parameter.

### Parameters
- `dictionary`: Let you choose the dictionary to work with, type: `str`, default: `"countries"`

- `addition`: An additional information item for the dictionary, type: `str`, default: `""`

### Usage example
```python
from countries_dictionary import quick_function

# Prints the main Countries dictionary (yep, it's the same as COUNTRIES in countries_dictionary/__init__.py)
print(quick_function())

# Adds all possible additional items into the Countries dictionary
from countries_dictionary import COUNTRIES
population_density = quick_function(addition="population density")
gdp_per_capital = quick_function(addition="GDP per capita")
iso = quick_function(addition="ISO 3166-2")
full_dictionary = COUNTRIES
for x in COUNTRIES:
    full_dictionary[x]["population density"] = population_density[x]["population density"]
    full_dictionary[x]["GDP per capita"] = gdp_per_capital[x]["GDP per capita"]
    full_dictionary[x]["ISO 3166-2"] = iso[x]["ISO 3166-2"]
print(full_dictionary)
```

## JSON dictionary
`json_dictionary()`, converts a dictionary into a JSON string.

### Parameters
- `dictionary`: The dictionary to convert, type: `str`, default: `"countries"`

- `addition`: An additional information item for the dictionary, type: `str`, default: `""`

- `indent`: The indentation of the JSON string, type: `int`, `str`, `None`, default: `None`

### Usage example
```python
from countries_dictionary import json_dictionary

# Converts the main Countries dictionary into 4 spaces indentation JSON and prints it
print(json_dictionary(indent=4))

# Use an equivalent as "friendly_aid_to_our_little_moon_lua" through a JSON file
with open("friendly_aid_to_our_little_moon_lua.json", "w") as f: f.write(json_dictionary(indent=4))
```

## Sort dictionary
`sort_dictionary()`, sorts a dictionary by a sortable key.

### Parameters
- `chosen_key`: The key by which the dictionary will be sorted, type: `str` (must be a sortable key)

- `dictionary`: The dictionary to sort, type: `str`, default: `"countries"`

- `addition`: An additional information item for the dictionary, type: `str`, default: `""`

- `reverse`: Whether reverses the dictionary or not (the dictionary will be sorted from most to least by default), type: `bool`, default: `True`

### Usage example
```python
from countries_dictionary import sort_dictionary

# Sorts and prints the main Countries dictionary by population (from least to most)
print(sort_dictionary("population", reverse=False))

# Ranks every countries by HDI
sorted = sort_dictionary("HDI")
x = 0
for country in sorted:
    x += 1
    print(f"{x}. {country}: {sorted[country]["HDI"]}")
```
