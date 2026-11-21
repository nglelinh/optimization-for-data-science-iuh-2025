---
layout: post
title: 27-01 Đồ thị tính toán
chapter: '27'
order: 2
owner: Nguyen Le Linh
categories:
- chapter27
lang: vi
lesson_type: required
---


Một **đồ thị tính toán** là DAG mà nút là giá trị và cạnh ghi các ánh xạ sơ cấp ($$+$$, $$\times$$, $$\exp$$, `matmul`, …). Tham số, đầu vào, và loss vô hướng chỉ là các nút được đánh dấu.

Ví dụ. Mất mát logistic trên một mẫu với trọng số $$w\in\mathbb{R}^2$$:

$$
z = w_1 x_1 + w_2 x_2, \quad p=\sigma(z), \quad \ell = -y\log p -(1-y)\log(1-p).
$$

Nút: $$x$$, $$w$$, $$z$$, $$p$$, $$\ell$$. Đồ thị *chính là* chương trình. Đổi một trọng số đổi mọi nút hạ lưu; việc của AD là đẩy độ nhạy đó tới $$\ell$$ hoặc kéo độ nhạy của $$\ell$$ về phía sau.

Hai phong cách cài:

- **Băng Wengert / define-by-run** (PyTorch): đồ thị được ghi khi `forward` Python chạy. Luồng điều khiển là Python thường.
- **Define-then-run** (Theano lịch sử, vết `jit` của JAX): bạn dựng hoặc truy vết một đồ thị tĩnh rồi thực thi nhiều lần.

Với môn này, khác biệt chỉ để bạn biết vì sao `y.backward()` cần đồ thị còn tồn tại — gọi `backward` hai lần mà không `retain_graph` sẽ giải phóng băng.

**Bài tập.** Vẽ đồ thị cho $$\ell=\|W_2\,\phi(W_1 x)-y\|_2^2$$ với một tầng ẩn. Đếm số phép nhân chiều thuận. Con số đó sẽ xuất hiện lại như chi phí reverse mode.
