# Quick functions
Some quick functions (`countries_dictionary/quick_functions.py`) that may help you in your code.

## Quick function
Returns one of the dictionaries depends on the `dictionary` parameter and modify it depends on the `addition` parameter:

- `dictionary`: Lets you choose the dictionary to work with, type: `str`, default: `"countries"`, available allowed arguments: `"america"`, `"countries"`, `"russia"`, `"united states"`, `"vietnam"` (raises an `Exception` error otherwise)

- `addition`: An additional information item for the dictionary, type: `str`, default `""`, available arguments: `"population density"`, `"GDP per capita"`, `"ISO 3166-2"` (does nothing otherwise, `"GDP per capita"` and `"ISO 3166-2"` can only be used if the `dictionary`'s argument is `"countries"`, raises an `Exception` error otherwise)

### Usage example
```python
from countries_dictionary.quick_functions import quick_function

# Prints the main Countries dictionary (yep, it's the same as COUNTRIES in countries_dictionary/__init__.py)
print(quick_function())

# Adds all possible additional items into the Countries dictionary
w_population_density = quick_function(addition="population density")
w_gdp_per_capital = quick_function(addition="GDP per capita")
w_iso = quick_function(addition="ISO 3166-2")
for x in range(0, 195):
    full_dictionary = 

```