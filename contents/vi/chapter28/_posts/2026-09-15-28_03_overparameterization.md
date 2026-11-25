---
layout: post
title: 28-03 Quá tham số
chapter: '28'
order: 4
owner: Nguyen Le Linh
categories:
- chapter28
lang: vi
lesson_type: required
---

Trong thống kê cổ điển, có một điều răn tưởng chừng bất khả xâm phạm: *số tham số $$d$$ phải nhỏ hơn số mẫu dữ liệu $$n$$, nếu không mô hình sẽ "học thuộc lòng" (overfitting) và sụp đổ trên dữ liệu mới*. Thế nhưng mạng nơ-ron sâu hiện đại lại phá vỡ hoàn toàn điều răn đó: các mô hình có hàng trăm triệu, thậm chí hàng trăm tỷ tham số — lớn hơn số mẫu gấp nhiều lần — vẫn tổng quát hóa xuất sắc!

Chìa khóa để hiểu nghịch lý **quá tham số hóa (overparameterization)** nằm ở sự thay đổi vai trò của thuật toán tối ưu: khi hệ phương trình $$F(w) = 0$$ có **vô số nghiệm**, bản thân thuật toán tối ưu (khởi tạo từ đâu, đi bước thế nào) không còn chỉ là công cụ tìm nghiệm — nó trở thành **bộ chọn mô hình** sở hữu một **thiên kiến ẩn (implicit bias)** mạnh mẽ hướng về các nghiệm đơn giản, chuẩn nhỏ và lề lớn!

## Bản đồ kiến thức nền: Ba trụ cột của chế độ Quá tham số hóa

Bài học này làm rõ ba sự biến đổi sâu sắc khi ta bước qua ngưỡng $$d \gg n$$:

- **Đa tạp nghiệm nội suy (Interpolating Solution Manifold):** Khi $$d > n$$, tập $$\{w : Xw = y\}$$ là một không gian affine chiều $$d - n$$ thay vì một điểm duy nhất. Do đó, câu hỏi trung tâm chuyển từ *"có hội tụ về 0 không?"* sang *"thuật toán sẽ chọn điểm nào trên mặt phẳng nghiệm $$0$$ này?"*.
- **Thiên kiến ẩn của Gradient Descent (Implicit Bias / Implicit Regularization):** Dù không hề thêm số hạng phạt $$\frac{\lambda}{2}\|w\|_2^2$$ vào hàm mất mát, Gradient Descent xuất phát từ $$w_0 = 0$$ trên hồi quy tuyến tính thiếu xác định vẫn **tự động hội tụ về nghiệm nội suy có chuẩn $$\ell_2$$ nhỏ nhất**! Trên phân loại tuyến tính tách được với hàm mất mát mũ/logistic, nó tự động hướng về siêu phẳng **cực đại hóa lề (max-margin SVM)**!
- **Hình học thuận lợi cục bộ và Điều kiện PL:** Khi mạng đủ rộng (chế độ NTK / quá tham số hóa), ma trận Jacobian tại khởi tạo có hạng đầy đủ, khiến hàm mất mát thỏa điều kiện Polyak–Łojasiewicz (PL) cục bộ — đảm bảo GD hội tụ nhanh về mất mát huấn luyện bằng $$0$$ mà không cần tính lồi.

### Khung giải thích (nên đọc chậm): Chứng minh bằng tay Thiên kiến ẩn của GD trên hệ thiếu xác định

Xét bài toán hồi quy tuyến tính quá tham số hóa tối giản nhất: chỉ có $$n = 1$$ mẫu dữ liệu $$(x_1, x_2) = (1,\; 2)$$ với nhãn $$y = 5$$, nhưng có tới $$d = 2$$ tham số $$w = (w_1, w_2)^T$$:

$$
F(w_1, w_2) = \frac{1}{2}(w_1 + 2w_2 - 5)^2.
$$

1. **Tập nghiệm nội suy $$F(w) = 0$$ gồm vô số điểm trên đường thẳng $$w_1 + 2w_2 = 5$$:**
   - Nghiệm A: $$w_A = (5,\; 0)$$ có $$\|w_A\|_2^2 = 25$$.
   - Nghiệm B: $$w_B = (0,\; 2.5)$$ có $$\|w_B\|_2^2 = 6.25$$.
   - Nghiệm C: $$w_C = (1,\; 2)$$ có $$\|w_C\|_2^2 = 1^2 + 2^2 = 5$$ (nhỏ nhất!).
2. **Quan sát quỹ đạo của Gradient Descent xuất phát từ $$w^{(0)} = (0,\; 0)$$:**
   Tính gradient tại mọi điểm $$w$$:
   $$\nabla F(w) = (w_1 + 2w_2 - 5) \cdot \begin{pmatrix} 1 \\ 2 \end{pmatrix}.$$
   Nhận xét chấn động: **ở mọi vòng lặp $$k$$, vector gradient luôn song song với vector $$(1, 2)^T$$!**
   Vì $$w^{(0)} = (0, 0)$$ và mọi bước cập nhật chỉ cộng trừ một bội số của $$(1, 2)^T$$, nên mọi điểm lặp $$w^{(k)}$$ đều buộc phải có dạng $$w^{(k)} = \alpha_k (1,\; 2)^T$$!
