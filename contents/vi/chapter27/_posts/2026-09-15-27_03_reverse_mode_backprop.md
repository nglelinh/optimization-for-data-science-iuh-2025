---
layout: post
title: 27-03 Chiều nghịch và lan truyền ngược
chapter: '27'
order: 4
owner: Nguyen Le Linh
categories:
- chapter27
lang: vi
lesson_type: required
---


**AD chiều nghịch** gắn cho mỗi nút $$v$$ một **liên hợp** $$\bar v = \frac{\partial \ell}{\partial v}$$ với đầu ra vô hướng $$\ell$$. Sau lượt thuận lưu trung gian, ta đi *ngược*:

$$
\bar u \mathrel{+}= \bar v\cdot \partial_u h
\quad\text{khi } v=h(u,\ldots).
$$

Một lượt nghịch cho cả gradient $$\nabla_w \ell$$ — một **tích vector–Jacobian** $$(\nabla \ell)^\top J$$. Chi phí là một hằng số nhỏ lần chi phí thuận, *không phụ thuộc số tham số*. Một câu đó là lý do học sâu khả thi về tính toán.

**Lan truyền ngược** là AD chiều nghịch áp lên mạng phân tầng, liên hợp của một tầng là $$\delta$$ quen thuộc:

$$
\delta^{(\ell)} = \bigl(W^{(\ell+1)\top}\delta^{(\ell+1)}\bigr)\odot \phi'(z^{(\ell)}).
$$

Không có gì huyền bí: nhân ma trận là nút sơ cấp với Jacobian địa phương đã biết.

```python
# Đồ chơi vô hướng: ℓ = (w2 * relu(w1 * x) - y)**2
x, y = 1.5, 0.3
w1, w2 = 0.8, -0.4
z = w1 * x
h = max(z, 0.0)
pred = w2 * h
ell = (pred - y) ** 2
d_ell = 1.0
d_pred = d_ell * 2 * (pred - y)
d_w2 = d_pred * h
d_h = d_pred * w2
d_z = d_h * (1.0 if z > 0 else 0.0)
d_w1 = d_z * x
print(d_w1, d_w2)
```

So với PyTorch: dựng cùng biểu thức bằng tensor `requires_grad=True` rồi `ell.backward()`.

**Bộ nhớ.** Chiều nghịch lưu băng thuận. Checkpoint / tính lại đổi compute lấy RAM — lý do gradient checkpointing xuất hiện khi huấn luyện mô hình lớn. Đó là chú thích cài đặt, không phải đạo hàm khác.

Khi có *nhiều* đầu ra và ít đầu vào, ưu tiên chiều thuận. Khi có một loss và biển trọng số, ưu tiên chiều nghịch. Chế độ hỗn hợp (Hessian–vector forward-over-reverse) là cách một số phương pháp bậc hai và hai tầng giữ chi phí tuyến tính theo chiều.
