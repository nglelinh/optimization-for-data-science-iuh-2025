---
layout: post
title: 02-01 Tập Affine và Tập Lồi
chapter: '02'
order: 2
owner: Wontak Ryu
categories:
- chapter02
lang: vi
lesson_type: required
---

Một điều rất đẹp trong hình học lồi là ba họ tập hợp quan trọng nhất — **tập affine**, **tập lồi** và **hình nón lồi** — thực chất đều sinh ra từ cùng một công thức tổ hợp tuyến tính $$\theta_1 x_1 + \theta_2 x_2$$, chỉ khác nhau ở hai chữ số nhỏ trên hệ số $$\theta_1, \theta_2$$! Thay vì học thuộc lòng ba định nghĩa rời rạc, hãy nhìn chúng như một chiếc bảng điều khiển có hai công tắc: "tổng bằng 1" và "không âm".

Phần 02-01 sẽ đưa bạn đi qua từng viên gạch hình học sơ cấp từ đường thẳng, đoạn thẳng, tia cho đến siêu phẳng.

## Kiến thức cần nhớ: Bảng hai công tắc sinh ra bốn họ tập hợp

- **Không gian con (Subspace):** $$\theta_1, \theta_2 \in \mathbb{R}$$ hoàn toàn tự do (luôn chứa gốc tọa độ $$0$$).
- **Tập Affine:** Bật công tắc $$\theta_1 + \theta_2 = 1$$ (trượt tự do trên toàn đường thẳng đi qua $$x_1, x_2$$; mô tả ràng buộc đẳng thức $$Ax = b$$).
- **Tập Lồi:** Bật cả hai công tắc $$\theta_1 + \theta_2 = 1$$ và $$\theta_1, \theta_2 \ge 0$$ (chỉ giữ lại đoạn thẳng nằm giữa $$x_1$$ và $$x_2$$).
- **Hình nón lồi:** Chỉ bật công tắc $$\theta_1, \theta_2 \ge 0$$ (cho phép co giãn tùy ý theo hướng dương, tạo thành chùm tia xuất phát từ gốc tọa độ).

### Giải thích: Cùng hai điểm $$x_1 = (1, 0),\ x_2 = (0, 2)$$ tạo ra ba loại tổ hợp khác nhau

Xét hai điểm $$x_1 = (1, 0)^T$$ và $$x_2 = (0, 2)^T$$ trong $$\mathbb{R}^2$$:

1. **Tổ hợp affine ($$\theta_1 + \theta_2 = 1$$, cho phép âm):** Chọn $$\theta_1 = 2,\ \theta_2 = -1$$:
   $$z_{\text{aff}} = 2(1, 0) + (-1)(0, 2) = (2, -2).$$
   Điểm này nằm trên đường thẳng $$2x_1 + x_2 = 2$$ (kiểm tra: $$2(2) + (-2) = 2$$), nhưng nằm ngoài đoạn nối $$x_1, x_2$$.
2. **Tổ hợp lồi ($$\theta_1 + \theta_2 = 1,\ \theta_i \ge 0$$):** Chọn $$\theta_1 = 0.5,\ \theta_2 = 0.5$$:
   $$z_{\text{conv}} = 0.5(1, 0) + 0.5(0, 2) = (0.5, 1).$$
   Điểm này nằm đúng trên đoạn thẳng nối $$x_1$$ và $$x_2$$.
3. **Tổ hợp nón ($$\theta_1, \theta_2 \ge 0$$, không cần tổng bằng 1):** Chọn $$\theta_1 = 2,\ \theta_2 = 1$$:
   $$z_{\text{cone}} = 2(1, 0) + 1(0, 2) = (2, 2).$$
   Điểm này không còn nằm trên đường thẳng $$2x_1 + x_2 = 2$$ (vì $$2(2)+2 = 6 \ne 2$$), mà nằm sâu trong góc phần tư thứ nhất $$\mathbb{R}_+^2$$.

---

Phần này giới thiệu các khái niệm và định nghĩa cơ bản xoay quanh tập lồi. Chúng ta sẽ lần lượt xét ba loại tập hợp: cơ bản nhất là tập affine, sau đó bằng cách đặt thêm điều kiện lên tập affine, ta định nghĩa tập lồi và hình nón.

Một cách trực quan, ba loại tập hợp này có thể được hình dung như tập hợp tạo thành từ các đường thẳng, đoạn thẳng hoặc tia: tập affine được xây dựng từ các đường thẳng, tập lồi từ các đoạn thẳng và hình nón từ các tia. Cách nhìn này giúp việc nắm bắt sự khác nhau giữa chúng trở nên rõ ràng hơn. Ngoài ra, hình nón còn được gọi là tập thuần nhất không âm (nonnegative homogeneous set), phản ánh tính chất kéo dài vô hạn chỉ theo một hướng tính từ gốc tọa độ.
