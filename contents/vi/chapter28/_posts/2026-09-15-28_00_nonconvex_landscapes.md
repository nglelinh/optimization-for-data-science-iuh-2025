---
layout: post
title: 28 Phong cảnh không lồi cho học sâu
chapter: '28'
order: 1
owner: Nguyen Le Linh
categories:
- chapter28
lang: vi
lesson_type: required
---

Suốt 25 chương đầu, tính lồi là tấm lưới bảo hiểm tuyệt đối của ta: chỉ cần tìm được một điểm có gradient bằng $$0$$, ta chắc chắn đang đứng ở đáy sâu nhất toàn vũ trụ. Nhưng ngay khi bước sang mạng nơ-ron sâu, tấm lưới bảo hiểm ấy biến mất hoàn toàn — hàm mất mát $$F(w)$$ trở nên **không lồi** với hàng triệu tham số lồng nhau qua các phép nhân ma trận và hàm kích hoạt phi tuyến.

Thế nhưng một nghịch lý tuyệt đẹp của khoa học máy tính thế kỷ 21 đã xảy ra: thay vì mắc kẹt mãi ở những "hố cực tiểu địa phương tồi tệ" như trực giác 2 chiều cảnh báo, SGD và AdamW lại huấn luyện mạng sâu xuống gần mức mất mát bằng $$0$$ một cách đáng kinh ngạc! Chương 28 sẽ giải mã bí ẩn đó thông qua ba chìa khóa hình học: **điểm yên ngựa trong không gian nhiều chiều**, **cơ chế thoát yên ngựa nhờ nhiễu**, và **sự dồi dào nghiệm của chế độ quá tham số hóa**.

## Kiến thức cần nhớ: Bốn trụ cột của địa hình không lồi trong học sâu

![Địa hình Không lồi: Điểm yên ngựa & Điều kiện PL]({{ site.baseurl }}/img/chapter_img/zero_fill/ch28_nonconvex_saddles_pl.svg)

Để đọc hiểu các bài 28-01 đến 28-05 một cách hệ thống, hãy nắm bốn trụ cột hình học sau:

- **Phân loại điểm tới hạn theo phổ Hessian:** Trong không gian $$d$$ chiều lớn, xác suất cả $$d$$ trị riêng của Hessian cùng dương tại một điểm tới hạn là cực nhỏ; vì vậy, kẻ cản đường phổ biến nhất không phải cực tiểu địa phương kém mà là **điểm yên ngựa chặt (strict saddle)** và các vùng cao nguyên phẳng.
- **Động lực học thoát yên ngựa (Escaping Saddles):** Phương pháp bậc nhất tất định có thể bị kẹt nếu rơi đúng vào mặt ổn định của yên ngựa, nhưng nhiễu ngẫu nhiên từ minibatch SGD (hoặc nhiễu thêm vào có chủ đích) luôn có hình chiếu khác 0 lên hướng độ cong âm, đẩy quỹ đạo trượt xuống nhanh chóng.
- **Quá tham số hóa và Thiên kiến ẩn (Overparameterization & Implicit Bias):** Khi số tham số $$d \gg n$$, tập nghiệm nội suy $$F(w) = 0$$ không phải một điểm cô lập mà là một đa tạp liên tục rộng lớn; thuật toán tối ưu (SGD, AdamW) đóng vai trò bộ chọn ẩn quyết định mô hình rơi vào nghiệm nào trên đa tạp đó.
- **Điều kiện Polyak–Łojasiewicz (PL):** Một bất đẳng thức gradient đơn giản cho phép chứng minh hội tụ tuyến tính của GD ngay cả khi hàm mất mát hoàn toàn không lồi — cây cầu nối thẳng tối ưu lồi Chương 06 sang học sâu hiện đại.

### Giải thích: Mạng tuyến tính 2 lớp — thu nhỏ toàn bộ địa hình học sâu vào 2 biến

Xét mạng nơ-ron tuyến tính tối giản nhất thế giới gồm 2 trọng số vô hướng $$u, v \in \mathbb{R}$$ khớp một điểm dữ liệu $$(x = 1, y = 1)$$:

$$
F(u, v) = \frac{1}{2}(uv - 1)^2.
$$

Hàm này **không lồi** (ví dụ trung điểm của hai nghiệm tối ưu $$(1, 1)$$ và $$(-1, -1)$$ là $$(0, 0)$$ có giá trị $$F(0, 0) = 0.5 > 0$$!). Hãy tìm mọi điểm tới hạn của nó:

