---
layout: post
title: 02-06 Hình nón đối ngẫu và bất đẳng thức tổng quát
chapter: '02'
order: 14
owner: Wontak Ryu
categories:
- chapter02
lang: vi
---

Làm thế nào để kiểm tra một điểm $$x$$ có nằm trong một hình nón phức tạp $$K$$ hay không, hoặc tìm ra tất cả các phương án tối ưu Pareto của một bài toán đa mục tiêu mà không phải dò mù trong không gian nhiều chiều? Câu trả lời của giải tích lồi là bước sang "thế giới gương": gắn cho mỗi hình nón $$K$$ một **hình nón đối ngẫu** $$K^*$$ gồm tất cả các vector tạo góc nhọn (hoặc vuông) với mọi phần tử của $$K$$.

Phần 02-06 mở màn cho tư duy đối ngẫu — một trong những công cụ biến đổi góc nhìn mạnh mẽ nhất của toàn bộ lý thuyết tối ưu hóa.

## Bản đồ kiến thức nền: Ba vai trò của Hình nón đối ngẫu

- **Định nghĩa hình học qua góc nhọn:** $$K^* = \{y : y^T x \ge 0,\ \forall x \in K\}$$. Dù $$K$$ có lồi hay không, $$K^*$$ **luôn là hình nón lồi đóng** (vì là giao của vô số nửa không gian đi qua gốc tọa độ)!
- **Tính tự đối ngẫu (Self-duality):** Ba hình nón quan trọng nhất trong tối ưu hóa — $$\mathbb{R}_+^n$$, nón bậc hai $$\ell_2$$ và nón ma trận $$\mathbb{S}_+^n$$ — đều có tính chất kỳ diệu $$K^* = K$$.
- **Đặc trưng hóa bất đẳng thức và cực tiểu Pareto:** Nhờ $$K^*$$, bài toán tìm nghiệm cực tiểu theo thứ tự nón phức tạp chuyển thành bài toán vô hướng hóa (scalarization) $$\min_{x \in S} \lambda^T x$$ với trọng số $$\lambda \in K^*$$.

### Khung giải thích (nên đọc chậm): Dùng nhân chứng đối ngẫu để kiểm tra $$x \succeq_K 0$$

Xét hình nón thích hợp $$K = \mathbb{R}_+^2$$ (tự đối ngẫu: $$K^* = \mathbb{R}_+^2$$). Tính chất nền tảng khẳng định:
$$x \in K \iff \lambda^T x \ge 0 \quad \text{với mọi } \lambda \in K^*.$$

1. **Trường hợp đúng ($$x = (2, 3)^T$$):** Với mọi $$\lambda = (\lambda_1, \lambda_2)^T \in \mathbb{R}_+^2$$ (tức $$\lambda_1, \lambda_2 \ge 0$$), ta luôn có $$\lambda^T x = 2\lambda_1 + 3\lambda_2 \ge 0$$. Vậy $$x \in K$$.
2. **Trường hợp sai ($$x = (2, -1)^T$$):** Ta chỉ cần chỉ ra **một nhân chứng đối ngẫu** duy nhất $$\lambda = (0, 1)^T \in K^*$$:
   $$\lambda^T x = 0(2) + 1(-1) = -1 < 0.$$
   Nhân chứng $$\lambda = (0, 1)^T$$ lập tức bác bỏ $$x \in K$$ — đây chính là cơ chế hình học đằng sau "chứng chỉ vô nghiệm" (certificate of infeasibility) trong các bộ giải tối ưu!

---

Phần này giới thiệu khái niệm hình nón đối ngẫu gắn với mỗi hình nón và bất đẳng thức tổng quát đối ngẫu tương ứng. Nhờ bất đẳng thức tổng quát đối ngẫu, ta có thể chuyển việc so sánh theo thứ tự hình nón về so sánh các tích vô hướng, giúp việc phân tích trở nên thuận tiện hơn nhiều.