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

Một câu nói nổi tiếng của nhà toán học R. Tyrrell Rockafellar năm 1993 đã định hình lại cách cả thế giới nhìn về tối ưu hóa: *"Ranh giới thực sự phân chia các bài toán tối ưu không phải là giữa tuyến tính và phi tuyến, mà là giữa **lồi** và **không lồi**."* Một bài toán không lồi chỉ có vài chục biến đôi khi khiến siêu máy tính bó tay vì hàng triệu cái bẫy cực tiểu địa phương; ngược lại, một bài toán tối ưu hóa lồi có tới hàng triệu biến lại có thể giải tới độ chính xác gần như tuyệt đối chỉ trong vài giây.

Chương 01 mở cánh cửa bước vào thế giới tối ưu hóa lồi: định nghĩa bài toán tối ưu tổng quát, nhận diện cấu trúc lồi, lộ trình khóa học và câu chuyện lịch sử gần một thế kỷ tạo nên các bộ giải hiện đại.

## Kiến thức cần nhớ: Bốn khái niệm mở màn của Chương 01

- **Mô hình hóa bài toán tối ưu hóa:** Quy mọi bài toán ra quyết định về ba thành phần chuẩn hóa: biến quyết định $$x$$, hàm mục tiêu $$f_0(x)$$ và tập ràng buộc khả thi $$g_i(x) \le 0,\ h_j(x) = 0$$.
- **Lồi so với Không lồi (Convex vs. Non-convex):** Hiểu vì sao tính lồi loại bỏ hoàn toàn các "bẫy" cực tiểu địa phương: trong bài toán lồi, mọi điểm thấp nhất trong lân cận đều là điểm thấp nhất toàn cục.
- **Các họ bài toán kinh điển:** Định vị Bình phương tối thiểu (LS), Quy hoạch tuyến tính (LP), Quy hoạch bậc hai (QP) và Quy hoạch bán xác định (SDP) trên cùng một bản đồ phân cấp.
- **Tư duy thuật toán hiện đại:** Biết rằng giải một bài toán lớn trong thực tế không chỉ dựa vào công thức đạo hàm, mà còn dựa vào việc khai thác cấu trúc bài toán (như ADMM, điểm trong, gradient gần kề).

### Giải thích: Thấy tận mắt "bẫy cực tiểu địa phương" của hàm không lồi

So sánh hai hàm số một biến trên $$\mathbb{R}$$:

1. **Hàm lồi $$f_1(x) = (x - 2)^2$$:**
   - Đạo hàm $$f_1'(x) = 2(x - 2) = 0 \iff x = 2$$, và $$f_1''(x) = 2 > 0$$ mọi nơi.
   - Dù xuất phát từ $$x_0 = -100$$ hay $$x_0 = +100$$, thuật toán hạ dốc đều trượt về đúng một đáy duy nhất $$x^* = 2$$ với $$f_1(2) = 0$$.
2. **Hàm không lồi $$f_2(x) = \frac{1}{4}x^4 - \frac{1}{3}x^3 - x^2$$:**
   - Đạo hàm: $$f_2'(x) = x^3 - x^2 - 2x = x(x - 2)(x + 1) = 0 \implies x \in \{-1,\ 0,\ 2\}$$.
   - Kiểm tra đạo hàm cấp hai $$f_2''(x) = 3x^2 - 2x - 2$$:
     - Tại $$x = -1$$: $$f_2''(-1) = 3 > 0$$ (cực tiểu địa phương), $$f_2(-1) = \frac{1}{4} + \frac{1}{3} - 1 = -\frac{5}{12} \approx -0.417$$.
     - Tại $$x = 0$$: $$f_2''(0) = -2 < 0$$ (cực đại địa phương), $$f_2(0) = 0$$.
     - Tại $$x = 2$$: $$f_2''(2) = 6 > 0$$ (cực tiểu toàn cục), $$f_2(2) = 4 - \frac{8}{3} - 4 = -\frac{8}{3} \approx -2.667$$.
   Nếu thuật toán bắt đầu ở $$x_0 = -2$$, nó sẽ rơi vào thung lũng nông $$x = -1$$ ($$-0.417$$) và mắc kẹt vĩnh viễn, bỏ lỡ thung lũng sâu hơn gấp 6 lần ở $$x = 2$$ ($$-2.667$$)!

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
