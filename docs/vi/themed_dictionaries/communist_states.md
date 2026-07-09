# Từ điển Nhà nước cộng sản
Từ điển các nhà nước cộng sản, bao gồm toàn bộ các quốc gia cộng sản còn tồn tại và thông tin của các nước trên.

## Cấu trúc
Each key in the `COMMUNIST_STATES` constant has 10 items:
Mỗi khóa trong biến `COMMUNIST_STATES` có 10 cặp dữ liệu:
```py
COMMUNIST_STATES = {
    "China": {
        "party": "Communist Party of China",
        "politburo seats": 23,
        "politburo's term": 20,
        "central committee's members": 205,
        "central committee's alternates": 171,
        "central committee's term": 20,
        "SSOP": "National People's Congress",
        "SSOP seats": 2977, # Excluding NPCSC
        "party's SSOP seats": 2040, # Excluding NPCSC
        "SSOP's term": 14,
    },
    # ...
}
```

- `"party"`: Đảng cộng sản đang cầm quyền, loại dữ liệu: `str`

- `"politburo seats"`: Số ghế của Bộ Chính trị của đảng cầm quyền, loại dữ liệu: `int`

- `"politburo's term"`: Khóa hiện tại của Bộ Chính trị, loại dữ liệu: `int`

- `"central committee's members"`: Số ủy viên của Ban Chấp hành Trung ương của đảng cầm quyền, loại dữ liệu: `int`

- `"central committee's alternates"`: Số ủy viên dự khuyết của Ban Chấp hành Trung ương của đảng cầm quyền, loại dữ liệu: `int`

- `"central committee's term"`: Khóa hiện tại của Ban Chấp hành Trung ương, loại dữ liệu: `int`

- `"SSOP"`: Tên của cơ quan lập pháp, loại dữ liệu: `str`

- `"SSOP seats"`: Tổng số ghế của cơ quan lập pháp, loại dữ liệu: `int`

- `"party's SSOP seats"`: Số ghế đảng cầm quyền nắm trong cơ quan lập pháp, loại dữ liệu: `int`

- `"SSOP's term"`: Khóa hiện tại của cơ quan lập pháp, loại dữ liệu: `int`

## Ví dụ sử dụng
```py
from countries_dictionary import COMMUNIST_STATES

# In tên đảng cầm quyền của một quốc gia ra console
print(COMMUNIST_STATES["Vietnam"]["party"])

# So sánh khóa hiện tại của cơ quan lập pháp của 2 quốc gia
print(COMMUNIST_STATES["Cuba"]["SSOP's term"] > COMMUNIST_STATES["Laos"]["SSOP's term"])
print(COMMUNIST_STATES["Cuba"]["SSOP's term"] == COMMUNIST_STATES["Laos"]["SSOP's term"])
print(COMMUNIST_STATES["Cuba"]["SSOP's term"] < COMMUNIST_STATES["Laos"]["SSOP's term"])

# Tạo danh sách toàn bộ các nhà nước cộng sản
list_of_communist_states = list(COMMUNIST_STATES.keys())
print(list_of_communist_states)
```
