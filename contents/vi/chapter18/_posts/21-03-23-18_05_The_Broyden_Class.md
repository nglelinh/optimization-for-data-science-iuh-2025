---
layout: post
title: 18-05 Lớp Broyden
chapter: '18'
order: 6
owner: Hooncheol Shin
categories:
- chapter18
lang: vi
---

Lớp Broyden (Broyden class) là họ công thức tổng quát hóa cả BFGS, DFP và SR1 theo biểu thức tổ hợp tuyến tính sau:

* **Lưu ý:** $$B^+_{\text{BFGS}}$$ và $$B^+_{\text{DFP}}$$ lần lượt ký hiệu ma trận $$B^+$$ thu được từ công thức cập nhật BFGS và DFP.

>$$
>B^+ = (1 - \phi)B^+_{\text{BFGS}} + \phi B^+_{\text{DFP}}, \text{ với } \phi \in \mathbb{R}.
>$$

Đặt $$v = \frac{y}{y^Ts} - \frac{Bs}{s^TBs}$$, công thức trên có thể viết lại thành:

>$$
>B^+ = B - \frac{Bss^TB}{s^TBs} + \frac{yy^T}{y^Ts} + \phi(s^TBs)vv^T.
>$$

Nhận xét:
* Khi $$\phi = 0$$, công thức trùng với cập nhật BFGS.
* Khi $$\phi = 1$$, công thức trùng với cập nhật DFP.
* Khi $$\phi = \frac{y^Ts}{y^Ts - s^TBs}$$, công thức trùng với cập nhật SR1.

**Tham khảo:** Trường hợp giới hạn tham số $$\phi \in [0, 1]$$ được gọi là **lớp Broyden hạn chế (restricted Broyden class)** [14].