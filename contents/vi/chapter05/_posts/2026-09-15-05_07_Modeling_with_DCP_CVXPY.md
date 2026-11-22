---
layout: post
title: 05-07 Mô hình hóa bằng DCP và CVXPY
chapter: '05'
order: 13
owner: Nguyen Le Linh
categories:
- chapter05
lang: vi
lesson_type: required
---

Quy hoạch lồi có kỷ luật (Disciplined Convex Programming - DCP) là quy tắc mô hình hóa nền tảng của [CVXPY](https://www.cvxpy.org/): người dùng lắp ghép các hàm nguyên tử (atoms) đã được thư viện xác định trước tính lồi hoặc lõm theo các quy tắc *bảo toàn tính lồi*. Khi bộ chuẩn hóa/chuyển đổi (canonicalizer) chấp nhận mô hình, bài toán sẽ được tự động đưa về một bài toán quy hoạch nón chuẩn (đúng theo hệ phân loại của chương này) và chuyển cho các bộ giải số như OSQP, SCS, Clarabel hoặc ECOS.

Đây là nguyên tắc thực hành quen thuộc của khóa học Stanford EE364a: **mô hình hóa trước, chọn thuật toán sau**. Đối với các bài toán chuẩn như Lasso, SVM hay QP tối ưu hóa danh mục đầu tư, ta nên mô hình hóa trực tiếp bằng công cụ chuyên dụng thay vì tự cài đặt hạ gradient chiếu (trừ khi mục tiêu là học sâu về thuật toán).

## Tóm tắt ý tưởng DCP

Hàm hợp $$f(g(x))$$ là hàm lồi khi, chẳng hạn, $$f$$ lồi và đơn điệu tăng còn $$g$$ là hàm lồi (Boyd & Vandenberghe, Chương 3). CVXPY cung cấp một danh mục hữu hạn các hàm nguyên tử (`norm`, `sum_squares`, `abs`, `quad_over_lin`, `logistic`, …) và sẽ từ chối các biểu thức không thể chứng nhận tính lồi theo quy tắc này. Việc bị từ chối không nhất thiết có nghĩa là bài toán không lồi — đôi khi biểu thức chỉ đang được viết ở dạng mà bộ chuẩn hóa/chuyển đổi không nhận diện được. Cách xử lý đúng là viết lại biểu thức bằng các hàm nguyên tử hợp lệ chứ không tắt kiểm tra DCP.

Cài đặt thư viện:

```bash
pip install cvxpy numpy
```

## Bài thực hành nhỏ A — Lasso

Cho ma trận thiết kế $$A\in\mathbb{R}^{m\times n}$$ và vectơ mục tiêu $$b$$, bài toán Lasso:

$$
\min_x \tfrac12\|Ax-b\|_2^2 + \lambda \|x\|_1
$$

có thể viết lại như một bài toán QP lồi (số hạng sai số bình phương là hàm bậc hai lồi; chuẩn $$\|\cdot\|_1$$ là hàm lồi). Trong CVXPY, mô hình chỉ cần vài dòng với các hàm nguyên tử sẵn có:

```python
import cvxpy as cp
import numpy as np

np.random.seed(0)
m, n = 80, 40
A = np.random.randn(m, n)
x_true = np.zeros(n)
x_true[:5] = np.array([1.2, -0.8, 0.4, 0.0, -1.1])
b = A @ x_true + 0.05 * np.random.randn(m)
lam = 0.2

x = cp.Variable(n)
objective = 0.5 * cp.sum_squares(A @ x - b) + lam * cp.norm1(x)
prob = cp.Problem(cp.Minimize(objective))
prob.solve(solver=cp.OSQP)  # hoặc SCS / CLARABEL
print("status:", prob.status, "opt:", prob.value)
print("nnz ~", np.sum(np.abs(x.value) > 1e-4))
```

Hãy so sánh tập tọa độ khác không (support) khôi phục được với `x_true`, đồng thời thử thay đổi $$\lambda$$ để quan sát sự đánh đổi giữa độ thưa và độ khớp dữ liệu — đây cũng chính là quỹ đạo nghiệm mà phương pháp hạ gradient cận kề sẽ khảo sát ở Chương 09.

## Bài thực hành nhỏ B — SVM biên cứng dưới dạng QP

Với các cặp dữ liệu gán nhãn tách tuyến tính được $$(a_i,y_i)$$, $$y_i\in\{-1,1\}$$, bài toán SVM biên cứng có dạng:

$$
\begin{align}
\min_{w,b} \quad & \tfrac12 \|w\|_2^2 \\
\text{s.t.} \quad & y_i(w^\top a_i + b) \ge 1, \quad i=1,\ldots,m.
\end{align}
$$

```python
import cvxpy as cp
import numpy as np

np.random.seed(1)
m, d = 60, 2
a = np.random.randn(m, d)
y = np.sign(a[:, 0] - 0.2 * a[:, 1] + 0.1)
y[y == 0] = 1

w = cp.Variable(d)
b = cp.Variable()
prob = cp.Problem(
    cp.Minimize(0.5 * cp.sum_squares(w)),
    [cp.multiply(y, a @ w + b) >= 1],
)
prob.solve()
print("status:", prob.status, "||w|| =", np.linalg.norm(w.value))
```

Nếu `status` trả về `infeasible`, tập điểm dữ liệu không tách tuyến tính được — khi đó có thể chuyển sang mô hình SVM biên mềm với hàm mất mát hinge (`cp.pos(1 - cp.multiply(y, a @ w + b))`), vốn vẫn tuân thủ đầy đủ quy tắc DCP.

## Điểm cần ghi nhớ

- DCP là một hệ quy tắc *đủ* để chứng nhận tính lồi, nhưng không phải điều kiện cần (không bao quát mọi cách viết của hàm lồi).
- Bộ giải (chứ không phải vòng lặp Python tự viết) sẽ quyết định việc dùng Simplex, phương pháp điểm trong hay phương pháp nón bậc nhất.
- Khi bài toán không thể biểu diễn theo DCP (như huấn luyện mạng nơ-ron sâu hoặc phần lớn bài toán ERM không lồi), ta chuyển sang các phương pháp tối ưu không lồi ở [Chương 26]({{ site.baseurl }}/contents/vi/chapter26/) kết hợp vi phân tự động ([Chương 27]({{ site.baseurl }}/contents/vi/chapter27/)).

**Bài tập.** Thay số hạng phạt của Lasso bằng Elastic Net $$\lambda(\alpha\|x\|_1 + \tfrac{1-\alpha}{2}\|x\|_2^2)$$ và kiểm chứng rằng CVXPY vẫn chấp nhận bài toán. Sau đó thử viết chuẩn giả $$\|x\|_0$$ — bộ chuẩn hóa/chuyển đổi sẽ từ chối vì không tuân thủ DCP.
