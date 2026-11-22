---
layout: post
title: 27-04 Khung vi phân tự động và ML khoa học
chapter: '27'
order: 5
owner: Nguyen Le Linh
categories:
- chapter27
lang: vi
lesson_type: optional
---


Các bài 27-01 đến 27-03 trình bày nền tảng toán học của vi phân tự động: đồ thị tính toán, tích Jacobian–vector (JVP) ở chế độ thuận và tích vector–Jacobian (VJP) ở chế độ nghịch. Bài đọc tùy chọn này giới thiệu cách các chế độ đó được triển khai trong *hệ sinh thái phần mềm* giai đoạn 2022–2026. Bài tổng quan của Baydin, Pearlmutter, Radul và Siskind (*JMLR* 18(153), 2018, [jmlr.org/papers/v18/17-468.html](https://www.jmlr.org/papers/v18/17-468.html)) vẫn là tài liệu tham khảo lý thuyết chuẩn; còn các khung dưới đây là những công cụ được sử dụng trực tiếp trong thực tế.

## 1. PyTorch: chế độ nghịch trên băng động và biên dịch đồ thị

Paszke và cộng sự (*Automatic differentiation in PyTorch*, hội thảo Autodiff NIPS 2017; *PyTorch: An Imperative Style, High-Performance Deep Learning Library*, NeurIPS 2019) xây dựng AD chiều nghịch dựa trên băng tính toán động: chạy mã Python ở lượt thuận, ghi lại các nút `grad_fn` rồi phát ngược để tính đạo hàm. **PyTorch 2.0** (2023) bổ sung `torch.compile` (TorchDynamo + Inductor), cho phép thu nhận và biên dịch cùng đồ thị chiều nghịch đó để tối ưu tốc độ mà vẫn bảo toàn cơ chế vi phân. Nguyên tắc kiểm chứng không đổi: nếu kết quả `torch.autograd.grad` lệch so với biến liên hợp tính tay, lỗi nằm ở cấu trúc đồ thị hoặc thao tác `detach`. PyTorch phù hợp khi mô hình có đồ thị động, tận dụng hệ sinh thái thị giác máy tính / LLM và cần gỡ lỗi thuận tiện.

## 2. JAX: phép biến đổi hàm kết hợp JVP và VJP

Bradbury, Frostig, Hawkins, Johnson, Leary, Maclaurin, Necula, Paszke, VanderPlas, Wanderman-Milne và Zhang (*JAX: composable transformations of Python+NumPy programs*, 2018–, [github.com/google/jax](https://github.com/google/jax)) thiết kế `grad`, `vmap`, `jit` và `pmap` như các *phép biến đổi hàm thuần túy*. Hai chế độ `jax.jvp` (thuận) và `jax.vjp` / `jax.grad` (nghịch) được cung cấp trực tiếp ở mức API cốt lõi. Nhờ sử dụng mảng bất biến và hàm thuần, JAX trở thành lựa chọn phổ biến trong học máy khoa học giai đoạn 2022–2026 (mạng nơ-ron tích hợp vật lý, thế năng phân tử, mô phỏng khả vi): người dùng dễ dàng vector hóa một mô phỏng bằng `vmap` rồi lấy đạo hàm bằng `grad` và biên dịch qua XLA.

## 3. Enzyme: vi phân tự động ở tầng trình biên dịch

Moses và Churavy (*Instead of rewriting foreign code for machine learning, automatically synthesize fast gradients*, NeurIPS 2020) triển khai AD chiều nghịch trực tiếp trên **LLVM IR**, giúp các chương trình viết bằng C++, Fortran, Julia và Rust có thể vi phân tự động mà không cần viết lại bằng Python. Các công trình tiếp theo — Moses, Churavy, Paehler và cộng sự (*Reverse-Mode Automatic Differentiation and Optimization of GPU Kernels via Enzyme*, SC 2021) cùng Moses, Narayanan, Paehler và cộng sự (*Scalable Automatic Differentiation of Multiple Parallel Paradigms*, SC 2022) — mở rộng phương pháp này sang CUDA, OpenMP, MPI và các tác vụ song song trong Julia. Giao diện Enzyme-JAX (từ 2023) cho phép đăng ký các kernel đó như phép toán nguyên thủy của JAX, giúp `jax.grad` vi phân xuyên qua cả bộ giải truyền nhiệt viết bằng Fortran.

## 4. Học máy khoa học và mạng nơ-ron tích hợp vật lý (PINN)

Một mạng nơ-ron tích hợp vật lý (Physics-Informed Neural Network — PINN) cực tiểu hóa phần dư phương trình vi phân $$r_\theta(x)=\mathcal{L}[u_\theta](x)$$, trong đó các đạo hàm riêng theo *biến đầu vào* $$x$$ (không chỉ theo tham số $$\theta$$) đều được tính bằng AD. Công trình của Raissi, Perdikaris và Karniadakis (*J. Comput. Phys.* 378:686–707, 2019) và bài tổng quan của Karniadakis, Kevrekidis, Lu, Perdikaris, Wang và Yang (*Nature Reviews Physics* 3:422–440, 2021) đã đưa PINN thành một hướng nghiên cứu lớn. Các phát triển giai đoạn 2022–2025 (phần dư có trọng số nhân quả, học toán tử, mô phỏng lai Enzyme+JAX) đều kết hợp chế độ nghịch theo $$\theta$$ với chế độ thuận hoặc nghịch lồng nhau theo $$x$$. Đây là minh họa rõ ràng cho thấy “một hàm mất mát vô hướng với hàng triệu tham số” không phải là dạng truy vấn AD duy nhất trong thực tế.

```python
# JAX: chế độ nghịch cho tham số, JVP chế độ thuận cho đạo hàm theo hướng
import jax, jax.numpy as jnp

def loss(w, x, y):
    return jnp.mean((x @ w - y) ** 2)

w = jnp.zeros(3)
g = jax.grad(loss)(w, jnp.ones((8, 3)), jnp.zeros(8))  # VJP cho hàm mất mát vô hướng
_, jvp = jax.jvp(lambda v: v @ v, (w,), (jnp.ones(3),))  # đạo hàm theo hướng
```

**Bài tập.** Cài đặt hàm $$f(w)=\|Aw-b\|_2^2$$ bằng NumPy, PyTorch và (nếu có sẵn) JAX; đối chiếu công thức giải tích `2 * A.T @ (A @ w - b)` với `torch.autograd` và `jax.grad`. Tiếp theo, đo thời gian tính ma trận *Jacobian* của một ánh xạ có ít đầu vào (ví dụ 2 hoặc 3 chiều) và 8 đầu ra bằng hai cách: (i) 8 lần gọi chế độ nghịch theo từng đầu ra và (ii) các lần gọi JVP chế độ thuận theo từng đầu vào — chế độ thuận sẽ nhanh hơn, minh họa trực tiếp phân tích độ phức tạp ở mục 27-02.

## Nguồn

- A. G. Baydin et al., *JMLR* 18(153), 2018 — khảo sát AD.
- A. Paszke et al., NeurIPS 2019 — PyTorch.
- J. Bradbury et al., 2018– — JAX.
- W. S. Moses and V. Churavy, NeurIPS 2020; Moses et al., SC 2021 & SC 2022 — Enzyme.
- M. Raissi, P. Perdikaris, G. E. Karniadakis, *J. Comput. Phys.* 378, 2019 — PINN.
- G. E. Karniadakis et al., *Nat. Rev. Phys.* 3:422–440, 2021 — khảo sát ML thông tin vật lý.
