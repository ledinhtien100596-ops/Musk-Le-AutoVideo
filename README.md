# Musk Le AutoVideo

Bản đổi tên của **Concat v0.2.7**, giữ toàn bộ giao diện desktop và chức năng chỉnh sửa video. Dựa trên Concat của Jareer và các cộng tác viên, giấy phép AGPL-3.0-or-later.

## Trạng thái
Chưa có bản Windows được xác nhận chạy thành công. Theo dõi tab Actions; không coi việc có repository là đã có bộ cài hoàn chỉnh hoặc phần mềm đã được chứng nhận sạch mã độc.

## Build
Workflow Windows chạy khi có thay đổi bản vá hoặc workflow trên main, và có thể chạy thủ công. Nó tải nguồn Concat v0.2.7, đối chiếu SHA-256, áp dụng `musk/branding.patch`, giữ dependency có mã băm của upstream, rồi build bản Windows x64. Các bước tiếp theo gồm quét Defender, kiểm tra khởi động và tạo bộ cài. Không tự publish release.

Artifact thành công chứa bộ cài và toàn bộ nguồn tương ứng. Mã chỉnh sửa ở `musk/branding.patch`; script lấy nguồn ở `musk/prepare_source.py`. Nguồn đầy đủ được tái tạo trước khi build, không phải viết lại một editor rút gọn.

Giao diện, timeline, hiệu ứng, mẫu chữ, TTS, phụ đề và xuất video giữ nguyên. API và định dạng project Concat giữ tương thích. Thư mục cấu hình và định danh bộ cài tách riêng. Trang cập nhật vẫn trỏ đến Concat gốc và có thông báo rõ.

Nguồn upstream: https://github.com/jub0t/Concat/tree/v0.2.7

Không có giao diện web Python hoặc tài nguyên video cá nhân trong repository này.
