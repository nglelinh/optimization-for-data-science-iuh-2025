---
layout: post
title: 05-07 Mô hình hóa bằng DCP và CVXPY
chapter: '05'
order: 12
owner: Nguyen Le Linh
categories:
- chapter05
lang: vi
lesson_type: required
---

Disciplined convex programming (DCP) là hợp đồng mô hình hóa của [CVXPY](https://www.cvxpy.org/): bạn ghép các nguyên tử mà thư viện đã biết là lồi hoặc lõm, theo các quy tắc *bảo toàn* tính lồi. Nếu bộ viết lại chấp nhận mô hình, một bộ giải số (OSQP, SCS, Clarabel, ECOS, …) nhận một chương trình nón chuẩn — cùng phân loại với phần còn lại của chương này.

Đây là thói quen thực hành Stanford EE364a: **mô hình trước, thuật toán sau**. Với Lasso, SVM và QP danh mục, bạn không nên tự viết projected gradient trừ khi đang học thuật toán.

## Ý tưởng DCP trong một đoạn

Hợp thành $$f(g(x))$$ lồi khi, chẳng hạn, $$f$$ lồi và tăng còn $$g$$ lồi (Boyd & Vandenberghe, Ch. 3). CVXPY cài một catalog hữu hạn các nguyên tử (`norm`, `sum_squares`, `abs`, `quad_over_lin`, `logistic`, …) và từ chối biểu thức nó không chứng nhận được. Bị từ chối không phải lúc nào cũng nghĩa là “bài toán không lồi” — đôi khi bạn viết một hàm lồi theo dạng bộ viết lại không nhìn thấy. Cách sửa là viết lại bằng nguyên tử đã biết, không phải tắt lỗi.

Cài một lần:

```bash
pip install cvxpy numpy
```

## Mini-lab A — Lasso

Cho ma trận thiết kế $$A\in\mathbb{R}^{m\times n}$$ và vector đáp $$b$$, Lasso

$$
\min_x \tfrac12\|Ax-b\|_2^2 + \lambda \|x\|_1
$$

là một QP lồi dạng mở rộng (mất mát bình phương là toàn phương lồi; $$\|\cdot\|_1$$ là chuẩn lồi). Trong CVXPY chỉ còn vài nguyên tử:

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

So sánh hỗ trợ khôi phục với `x_true`. Đổi $$\lambda$$ và quan sát đánh đổi thưa–khớp — cùng quỹ đạo mà proximal gradient sẽ vẽ ở Chương 09.

## Mini-lab B — SVM lề cứng như một QP

Với các cặp gán nhãn tách được tuyến tính $$(a_i,y_i)$$, $$y_i\in\{-1,1\}$$, SVM lề cứng là

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

Nếu `status` là infeasible, đám mây không tách được tuyến tính — chuyển sang hinge lề mềm (`cp.pos(1 - cp.multiply(y, a @ w + b))`), vẫn DCP.

## Cần nhớ

- DCP là ngữ pháp *đủ* cho tính lồi, không phải ngữ pháp đầy đủ.
- Bộ giải, không phải vòng lặp Python của bạn, chọn giữa simplex, điểm trong, và phương pháp nón bậc nhất.
- Khi mô hình không viết lại được theo DCP (mạng sâu, phần lớn ERM không lồi), bạn rời chương này và vào [Chương 26]({{ site.baseurl }}/contents/vi/chapter26/) với autodiff ([Chương 27]({{ site.baseurl }}/contents/vi/chapter27/)).

**Bài tập.** Thay phạt Lasso bằng elastic net $$\lambda(\alpha\|x\|_1 + \tfrac{1-\alpha}{2}\|x\|_2^2)$$ và xác nhận CVXPY vẫn nhận bài toán. Rồi thử viết $$\|x\|_0$$ — bộ viết lại phải từ chối.
