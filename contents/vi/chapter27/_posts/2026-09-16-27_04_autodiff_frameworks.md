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


Các bài 27-01 đến 27-03 là toán: đồ thị tính toán, JVP chế độ thuận, VJP / lan truyền ngược chế độ nghịch. Ghi chú tùy chọn này là nơi các chế độ đó sống trong *phần mềm* năm 2022–2026. Baydin, Pearlmutter, Radul và Siskind, *JMLR* 18(153), 2018, [jmlr.org/papers/v18/17-468.html](https://www.jmlr.org/papers/v18/17-468.html), vẫn là khảo sát trên bàn; các khung dưới đây là những gì bạn thực sự import.

## 1. PyTorch: reverse-mode trên băng, rồi biên dịch

Paszke et al., *Automatic differentiation in PyTorch* (hội thảo Autodiff NIPS, 2017) và *PyTorch: An Imperative Style, High-Performance Deep Learning Library* (NeurIPS 2019) dựng AD chế độ nghịch trên băng động: chạy Python thuận, ghi `grad_fn`, phát băng ngược. Đó là 27-03 với bộ cấp phát. **PyTorch 2.0** (2023) thêm `torch.compile` (TorchDynamo + Inductor): cùng đồ thị chế độ nghịch được bắt, biên dịch, và vẫn được vi phân. Với môn này quy tắc không đổi. Nếu `torch.autograd.grad` lệch với adjoint bạn viết tay, đồ thị hoặc `detach` của bạn sai — không phải định nghĩa đạo hàm. Dùng PyTorch khi mô hình là mạng động, hệ sinh thái là thị giác / LLM, và bạn muốn một băng in được.

## 2. JAX: JVP và VJP kết hợp được

Bradbury, Frostig, Hawkins, Johnson, Leary, Maclaurin, Necula, Paszke, VanderPlas, Wanderman-Milne và Zhang, *JAX: composable transformations of Python+NumPy programs*, 2018–, [github.com/google/jax](https://github.com/google/jax), coi `grad`, `vmap`, `jit` và `pmap` là *phép biến đổi hàm*. `jax.jvp` chế độ thuận và `jax.vjp` / `jax.grad` chế độ nghịch là hai chế độ của chương này, lộ như API hạng nhất. Mảng bất biến; chương trình bạn vi phân là hàm thuần. Ràng buộc đó là lý do nhóm ML khoa học (mạng thông tin vật lý, thế năng phân tử, mô phỏng khả vi) chuẩn hóa trên JAX năm 2022–2026: bạn `vmap` một mô phỏng rồi `grad` phần dư. Dùng JAX khi bạn cần JVP/VJP lồng, batch, hoặc trình biên dịch (XLA) hơn một vườn mô hình tiền huấn luyện.

## 3. Enzyme: vi phân sau trình biên dịch

Moses và Churavy, *Instead of rewriting foreign code for machine learning, automatically synthesize fast gradients*, NeurIPS 2020, chạy AD chế độ nghịch trên **LLVM IR**, nên C++, Fortran, Julia và Rust trở nên khả vi mà không viết lại nguồn. Moses, Churavy, Paehler, et al., *Reverse-Mode Automatic Differentiation and Optimization of GPU Kernels via Enzyme*, SC 2021, và Moses, Narayanan, Paehler, et al., *Scalable Automatic Differentiation of Multiple Parallel Paradigms*, SC 2022, mở cùng ý tưởng tới CUDA, OpenMP, MPI và task Julia. Enzyme-JAX (2023–) đăng ký các kernel đó như primitive JAX, nên `jax.grad` nhìn thấy bộ giải nhiệt Fortran. Đây là câu trả lời thập niên 2020 cho “mô phỏng sản xuất của chúng tôi không phải mô-đun PyTorch.”

## 4. Học máy khoa học / PINN

Một mạng thông tin vật lý cực tiểu hóa phần dư $$r_\theta(x)=\mathcal{L}[u_\theta](x)$$ mà đạo hàm theo *đầu vào* $$x$$ (không chỉ tham số $$\theta$$) đến từ AD. Raissi, Perdikaris và Karniadakis, *J. Comput. Phys.* 378:686–707, 2019, là kinh điển; Karniadakis, Kevrekidis, Lu, Perdikaris, Wang và Yang, *Nature Reviews Physics* 3:422–440, 2021, là khảo sát khiến PINN thành chủ đề khoa học dữ liệu. Sóng 2022–2025 (phần dư nhân quả/có trọng số tốt hơn, học toán tử, mô phỏng lai Enzyme+JAX) vẫn đứng trên chế độ nghịch theo $$\theta$$ và thường *chế độ thuận* hoặc nghịch lồng theo $$x$$. Đó là lý do Chương 27 dạy cả hai chế độ: PINN là ví dụ mà “một loss vô hướng, hàng triệu tham số” *không* phải truy vấn AD duy nhất.

```python
# JAX: chế độ nghịch cho tham số, JVP chế độ thuận nếu cần đạo hàm hướng
import jax, jax.numpy as jnp

def loss(w, x, y):
    return jnp.mean((x @ w - y) ** 2)

w = jnp.zeros(3)
g = jax.grad(loss)(w, jnp.ones((8, 3)), jnp.zeros(8))  # VJP, một vô hướng
_, jvp = jax.jvp(lambda v: v @ v, (w,), (jnp.ones(3),))  # đạo hàm hướng
```

**Bài tập.** Hiện thực $$f(w)=\|Aw-b\|_2^2$$ trong NumPy, PyTorch, và (nếu cài) JAX. So `2 A.T @ (A@w-b)` với `torch.autograd` và `jax.grad`. Rồi bấm giờ một *Jacobian* của ánh xạ 8 đầu ra bằng (i) tám lời gọi chế độ nghịch và (ii) tám JVP chế độ thuận — thuận phải thắng, đó là bài 27-02 dưới dạng phần mềm.

## Nguồn

- A. G. Baydin et al., *JMLR* 18(153), 2018 — khảo sát AD.
- A. Paszke et al., NeurIPS 2019 — PyTorch.
- J. Bradbury et al., 2018– — JAX.
- W. S. Moses and V. Churavy, NeurIPS 2020; Moses et al., SC 2021 & SC 2022 — Enzyme.
- M. Raissi, P. Perdikaris, G. E. Karniadakis, *J. Comput. Phys.* 378, 2019 — PINN.
- G. E. Karniadakis et al., *Nat. Rev. Phys.* 3:422–440, 2021 — khảo sát ML thông tin vật lý.
