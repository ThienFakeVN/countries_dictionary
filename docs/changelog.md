# Changelog
## [1.0.0] 2025.07.09
The first version of Countries Dictionary.

__Added__

- Added 1 module file: `__init__.py`

- Added 4 types of countries' information: `"continents"`, `"area"`, `"population"`, `"nominal GDP"`

## [1.0.1] 2025.07.15
__Updated__

- Fixed the licence's name in `pyproject.toml`

## [1.0.2] 2025.07.17
__Updated__

- Fixed `README.md`'s grammar

## [2.0.0] 2025.07.30
The second major version of Countries Dictionary, which includes new module files

__Added__

- Added 3 module files: `quick_variables.py`, `russia.py`, `vietnam.py`

- Added 4 types of countries' information: `"formal name"`, `"land area"`, `"official languages"`, `"HDI"`

- Added 6 variables in `quick_variables.py`: `json_countries`, `json_russia`, `json_vietnam`, `countries_france_censored`, `countries_area_sorted`, `countries_population_sorted`

- Added 4 types of Russian subjects' information: `"federal district"`, `"economic region"`, `"area"`

- Added 3 types of Vietnamese provinces' information: `"region"`, `"area"`, `"population"`

__Updated__

- Reorganised the Countries Dictionary and the `README.md` file

- Rounded Vatican City's nominal GDP to millions

## [2.0.1] 2025.07.30
__Updated__

- Fixed how `quick_variables.py` imports `russia.py` and `vietnam.py`

## [2.1.0] 2025.07.31
Since this version, you can publicly see the codes, licence, etc. of this module at https://github.com/ThienFakeVN/countries_dictionary (though, if you see this `CHANGELOG.md` then you have already known that)

__Updated__

- The module can now be maintained on GitHub

## [2.2.0] 2025.08.02
The version which introduces `CHANGELOG.md` and various more things

__Added__

- Added `CHANGELOG.md`

- Added 1 type of Russian subjects' information: `"capital/administrative centre"`

- Added 1 type of Vietnamese provinces' information: `"administrative centre"`

- Added 4 variables in `quick_variables.py`: `russia_subjects_area_sorted`, `russia_subjects_population_sorted`, `vietnam_provinces_area_sorted`, `vietnam_provinces_population_sorted`

__Updated__

- Replace `[None]`s in `official languages`s with `[]`, and `None`s in `federal district`s and `economic region`s with `""`

## [2.2.1] 2025.08.02
__Updated__

- Removed the link to `CHANGELOG.md` in `README.md`

- Added a reference of the addition of the `CHANGELOG.md` file

## [2.2.2] 2025.08.02
__Updated__

- Added the link to the `CHANGELOG.md` file on GitHub in `README.md`

- Altered the `countries`'s documentation

