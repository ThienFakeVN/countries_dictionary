# Từ điển Liên minh châu Âu
Từ điển Liên minh châu Âu, bao gồm toàn bộ thành viên EU và thông tin của các nước đó.

## Cấy trúc
Mỗi khóa trong biến `EUROPEAN_UNION` có 2 cặp dữ liệu:
```py
EUROPEAN_UNION = {
    "Austria": {
        "date of accession": "1995.01.01",
        "eurozone": True
    },
    # ...
}
```

- `"date of accession"`: Ngày quốc gia đó gia nhập EU, loại dữ liệu: `str`

- `"eurozone"`: Quốc gia đó có thuộc khu vực đồng euro (nhóm các quốc gia thuộc EU chỉ sử dụng đồng euro làm đơn vị tiền tệ chính thức của mình) không, loại dữ liệu: `bool`

## Ví dụ sử dụng
```py
from countries_dictionary import EUROPEAN_UNION

# In ngày gia nhập EU của một quốc gia ra console
print(EUROPEAN_UNION["Sweden"]["date of accession"])

# Kiểm tra xem một quốc gia có thuộc khu vực đồng euro không (yeah chỉ thế thôi)
print(EUROPEAN_UNION["Poland"]["eurozone"])

# Tạo danh sách toàn bộ thành viên EU
list_of_EU_members = list(EUROPEAN_UNION.keys())
print(list_of_EU_members)
```
