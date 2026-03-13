# Nhật kí cập nhật
## [1.0.0] 2025.07.09
Phiên bản đầu tiên của Countries Dictionary.

__Thêm__

- Thêm vào 1 tệp mô đun: `__init__.py`

- Thêm vào 4 loại thông tin quốc gia: `"continents"`, `"area"`, `"population"`, `"nominal GDP"`

## [1.0.1] 2025.07.15
__Chỉnh sửa__

- Chỉnh sửa tên của giấy phép trên `pyproject.toml`

## [1.0.2] 2025.07.17
__Chỉnh sửa__

- Chỉnh sửa ngữ pháp trong `README.md`

## [2.0.0] 2025.07.30
Phiên bản lớn thứ hai của Countries Dictionary, thêm vào một số tệp mô đun mới.

__Thêm__

- Thêm vào 3 tệp mô đun: `quick_variables.py`, `russia.py`, `vietnam.py`

- Thêm vào 4 loại thông tin quốc gia: `"formal name"`, `"land area"`, `"official languages"`, `"HDI"`

- Thêm 6 biến vào `quick_variables.py`: `json_countries`, `json_russia`, `json_vietnam`, `countries_france_censored`, `countries_area_sorted`, `countries_population_sorted`

- Thêm vào 4 loại thông tin chủ thể liên bang của Nga: `"federal district"`, `"economic region"`, `"area"`, `"population"`

- Thêm vào 3 loại thông tin tỉnh thành của Việt Nam: `"region"`, `"area"`, `"population"`

__Chỉnh sửa__

- Sắp xếp lại mô đun <!--nhưng... nhưng như thế nào.?-->

- Làm tròn GDP danh nghĩa của Thành Vatican đến hàng triệu

## [2.0.1] 2025.07.30
__Chỉnh sửa__

- Sửa lại cách `quick_variables.py` nhập (import) `russia.py` và `vietnam.py`

## [2.1.0] 2025.07.31
Kể từ phiên bản này, bạn có thể thấy được mã nguồn, giấy phép, v.v. của mô đun này trên https://github.com/ThienFakeVN/countries_dictionary.

__Chỉnh sửa__

- Mô đun giờ đây có thể được quản lý trên GitHub

## [2.2.0] 2025.08.02
Phiên bản thêm vào `CHANGELOG.md` và nhiều thứ khác.

__Thêm__

- Thêm vào `CHANGELOG.md`

- Thêm vào một loại thông tin chủ thể liên bang của Nga: `"capital/administrative centre"`

- Thêm vào một loại thông tin tỉnh thành của Việt Nam: `"administrative centre"`

- Thêm 10 biến vào `quick_variables.py`: `json_countries`, `json_russia`, `json_vietnam`, `countries_france_censored`, `countries_area_sorted`, `countries_population_sorted`, `russia_subjects_area_sorted`, `russia_subjects_population_sorted`, `vietnam_provinces_area_sorted`, `vietnam_provinces_population_sorted`

__Chỉnh sửa__

- Thay thế `[None]` trong các khóa `official languages` với `[]`, và `None` trong các khóa `federal district` và `economic region` trong `russia.py` với `""`

## [2.2.1] 2025.08.02
__Chỉnh sửa__

- Loại bỏ liên kết đến `CHANGELOG.md` trong `README.md`

- Thêm đề cập về việc thêm `CHANGELOG.md` vào.

## [2.2.2] 2025.08.02
__Chỉnh sửa__

- Thêm liên kết đến `CHANGELOG.md` trên GitHub vào `README.md`

- Điều chỉnh mô tả của biến `countries`

## [2.3.0] 2025.08.09
Một phiên bản lớn đối với `quick_variables.py` và việc tôi sử dụng tiếng Anh Anh thay vì Anh Mỹ (dù tôi đã dùng nó từ phiên bản đầu rồi)

__Thêm__

- Thêm 9 hàm vào `quick_variables.py`: `chosen_dictionary()`, `json_dictionary()`, `sorted_dictionary()`, `filtered_dictionary()`, `countries_population_density()`, `russia_population_density()`, `vietnam_population_density()`, `countries_population_density()`, `countries_france_censored()`

__Loại bỏ__

