---
layout: post
title: 13 Ứng dụng của đối ngẫu và các tương ứng
chapter: "13"
order: 1
owner: "Wontak Ryu"
categories:
- chapter13
lang: vi
---

Nếu ở các chương trước, lý thuyết đối ngẫu có thể tạo cảm giác như một cấu trúc đại số thuần túy — nơi ta lập hàm Lagrange rồi lấy cực tiểu và cực đại — thì Chương 13 chính là lúc chiếc chìa khóa ấy mở ra hàng loạt cánh cửa thực chiến. Khi đứng trước một bài toán tối ưu hàng triệu biến với ràng buộc phức tạp, các nhà toán học hiếm khi đâm đầu giải trực tiếp; họ xoay bài toán sang "mặt gương đối ngẫu", nơi ràng buộc lồng ghép trở thành phép chiếu đơn giản và chuẩn không khả vi hóa thành hình hộp gọn gàng.

Chương này kết nối năm công cụ sắc bén nhất của phân tích lồi hiện đại: **tiêu chí dừng qua khoảng cách đối ngẫu**, **khôi phục nghiệm nguyên thủy từ đối ngẫu**, **chuẩn đối ngẫu**, **hàm liên hợp Fenchel** và **nón đối ngẫu**. Nắm vững các tương ứng này giống như có một cuốn từ điển hai chiều cho phép bạn dịch bài toán khó thành bài toán dễ chỉ trong vài dòng biến đổi.

## Bản đồ kiến thức nền: Bức tranh tổng thể của các tương ứng đối ngẫu

Để đọc thông suốt toàn bộ Chương 13, hãy hình dung bốn trụ cột sau như bốn bánh răng ăn khớp nhau:

- **Đối ngẫu Lagrange và chứng chỉ tối ưu:** Mọi điểm khả thi đối ngẫu đều sinh ra một chặn dưới chắc chắn cho giá trị tối ưu nguyên thủy $$f^\star$$. Khoảng cách đối ngẫu $$f(x) - g(u, v)$$ biến lý thuyết thành thước đo sai số thực tế mà không cần biết trước $$x^\star$$.
- **Hình học chuẩn và chuẩn đối ngẫu:** Chuẩn đo "độ dài" của vectơ trong không gian nguyên thủy, còn chuẩn đối ngẫu đo "độ lớn cực đại" của một hàm tuyến tính tác động lên quả cầu đơn vị. Cặp $$(\ell_1, \ell_\infty)$$ hay $$(\ell_2, \ell_2)$$ là cầu nối trực tiếp giữa phạt thưa và ràng buộc hộp.
- **Biến đổi Legendre–Fenchel (hàm liên hợp):** Thay vì mô tả một hàm lồi bằng đồ thị các điểm $$(x, f(x))$$, hàm liên hợp $$f^*(y)$$ mô tả nó bằng họ các siêu phẳng tiếp xúc có độ dốc $$y$$. Mọi phép cực tiểu hóa hàm Lagrange của hàm tách biến đều tự động gọi tên $$f^*$$.
- **Hình học nón và quy hoạch nón:** Khi ràng buộc không còn là số thực không âm mà là vectơ thuộc nón bậc hai hay ma trận nửa xác định dương, nón đối ngẫu $$K^*$$ giữ vai trò tổng quát hóa khái niệm "nhân tử không âm" sang không gian nhiều chiều.

### Khung giải thích (nên đọc chậm): Một bài toán nhỏ, nhìn bằng cả hai mặt gương

Xét bài toán cực tiểu hóa 1 biến có ràng buộc:

$$\min_{x \in \mathbb{R}} \frac{1}{2}x^2 - 4x \qquad \text{với điều kiện } x \le 2.$$

Ta thử giải nhanh bằng trực giác trước: parabol $$\frac{1}{2}x^2 - 4x$$ có đỉnh tự do tại $$x = 4$$, nhưng bị chặn bởi tường $$x \le 2$$ nên nghiệm tối ưu là $$x^\star = 2$$ với $$f^\star = \frac{1}{2}(4) - 8 = -6$$. Giờ hãy xem bốn bánh răng của Chương 13 vận hành trên đúng bài toán này:

1. **Lập hàm Lagrange và đối ngẫu:** Với nhân tử $$u \ge 0$$ cho ràng buộc $$x - 2 \le 0$$, ta có $$L(x, u) = \frac{1}{2}x^2 - 4x + u(x - 2) = \frac{1}{2}x^2 - (4 - u)x - 2u$$.
2. **Dùng hàm liên hợp để lấy cực tiểu theo $$x$$:** Nhớ rằng $$\min_x \{\frac{1}{2}x^2 - yx\} = -\frac{1}{2}y^2$$ (vì liên hợp của $$\frac{1}{2}x^2$$ là $$\frac{1}{2}y^2$$). Thay $$y = 4 - u$$, ta nhận ngay hàm đối ngẫu $$g(u) = -\frac{1}{2}(4 - u)^2 - 2u = -\frac{1}{2}u^2 + 2u - 8$$.
3. **Thử khoảng cách đối ngẫu tại một cặp điểm chưa tối ưu:** Chọn $$x = 1$$ (khả thi vì $$1 \le 2$$) và $$u = 1$$ (khả thi vì $$1 \ge 0$$). Khi đó $$f(1) = -3.5$$ và $$g(1) = -6.5$$. Dù chưa giải xong, ta lập tức có chứng chỉ: $$-6.5 \le f^\star \le -3.5$$, khoảng cách đối ngẫu là $$3.0$$.
4. **Cực đại hóa $$g(u)$$ và khôi phục $$x^\star$$:** Đạo hàm $$g'(u) = -u + 2 = 0 \implies u^\star = 2 \ge 0$$, cho $$g(2) = -6$$. Thay $$u^\star = 2$$ vào điều kiện dừng của $$L(x, u^\star)$$: $$x^\star - (4 - 2) = 0 \implies x^\star = 2$$, khoảng cách đối ngẫu bằng $$-6 - (-6) = 0$$.

---

Trong chương này, chúng ta sẽ tìm hiểu các ứng dụng của tính đối ngẫu (duality) và những khái niệm tương ứng liên quan thông qua các ví dụ cụ thể.

### Lưu ý về ký hiệu

Trong chương này, nghiệm tối ưu được ký hiệu là $$x^{\star}$$, còn phép liên hợp (conjugate) được ký hiệu bằng dấu sao $$f^{*}$$ để phân biệt rõ ràng.

## Ứng dụng hiện đại (2022–2026)

Bài đọc tùy chọn đi kèm gắn các khái niệm của chương với các ứng dụng giai đoạn 2022–2026: chuẩn đối ngẫu trong RobustBench, đối ngẫu Lasso trong kỹ thuật sàng lọc (screening) của skglm, hàm liên hợp trong Clarabel và CVXPY, cùng nón đối ngẫu trong $$\alpha,\beta$$-CROWN. Xem [13-07 Cách dùng hiện đại của liên hợp, chuẩn đối ngẫu và nón đối ngẫu]({% multilang_post_url contents/chapter13/2026-09-16-13_07_modern_applications %}).
