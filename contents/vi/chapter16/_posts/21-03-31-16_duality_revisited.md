---
layout: post
title: 16 Tính đối ngẫu - nhìn lại
chapter: '16'
order: 1
owner: Minjoo Lee
categories:
- chapter16
lang: vi
---

Nếu ví các chương trước về đối ngẫu như việc học từng nốt nhạc riêng lẻ — hàm Lagrange, điều kiện KKT, hàm liên hợp, đường trung tâm — thì Chương 16 chính là khoảnh khắc ta đứng lùi lại để nghe trọn vẹn **bản giao hưởng thống nhất** trước khi bước vào đỉnh cao của tối ưu hóa lồi: **phương pháp điểm trong nguyên thủy – đối ngẫu (Primal-Dual Interior-Point Method)** ở Chương 17.

Thay vì giải bài toán nguyên thủy rồi mới tìm biến đối ngẫu một cách thụ động như trong phương pháp chắn (Chương 15), phương pháp nguyên thủy – đối ngẫu sẽ cập nhật **cả biến nguyên thủy $$x$$ và biến đối ngẫu $$(u, v)$$ song song trong cùng một bước Newton**! Để cỗ máy song song đó vận hành trơn tru, Chương 16 hệ thống lại ba viên đá tảng ở góc nhìn tinh gọn và tổng quát nhất: **Đối ngẫu Lagrange dạng minimax**, **hệ điều kiện tối ưu KKT vs. đường trung tâm**, và **Đối ngẫu Fenchel cho quy hoạch nón**.

## Kiến thức cần nhớ: Ba viên đá tảng chuẩn bị cho Phương pháp Nguyên thủy – Đối ngẫu

- **Đối ngẫu Lagrange dạng trò chơi Minimax:** Viết cả bài toán nguyên thủy $$\min_x \max_{u \ge 0, v} L(x, u, v)$$ và bài toán đối ngẫu $$\max_{u \ge 0, v} \min_x L(x, u, v)$$ trên cùng một hàm $$L$$ giúp thấy ngay đối ngẫu yếu chỉ là bất đẳng thức $$\max \min \le \min \max$$, còn đối ngẫu mạnh là điểm yên ngựa!
- **So sánh trực diện KKT và phương trình đường trung tâm:** Hệ KKT gốc có phương trình bù yếu $$u_i h_i(x) = 0$$, còn đường trung tâm chỉ thay đúng số $$0$$ ấy bằng $$-1/t$$ — chuẩn bị trực tiếp cho bước giải hệ phi tuyến nguyên thủy – đối ngẫu bằng phương pháp Newton ở Chương 17.
- **Đối ngẫu Fenchel và Quy hoạch nón (Conic Programming):** Thay vì bị bó buộc bởi bất đẳng thức vô hướng $$h_i(x) \le 0$$, đối ngẫu Fenchel kết hợp hàm liên hợp $$f^*, g^*$$ với nón đối ngẫu $$K^*$$ để bao quát cùng lúc LP, SOCP và SDP dưới một khung lý thuyết duy nhất.

### Giải thích: Nhìn trọn vẹn bài toán nguyên thủy, đối ngẫu và điểm yên ngựa trên một ví dụ 2 biến

Xét bài toán quy hoạch tuyến tính chuẩn nhỏ nhất có thể:
$$\min_{x \in \mathbb{R}^2} 2x_1 + 3x_2 \qquad \text{với điều kiện } x_1 + x_2 = 1, \;\; x_1 \ge 0, \;\; x_2 \ge 0.$$

1. **Hàm Lagrange chung cho cả hai chiều:**
   Với $$u = (u_1, u_2) \ge 0$$ (cho $$-x_1 \le 0, -x_2 \le 0$$) và $$v \in \mathbb{R}$$ (cho $$1 - x_1 - x_2 = 0$$):
   $$L(x, u, v) = (2 - u_1 - v)x_1 + (3 - u_2 - v)x_2 + v.$$
2. **Nhìn theo chiều Nguyên thủy ($$\min_x \max_{u \ge 0, v} L$$):**
   Nếu $$x_1 < 0$$, chọn $$u_1 \to +\infty$$ đẩy $$\max L \to +\infty$$; nếu $$x_1 + x_2 \ne 1$$, chọn $$v \to \pm\infty$$ cũng đẩy $$\max L \to +\infty$$. Vậy cực tiểu chỉ tồn tại trên tập khả thi và đạt tại $$x^\star = (1, 0)^T$$ với $$p^\star = 2$$.
3. **Nhìn theo chiều Đối ngẫu ($$\max_{u \ge 0, v} \min_x L$$):**
   Để $$\min_x L > -\infty$$ ta cần $$2 - u_1 - v = 0$$ và $$3 - u_2 - v = 0$$, tức $$v \le 2$$ và $$v \le 3$$. Cực đại hóa $$v$$ cho ra $$v^\star = 2$$, $$u^\star = (0, 1)^T$$ và $$d^\star = 2 = p^\star$$!
4. **Điểm yên ngựa $$(x^\star, u^\star, v^\star)$$:** Tại $$x^\star = (1, 0), u^\star = (0, 1), v^\star = 2$$, mọi điều kiện KKT đều khớp hoàn toàn: $$u_1^\star x_1^\star = 0 \cdot 1 = 0$$ và $$u_2^\star x_2^\star = 1 \cdot 0 = 0$$!

---

Trong chương này, chúng ta hệ thống lại những kiến thức nền tảng về tính đối ngẫu trước khi đi vào phương pháp điểm trong nguyên thủy – đối ngẫu (Primal-Dual Interior-Point). Phương pháp điểm trong nguyên thủy – đối ngẫu có thể xem là một mở rộng của phương pháp rào cản (Barrier method), trong đó khái niệm đối ngẫu đóng vai trò then chốt xuyên suốt quá trình xây dựng thuật toán.

## Tài liệu tham khảo và đọc thêm

* O. Guler (2010), “Foundations of Optimization”, Chapter 11.
* J. Renegar (2001), “A mathematical view of interior-point methods in convex optimization,” Chapters 2 and 3.
* S. Wright (1997), “Primal-dual interior-point methods”, Chapters 5 and 6.
