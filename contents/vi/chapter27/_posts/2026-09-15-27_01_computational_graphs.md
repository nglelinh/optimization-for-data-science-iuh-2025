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


Một **đồ thị tính toán (computational graph)** là một đồ thị có hướng không chu trình (DAG), trong đó mỗi nút biểu diễn một giá trị trung gian và các cạnh biểu diễn các phép toán sơ cấp ($$+$$, $$\times$$, $$\exp$$, `matmul`, …). Các tham số, dữ liệu đầu vào và hàm mất mát vô hướng đều là các nút được đánh dấu trên đồ thị này.

**Ví dụ.** Xét hàm mất mát logistic trên một mẫu dữ liệu với vector trọng số $$w\in\mathbb{R}^2$$:

$$
z = w_1 x_1 + w_2 x_2, \quad p=\sigma(z), \quad \ell = -y\log p -(1-y)\log(1-p).
$$

Các nút của đồ thị gồm $$x$$, $$w$$, $$z$$, $$p$$ và $$\ell$$. Đồ thị tính toán *chính là* biểu diễn cấu trúc của chương trình. Khi một trọng số thay đổi, mọi nút phía sau đều chịu ảnh hưởng; nhiệm vụ của vi phân tự động là lan truyền độ nhạy từ đầu vào tới $$\ell$$ (chiều thuận) hoặc kéo ngược độ nhạy từ $$\ell$$ về các tham số (chiều nghịch).

Có hai cách triển khai phổ biến trong các thư viện:

* **Ghi băng động / define-by-run** (PyTorch): đồ thị (còn gọi là băng Wengert) được dựng trực tiếp trong lúc hàm `forward` chạy; các cấu trúc rẽ nhánh và vòng lặp dùng thẳng cú pháp Python.
* **Định nghĩa trước khi chạy / define-then-run** (Theano trước đây, hoặc cơ chế truy vết `jit` của JAX): chương trình được biên dịch hoặc truy vết thành một đồ thị tĩnh rồi thực thi lặp lại nhiều lần.

Hiểu cách quản lý đồ thị giải thích trực tiếp vì sao lệnh `y.backward()` trong PyTorch yêu cầu đồ thị còn tồn tại trong bộ nhớ: mặc định sau một lần gọi `backward()`, băng tính toán sẽ được giải phóng trừ khi truyền tham số `retain_graph=True`.

**Bài tập.** Vẽ đồ thị tính toán cho hàm mất mát $$\ell=\|W_2\,\phi(W_1 x)-y\|_2^2$$ của một mạng một lớp ẩn và đếm số phép nhân ma trận ở lượt thuận. Chi phí này sẽ xuất hiện tương ứng ở lượt chiều nghịch.
