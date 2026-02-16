# Từ điển Việt Nam
Từ điển Cộng hòa xã hội chủ nghĩa Việt Nam, bao gồm các tỉnh thành của quốc gia này và thông tin của chúng.

## Cấu trúc
Mỗi khóa trong biến `VIETNAM` có 6 cặp dữ liệu:
Each key in the `VIETNAM` constant has 6 items:
```py
VIETNAM = {
    "Hanoi": {
        "region": "Red River Delta",
        "landlocked": True,
        "administrative centre": "Hoàn Kiếm ward",
        "area": 3359.84,
        "population": 8807523,
        "ISO 3166-2:VN": "VN-HN",
    },
    # ...
}
```

- `"region"`: Vùng của tỉnh hoặc thành phố trước sáp nhập <!-- tôi chịu -->, loại dữ liệu: `str`

- `"landlocked"`: Tỉnh hoặc thành phố có nội lục hay không, loại dữ liệu: `bool`

- `"administrative centre"`: Trung tâm hành chính của tỉnh hoặc thành phố, loại dữ liệu: `str`

- `"area"`: Diện tích (tính bằng kilômét vuông) của tỉnh hoặc thành phố, loại dữ liệu: `float`

- `"population"`: Dân số của tỉnh hoặc thành phố, loại dữ liệu: `int`

- `"ISO 3166-2:VN"`: Các mã thuộc mục nhập cho Việt Nam trong ISO 3166-2, loại dữ liệu: `str`

## Ví dụ sử dụng
```python
from countries_dictionary import VIETNAM

# In diện tích của một thành phố ra console
print(VIETNAM["Ho Chi Minh City"]["population"])

# Kiểm tra xem hai tỉnh có chung khu vực hay không
print(VIETNAM["Nghệ An province"]["region"] == VIETNAM["Hà Tĩnh province"]["region"])

# Tạo danh sách toàn bộ các tỉnh thành
list_of_provinces = list(VIETNAM.keys())
print(list_of_provinces)
```
