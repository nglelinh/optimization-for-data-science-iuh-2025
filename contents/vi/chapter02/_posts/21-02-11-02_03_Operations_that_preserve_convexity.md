---
layout: post
title: 02-03 Các phép toán bảo toàn tính lồi của tập lồi
chapter: '02'
order: 11
owner: Wontak Ryu
categories:
- chapter02
lang: vi
---

Phần này trình bày các phép toán bảo toàn tính lồi của tập hợp. Những phép toán này giúp ta kiểm tra tính lồi của một tập phức tạp hoặc xây dựng tập lồi mới từ các tập cơ bản như siêu phẳng, nửa không gian và hình cầu chuẩn.

Các phép toán chính bảo toàn tính lồi gồm:

* Phép giao
* Hàm affine
* Hàm phối cảnh
* Hàm tuyến tính-phân thức

## Giao

Giao của các tập lồi là một tập lồi: nếu $$S_1$$ và $$S_2$$ là tập lồi thì $$S_1 \cap S_2$$ cũng là tập lồi. Tính chất này đúng cho giao của họ bất kỳ (kể cả vô hạn) các tập lồi. (Không gian con, tập affine và hình nón lồi cũng đóng đối với phép giao.)

Mọi tập lồi đóng đều có thể biểu diễn dưới dạng giao của các nửa không gian chứa nó, và ngược lại, giao của bất kỳ họ nửa không gian nào cũng là một tập lồi đóng:

> $$S = \bigcap \{\mathcal{H} \mid \mathcal{H} \text{ là nửa không gian }, S \subseteq \mathcal{H}\}$$

## Hàm affine

Cho $$A \in \mathbb{R}^{m \times n}$$ và $$b \in \mathbb{R}^{m}$$. Ánh xạ $$f : \mathbb{R}^n \to \mathbb{R}^m$$ xác định bởi $$f(x) = Ax + b$$ được gọi là hàm affine.

Nếu $$C \subseteq \mathbb{R}^n$$ và $$D \subseteq \mathbb{R}^m$$ là các tập lồi, thì:

* Ảnh affine $$f(C) = \{f(x) \mid x \in C\}$$ là tập lồi.
* Nghịch ảnh affine $$f^{-1}(D) = \{x \mid f(x) \in D\}$$ là tập lồi.

Nhờ tính chất này, các phép biến đổi affine như co giãn, tịnh tiến, phép chiếu, tổng hai tập hợp và tổng từng phần đều bảo toàn tính lồi.

Hai ví dụ quan trọng suy ra từ tính chất này là:

* Tập nghiệm của một bất đẳng thức ma trận tuyến tính $$\{x \mid x_1 A_1 + \cdots + x_m A_m \preceq B\}$$ (với $$A_i, B \in S^n$$) là tập lồi.
* Hình nón hyperbolic $$\{x \mid x^T P x < (c^T x)^2, c^T x > 0\}$$ (với $$P \in S^n_+$$, $$c \in \mathbb{R}^n$$) cũng là tập lồi.

## Hàm phối cảnh

**Hàm phối cảnh** mô hình hóa hiện tượng các vật thể trông nhỏ hơn khi ở xa và lớn hơn khi ở gần, tương tự cách máy ảnh chiếu vật thể từ không gian $$\mathbb{R}^{n+1}$$ xuống mặt phẳng ảnh trong $$\mathbb{R}^n$$.

Hàm phối cảnh $$P : \mathbb{R}^{n+1} \to \mathbb{R}^{n}$$ có miền xác định **dom** $$P = \mathbb{R}^{n} \times \mathbb{R}_{++}$$ (với $$\mathbb{R}_{++} = \{x \in \mathbb{R} \mid x > 0\}$$) và được cho bởi $$P(z,t) = z/t$$. Phép biến đổi này chuẩn hóa tọa độ cuối cùng về 1 rồi bỏ tọa độ đó đi, đưa điểm từ $$\mathbb{R}^{n+1}$$ về $$\mathbb{R}^n$$. Nếu $$C \subseteq$$ **dom** $$P$$ là tập lồi, thì ảnh $$P(C) = \{P(x) \mid x \in C\}$$ cũng là tập lồi.

Hàm phối cảnh hoạt động như một máy ảnh lỗ kim: vật ở xa lỗ kim cho ảnh chiếu nhỏ hơn, còn các điểm nằm trên cùng một tia xuất phát từ lỗ kim sẽ có cùng ảnh chiếu.