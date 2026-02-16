# Từ điển Nga
Từ điển Liên bang Nga, gồm các chủ thể liên bang của quốc gia này và thông tin của chúng.

## Cấu trúc
Mỗi khóa trong biến `RUSSIA` có 7 cặp dữ liệu:
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

- `"federal district"`: Quận liên bang của chủ thể liên bang, loại dữ liệu: `str`, `None` (for Russian-occupied regions in Ukraine after the 2022 invasion)

- `"economic region"`: Khu vực kinh tế của chủ thể liên bang, loại dữ liệu: `str`, `None` (for Russian-occupied regions in Ukraine after the 2022 invasion)

- `"landlocked"`: Chủ thể liên bang có nội lục không, loại dữ liệu: `bool`

- `"capital/administrative centre"`: Thủ phủ của chủ thể liên bang là nước cộng hòa, hoặc trung tâm hành chính của chủ thể liên bang đối với những trường hợp khác, loại dữ liệu: `str`

- `"area"`: Diện tích (tính bằng kilômét vuông) của chủ thể liên bang, loại dữ liệu: `float`

- `"population"`: Dân số của chủ thể liên bang, loại dữ liệu: `int`

- `"ISO 3166-2:RU"`: Các mã thuộc mục nhập cho Nga trong ISO 3166-2, loại dữ liệu: `str`, `None` (đối với các vùng Nga chiếm đóng trong cuộc chiến với Ukraine)

## Ví dụ sử dụng
```python
from countries_dictionary import RUSSIA

# In trung tâm hành chính của một vùng ra console
print(RUSSIA["Primorsky Krai"]["capital/administrative centre"])

# Kiểm tra xem hai chủ thể liên bang có cùng quận liên bang hay không
print(RUSSIA["Tuva"]["federal district"] == RUSSIA["Altai Republic"]["federal district"])

# Tạo danh sách toàn bộ chủ thể liên bang
list_of_federal_subjects = list(RUSSIA.keys())
print(list_of_federal_subjects)
```
