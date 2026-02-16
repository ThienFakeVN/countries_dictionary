# *ISO Finder*
*ISO Finder* is a tool for finding a country (or the subdivision of the country that has a dictionary) and chosen information of it based on the provided ISO 3166 code.

## Common parameters
All functions of *ISO Finder* have the same parameters:

- `code`: The ISO 3166 code of the country or subdivision, type: `str` (must be an ISO 3166-1 alpha-2, alpha-3, numeric or ISO 3166-2 code, or an ISO 3166-2 code for subdivisions)

- `info_included`: Information that will be included in the returned `list`, type: `str`, `None`, default `None` (must be an default key of a country or subdivision in its dictionary)

## Functions
| Functions (and their codes) | For |
| ------ | ----------- |
| Main ISO Finder (`iso_finder()`) | Members and observers of the United Nations |
| Russia ISO Finder (`iso_ru_finder()`) | Russian federal subjects |
| United States ISO Finder (`iso_us_finder()`) | US states, federal district and inhabited territories |
| Vietnam ISO Finder (`iso_vn_finder()`) | Vietnamese provinces and municipalities |
