# Changelog

## [1.0.0] 2025.07.09
First release of Countries Dictionary.

### Added
- Added 1 module file: `__init__.py`
- Added 4 types of countries' information: `continents`, `area`, `population`, `nominal GDP`

## [1.0.1] 2025.07.15
### Updated
- Fixed the licence's name in `pyproject.toml`

## [1.0.2] 2025.07.17
### Updated
- Fixed the `README.md`'s grammar

## [2.0.0] 2025.07.30
The second major release of Countries Dictionary, which includes new module files

### Added
- Added 3 module files: `quick_variables.py`, `russia.py`, `vietnam.py`
- Added 4 types of countries' information: `formal name`, `land area`, `official languages`, `HDI`
- Added 6 variables in `quick_variables.py`: `json_countries`, `json_russia`, `json_vietnam`, `countries_france_censored`, `countries_area_sorted`, `countries_population_sorted`
- Added 4 types of Russian subjects' information: `federal district`, `economic region`, `area`, `region`
- Added 3 types of Vietnamese provinces' information: `region`, `area`, `population`

### Updated
- Reorganised the Countries Dictionary and the `README.md` file
- Rounded Vatican City's nominal GDP to millions

## [2.0.1] 2025.07.30
### Updated
- Fixed how `quick_variables.py` imports `russia.py` and `vietnam.py`

## [2.1.0] 2025.07.31
Since this release, you can publicly see the codes, licence, etc. of this module at https://github.com/ThienFakeVN/countries_dictionary (though, if you see this `CHANGELOG.md` then you have already known that)

### Updated
- The module can now be maintained on GitHub

## [2.2.0] 2025.08.02
The release which introduces `CHANGELOG.md` and various more things

### Added
- Added `CHANGELOG.md`
- Added 1 type of Russian subjects' information: `capital/administrative centre`
- Added 1 type of Vietnamese provinces' information: `administrative centre`
- Added 4 variables in `quick_variables.py`: `russia_subjects_area_sorted`, `russia_subjects_population_sorted`, `vietnam_provinces_area_sorted`, `vietnam_provinces_population_sorted`

### Updated
- Replace `[None]`s in `official languages`s with `[]`, and `None`s in `federal district`s and `economic region`s with `""`

## [2.2.1] 2025.08.02
### Updated
- Removed the link to `CHANGELOG.md` in `README.md`
- Added a reference of the adđition of the `CHANGELOG.md` file

## [2.2.2] 2025.08.02
### Updated
- Added the link to the `CHANGELOG.md` file on GitHub in `README.md`
- Slightly modified the `countries_dictionary`'s documentation

## [2.3.0] 2025.08.09
A big release for `quick_variables.py` and British English (even though I've been used it since the first release), alongside adding some information for minor and major releases.

### Added
- Added 9 functions in `quick_variables.py`: `chosen_dictionary()`, `json_dictionary()`, `sorted_dictionary()`, `filtered_dictionary()`, `countries_population_density()`, `russia_population_density()`, `vietnam_population_density()`, `countries_population_density()`, `countries_france_censored()`

### Removed
- Removed the 10 previous variables in `quick_variables.py`: `json_countries`, `json_russia`, `json_vietnam`, `countries_france_censored`, `countries_area_sorted`, `countries_population_sorted`, `russia_subjects_area_sorted`, `russia_subjects_population_sorted`, `vietnam_provinces_area_sorted`, `vietnam_provinces_population_sorted`

### Updated
- Changed the name of `LICENSE` to `LICENCE`
- Replaced the licence's name with the `LICENCE` file in `pyproject.toml`
- Modified `README.md` significantly
- Fixed the `land area`s of some countries

## [2.3.1] 2025.08.13
### Updated
- Modified `README.md` slightly
- Modified some lines in `CHANGELOG.md`
- Changed the name of `countries`, `russia`, `vietnam` to `COUNTRIES`, `RUSSIA`, `VIETNAM` respectively in the module files

## [3.0.0] 2025.08.17
The third major release of Countries Dictionary, which includes ISO codes (with related things) and the United States dictionary

### Added
- Added 2 module files: `iso_finder.py`, `united_states.py`
- Added 1 type of countries' information: `ISO 3166-1`
- Added 3 types of ISO codes: `alpha-2`, `alpha-3`, `numeric`
- Added 2 function of `quick_variables.py`: `united_states_population_density()`, `countries_iso_3166_2()`
- Added 6 types of US states: `capital`, `date of ratification/establishment/acquiring`, `area`, `population`, `House Representatives`, `postal code`

### Updated
- Modified some documentaion
- Renamed `quick_variables.py` to `quick_functions.py`