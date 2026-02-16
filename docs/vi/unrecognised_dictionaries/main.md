# Từ điển Lãnh thổ không được công nhận chính
Từ điển các vùng lãnh thổ không thuộc Liên Hợp Quốc, gồm các lãnh thổ như thế và thông tin của chúng.

## Cấu trúc
Biến `UNRECOGNISED_STATES` có cùng cấu trúc với biến `COUNTRIES` của từ điển Quốc gia chính với những cặp dữ liệu giống nhau:
```python
UNRECOGNISED_STATES = {
    "Cook Islands": {
        "formal name": "Cook Islands",
        "motto": None,
        "continents": "Oceania",
        "landlocked": False,
        "area": 236.0,
        "land area": 236.0,
        "population": 15040,
        "official languages": ["English", "Cook Islands Māori", "Pukapukan"],
        "official religion": None,
        "nominal GDP": 384000000,
        "HDI": None,
        "PwrIndx": .0,
        "ISO 3166-1": {"alpha-2": "CK", "alpha-3": "COK", "numeric": "184"},
    },
    # ...
}
```

## Ví dụ sử dụng
```python
from countries_dictionary import UNRECOGNISED_STATES

# In quốc hiệu của một vùng lãnh thổ ra console
print(UNRECOGNISED_STATES["Transnistria"]["formal name"])

# So sánh dân số của hai vùng lãnh thổ
print(UNRECOGNISED_STATES["Abkhazia"]["population"] > UNRECOGNISED_STATES["South Ossetia"]["population"])
print(UNRECOGNISED_STATES["Abkhazia"]["population"] == UNRECOGNISED_STATES["South Ossetia"]["population"])
print(UNRECOGNISED_STATES["Abkhazia"]["population"] < UNRECOGNISED_STATES["South Ossetia"]["population"])

# Tạo danh sách toàn bộ các nước
list_of_countries_i_mean_states = list(UNRECOGNISED_STATES.keys())
print(list_of_countries_i_mean_states)
```
<!--ralsei ralsei-->
