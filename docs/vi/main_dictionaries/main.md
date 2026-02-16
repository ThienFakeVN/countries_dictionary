# Từ điển Quốc gia chính
Từ điển các quốc gia thành viên và quan sát viên của Liên Hợp Quốc, gồm các quốc gia và thông tin của các nước.

## Cấu trúc
Mỗi khóa trong biến `COUNTRIES` có 12 cặp dữ liệu:
```python
COUNTRIES = {
    "Afghanistan": {
        "formal name": "Islamic Emirate of Afghanistan",
        "motto": "There is no god but God; Muhammad is the messenger of God",
        "continents": "Asia",
        "landlocked": True,
        "area": 652864.0,
        "land area": 652230.0,
        "population": 43844000,
        "official languages": ["Dari", "Pashto"],
        "official religion": "Sunni Islam",
        "nominal GDP": 16417000000,
        "HDI": 0.496,
        "PwrIndx": 2.7342,
        "ISO 3166-1": {"alpha-2": "AF", "alpha-3": "AFG", "numeric": "004"},
    },
    # ...
}
```

- `"formal name"`: Quốc hiệu của quốc gia đó, loại dữ liệu: `str`

- `"motto"`: Tiêu ngữ của quốc gia đó, loại dữ liệu: `str`, `None` (nếu quốc gia không có tiêu ngữ)

- `"continents"`: Châu lục của chính quốc của quốc gia đó, loại dữ liệu: `str`, `list` (nếu quốc gia có nhiều hơn một ngôn ngữ)

- `"landlocked"`: Quốc gia có nội lục hay không, loại dữ liệu: `bool`

- `"area"`: Diện tích (tính bằng kilômét vuông) của quốc gia đó, loại dữ liệu: `float`

- `"land area"`: Diện tích đất liền (tính bằng kilômét vuông) của quốc gia đó, loại dữ liệu: `float`

- `"population"`: Dân số của quốc gia đó, loại dữ liệu: `int`

- `"official languages"`: Ngôn ngữ chính thức của quốc gia đó, loại dữ liệu: `str`, `list` (nếu quốc gia đó có nhiều ngôn ngữ chính thức)

- `"official religion"`: Tôn giáo chính thức của quốc gia đó, loại dữ liệu: `str`, `None` (nếu quốc gia đó không có ngôn ngữ chính thức)

- `"nominal GDP"`: Tổng sản phẩm nội địa danh nghĩa của quốc gia đó, loại dữ liệu: `int`

- `"HDI"`: Chỉ số phát triển con người của quốc gia đó, loại dữ liệu: `float`, `None` (nếu quốc gia đó không được đo đạc)

- `"PwrIndx"`: Chỉ số sức mạnh (Power Index, dựa trên số liệu của Global Firepower) của quốc gia đó, loại dữ liệu: `float`, `None` (nếu quốc gia đó không được đo đạc)

- `"ISO 3166-1"`: Mã ISO 3166-1 hai chữ cái, ba chữ cái và ba chữ số của quốc gia đó, loại dữ liệu: `dict`

## Ví dụ sử dụng
```python
from countries_dictionary import COUNTRIES

# In quốc hiệu của một quốc gia ra console
print(COUNTRIES["Vietnam"]["formal name"])

# So sánh dân số của hai quốc gia
print(COUNTRIES["North Korea"]["population"] > COUNTRIES["South Korea"]["population"])
print(COUNTRIES["North Korea"]["population"] == COUNTRIES["South Korea"]["population"])
print(COUNTRIES["North Korea"]["population"] < COUNTRIES["South Korea"]["population"])

# Tạo danh sách toàn bộ các nước
list_of_countries = list(COUNTRIES.keys())
print(list_of_countries)
```