- Loại bỏ 10 biến trong `quick_variables.py`: `json_countries`, `json_russia`, `json_vietnam`, `countries_france_censored`, `countries_area_sorted`, `countries_population_sorted`, `russia_subjects_area_sorted`, `russia_subjects_population_sorted`, `vietnam_provinces_area_sorted`, `vietnam_provinces_population_sorted`

__Chỉnh sửa__

- Đổi tên `LICENSE` thành `LICENCE`

- Thay thế tên của giấy phép thành tệp `LICENCE` trong `pyproject.toml`

- Điều chỉnh đáng kể `README.md`

- Sửa lại giá trị khóa `"land area"` của một số quốc gia

## [2.3.1] 2025.08.13
__Chỉnh sửa__

- Điều chỉnh `README.md`

- Điều chỉnh một số dòng trong `CHANGELOG.md`

- Đổi tên `countries`, `russia`, `vietnam` lần lượt thành `COUNTRIES`, `RUSSIA`, `VIETNAM` trong các tệp mô đun

## [3.0.0] 2025.08.17
Phiên bản lớn thứ ba của Countries Dictionary, thêm vào mã ISO (với một số thứ liên quan) và từ điển Hoa Kỳ.

__Thêm__

- Thêm vào 2 tệp mô đun: `iso_finder.py`, `united_states.py`

- Thêm vào 1 loại thông tin quốc gia: `"ISO 3166-1"`

- Thêm 2 hàm vào `quick_variables.py`: `united_states_population_density()`, `countries_iso_3166_2()`

- Thêm vào 6 loại thông tin bang của Hoa Kỳ: `"capital"`, `"date of ratification/establishment/acquiring"`, `"area"`, `"population"`, `"House Representatives"`, `"postal code"`

__Chỉnh sửa__

- Điểu chỉnh một vài mô tả

- Đổi tên `quick_variables.py` thành `quick_functions.py`

## [3.0.1] 2025.08.18
__Chỉnh sửa__

- Thêm mô tả cho `iso_finder()`

- Sửa lại cách `quick_functions.py` nhập các tệp mô đun khác

## [3.0.2] 2025.08.18
__Chỉnh sửa__

- Thêm thông tin về từ điển Hoa Kỳ vào `README.md`

## [3.0.3] 2025.08.18
__Chỉnh sửa__

- Thêm thông tin về phiên bản [3.0.1] và [3.0.2] vào `CHANGELOG.md`

## [3.1.0] 2025.08.20
Phiên bản này tập trung vào `README.md` và `CHANGELOG.md`

__Chỉnh sửa__

- Thêm hình ảnh cho các sửa đổi trong `CHANGELOG.md`

- Thêm thông tin <!--gì?--> vào `README.md`

## [3.1.1] 2025.08.20
__Chỉnh sửa__

- Thêm một số từ khóa vào `pyproject.toml`

## [3.1.2] 2025.08.22
🥀

## [3.1.3] 2025.08.20
__Chỉnh sửa__

- Thêm thông tin về phiên bản [3.1.1]

## [3.1.4] 2025.08.22
__Chỉnh sửa__

- Sửa tên của Hoa Kỳ trong `README.md`

- `iso_finder()` bây giờ cho phép sử dụng ISO 3166-2

## [4.0.0] 2025.10.23
Một phiên bản lớn mà từ điển các vùng lãnh thổ không được công nhận được thêm vào. Btw phiên bản trước là [3.1.4], yep, là π

__Thêm__

- Thêm vào 2 loại thông tin quốc gia: `"motto"`, `"landlocked"`

- Thêm một mô đun phụ cho các vùng lãnh thổ không được công nhận

- Thêm vào 1 tệp mô đun trong unrecognised_states: `__init__.py`

- Thêm vào 11 loại thông tin các vùng lãnh thổ không được công nhận: `"formal name"`, `"motto"`, `"continents"`, `"landlocked"`, `"area"`, `"land area"`, `"population"`, `"official languages"`, `"nominal GDP"`, `"HDI"`, `"ISO 3166-1"`

- Thêm 1 tệp mô đun: `countries_languages`

- Thêm các hàm cho các chủ thể liên bang của Nga, bang của Mỹ và tỉnh thành của Việt Nam trong `iso_finder.py`

