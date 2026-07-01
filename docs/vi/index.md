# Countries Dictionary
Countries Dictionary (`countries-dictionary` trên PyPI) là mô đun cung cấp từ điển (dictionary) các quốc gia và vùng lãnh thổ, từ thành viên của Liên Hợp Quốc đến các nước không được công nhận.

Mô đun này được tạo ra để làm nguồn thông tin về các nước giúp lập trình viên dễ dàng tiếp cận và sử dụng — kể cả khi ngoại tuyến.

```py
from countries_dictionary import COUNTRIES

print(f"Liệu bạn có biết, người tạo ra mô đun này là một trong {COUNTRIES["Vietnam"]["population"]} người sống ở Việt Nam?")
```

## Cách cài đặt module
Sao chép lệnh này, dán nó vào trình thông dịch lệnh của thiết bị của bạn (ví dụ như PowerShell trên Windows) và chạy lệnh:
```shell
pip install countries-dictionary
```
