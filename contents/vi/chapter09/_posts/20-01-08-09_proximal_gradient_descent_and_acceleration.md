---
layout: post
title: Phương pháp gradient gần kề và tăng tốc
chapter: '09'
order: 1
owner: Kyeongmin Woo
categories:
- chapter09
lang: vi
---

Ở cuối Chương 08, ta từng chạm phải một bức tường cứng: phương pháp subgradient giải được mọi hàm lồi không trơn, nhưng phải trả giá bằng tốc độ chậm chạp $$O(1/\epsilon^2)$$. Câu hỏi đặt ra cho Chương 09 là: nếu bài toán thực tế không "gấp khúc hỗn loạn ở mọi nơi", mà là sự kết hợp gọn gàng giữa một phần **trơn mượt** $$g(x)$$ (như sai số bình phương hay log-loss) và một phần **không trơn nhưng có cấu trúc đơn giản** $$h(x)$$ (như chuẩn $$\ell_1$$, chuẩn hạt nhân hay hàm chỉ thị tập lồi), ta có thể làm nhanh hơn bao nhiêu?

Câu trả lời làm thay đổi hoàn toàn bộ mặt của tối ưu hóa quy mô lớn và xử lý tín hiệu hiện đại: bằng cách tách riêng hai phần trong **phương pháp gradient gần kề (Proximal Gradient Descent)**, ta lập tức kéo tốc độ từ $$O(1/\epsilon^2)$$ lên $$O(1/\epsilon)$$ — ngang hàng với gradient descent trên hàm trơn! Và chưa dừng lại ở đó, khi gắn thêm "động cơ quán tính" **tăng tốc Nesterov / FISTA**, tốc độ vọt thẳng lên $$O(1/\sqrt{\epsilon})$$, đạt chuẩn tối ưu bậc nhất của lý thuyết tối ưu lồi.

## Kiến thức cần nhớ: Bốn trụ cột của tối ưu gần kề và tăng tốc

- **Mô hình tối ưu tổng hợp (Composite Optimization):** Phân tách hàm mục tiêu thành $$f(x) = g(x) + h(x)$$, trong đó $$g$$ lồi khả vi với $$\nabla g$$ liên tục $$L$$-Lipschitz, còn $$h$$ lồi (có thể không khả vi, thậm chí nhận giá trị $$+\infty$$ để mã hóa ràng buộc) nhưng "dễ giải" qua toán tử gần kề.
- **Toán tử gần kề (Proximal Operator):** Định nghĩa $$\operatorname{prox}_{t h}(v) = \arg\min_z \left\{\frac{1}{2t}\|z - v\|_2^2 + h(z)\right\}$$ — tìm một điểm dung hòa giữa việc giữ gần điểm $$v$$ và làm nhỏ $$h(z)$$. Đây là tổng quát hóa tự nhiên của phép chiếu Euclid lên tập lồi.
- **Khôi phục tốc độ $$O(1/k)$$ và tính chất tạo thưa chính xác:** Nhờ giữ nguyên $$h(x)$$ thay vì xấp xỉ tuyến tính nó, mỗi vòng lặp vừa đạt tốc độ $$O(1/k)$$ (tương đương $$O(1/\epsilon)$$), vừa đưa thẳng các tọa độ nhỏ về **đúng bằng $$0$$** (không dao động quanh $$0$$ như subgradient).
- **Tăng tốc Nesterov (FISTA):** Thay vì tính gradient tại điểm cũ $$x^{(k)}$$, ta ngoại suy thêm một bước quán tính tới $$y^{(k)} = x^{(k)} + \beta_k(x^{(k)} - x^{(k-1)})$$ rồi mới áp dụng bước gần kề, nâng tốc độ từ $$O(1/k)$$ lên $$O(1/k^2)$$ (tức $$O(1/\sqrt{\epsilon})$$).

### Giải thích: So sánh tốc độ hội tụ của 3 thế hệ thuật toán trên cùng một bài toán

Giả sử ta cần giải bài toán Lasso $$f(x) = \frac{1}{2}\|Ax - b\|_2^2 + \lambda\|x\|_1$$ đến độ chính xác $$\epsilon = 10^{-4}$$ (với các hằng số bài toán đều chuẩn hóa bằng $$1$$):

1. **Thế hệ 1 — Phương pháp Subgradient (Chương 08):** Tốc độ $$O(1/\epsilon^2)$$.
   Để đạt $$\epsilon = 10^{-4}$$, số vòng lặp cỡ $$(10^4)^2 = 100{,}000{,}000$$ bước — gần như bất khả thi với dữ liệu lớn!
2. **Thế hệ 2 — Proximal Gradient / ISTA (Chương 09, phần đầu):** Tốc độ $$O(1/\epsilon)$$.
   Số vòng lặp giảm mạnh xuống cỡ $$10^4 = 10{,}000$$ bước — nhanh hơn **10,000 lần**!
3. **Thế hệ 3 — Accelerated Proximal Gradient / FISTA (Chương 09, phần sau):** Tốc độ $$O(1/\sqrt{\epsilon})$$.
   Số vòng lặp chỉ còn cỡ $$\sqrt{10^4} = 100$$ bước — nhanh hơn ISTA thêm **100 lần**, và nhanh hơn subgradient đúng **1 triệu lần**!
Chỉ bằng cách tôn trọng cấu trúc $$g + h$$ và thêm một dòng quán tính Nesterov, cùng một bài toán đã biến từ "bất khả thi" thành chạy xong trong tích tắc.

# Phương pháp gradient gần kề và tăng tốc

Chương này giới thiệu phương pháp gradient gần kề (proximal gradient descent) cùng các kỹ thuật tăng tốc cho các bài toán tối ưu có hàm mục tiêu dạng tổng hợp.

## Tổng quan
- Phương pháp gradient gần kề được dùng cho các bài toán mà hàm mục tiêu có thể tách thành một phần khả vi và một phần không khả vi.
- Các kỹ thuật tăng tốc như tăng tốc Nesterov và FISTA giúp cải thiện đáng kể tốc độ hội tụ.

## Cấu trúc chương
- Phần 1: Phương pháp gradient gần kề
- Phần 2: Phân tích hội tụ
- Phần 3: Ví dụ về hoàn thiện ma trận
- Phần 4: Các trường hợp đặc biệt
- Phần 5: Các phương pháp tăng tốc — bắt đầu từ góc nhìn trực quan kiểu Distill ở [09-05]({% multilang_post_url contents/chapter09/20-01-08-09_05_acceleration %}), tiếp theo là phần trình bày giải tích về FISTA ở 09-05-01; biến thể ngẫu nhiên với hệ số $$\beta$$ cố định được trình bày tại [26-02]({% multilang_post_url contents/chapter26/2026-09-15-26_02_momentum_and_nesterov %}).

Tham khảo từng bài học dưới đây để xem chi tiết thuật toán và phân tích toán học.

## Ứng dụng hiện đại (2022–2026)

Bài đọc tùy chọn đi kèm nối tiếp khuôn mẫu proximal gradient / FISTA sang các ứng dụng như tái tạo ảnh plug-and-play (PnP), trải phẳng thuật toán (unrolling) trong FISTA-Net / pFISTA-DR, và đường chính quy hóa elastic net trong thực tế. Xem [09-06 Ứng dụng hiện đại của proximal GD và tăng tốc]({% multilang_post_url contents/chapter09/2026-09-16-09_06_modern_applications %}).