- Thêm 1 hàm vào `quick_functions.py`: `countries_allahu_akbar()`

- Thêm vào 1 loại thông tin chủ thể liên bang của Nga: `ISO 3166-2:RU`

- Thêm vào 1 loại thông tin tỉnh thành của Việt Nam: `ISO 3166-2:VN`

- Thêm vào 1 tệp mô đun trong unrecognised_states: `transnistria.py`

- Thêm vào 3 loại thông tin quận của Transnistria: `"administrative centre"`, `"area"`, `"population"`

__Chỉnh sửa__

- Loại bỏ hầu hết thông tin trong `README.md`

- Các hàm trong `iso_finder.py` giờ có thể trả về một thông tin được chọn

- Đổi tên khóa `"postal code"` thành `"ISO 3166-2:US"` trong `united_states.py`

## [4.0.1] 2025.10.23
__Chỉnh sửa__

- Thêm thông tin về phiên bản [4.0.0]

## [4.0.2] 2025.10.22
__Chỉnh sửa__

- Cập nhật dân số một số quốc gia

## [4.0.3] 2025.12.15
__Chỉnh sửa__

- Sửa thông tin <!--gì nữa?--> trong `README.md`

## [5.0.0] 2026.01.08
Từ phiên bản này trở đi, thông tin như dân số sẽ được cập nhật thường xuyên. Nhân tiện, chúc mừng năm mới.

__Thêm__

- Thêm vào 1 loại thông tin quốc gia: `"state religion"`

- Thêm vào 1 loại thông tin các vùng lãnh thổ không được công nhận: `"state religion"`

__Loại bỏ__

- Loại bỏ 9 hàm cũ trong `quick_functions.py`: `filtered_dictionary()`, `countries_population_density()`, `russia_population_density()`, `united_states_population_density()`, `vietnam_population_density()`, `countries_population_density()`, `countries_iso_3166_2()`, `countries_france_censored()`, `countries_allahu_akbar()`

__Chỉnh sửa__

- Sửa lại mô tả của `united_states` và `unrecognised_states`

- Đổi tên `chosen_dictionary()` thành `quick_function()`

- Cập nhật thông tin dân số hàng tháng

- Cập nhật thông tin diện tích hàng quý (3 tháng)

## [5.0.1] 2026.01.10
__Chỉnh sửa__

- Sửa lại ngày phát hành phiên bản [5.0.0]

- Sửa lại thông báo lỗi của `iso_ru_finder()`

## [5.0.2] 2026.01.11
__Chỉnh sửa__

- Sửa đổi một số mã của `quick_functions.py`

## [5.0.3] 2026.01.11
__Chỉnh sửa__

- Điều chỉnh một số mã trong `quick_functions.py`

## [5.1.0] 2026.01.11
Giá trị của khóa `"HDI"` của Monaco, Triều Tiên và Thành Vatican trước đây là `.0`, nhưng bây giờ là `None`. Ehehehe.

__Chỉnh sửa__

- Đổi các giá trị trống (ví dụ: `""` của `"motto"` và `.0` của `"HDI"`) thành `None`

- `sort_dictionary()` trong `quick_functions.py` giờ có thể lọc ra các giá trị `None`

## [5.1.1] 2026.01.11
__Chỉnh sửa__

- Sửa đổi một số mã trong `quick_functions.py`

## [5.1.2] 2026.01.13
__Chỉnh sửa__

- Sửa đổi một số mã trong `quick_functions.py`

## [5.1.3] 2026.01.13
__Chỉnh sửa__

- Sửa lại `"HDI"` của Cộng hòa Congo

## [6.0.0] 2026.01.24
Một phiên bản lớn khác, trang tài liệu của mô đun này được thêm vào trong phiên bản này.

__Thêm__

- Thêm vào một trang tài liệu cho Countries Dictionary <!-- thanks to mkdocs! -->

__Chỉnh sửa__

- Đổi tên `CHANGELOG.md` thành `changelog.md`

- Điều chỉnh cách `quick_functions.py` và `iso_finder.py` nhập các tệp mô đun khác

- Điều chỉnh đáng kể các giá trị <!-- gì -_- ? --> trong 2 tệp `__init__.py`

