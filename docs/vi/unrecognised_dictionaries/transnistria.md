# Transnistra dictionary
Từ điển Cộng hòa Moldova Pridnestrovia, gồm các quận, thành phố của quốc gia này và thông tin của chúng.

## Structure
Mỗi khóa trong biến `TRANSNISTRIA` có 3 cặp dữ liệu:
Each key in the `TRANSNISTRIA` constant has 3 items:
```python
TRANSNISTRIA = {
    "Camenca": {
        "administrative centre": "Camenca",
        "area": 434.5,
        "population": 21000,
    },
    # ...
}
```

- `"administrative centre"`: Trung tâm hành chính của quận hoặc thành phố, type: `str`

- `"area"`: Diện tích (tính bằng kilômét vuông) của quận hoặc thành phố, type: `float`

- `"population"`: Dân số của quận hoặc thành phố, type: `int`

## Usage example
```python
from countries_dictionary import TRANSNISTRIA

# In diện tích của một quận ra console
print(TRANSNISTRIA["Rîbnița"]["area"])

# So sánh dân số của hai quận
print(TRANSNISTRIA["Camenca"]["population"] > TRANSNISTRIA["Tiraspol"]["population"])
print(TRANSNISTRIA["Camenca"]["population"] == TRANSNISTRIA["Tiraspol"]["population"])
print(TRANSNISTRIA["Camenca"]["population"] < TRANSNISTRIA["Tiraspol"]["population"])

# Tạo danh sách toàn bộ các quận và thành phố
list_of_raions = list(TRANSNISTRIA.keys())
print(list_of_raions)
```