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

Trước năm 2005, nếu muốn dùng bộ giải điểm trong để giải một bài toán tối ưu hóa lồi mới, nghiên cứu sinh phải dành hàng tuần biến đổi tay các hàm $$\log$$, chuẩn $$\ell_1$$, tổng bình phương thành hàng trăm ma trận thưa $$G, h, A, b$$ của Quy hoạch Nón — chỉ cần nhầm một dấu trừ là bộ giải báo vô nghiệm hoặc ra kết quả vô nghĩa!

Mọi thứ thay đổi hoàn toàn khi Michael Grant và Stephen Boyd phát minh ra **Quy hoạch Lồi có Kỷ luật (Disciplined Convex Programming - DCP)** và sau đó cộng đồng xây dựng thư viện mã nguồn mở **CVXPY**. Với DCP, bạn viết bài toán gần như y hệt công thức toán trên bảng trắng; bộ kiểm tra tự động xác minh tính lồi theo cây cú pháp rồi tự động biên dịch xuống đúng nón LP/QP/SOCP/SDP và gọi bộ giải cho bạn chỉ trong vài dòng Python!

## Kiến thức cần nhớ: Bộ quy tắc ngữ pháp của DCP và CVXPY

Để không bao giờ bị CVXPY báo lỗi `DCPError` mà không hiểu tại sao, hãy nắm chắc ba trụ cột:

- **Thư viện hàm nguyên tử (Atoms) có sẵn độ cong và tính đơn điệu:** Mỗi hàm cơ bản trong CVXPY (như `sum_squares`, `norm1`, `log`, `quad_over_lin`) đều gắn nhãn sẵn: *độ cong* (affine, convex, concave) và *tính đơn điệu* (tăng, giảm, không đơn điệu) trên từng đối số.
- **Quy tắc hợp thành DCP (DCP Composition Rule):** Để khẳng định $$h(g(x))$$ là **lồi** mà không cần tính Hessian, DCP kiểm tra điều kiện đủ:
  - $$h$$ lồi và **tăng**, còn $$g$$ **lồi**; HOẶC
  - $$h$$ lồi và **giảm**, còn $$g$$ **lõm**; HOẶC
  - $$g$$ là hàm **affine**.
  (Lưu ý quan trọng: DCP là điều kiện *đủ*, không phải *cần*! Một biểu thức thực sự lồi như `sqrt(1 + x^2)` vẫn bị DCP từ chối nếu viết ngây thơ, và phải viết lại bằng atom `norm2([1, x])`!)
- **Tự động chuẩn hóa về dạng nón (Canonicalization):** Sau khi vượt qua kiểm tra DCP, CVXPY tự động sinh biến phụ epigraph để biến biểu thức cấp cao (như Lasso hay SVM) thành ma trận chuẩn cho bộ giải Clarabel, OSQP, ECOS hay SCS.

### Giải thích: Bắt lỗi một biểu thức "lồi thật nhưng vi phạm DCP" và cách sửa chuẩn

Giả sử bạn muốn cực tiểu hóa hàm $$f(x) = \sqrt{x^2 + 4}$$ trên $$x \in \mathbb{R}$$ trong CVXPY.

1. **Bước 1 — Kiểm tra toán học thật:** Đạo hàm $$f'(x) = \frac{x}{\sqrt{x^2+4}}$$, đạo hàm bậc hai $$f''(x) = \frac{4}{(x^2+4)^{3/2}} > 0$$ với mọi $$x$$. Vậy $$f(x)$$ **chắc chắn là hàm lồi chặt**!
2. **Bước 2 — Vì sao viết `cp.sqrt(cp.square(x) + 4)` lại bị lỗi `DCPError`?**
   - Biểu thức trong `g(x) = x^2 + 4` là hàm **lồi** (convex).
   - Hàm ngoài `h(u) = sqrt(u)` là hàm **lõm** (concave) và tăng.
   - Hợp thành *lõm(lồi)* có độ cong **không xác định** theo bảng quy tắc DCP! CVXPY từ chối ngay để bảo đảm an toàn tuyệt đối.
3. **Bước 3 — Viết lại đúng chuẩn DCP:**
   Nhận ra $$\sqrt{x^2 + 4} = \left\| \begin{pmatrix} x \\ 2 \end{pmatrix} \right\|_2$$ — tức là chuẩn Euclidean của một vector **affine** theo $$x$$!
   Trong CVXPY, ta viết `cp.norm2(cp.hstack([x, 2]))`.
   - Đối số bên trong `[x, 2]` là **affine**.
   - Hàm ngoài `norm2` là **lồi**.
   - Theo quy tắc DCP, *lồi(affine)* luôn **lồi**! CVXPY lập tức chấp nhận và biên dịch thành đúng 1 ràng buộc SOCP, trả về nghiệm $$x^\star = 0,\; f^\star = 2$$.

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