- Sửa lại giá trị trong `russia.py` <!-- à nhớ sửa gì rồi -->

- Đổi tên khóa `"date of ratification/establishment/acquiring"` thành `"date of ratification/establishment/acquisition"` trong `united_states.py`

- Điều chỉnh đáng kể mã của `quick_functions.py`

## [6.0.1] 2026.01.24
__Chỉnh sửa__

- Sửa một lỗi nghiêm trọng <!-- đừng hỏi tôi lỗi gì -->

## [6.0.2] 2026.01.24
__Chỉnh sửa__

- Điều chỉnh một số thông tin trong `changelog.md`

## [6.0.3] 2026.01.24
__Chỉnh sửa__

- Thêm tệp `changelog.md` vào trang tài liệu

## [6.0.4] 2026.01.24
__Chỉnh sửa__

- Build trang tài liệu (tôi quên build :v)

## [6.0.5] 2026.01.25
__Chỉnh sửa__

- Thêm liên kết đến trang tài liệu trong `pyproject.toml`

## [6.0.7] 2026.01.27
__Chỉnh sửa__

- Sửa lại trang tài liệu

## [6.0.8] 2026.02.02
__Chỉnh sửa__

- Điều chỉnh quốc hiệu Brunei

- Cập nhật thông tin dân số hàng tháng

- Cập nhật GDP của Thành Vatican hàng tháng

## [7.0.0.dev1] 2026.02.02
__Chỉnh sửa__

- Chỉnh sửa đáng kể cấu trúc mô đun

## [7.0.0.dev2] 2026.02.02
__Chỉnh sửa__

- Điều chỉnh cách `__init__.py` nhập các tệp mô đun khác

## [7.0.0.dev3] 2026.02.02
__Chỉnh sửa__

- Điều chỉnh cách các tệp mô đun nhập các tệp khác

## [7.0.0] 2026.02.02
Đây là phiên bản đầu tiên có những bản cập nhật phát triển (development version).

__Chỉnh sửa__

- Không có thay đổi

## [8.0.0.dev1] 2026.02.03
__Chỉnh sửa__

- Đổi tên `unrecognised.py` thành `__init__.py`

- Từ điển Lãnh thổ không được công nhận và Transnistra được thêm vào hàm `quick_function()`

- Điều chỉnh vị trí của tệp `iso_finder.py` và `quick_functions.py`

- Điều chỉnh cách tệp `__init__.py` chính nhập các tệp trên

## [8.0.0] 2026.02.03
Một phiên bản khác có các phiên bản phát triển, cũng như điều chỉnh cấu trúc mô đun.

__Chỉnh sửa__

- Không có thay đổi

## [8.1.0.dev1] 2026.02.12
__Thêm__

- Điều chỉnh cách tệp `__init__.py` chính nhập các tệp mô đun khác

- Thêm vào 1 loại thông tin quốc gia và vùng lãnh thổ không được công nhận: `"PwrIndx"`

## [8.1.0] 2026.02.14
Phiên bản này thêm vào Chỉ số sức mạnh (Power Index) của Global Firepower và các biến có dấu gạch dưới (dunder variable).

__Thêm__

- Thêm vào 3 biến trong `__init__.py`: `__author__`, `__email__`, `__version__`

## [8.1.1] 2026.02.14
__Chỉnh sửa__

- Sửa lại ngày phát hành phiên bản [8.1.0]

## [8.2.0] 2026.02.16
Phiên bản này thêm vào bản tiếng Việt cho trang tài liệu của mô đun này. Yep là cái thứ bạn đang đọc đấy. Chúc mừng Năm Bính Ngọ (sớm hơn 1 ngày)

__Thêm__

- Thêm vào bản bản tiếng Việt của trang tài liệu

## [8.2.1] 2026.02.16
__Chỉnh sửa__

- Sửa một lỗi nghiêm trọng

## [8.2.2] 2026.02.27
__Chỉnh sửa__

- Sửa một lỗi khiến cho nút chuyển ngôn ngữ không hoạt động chính xác
- Sửa một số dòng trong hai `changelog.md`

## [8.2.3] 2026.03.13
__Chỉnh sửa__

- Cập nhật thông tin dân số hàng tháng

- Cập nhật GDP của Thành Vatican hàng tháng
