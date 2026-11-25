---
layout: post
title: 07-03 Điều kiện tối ưu gradient dưới
chapter: '07'
order: 6
owner: Kyeongmin Woo
categories:
- chapter07
lang: vi
---

Trong giải tích cổ điển, mọi bài toán tìm cực tiểu không ràng buộc đều hội tụ về một phương trình duy nhất: $$\nabla f(x^\star) = 0$$. Khi bước sang thế giới hàm lồi không khả vi của Chương 07, ta chỉ cần thay dấu bằng "`=`" bằng dấu thuộc "`∈`" — và toàn bộ lý thuyết tối ưu hóa lồi (cả không ràng buộc lẫn có ràng buộc, cả trơn lẫn không trơn!) đồng loạt sụp gọn thành **một biểu thức ba ký tự kinh điển**:
$$0 \in \partial f(x^\star).$$

Mục 07-03 sẽ chứng minh định lý gọn nhẹ đến khó tin này, dùng nó để suy dẫn ngược lại điều kiện tối ưu bậc nhất của Chương 04 trong đúng 3 dòng, và giải tường minh ba ví dụ huyền thoại của học máy hiện đại: **Lasso**, **Ngưỡng mềm (Soft-Thresholding)** và **Khoảng cách đến tập lồi**.

## Bản đồ kiến thức nền: Bốn nhánh ứng dụng xuất phát từ $$0 \in \partial f(x^\star)$$

Mọi bài học con trong phần 07-03 đều là một lát cắt trực tiếp của công thức $$0 \in \partial f(x^\star)$$:

- **Chứng minh 1 dòng của $$0 \in \partial f(x^\star)$$:** Không cần đạo hàm, không cần giới hạn, thậm chí **không cần $$f$$ lồi**! Theo định nghĩa subgradient, $$0 \in \partial f(x^\star) \iff f(y) \ge f(x^\star) + 0^T(y - x^\star) \iff f(y) \ge f(x^\star) \; \forall y$$!
- **Hợp nhất Tối ưu có ràng buộc (Chương 04):** Viết $$\min_{x \in C} f(x)$$ thành $$\min_x (f(x) + I_C(x))$$ rồi áp dụng $$0 \in \partial f(x^\star) + N_C(x^\star)$$ cho ngay $$-\nabla f(x^\star) \in N_C(x^\star) \iff \nabla f(x^\star)^T(y - x^\star) \ge 0 \; \forall y \in C$$!
- **Giải mã Lasso & Soft-Thresholding:** Áp dụng $$0 \in X^T(X\beta - y) + \lambda \partial \|\beta\|_1$$ giải thích chính xác tại sao $$\beta_j^\star = 0$$ khi tương quan phần dư $$|X_j^T(y - X\beta^\star)| \le \lambda$$!
- **Hình học Phép chiếu (Khoảng cách đến tập lồi):** Tính subgradient của $$\operatorname{dist}(x, C) = \min_{y \in C} \|x - y\|_2$$ cho thấy hướng ra xa tập lồi $$C$$ chính là vector đơn vị $$\frac{x - P_C(x)}{\|x - P_C(x)\|_2}$$.

### Khung giải thích (nên đọc chậm): Giải bài toán không trơn 1 biến bằng $$0 \in \partial f(x^\star)$$

Tìm cực tiểu toàn cục của hàm $$f(x) = |x - 1| + |x - 3| + |x - 8|$$ (bài toán tìm **trung vị — median** của 3 điểm $$1, 3, 8$$!):

1. **Thử tại $$x = 3$$ (điểm ở giữa):**
   - Tại $$x = 3$$: $$|x - 1|$$ có đạo hàm $$+1$$; $$|x - 8|$$ có đạo hàm $$-1$$; còn $$|x - 3|$$ gãy khúc nên có vi phân dưới $$[-1, 1]$$.
   - Áp dụng quy tắc tổng:
     $$\partial f(3) = \{+1\} + [-1, 1] + \{-1\} = [-1, 1].$$
2. **Kiểm tra điều kiện tối ưu:** Vì $$0 \in [-1, 1] = \partial f(3)$$, ta khẳng định ngay $$x^\star = 3$$ là **điểm cực tiểu toàn cục** (với $$f^\star = |3-1| + 0 + |3-8| = 7$$)!
3. **Thử tại $$x = 4$$ (trung bình cộng $$1+3+8 = 12 \implies 12/3 = 4$$):**
   $$\partial f(4) = \{+1\} + \{+1\} + \{-1\} = \{+1\} \not\ni 0.$$
   (Thật vậy, $$f(4) = 3 + 1 + 4 = 8 > 7$$!) Đó là chứng minh tuyệt đẹp nhất cho thấy **trung vị** tối thiểu hóa tổng sai số tuyệt đối ($$\ell_1$$), còn **trung bình** tối thiểu hóa tổng bình phương sai số ($$\ell_2$$)!

---

Trong phần này, chúng ta trình bày điều kiện tối ưu phát biểu qua gradient dưới, đồng thời phân tích một số ví dụ cụ thể để minh họa cách áp dụng và vai trò của điều kiện này.