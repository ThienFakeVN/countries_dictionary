# *ISO Finder*
*ISO Finder* là công cụ để tìm kiếm một quốc gia (hoặc đơn vị hành chính của một quốc gia) và một thông tin được chọn của nó dựa trên mã ISO 3166.

## Tham số chung
Tất cả hàm thuộc *ISO Finder* đều có các tham số chung:

- `code`: Mã ISO 3166 của quốc gia hoặc đơn vị hành chính, loại dữ liệu cho phép: `str` (phải là mã ISO 3166-1 hai chữ cái, ba chữ cái, ba chữ số hoặc ISO 3166-2, hoặc mã ISO 3166-2 thuộc mục nhập đối với các đơn vị hành chính)

- `info_included`: Một thông tin được thêm vào trong `list` được trả về, loại dữ liệu cho phép: `str`, `None`, mặc định: `None` (phải là một khóa có sẵn của từ điển)

## Các hàm
| Các hàm | Dành cho... |
| ------ | ----------- |
| ISO Finder cho các quốc gia (`iso_finder()`) | Thành viên và quan sát viên của Liên Hợp Quốc |
| ISO Finder Nga (`iso_ru_finder()`) | Chủ thể liên bang của Nga |
| ISO Finder Hoa Kỳ (`iso_us_finder()`) | Bang, đặc khu liên bang, lãnh thổ của Hoa Kỳ |
| ISO Finder Việt Nam (`iso_vn_finder()`) | Tỉnh thành của Việt Nam |
