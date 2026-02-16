# Hàm nhanh
Một số hàm được chuẩn bị sẵn có thể giúp ích cho bạn.

## Quick function
`quick_function()`, trả về một từ điển dựa trên tham số `dictionary` và điều chỉnh nó dựa trên tham số `addition`.

### Tham số
- `dictionary`: Từ điển để làm việc, loại dữ liệu cho phép: `str`, mặc định: `"countries"`

- `addition`: Một thông tin thêm vào cho từ điển bạn chọn trên (ví dụ: mật độ dân số), loại dữ liệu cho phép: `str`, mặc định `""`

### Ví dụ sử dụng
```python
from countries_dictionary import quick_function

# In từ điển Quốc gia chính (yep, ko sửa đổi) ra console
print(quick_function())

# Thêm toàn bộ các thông tin thêm có thể thêm vào từ điển quốc gia chính
from countries_dictionary import COUNTRIES
population_density = quick_function(addition="population density")
gdp_per_capital = quick_function(addition="GDP per capita")
iso = quick_function(addition="ISO 3166-2")
full_dictionary = COUNTRIES
for x in COUNTRIES:
    full_dictionary[x]["population density"] = population_density[x]["population density"]
    full_dictionary[x]["GDP per capita"] = gdp_per_capital[x]["GDP per capita"]
    full_dictionary[x]["ISO 3166-2"] = iso[x]["ISO 3166-2"]
print(full_dictionary)
```

## JSON dictionary
`json_dictionary()`, chuyển đổi một từ điển thành chuỗi JSON.

### Tham số
- `dictionary`: Từ điển để chuyển đổi, loại dữ liệu cho phép: `str`, mặc định: `"countries"`

- `addition`: Một thông tin thêm vào cho từ điển bạn chọn trên, loại dữ liệu cho phép: `str`, mặc định: `""`

- `indent`: Thụt lề, loại dữ liệu cho phép: `int`, `str`, `None`, mặc định: `None`

### Ví dụ sử dụng
```python
from countries_dictionary import json_dictionary

# Chuyển đổi từ điển Quốc gia chính thành chuỗi JSON thụt lề 4 lần và in nó ra console
print(json_dictionary(indent=4))

# Sử dụng một chuỗi JSON tương tự như trên làm món "donate_cho_lua" qua một tệp JSON
with open("donate_cho_lua.json", "w") as f: f.write(json_dictionary(indent=4))
```

## Sort dictionary
`sort_dictionary()`, sắp xếp một từ điển dựa trên một khóa.

### Tham số
- `chosen_key`: Khóa được sử dụng để sắp xếp từ điển, loại dữ liệu cho phép: `str` (phải là một khóa có thể sử dụng để sắp xếp, ví dụ: dân số `"population"`)

- `dictionary`: Từ điển sẽ được sắp xếp, loại dữ liệu cho phép: `str`, mặc định: `"countries"`

- `addition`: Một thông tin thêm vào cho từ điển bạn chọn trên, loại dữ liệu cho phép: `str`, mặc định: `""`

- `reverse`: Có đảo ngược từ điển lại không (như sắp xếp từ lớn đến nhỏ (mặc định) hay ngược lại), loại dữ liệu cho phép: `bool`, mặc định: `True`

### Ví dụ sử dụng
```python
from countries_dictionary import sort_dictionary

# Sắp xếp (theo dân số, từ nhỏ đến lớn) và in từ điển Quốc gia chính ra console
print(sort_dictionary("population", reverse=False))

# Xếp hạng HDI của các quốc gia
sorted = sort_dictionary("HDI")
x = 0
for country in sorted:
    x += 1
    print(f"{x}. {country}: {sorted[country]["HDI"]}")
```
