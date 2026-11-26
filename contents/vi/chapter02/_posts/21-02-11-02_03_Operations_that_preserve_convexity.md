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

Khi đối mặt với một miền khả thi phức tạp như tập các ma trận có trị riêng lớn nhất không quá 1, hay tập nghiệm của một bài toán quy hoạch phân thức tuyến tính, việc trực tiếp lấy hai điểm $$x_1, x_2$$ rồi kiểm tra $$\theta x_1 + (1-\theta)x_2$$ thường vừa dài vừa dễ rối. Bí quyết của giới tối ưu hóa là **tư duy lắp ghép**: xuất phát từ vài tập lồi đơn giản đã biết, rồi áp dụng các **phép toán bảo toàn tính lồi** (giao, ảnh/ảnh ngược affine, hàm phối cảnh) để kết luận ngay tập kết quả chắc chắn lồi!

Bài học này trang bị bộ quy tắc lắp ghép tập lồi sẽ giúp bạn chứng minh tính lồi chỉ trong 2–3 dòng suy luận.

## Kiến thức cần nhớ: Bốn phép toán vàng bảo toàn tính lồi

![Mô hình hộp tối (Pinhole Camera)]({{ site.baseurl }}/img/chapter_img/chapter02/02.03_03_pine_hole.png)

![Phép chiếu phối cảnh qua lỗ kim]({{ site.baseurl }}/img/chapter_img/chapter02/02.03_04_pine_hole_camera_model.png)

![Hàm phân thức tuyến tính bảo toàn tính lồi]({{ site.baseurl }}/img/chapter_img/chapter02/02.03_05_linear_fractional_function.png)

- **Phép giao (Intersection):** Giao của một họ **bất kỳ** (hữu hạn hoặc vô hạn!) các tập lồi luôn là tập lồi. Đây là cách chứng minh nhanh nhất rằng đa diện (giao hữu hạn nửa không gian) và hình nón $$\mathbb{S}_+^n$$ (giao vô hạn nửa không gian $$z^T X z \ge 0$$) đều lồi.
- **Ánh xạ affine ($$f(x) = Ax + b$$) và ảnh ngược affine:** Tịnh tiến, co giãn, xoay, phép chiếu trực giao và tổng Minkowski $$S_1 + S_2$$ của các tập lồi đều bảo toàn tính lồi. Đặc biệt, ảnh ngược của một tập lồi qua $$Ax + b$$ cũng luôn lồi.
- **Hàm phối cảnh (Perspective Function):** $$P(z, t) = z / t$$ trên $$t > 0$$ — tương ứng hình học với máy ảnh lỗ kim chiếu không gian 3D lên màn ảnh 2D. Cả ảnh xuôi lẫn ảnh ngược của tập lồi qua $$P$$ đều lồi!
- **Hàm phân thức tuyến tính (Linear-Fractional):** Kết hợp ánh xạ affine và hàm phối cảnh $$f(x) = \frac{Ax + b}{c^T x + d}$$ (với $$c^T x + d > 0$$) — chìa khóa giải quyết bài toán tối ưu phân thức (như tỷ lệ lợi nhuận trên rủi ro).

### Giải thích: Quan sát hàm phối cảnh biến trung điểm thành tổ hợp lồi có trọng số mới

Xét hàm phối cảnh $$P(z, t) = \frac{z}{t}$$ (với $$z \in \mathbb{R},\ t > 0$$). Giả sử một tập lồi $$C \subset \mathbb{R} \times \mathbb{R}_{++}$$ chứa hai điểm $$u_1 = (z_1, t_1) = (2, 1)$$ và $$u_2 = (z_2, t_2) = (12, 3)$$:

1. **Ảnh phối cảnh của hai đầu mút:**
   $$P(u_1) = \frac{2}{1} = 2, \qquad P(u_2) = \frac{12}{3} = 4.$$
2. **Lấy trung điểm ($$\theta = 0.5$$) trong miền nguồn $$C$$:**
   $$u_{\text{mid}} = 0.5(2, 1) + 0.5(12, 3) = (7, 2) \in C.$$
3. **Tính ảnh phối cảnh của trung điểm:**
   $$P(u_{\text{mid}}) = \frac{7}{2} = 3.5.$$
4. **Kiểm chứng tính lồi (với trọng số $$\mu$$ đã đổi do chia cho $$t$$):**
   Chú ý rằng $$3.5$$ không phải trung điểm $$3$$ của $$2$$ và $$4$$, mà là tổ hợp lồi với trọng số mới:
   $$\mu = \frac{\theta t_1}{\theta t_1 + (1-\theta)t_2} = \frac{0.5 \cdot 1}{0.5 \cdot 1 + 0.5 \cdot 3} = \frac{0.5}{2} = \frac{1}{4} \in [0, 1].$$
   Thay vào: $$\mu P(u_1) + (1-\mu) P(u_2) = \frac{1}{4}(2) + \frac{3}{4}(4) = 0.5 + 3 = 3.5 = P(u_{\text{mid}})$$! Ảnh của cả đoạn thẳng $$[u_1, u_2]$$ vẫn là đúng đoạn thẳng $$[2, 4]$$, chỉ bị kéo giãn dọc theo trục $$t$$!

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