3. **Tìm điểm hội tụ duy nhất:**
   Khi $$F(w^{(k)}) \to 0$$, điểm giới hạn $$w^\star = \alpha^\star (1, 2)^T$$ phải thỏa phương trình đường thẳng $$w_1 + 2w_2 = 5$$:
   $$\alpha^\star(1) + 2(\alpha^\star \cdot 2) = 5 \implies 5\alpha^\star = 5 \implies \alpha^\star = 1 \implies w^\star_{\text{GD}} = (1,\; 2)^T!$$
   Không hề có một dòng code nào yêu cầu cực tiểu hóa $$\|w\|_2^2$$, vậy mà cấu trúc đại số của GD tự động giao cắt vuông góc với đường thẳng nghiệm và chọn đúng điểm $$w_C = (1, 2)$$ có chuẩn Euclid nhỏ nhất!

Một mô hình được gọi là **quá tham số hóa (overparameterized)** khi số lượng tham số $$d$$ lớn hơn đáng kể so với số ràng buộc hiệu dụng từ dữ liệu huấn luyện (trường hợp kinh điển là $$d \gg n$$ để nội suy $$n$$ nhãn vô hướng). Khi đó, phương trình $$F(w)=0$$ (tức hàm mất mát huấn luyện xấp xỉ 0) có cả một **tập nghiệm rất lớn**. Quá trình huấn luyện không còn là bài toán “tìm cực tiểu duy nhất”, mà trở thành câu hỏi: *thuật toán tối ưu sẽ chọn nghiệm nội suy nào trong số đó?*

Đây chính là góc nhìn **thiên kiến ẩn (implicit bias)**. Trên bài toán bình phương tối thiểu thiếu xác định, gradient descent xuất phát từ gốc hội tụ về nghiệm nội suy có **chuẩn $$\ell_2$$ nhỏ nhất** trong không gian sinh bởi các đặc trưng; trên bài toán phân loại tuyến tính tách được, nó hội tụ theo hướng cực đại hóa lề (Soudry và cộng sự, cùng nhiều nghiên cứu nối tiếp). Dù mạng nơ-ron sâu là phi tuyến, nguyên lý cốt lõi vẫn giữ nguyên: **thuật toán tối ưu là một phần của thiên kiến quy nạp (inductive bias)**.

Quá tham số hóa cũng làm thay đổi hình học của $$F$$. Trong nhiều chế độ mô hình đặc trưng ngẫu nhiên và mạng đủ rộng, bề mặt hàm mất mát trở nên thuận lợi về mặt cục bộ: khi điểm lặp đã vào đủ gần, mọi điểm tới hạn mà SGD gặp đều nội suy dữ liệu huấn luyện, nên câu hỏi chính không còn là có bị kẹt ở điểm yên ngựa hay không mà là mô hình hội tụ tới *điểm nội suy nào*. Điều này giải thích vì sao nhận định “không lồi thì chắc chắn kẹt ở cực tiểu địa phương xấu” không phản ánh đúng thực tế của học sâu hiện đại.

**Điều kiện Polyak–Łojasiewicz (PL)** (giới thiệu ngắn gọn). Nếu hàm $$F$$ thỏa mãn:

$$
\tfrac12 \|\nabla F(w)\|_2^2 \ge \mu \bigl(F(w)-F^\star\bigr)
$$

với hằng số $$\mu>0$$, thì gradient descent vẫn đạt tốc độ hội tụ tuyến tính *mà không cần tính lồi*. Nhiều bài toán bình phương tối thiểu quá tham số hóa và một số chế độ mạng rộng thỏa điều kiện PL cục bộ. Bài tùy chọn [28-05]({% multilang_post_url contents/chapter28/2026-09-18-28_05_pl_condition %}) trình bày chi tiết cách kế thừa chứng minh Chương 06 cho bất đẳng thức này (Karimi, Nutini & Schmidt, [arXiv:1608.04636](https://arxiv.org/abs/1608.04636)).

**Bài tập.** Khớp $$n=20$$ điểm dữ liệu vô hướng bằng một đa thức bậc $$50$$ theo hai cách: (i) nghiệm chuẩn tối thiểu từ `numpy.linalg.lstsq` và (ii) gradient descent xuất phát từ hai điểm khởi tạo ngẫu nhiên khác nhau. So sánh sai số kiểm tra trên một hàm gốc trơn: cả hai đều đạt mất mát huấn luyện gần bằng 0 nhưng cho ra các nghiệm nội suy khác nhau.
