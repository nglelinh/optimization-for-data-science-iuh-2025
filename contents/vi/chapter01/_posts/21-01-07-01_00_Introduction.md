---
layout: post
title: 01 Giới thiệu
chapter: '01'
order: 1
owner: Kyeongmin Woo
categories:
- chapter01
lang: vi
lesson_type: required
---

Chương này là cửa vào môn học: một bài toán tối ưu *là gì*, vì sao các bài toán **lồi** là những bài ta có thể chứng nhận, và phần còn lại của học kỳ mang lại gì cho sinh viên khoa học dữ liệu.

Một chương trình toán học tìm điểm $$x$$ trong tập khả thi làm cho hàm mục tiêu nhỏ (hoặc lớn) nhất có thể:

$$
\begin{align}
\underset{x}{\text{minimize}} \quad & f(x) \\
\text{subject to} \quad & x \in \mathcal{C}.
\end{align}
$$

Trong học máy, cùng một khuôn mẫu xuất hiện khắp nơi. Huấn luyện bộ dự đoán thường là **tối thiểu hóa rủi ro thực nghiệm**

$$
\min_w \frac{1}{n}\sum_{i=1}^n \ell\bigl(h_w(x_i), y_i\bigr) + \lambda R(w),
$$

với $$\ell$$ là hàm mất mát và $$R$$ là regularizer. Chọn đặc trưng, trọng số danh mục, tham số hợp lý cực đại, và đối ngẫu của máy vector hỗ trợ đều là cùng ý tưởng với $$f$$ và $$\mathcal{C}$$ khác nhau.

Các chương trình **lồi** — $$f$$ lồi trên $$\mathcal{C}$$ lồi — đặc biệt: mọi cực tiểu địa phương là toàn cục, điều kiện bậc nhất thường đủ, và ta có thuật toán đáng tin (gradient, proximal, điểm trong). Mạng sâu không lồi vẫn dùng các thuật toán đó; [Chương 28]({{ site.baseurl }}/contents/vi/chapter28/) hỏi vì sao phong cảnh thường dễ chịu hơn lý thuyết trường hợp xấu nhất.

## Chương này gồm những gì

1. **Bài toán tối ưu** — biến, mục tiêu, ràng buộc, tính khả thi.
2. **Bài toán tối ưu lồi** — định nghĩa bạn sẽ dùng mỗi tuần.
3. **Mục tiêu và chủ đề** — cách Chương 02–25 (trục cổ điển) và 26–29 (lộ trình hiện đại 2026) khớp nhau.
4. **Lược sử** — từ quy hoạch tuyến tính đến học sâu dẫn dắt bởi autodiff.

Đọc bài tiếp theo về dạng chuẩn với ràng buộc bất đẳng thức và đẳng thức; rồi thử quyết định, với một bài bạn đã biết (bình phương tối thiểu, hồi quy logistic, *k*-means), phần nào là lồi.
