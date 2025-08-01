# Changelog

## [1.0.0] 2025.07.09
First release of Countries Dictionary.

### Added
- Added 1 module file: `__init__.py`
- Added 4 types of countries' information: `continents`, `area`, `population`, `nominal GDP`
## [1.0.1] 2025.07.15
### Updated
- Fixed the licence's name

## [1.0.2] 2025.07.17
### Updated
- Fixed the `README.md`'s grammar

## [2.0.0] 2025.07.30
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
### Updated
- The module can now be maintained on GitHub

## [2.2.0] 2025.08.02
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