## [2.3.0] 2025.08.09
A big version for `quick_variables.py` and British English (even though I've been using it since the first version), alongside adding some information for minor and major versions.

__Added__

- Added 9 functions in `quick_variables.py`: `chosen_dictionary()`, `json_dictionary()`, `sorted_dictionary()`, `filtered_dictionary()`, `countries_population_density()`, `russia_population_density()`, `vietnam_population_density()`, `countries_population_density()`, `countries_france_censored()`

__Removed__

- Removed the 10 previous variables in `quick_variables.py`: `json_countries`, `json_russia`, `json_vietnam`, `countries_france_censored`, `countries_area_sorted`, `countries_population_sorted`, `russia_subjects_area_sorted`, `russia_subjects_population_sorted`, `vietnam_provinces_area_sorted`, `vietnam_provinces_population_sorted`

__Updated__

- Renamed `LICENSE` to `LICENCE`

- Replaced the licence's name with the `LICENCE` file in `pyproject.toml`

- Modified `README.md` significantly

- Fixed `"land area"`s of some countries

## [2.3.1] 2025.08.13
__Updated__

- Modified `README.md` slightly

- Modified some lines in `CHANGELOG.md`

- Renamed `countries`, `russia`, `vietnam` to `COUNTRIES`, `RUSSIA`, `VIETNAM` respectively in the module files

## [3.0.0] 2025.08.17
The third major version of Countries Dictionary, which includes ISO codes (with related things) and the United States dictionary

__Added__

- Added 2 module files: `iso_finder.py`, `united_states.py`

- Added 1 type of countries' information: `"ISO 3166-1"`

- Added 2 function of `quick_variables.py`: `united_states_population_density()`, `countries_iso_3166_2()`

- Added 6 types of US states' information: `"capital"`, `"date of ratification/establishment/acquiring"`, `"area"`, `"population"`, `"House Representatives"`, `"postal code"`

__Updated__

- Modified some documentaion

- Renamed `quick_variables.py` to `quick_functions.py`

## [3.0.1] 2025.08.18
__Updated__

- Added documentation to `iso_finder()` of `iso_finder.py`

- Fixed the module which is imported in `quick_functions.py`

## [3.0.2] 2025.08.18
__Updated__

- Added information of the United States dictionary in `README.md`

## [3.0.3] 2025.08.18
__Updated__

- Added information of [3.0.1] and [3.0.2] versions in `CHANGELOG.md`

## [3.1.0] 2025.08.20
This version focuses on the `README.md` and `CHANGELOG.md`

__Updated__

- Added media for changes in `CHANGELOG.md`

- Added information in `README.md`

## [3.1.1] 2025.08.20
__Updated__

- Added some keywords in `pyproject.toml`

## [3.1.2] 2025.08.22
🥀

## [3.1.3] 2025.08.20
__Updated__

- Added information about [3.1.1] version

## [3.1.4] 2025.08.22
__Updated__

- Fixed the name of the United States of America in `README.md`

- `iso_finder()` now includes ISO 3166-2

## [4.0.0] 2025.10.23
A big version in which unrecognised states are included. By the way, the last version was [3.1.4], you see something? π

__Added__

- Added 2 types of countries' information: `"motto"`, `"landlocked"`

- Added a submodule for unrecognised states

- Added 1 module file in unrecognised_states: `__init__.py`

- Added 11 types of unrecognised states' information: `"formal name"`, `"motto"`, `"continents"`, `"landlocked"`, `"area"`, `"land area"`, `"population"`, `"official languages"`, `"nominal GDP"`, `"HDI"`, `"ISO 3166-1"`

- Added 1 module file: `countries_languages`

- Added ISO finders for Russian subjects, US states, and Vietnamese provinces in `iso_finder.py`

- Added 1 function in `quick_functions.py`: `countries_allahu_akbar()`

- Added 1 type of Russian subjects' information: `ISO 3166-2:RU`

- Added 1 type of Vietnamese provinces' information: `ISO 3166-2:VN`

- Added 1 module file: `transnistria.py`

- Added 3 types of Pridnestrovian raions: `"administrative centre"`, `"area"`, `"population"`

__Updated__

- Removed most information in `README.md`

- ISO finder can now display a specifically chosen information

- Renamed `"postal code"` into `"ISO 3166-2:US"` in `united_states.py`

## [4.0.1] 2025.10.23
__Updated__

- Added some information about the [4.0.0] version

## [4.0.2] 2025.10.22
__Updated__

- updated some population information

## [4.0.3] 2025.12.15
__Updated__

- Fixed information in README.md

## [5.0.0] 2026.01.08
A major version, in which information such as `"population"` will now be updated regularly. Happy New Year by the way.

__Added__

- Added 1 type of countries' information: `"state religion"`

- Added 1 type of unrecognised states' information: `"state religion"`

__Removed__

- Removed the 9 previous functions in `quick_functions.py`: `filtered_dictionary()`, `countries_population_density()`, `russia_population_density()`, `united_states_population_density()`, `vietnam_population_density()`, `countries_population_density()`, `countries_iso_3166_2()`, `countries_france_censored()`, `countries_allahu_akbar()`

__Updated__

- Fixed `united_states` and `unrecognised_states`'s documentation

- Renamed `chosen_dictionary()` to `quick_function()`

- Monthly updated population information

- Quarterly updated area information

## [5.0.1] 2026.01.10
__Updated__

- Fixed the date of [5.0.0]'s version

- Fixed `iso_ru_finder`'s `Exception`'s parameter

## [5.0.2] 2026.01.11
__Updated__

- Fixed some code in `quick_functions.py`

## [5.0.3] 2026.01.11
__Updated__

- Altered some code in `quick_functions.py`

## [5.1.0] 2026.01.11
Monaco, North Korea and Vatican City's `"HDI"` were only `.0`, but now, they are literal `None`s, just as how I planned months ago. Hehehehe.

__Updated__

- Changed values that are empty (e.g. `""` in `"motto"`) into `None`

- `sort_dictionary` in `quick_functions.py` now can filter out `None` values

## [5.1.1] 2026.01.11
__Updated__

- Fixed some code in `quick_functions.py`

## [5.1.2] 2026.01.13
__Updated__

- Fixed some code in `quick_functions.py`

## [5.1.3] 2026.01.13
__Updated__

- Fixed Republic of the Congo's `HDI`

## [6.0.0] 2026.01.24
A very big version, where I added a documentation site for my module.

__Added__

- Added a documentation site for the Countries Dictionary <!-- thanks to mkdocs! -->

- Added 1 module file: `mkdocs.yml`

__Updated__

- Renamed `CHANGELOG.md` into `changelog.md`

- Altered how `quick_functions.py` and `iso_finder.py` import other module files

- Altered significantly values in `__init__.py`s

- Fixed values in `russia.py`

- Renamed `"date of ratification/establishment/acquiring"` keys into `"date of ratification/establishment/acquisition"` in `united_states.py`

- Altered significantly code in `quick_functions.py`

## [6.0.1] 2026.01.24
__Updated__

- Fixed a critical error

## [6.0.2] 2026.01.24
__Updated__

- Fixed some information in `changelog.md`

## [6.0.3] 2026.01.24
__Updated__

- Included the `changelog.md` file into the documentation site

## [6.0.4] 2026.01.24
__Updated__

- Built the documentation site <!--i forgot to-->

## [6.0.5] 2026.01.25
__Updated__

- Added the link to the documentation site in `pyproject.toml`

## [6.0.7] 2026.01.27
__Updated__

- Fixed the documentation site

## [6.0.8] 2026.02.02
__Updated__

- Altered Brunei's `formal name`

- Monthly updated population information

- Monthly updated Vatican City's GDP

## [7.0.0.dev1] 2026.02.02
__Updated__

- Altered significantly the module's structure

## [7.0.0.dev2] 2026.02.02
__Updated__

- Altered how `__init__.py` imports other module files

## [7.0.0.dev3] 2026.02.02
__Updated__

- Altered how most module files import others

## [7.0.0] 2026.02.02
The first version ever that has previous development versions.

__Updated__

- Relabelled [7.0.0.dev3] as [7.0.0]

## [8.0.0.dev1] 2026.02.03
__Updated__

- Renamed `unrecognised.py` into `__init__.py`

- Included the Unrecognised states and Transnistria dictionaries into the `quick_function()` function 

- Altered `iso_finder.py` and `quick_functions.py`'s directory

- Altered how the main `__init__.py` imports said module files

## [8.0.0] 2026.02.03
Another major version that has a previous development version and also altered the module structure.

__Updated__

- Relabelled [8.0.0.dev1] as [8.0.0]

## [8.1.0.dev1] 2026.02.12
__Added__

- Altered how the main `__init__.py` imports other module files

- Added 1 type of countries' and unrecognised states' information: `"PwrIndx"`

## [8.1.0] 2026.02.13
This version includes Global Firepower's Power Index and some dunder variables.

__Added__

- Added 3 dunder variables in the main `__init__.py`: `__author__`, `__email__`, `__version__`
