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

Chương này mở đầu khóa học bằng ba câu hỏi cốt lõi: một bài toán tối ưu hóa *là gì*, vì sao các bài toán **lồi** cho phép ta đảm bảo chất lượng nghiệm, và phần còn lại của khóa học trang bị những gì cho sinh viên khoa học dữ liệu.

Một bài toán quy hoạch toán học tìm điểm $$x$$ thuộc tập khả thi sao cho hàm mục tiêu đạt giá trị nhỏ nhất (hoặc lớn nhất):

$$
\begin{align}
\underset{x}{\text{minimize}} \quad & f(x) \\
\text{subject to} \quad & x \in \mathcal{C}.
\end{align}
$$

Trong học máy, cấu trúc này xuất hiện ở hầu hết mọi mô hình. Huấn luyện một bộ dự đoán thường có dạng bài toán **cực tiểu hóa rủi ro thực nghiệm**:

$$
\min_w \frac{1}{n}\sum_{i=1}^n \ell\bigl(h_w(x_i), y_i\bigr) + \lambda R(w),
$$

trong đó $$\ell$$ là hàm mất mát và $$R$$ là hàm điều chuẩn (regularizer). Lựa chọn đặc trưng, phân bổ trọng số danh mục đầu tư, ước lượng hợp lý tối đa và bài toán đối ngẫu của máy vector hỗ trợ (SVM) đều chung khuôn mẫu này, chỉ khác nhau ở hàm mục tiêu $$f$$ và tập khả thi $$\mathcal{C}$$.

Các bài toán quy hoạch **lồi** — khi $$f$$ là hàm lồi trên tập lồi $$\mathcal{C}$$ — có tính chất đặc biệt: mọi cực tiểu địa phương đều là cực tiểu toàn cục, điều kiện bậc nhất thường là điều kiện đủ, và ta có các thuật toán đáng tin cậy (gradient, proximal, điểm trong). Các mạng nơ-ron sâu dù không lồi vẫn sử dụng những thuật toán này; [Chương 28]({{ site.baseurl }}/contents/vi/chapter28/) sẽ phân tích vì sao bề mặt hàm mất mát trong thực tế thường thuận lợi hơn so với dự đoán từ lý thuyết trường hợp xấu nhất.

## Nội dung của chương này

1. **Bài toán tối ưu hóa** — biến quyết định, hàm mục tiêu, ràng buộc và tính khả thi.
2. **Bài toán tối ưu hóa lồi** — định nghĩa nền tảng dùng xuyên suốt khóa học.
3. **Mục tiêu và chủ đề** — cách kết nối giữa Chương 02–25 (nền tảng cổ điển) và Chương 26–29 (lộ trình hiện đại 2026).
4. **Lược sử** — từ quy hoạch tuyến tính đến học sâu gắn với vi phân tự động (autodiff).

Hãy đọc bài tiếp theo về dạng chuẩn với ràng buộc bất đẳng thức và đẳng thức; sau đó thử tự phân loại với những bài toán quen thuộc (bình phương tối thiểu, hồi quy logistic, *k*-means) xem bài nào là bài toán lồi.

Bài đọc tùy chọn ở cuối chương, [01-05 Ứng dụng và phát triển gần đây]({% multilang_post_url contents/chapter01/2026-09-16-01_05_Applications_Recent %}), áp dụng cùng khuôn mẫu này cho bài toán huấn luyện LLM tối ưu theo tính toán, khuôn khổ predict-then-optimize và tối ưu hóa với ràng buộc công bằng.
