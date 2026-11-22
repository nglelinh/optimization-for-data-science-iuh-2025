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


**Vi phân tự động chiều nghịch (reverse-mode AD)** gắn cho mỗi nút $$v$$ một biến **liên hợp (adjoint)** $$\bar v = \frac{\partial \ell}{\partial v}$$ đối với đầu ra vô hướng $$\ell$$. Sau lượt thuận lưu lại các giá trị trung gian, thuật toán duyệt *ngược* đồ thị và cộng dồn đạo hàm:

$$
\bar u \mathrel{+}= \bar v\cdot \partial_u h
\quad\text{khi } v=h(u,\ldots).
$$

Chỉ trong một lượt duyệt ngược duy nhất, thuật toán thu được toàn bộ gradient $$\nabla_w \ell$$ — tương ứng với một **tích vector–Jacobian (VJP)** $$(\nabla \ell)^\top J$$. Chi phí tính toán chỉ gấp một hằng số nhỏ lần chi phí lượt thuận và *không phụ thuộc vào số lượng tham số*. Tính chất này chính là nền tảng giúp việc huấn luyện các mạng nơ-ron sâu hàng triệu hoặc hàng tỷ tham số trở nên khả thi.

**Lan truyền ngược (backpropagation)** là trường hợp riêng của AD chiều nghịch áp dụng cho mạng nơ-ron nhiều lớp, trong đó biến liên hợp tại lớp $$\ell$$ chính là tín hiệu sai số $$\delta^{(\ell)}$$ quen thuộc:

$$
\delta^{(\ell)} = \bigl(W^{(\ell+1)\top}\delta^{(\ell+1)}\bigr)\odot \phi'(z^{(\ell)}).
$$

Về bản chất, không có phép biến đổi đặc biệt nào ngoài quy tắc dây chuyền: mỗi phép nhân ma trận và hàm kích hoạt chỉ là một nút sơ cấp với Jacobian cục bộ đã biết.

```python
# Ví dụ vô hướng: ℓ = (w2 * relu(w1 * x) - y)**2
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

Bạn có thể đối chiếu kết quả trên với PyTorch bằng cách dựng cùng biểu thức với các tensor đặt `requires_grad=True` rồi gọi `ell.backward()`.

**Đánh đổi bộ nhớ.** Chế độ nghịch phải lưu lại các giá trị trung gian của lượt thuận để dùng khi duyệt ngược. Kỹ thuật *gradient checkpointing* (tính lại một phần lượt thuận khi cần) đánh đổi thời gian tính toán lấy dung lượng bộ nhớ RAM/VRAM khi huấn luyện mô hình lớn — đây là kỹ thuật quản lý bộ nhớ trong cài đặt, không làm thay đổi giá trị đạo hàm.

Tóm lại, hãy ưu tiên chế độ thuận khi bài toán có ít đầu vào và nhiều đầu ra, còn ưu tiên chế độ nghịch khi có một hàm mất mát vô hướng và rất nhiều tham số. Sự kết hợp hai chế độ (chẳng hạn tính tích Hessian–vector bằng lược đồ thuận-trên-nghịch) cho phép các phương pháp bậc hai và tối ưu hai mức giữ chi phí tuyến tính theo số chiều.
