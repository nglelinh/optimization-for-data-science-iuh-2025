---
layout: post
title: 02-03 Các phép toán bảo toàn tính lồi của tập lồi
chapter: '02'
order: 9
owner: Wontak Ryu
categories:
- chapter02
lang: vi
---

Phần này thảo luận về các phép toán bảo toàn tính lồi của tập lồi. Những phép toán này hữu ích để xác định tính lồi hoặc xây dựng các tập lồi mong muốn từ những tập đơn giản như siêu phẳng, nửa không gian và hình cầu chuẩn.

Các phép toán bảo toàn tính lồi bao gồm:

* Giao
* Hàm affine
* Hàm phối cảnh
* Hàm tuyến tính-phân thức

## Giao

Giao của các tập lồi là lồi. Tức là, nếu $$S_1$$ và $$S_2$$ là lồi, thì $$S_1 \cap S_2$$ là lồi. Tính chất này đúng ngay cả với vô số tập hợp. (Không gian con, tập affine và hình nón lồi cũng đóng kín dưới phép giao.)

Tính lồi có thể được biểu diễn như giao của vô số nửa không gian, và điều ngược lại cũng đúng. Tức là, một tập lồi đóng $$S$$ có thể được định nghĩa như giao của tất cả các nửa không gian chứa $$S$$:

> $$S = \bigcap \{\mathcal{H} \mid \mathcal{H} \text{ là nửa không gian }, S \subseteq \mathcal{H}\}$$

## Hàm affine

Cho $$A \in \mathbb{R}^{m \times n}$$ và $$b \in \mathbb{R}^{m}$$. Hàm $$f : \mathbb{R}^n \to \mathbb{R}^m$$ được định nghĩa bởi $$f(x) = Ax + b$$ được gọi là hàm affine.

Nếu $$C \subseteq \mathbb{R}^n$$ là lồi và $$D \subseteq \mathbb{R}^m$$ là lồi, thì:

* Ảnh affine $$f(C) = \{f(x) \mid x \in C\}$$ là lồi.
* Nghịch ảnh affine $$f^{-1}(D) = \{x \mid f(x) \in D\}$$ là lồi.

Áp dụng các hàm affine như co giãn và tịnh tiến, phép chiếu, tổng của hai tập hợp, và tổng từng phần lên các tập lồi sẽ cho kết quả là các tập lồi.

Tập nghiệm của một bất đẳng thức ma trận tuyến tính $$\{x \mid x_1 A_1 + \cdots + x_m A_m \preceq B\}$$ (với $$A_i, B \in S^n$$) cũng là lồi.

Một hình nón hyperbolic $$\{x \mid x^T P x < (c^T x)^2, c^T x > 0\}$$ (với $$P \subseteq S^n_+$$, $$c \in \mathbb{R}^n$$) cũng là lồi.

## Hàm phối cảnh

**Hàm phối cảnh** mô hình hóa cách các vật thể xuất hiện nhỏ hơn khi ở xa và lớn hơn khi ở gần, tương tự như cách máy ảnh chiếu hình ảnh. Vật thể nằm trong $$\mathbb{R}^{n+1}$$ và ảnh của nó nằm trong $$\mathbb{R}^n$$.

Hàm phối cảnh được định nghĩa là $$P : \mathbb{R}^{n+1} \to \mathbb{R}^{n}$$ với **dom** $$P = \mathbb{R}^{n} \times \mathbb{R}_{++}$$ và $$P(z,t) = z/t$$, trong đó $$\mathbb{R}_{++} = \{x \in \mathbb{R} \mid x > 0\}$$. Hàm này chuẩn hóa tọa độ cuối cùng về 1 và bỏ qua nó, giảm chiều từ $$\mathbb{R}^{n+1}$$ xuống $$\mathbb{R}^n$$. Nếu $$C \subseteq$$ **dom** $$P$$ là lồi, thì ảnh $$P(C) = \{P(x) \mid x \in C\}$$ cũng là lồi.

Hàm phối cảnh hoạt động như một máy ảnh lỗ kim: các vật thể xa hơn từ lỗ kim được chiếu nhỏ hơn. Hình dưới đây minh họa nguyên lý này, cho thấy rằng các vật thể trong cùng một tia bị bắt sẽ được chiếu giống hệt nhau.