1. **Giải $$\nabla F(u, v) = 0$$:**
   $$\nabla F(u, v) = \bigl(v(uv - 1),\; u(uv - 1)\bigr) = (0,\; 0).$$
   Hệ này chỉ có đúng hai họ nghiệm:
   - *Họ 1 (Đa tạp cực tiểu toàn cục):* Mọi điểm trên đường hyperbol $$uv = 1$$ đều đạt $$F(u, v) = 0$$ — có **vô số** cực tiểu toàn cục nối liền nhau!
   - *Họ 2 (Điểm tới hạn ở gốc):* $$(u, v) = (0, 0)$$ với $$F(0, 0) = 0.5$$.
2. **Kiểm tra Hessian tại $$(0, 0)$$:**
   $$H(u, v) = \begin{pmatrix} v^2 & 2uv - 1 \\ 2uv - 1 & u^2 \end{pmatrix} \implies H(0, 0) = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}.$$
   Hai trị riêng của $$H(0, 0)$$ là $$\lambda_1 = +1$$ và $$\lambda_2 = -1$$!
3. **Kết luận tuyệt đẹp:** Gốc tọa độ $$(0, 0)$$ là một **điểm yên ngựa chặt** (trượt xuống dọc hướng $$u = v$$), và **không tồn tại bất kỳ cực tiểu địa phương xấu nào** trên toàn bộ mặt phẳng $$\mathbb{R}^2$$! Chỉ một đa thức bậc 4 hai biến đã tái hiện trọn vẹn bức tranh hình học của Chương 28.

# Địa hình hàm mất mát không lồi trong học sâu

Tính lồi là nền tảng bảo đảm ở các Chương 02–25: mọi cực tiểu địa phương đều là cực tiểu toàn cục và điều kiện bậc nhất đủ để chứng nhận nghiệm tối ưu. Tuy nhiên, hàm mất mát huấn luyện $$F(w)$$ của mạng nơ-ron sâu là **không lồi**. Chương này khảo sát cụ thể những dạng phi lồi thực sự xuất hiện trong học sâu.

Ta sẽ phân loại các **điểm tới hạn** ($$\nabla F(w)=0$$) dựa trên dấu trị riêng của ma trận Hessian thành cực tiểu, cực đại và **điểm yên ngựa (saddle point)**. Từ đó, ta thấy vì sao trong không gian nhiều chiều, các điểm yên ngựa mới là trở ngại phổ biến hơn các cực tiểu địa phương kém, và vì sao trạng thái **quá tham số hóa** (số tham số lớn hơn số ràng buộc dữ liệu) lại khiến nhiều điểm cực tiểu đạt khả năng nội suy dữ liệu huấn luyện.

Các giáo trình tối ưu hiện đại như EPFL CS-439 và USC CSCI 599 xem đây là phần kiến thức cốt lõi cho học sâu. Chương này dừng ở các định nghĩa chính xác cùng trực giác hình học, không đi vào các giới hạn phương trình đạo hàm riêng trường trung bình (mean-field PDE).

Bạn có thể mở mô phỏng [loss_function_landscapes.html](https://nglelinh.github.io/interactive_math/optimization/loss_function_landscapes.html) trong quá trình đọc.

## Nội dung các bài

1. Điểm tới hạn và điểm yên ngựa.
2. Thoát khỏi điểm yên ngựa và hình học địa hình hàm mất mát.
3. Quá tham số hóa (và giới thiệu điều kiện PL).
4. Các hiện tượng địa hình hiện đại (tùy chọn) — liên thông mode, grokking, double descent, cực tiểu phẳng.
5. Điều kiện Polyak–Łojasiewicz (PL) và tốc độ hội tụ tuyến tính (tùy chọn) — kết quả của Karimi và cộng sự, mở rộng chứng minh Chương 06 mà không cần tính lồi.

Bài tùy chọn [28-05]({% multilang_post_url contents/chapter28/2026-09-18-28_05_pl_condition %}) xây dựng cầu nối từ tốc độ hội tụ lồi mạnh ở 06-03-04 sang lớp bài toán không lồi thỏa điều kiện PL, còn các hiện tượng thực nghiệm giai đoạn 2022–2026 được tổng hợp tại [28-04]({% multilang_post_url contents/chapter28/2026-09-16-28_04_modern_landscapes %}).
