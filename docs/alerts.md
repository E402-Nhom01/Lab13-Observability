# Cảnh báo và Kịch bản ứng phó (Alert Rules and Runbooks)

## 1. High latency P95
- **Mức độ nghiêm trọng (Severity):** P2
- **Điều kiện kích hoạt (Trigger):** `latency_p95_ms > 5000 for 30m`
- **Tác động (Impact):** Độ trễ bị kéo dài quá mức, vi phạm cam kết SLO.
- **Các bước kiểm tra (First checks):**
  1. Mở danh sách các trace phản hồi chậm nhất trong 1 giờ qua.
  2. So sánh thời gian xử lý (span) của RAG với thời gian của LLM.
  3. Kiểm tra xem sự cố giả lập `rag_slow` có đang bị bật (enabled) hay không.
- **Khắc phục kịp thời (Mitigation):**
  - Cắt ngắt các câu truy vấn (query) quá dài.
  - Chuyển sang nguồn tìm kiếm dự phòng (fallback retrieval source).
  - Giảm kích thước của prompt.

## 2. High error rate
- **Mức độ nghiêm trọng (Severity):** P1
- **Điều kiện kích hoạt (Trigger):** `error_rate_pct > 5 for 5m`
- **Tác động (Impact):** Người dùng liên tục nhận cảnh báo lỗi hệ thống.
- **Các bước kiểm tra (First checks):**
  1. Nhóm (group) các log lại dựa trên trường `error_type`.
  2. Kiểm tra chi tiết nguyên nhân bên trong các trace bị lỗi.
  3. Phân tích xem lỗi xuất phát từ LLM, từ Web Tool hay do sai định dạng Schema.
- **Khắc phục kịp thời (Mitigation):**
  - Trở về phiên bản code ổn định trước đó (rollback).
  - Tắt (disable) công cụ đang gây lỗi.
  - Thử gọi lại (retry) thông qua một model dự phòng (fallback model).

## 3. Cost budget spike
- **Mức độ nghiêm trọng (Severity):** P2
- **Điều kiện kích hoạt (Trigger):** `hourly_cost_usd > 2x_baseline for 15m`
- **Tác động (Impact):** Tốc độ đốt tiền (burn rate) vượt quá ngân sách cho phép.
- **Các bước kiểm tra (First checks):**
  1. Phân loại các trace theo từng tính năng (feature) và model đang dùng.
  2. So sánh lượng token đầu vào (tokens_in) và token sinh ra (tokens_out).
  3. Kiểm tra xem sự cố giả lập `cost_spike` có đang bị bật hay không.
- **Khắc phục kịp thời (Mitigation):**
  - Làm ngắn gọn lại các prompt đầu vào.
  - Rút gọi các luồng xử lý đơn giản sang các model giá rẻ hơn.
  - Áp dụng bộ nhớ đệm (prompt cache) để tái sử dụng kết quả.
