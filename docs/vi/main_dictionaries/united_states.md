# United States dictionary
Từ điển Hợp chúng quốc Hoa Kỳ, gồm các bang, đặc khu liên bang, lãnh thổ của quốc gia này và thông tin của chúng.

## Structure
Mỗi khóa trong biến `UNITED_STATES` có 7 cặp dữ liệu:
```python
UNITED_STATES = {
    "Alabama": {
        "capital": "Montgomery",
        "date of ratification/establishment/acquisition": "1819.12.14",
        "landlocked": False,
        "area": 135767.0,
        "population": 5024279,
        "Representatives": 7,
        "ISO 3166-2:US": "US-AL",
    },
    # ...
}
```

- `"capital"`: Thủ phủ của bang hoặc lãnh thổ, loại dữ liệu: `str`, `None` (đối với đặc khu liên bang)

- `"date of ratification/establishment/acquisition"`: Ngày (định dạng: năm.tháng.ngày) bang gia nhập Hợp chúng quốc, hoặc ngày thành lập đặc khu liên bang, hoặc ngày sáp nhập lãnh thổ, loại dữ liệu: `str`

- `"landlocked"`: Bang, đặc khu liên bang hoặc lãnh thổ có nội lục không, loại dữ liệu: `bool`

- `"area"`: Diện tích (tính bằng kilômét vuông) của bang, đặc khu liên bang hoặc lãnh thổ, loại dữ liệu: `float`

- `"population"`: Dân số của bang, đặc khu liên bang hoặc lãnh thổ, loại dữ liệu: `int`

- `"Representatives"`: Số lượng dân biểu của bang, đặc khu liên bang hoặc lãnh thổ, loại dữ liệu: `int`

- `"ISO 3166-2:US"`: Các mã thuộc mục nhập cho Hoa Kỳ trong ISO 3166-2, loại dữ liệu: `str`

## Usage example
```python
from countries_dictionary import UNITED_STATES

# In tên thủ phủ của một bang ra console
print(UNITED_STATES["Ohio"]["capital"])

# So sánh lượng dân biểu của hai bang
print(UNITED_STATES["California"]["Representatives"] > UNITED_STATES["Texas"]["Representatives"])
print(UNITED_STATES["California"]["Representatives"] == UNITED_STATES["Texas"]["Representatives"])
print(UNITED_STATES["California"]["Representatives"] < UNITED_STATES["Texas"]["Representatives"])

# Tạo danh sách toàn bộ các bang, đặc khu liên bang và lãnh thổ
list_of_states = list(UNITED_STATES.keys())
print(list_of_states)
```
