---
layout: post
title: 00-02 Đại số tuyến tính cơ bản
chapter: '00'
order: 7
owner: GitHub Copilot
lang: vi
categories:
- chapter00
lesson_type: required
---

Nếu giải tích là đôi mắt giúp thuật toán nhìn độ dốc, thì **đại số tuyến tính** là khung xương nâng đỡ toàn bộ tính toán trong tối ưu hóa. Một hệ thống 10.000 ràng buộc sản xuất thu gọn thành đúng một dòng $$Ax \le b$$; độ cong của hàm mất mát trong không gian triệu chiều thu gọn thành dạng toàn phương $$x^T Q x$$; và bài toán hồi quy cổ điển nhất lịch sử — bình phương tối thiểu — giải xong chỉ bằng một phép chiếu trực giao.

Phần 00-02 giúp bạn chuyển từ cách nhớ công thức nhân ma trận máy móc sang tư duy hình học về không gian con, phép biến đổi và phổ giá trị riêng.

## Kiến thức cần nhớ: Ba trụ cột đại số tuyến tính trong tối ưu hóa

- **Không gian vector, tích vô hướng và chuẩn:** Cung cấp thước đo khoảng cách ($$\ell_1, \ell_2, \ell_\infty$$) và góc giữa các hướng đi. Việc đổi chuẩn từ $$\ell_2$$ sang $$\ell_1$$ chính là bí quyết biến hồi quy Ridge trơn thành hồi quy Lasso tạo nghiệm thưa.
- **Ma trận và ánh xạ tuyến tính:** Mô tả mọi ràng buộc tuyến tính $$Ax = b$$, toán tử chiếu lên không gian con và cấu trúc hạng (rank) quyết định bài toán có nghiệm duy nhất, vô số nghiệm hay vô nghiệm.
- **Giá trị riêng, vector riêng và ma trận xác định dương:** Phổ của ma trận Hessian $$\nabla^2 f$$ quyết định hình dáng các đường mức (hình tròn đẹp hay elip kéo dẹt khó hội tụ) thông qua **chỉ số điều kiện** $$\kappa = \lambda_{\max}/\lambda_{\min}$$.

### Giải thích: Giải tay bài toán bình phương tối thiểu bằng phương trình chuẩn

Giả sử ta muốn tìm số thực $$x \in \mathbb{R}$$ khớp tốt nhất hai phương trình mâu thuẫn $$1\cdot x \approx 2$$ và $$2\cdot x \approx 5$$, tức giải $$\min_x \|Ax - b\|_2^2$$ với $$A = \begin{pmatrix}1\\ 2\end{pmatrix}, b = \begin{pmatrix}2\\ 5\end{pmatrix}$$:

1. **Lập phương trình chuẩn $$A^T A x = A^T b$$:**
   $$A^T A = 1^2 + 2^2 = 5, \qquad A^T b = 1\cdot 2 + 2\cdot 5 = 12.$$
2. **Giải nghiệm tối ưu:**
   $$x^* = \frac{12}{5} = 2.4.$$
3. **Kiểm tra trực giao hình học:** Vector sai số (phần dư) là:
   $$r = b - Ax^* = \begin{pmatrix}2\\ 5\end{pmatrix} - \begin{pmatrix}2.4\\ 4.8\end{pmatrix} = \begin{pmatrix}-0.4\\ 0.2\end{pmatrix}.$$
   Tính tích vô hướng với cột của $$A$$: $$A^T r = 1(-0.4) + 2(0.2) = 0$$! Phần dư $$r$$ vuông góc tuyệt đối với không gian cột của $$A$$, chứng tỏ $$Ax^*$$ chính là hình chiếu gần $$b$$ nhất với sai số bình phương nhỏ nhất $$\|r\|_2^2 = (-0.4)^2 + 0.2^2 = 0.2$$.

---

Trong hầu hết các thuật toán tối ưu hóa, mỗi bước lặp đều thao tác trên vector, mỗi ràng buộc tuyến tính là một tích ma trận–vector, và độ cong cục bộ được mô tả qua các giá trị riêng của ma trận Hessian hoặc ma trận Gram. Trang này giới thiệu tổng quan cho ba bài đại số tuyến tính tiếp theo.

## Các đối tượng sử dụng xuyên suốt khóa học

- **Vector và tích trong.** Hình học Euclid $$\langle g, d\rangle = g^\top d$$ quyết định $$d$$ có phải hướng giảm hay không ($$g^\top d < 0$$). Các hình học khác (Mahalanobis, ánh xạ gương) sẽ xuất hiện ở phần sau dưới dạng tiền điều kiện và chuẩn đối ngẫu (Chương 13).
- **Ma trận như ánh xạ tuyến tính.** Ràng buộc đẳng thức $$Ax = b$$ xác định một không gian affine; hạt nhân (kernel) của $$A$$ là không gian các hướng bước khả thi. Bài toán bình phương tối thiểu (Chương 05) giải hệ $$A^\top A \hat{x} = A^\top y$$ khi $$A$$ đủ hạng cột.
- **Giá trị riêng và dạng toàn phương.** Nếu $$Q\succeq 0$$ thì hàm $$x\mapsto x^\top Q x$$ là hàm lồi; số điều kiện $$\kappa = \lambda_{\max}(Q)/\lambda_{\min}(Q)$$ của một hàm toàn phương lồi mạnh chính là yếu tố làm chậm gradient descent thuần và là động lực cho các phương pháp tăng tốc (Chương 06, 09, 26).

Mọi ma trận đối xứng $$Q$$ đều chéo hóa trực giao được dưới dạng $$Q = U\Lambda U^\top$$. Thương Rayleigh

$$
\lambda_{\min}(Q) = \min_{\|x\|_2=1} x^\top Q x, \qquad \lambda_{\max}(Q) = \max_{\|x\|_2=1} x^\top Q x
$$

là cách trực quan nhất để xác định các hằng số lồi mạnh và độ trơn.

## Các bài trong phần này

1. Vector và không gian vector
2. Ma trận và phép biến đổi tuyến tính
3. Giá trị riêng và vector riêng

Tự kiểm tra: hãy giải thích trong một câu vì sao điều kiện $$\nabla^2 f(x)\succeq 0$$ tại mọi điểm kéo theo hàm $$f$$ khả vi hai lần là hàm lồi. (Chương 03 sẽ chứng minh đầy đủ; đại số tuyến tính giúp ta hiểu rõ ý nghĩa của mệnh đề này.)
