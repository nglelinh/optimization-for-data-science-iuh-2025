---
layout: post
title: 02 Tập Lồi
chapter: '02'
order: 1
owner: Wontak Ryu
categories:
- chapter02
lang: vi
---

Hãy hình dung bạn đang đứng trong một căn phòng và muốn nhìn thẳng tới một người bạn ở góc phòng kia mà không bị bức tường nào che khuất. Nếu *bất kỳ* hai người nào đứng trong phòng đều luôn nhìn thấy nhau qua một đường thẳng không đụng tường, thì căn phòng đó chính là một **tập lồi**! Hình ảnh giản dị ấy lại ẩn chứa sức mạnh phi thường của Chương 02: trong tối ưu hóa, miền khả thi lồi đảm bảo ta luôn có thể trượt thẳng từ một phương án tốt sang một phương án tốt hơn mà không bao giờ bị vướng "góc lõm" hay rơi ra ngoài vùng hợp lệ.

Chương 02 xây dựng toàn bộ hình học của không gian tìm kiếm lồi — từ đoạn thẳng, siêu phẳng, đa diện, hình nón bán xác định dương cho tới các định lý phân tách và hình nón đối ngẫu.

## Bản đồ kiến thức nền: Bốn nhánh hình học của Chương 02

- **Phân cấp tổ hợp tuyến tính:** Từ đường thẳng (tập affine) $$\to$$ đoạn thẳng (tập lồi) $$\to$$ tia không âm (hình nón lồi), chỉ bằng cách thêm dần các ràng buộc đơn giản lên trọng số $$\theta_i$$.
- **Kho tàng các tập lồi kinh điển:** Siêu phẳng, nửa không gian, đa diện (LP), hình cầu chuẩn và ellipsoid (SOCP/QP), và hình nón ma trận bán xác định dương $$\mathbb{S}_+^n$$ (SDP).
- **Phép toán bảo toàn tính lồi:** Cách kiểm chứng một miền khả thi phức tạp là lồi mà không cần chứng minh trực tiếp từ định nghĩa, thông qua giao, ánh xạ affine và ánh xạ phối cảnh.
- **Phân tách, hỗ trợ và đối ngẫu hình học:** Định lý siêu phẳng phân tách và hình nón đối ngẫu — chiếc cầu hình học trực tiếp dẫn tới lý thuyết đối ngẫu Lagrange và điều kiện KKT ở các chương sau.

### Khung giải thích (nên đọc chậm): Phân biệt tập lồi và tập không lồi trên mặt phẳng $$\mathbb{R}^2$$

So sánh hai miền trong $$\mathbb{R}^2$$: hình vuông đơn vị $$C = [0, 1]^2$$ và hình chữ L $$S = [0, 2]^2 \setminus (1, 2]^2$$:

1. **Kiểm tra hình vuông $$C = [0, 1]^2$$:** Lấy hai điểm bất kỳ $$x = (x_1, x_2),\ y = (y_1, y_2) \in C$$ và $$\theta \in [0, 1]$$. Tọa độ thứ nhất của tổ hợp lồi là $$z_1 = \theta x_1 + (1-\theta)y_1$$. Vì $$0 \le x_1, y_1 \le 1$$, ta có $$0 \le z_1 \le \theta\cdot 1 + (1-\theta)\cdot 1 = 1$$ (tương tự cho $$z_2$$). Vậy $$z \in C$$, chứng tỏ $$C$$ là **tập lồi**.
2. **Bác bỏ tính lồi của hình chữ L $$S$$ bằng một phản ví dụ:**
   - Chọn $$x = (0.5,\ 1.8) \in S$$ (vì $$0.5 \le 1$$) và $$y = (1.8,\ 0.5) \in S$$ (vì $$0.5 \le 1$$).
   - Lấy trung điểm ($$\theta = 0.5$$):
     $$z = \frac{1}{2}(0.5, 1.8) + \frac{1}{2}(1.8, 0.5) = (1.15,\ 1.15).$$
   - Vì cả hai tọa độ đều lớn hơn $$1$$, điểm $$z = (1.15, 1.15)$$ rơi vào góc khuyết $$(1, 2]^2$$ nên $$z \notin S$$! Chỉ cần một đoạn thẳng cắt ra ngoài, $$S$$ lập tức **không lồi**.

---

Trong chương này, chúng ta sẽ tìm hiểu khái niệm tập lồi — nền tảng của tối ưu hóa lồi.

### Bối cảnh
Tối ưu hóa lồi nghiên cứu các phương pháp tìm cực đại hoặc cực tiểu cho những bài toán được xây dựng bằng hàm lồi. Tập lồi gắn bó chặt chẽ với hàm lồi theo hai phương diện chính:

* Hàm lồi được xác định trên tập lồi. Miền xác định và miền giá trị của hàm có vai trò trực tiếp trong việc định nghĩa và suy ra các tính chất cơ bản của hàm lồi.
* Khi chuyển được một bài toán tối ưu hóa về dạng có hàm lồi, bài toán thường dễ giải hơn đáng kể. Trong nhiều trường hợp không dễ nhận biết trực tiếp một hàm có lồi hay không, ta có thể kiểm tra xem epigraph (trên đồ thị) của hàm đó có phải là tập lồi hay không.

### Nội dung
Chương này trình bày định nghĩa và các ví dụ tiêu biểu về tập lồi, những tính chất cơ bản của chúng, cùng các phép toán bảo toàn tính lồi.

Xem thêm bài tùy chọn [02-07 Ứng dụng và phát triển gần đây]({% multilang_post_url contents/chapter02/2026-09-16-02_07_Applications_Recent %}) về đơn hình, quả cầu Wasserstein và polytope công bằng.