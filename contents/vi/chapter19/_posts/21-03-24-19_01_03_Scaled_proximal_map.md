---
layout: post
title: '19-01-03 Ánh xạ proximal có tỉ lệ (Scaled proximal map)'
chapter: '19'
order: 5
owner: Hooncheol Shin
categories:
- chapter19
lang: vi
---

Một trong những nét thanh lịch nhất của giải tích lồi là khi ta đổi góc nhìn bằng đúng ký hiệu, cả một thuật toán phức tạp đột nhiên trở nên gọn gàng như một dòng thơ. Bằng cách định nghĩa **ánh xạ proximal có tỉ lệ** $$\operatorname{prox}_H(x) = \arg\min_z \frac{1}{2}\|x - z\|_H^2 + h(z)$$, toàn bộ bước cập nhật của phương pháp Newton proximal được viết lại thành đúng một dòng y hệt proximal gradient descent — chỉ thay $$t$$ bằng $$H^{-1}$$! Hơn thế nữa, ánh xạ mới này bảo toàn trọn vẹn các tính chất vàng của toán tử prox chuẩn trong không gian trang bị tích vô hướng $$\langle u, v \rangle_H = u^T H v$$.

## Bản đồ kiến thức nền: Ba trụ cột hình học của ánh xạ proximal có tỉ lệ

Để hiểu sâu chứng minh tính duy nhất và tính không giãn (non-expansiveness) trong bài, hãy nắm chắc ba khái niệm sau:

- **Không gian Euclid biến dạng bởi ma trận $$H \succ 0$$:** Đặt tích vô hướng mới $$\langle u, v \rangle_H = u^T H v$$ và chuẩn $$\|u\|_H = \sqrt{u^T H u}$$. Hình cầu đơn vị trong chuẩn này là một hình elip trong không gian gốc; phép đổi biến $$y = H^{1/2} x$$ biến chuẩn $$H$$ trở về chuẩn Euclid thông thường!
- **Tính duy nhất và điều kiện tối ưu bậc nhất:** Vì $$H \succ 0$$ nên $$\frac{1}{2}\|x - z\|_H^2$$ lồi mạnh, kéo theo $$\operatorname{prox}_H(x)$$ luôn tồn tại và **duy nhất**, đặc trưng bởi bao hàm thức dưới vi phân $$H(x - z) \in \partial h(z)$$.
- **Tính không giãn vững (Firm Non-Expansiveness) theo chuẩn $$H$$:** Bất đẳng thức $$\|\operatorname{prox}_H(x) - \operatorname{prox}_H(y)\|_H \le \|x - y\|_H$$ đảm bảo ánh xạ không khuếch đại sai số — công cụ cốt lõi để chứng minh định lý hội tụ của Newton proximal ở bài 19-04.

### Khung giải thích (nên đọc chậm): Tính tay $$\operatorname{prox}_H(x)$$ và kiểm chứng tính không giãn trong chuẩn $$H$$

Xét $$h(z) = \|z\|_1 = |z_1| + |z_2|$$ và ma trận độ cong đường chéo $$H = \begin{bmatrix} 2 & 0 \\ 0 & 8 \end{bmatrix} \succ 0$$.

1. **Tính $$\operatorname{prox}_H(x)$$ tại $$x = (1, 1)^T$$:**
   $$\operatorname{prox}_H(x) = \arg\min_{z_1, z_2} \left\{ \frac{1}{2}\left[2(z_1 - 1)^2 + 8(z_2 - 1)^2\right] + |z_1| + |z_2| \right\}.$$
   Bài toán tách theo từng tọa độ:
   - Tọa độ 1: $$\min_{z_1} (z_1 - 1)^2 + |z_1| \iff \min_{z_1} \frac{1}{2}(z_1 - 1)^2 + \frac{1}{2}|z_1| \implies z_1^\star = S_{1/2}(1) = 0.5$$.
   - Tọa độ 2: $$\min_{z_2} 4(z_2 - 1)^2 + |z_2| \iff \min_{z_2} \frac{1}{2}(z_2 - 1)^2 + \frac{1}{8}|z_2| \implies z_2^\star = S_{1/8}(1) = 0.875$$.
   Vậy $$\operatorname{prox}_H(1, 1) = (0.5, \; 0.875)^T$$. Chú ý: trục có độ cong lớn hơn ($$H_{22} = 8$$) có ngưỡng co nhỏ hơn gấp 4 lần ($$1/8$$ so với $$1/2$$)!
2. **Kiểm chứng tính không giãn giữa $$x = (1, 1)^T$$ và $$y = (0, 0)^T$$:**
   - Ta có $$\operatorname{prox}_H(0, 0) = (0, 0)^T$$.
   - Khoảng cách đầu vào theo chuẩn $$H$$: $$\|x - y\|_H^2 = 2(1)^2 + 8(1)^2 = 10 \implies \|x - y\|_H = \sqrt{10} \approx 3.162$$.
   - Khoảng cách đầu ra theo chuẩn $$H$$: $$\|\operatorname{prox}_H(x) - \operatorname{prox}_H(y)\|_H^2 = 2(0.5)^2 + 8(0.875)^2 = 0.5 + 6.125 = 6.625 \implies \sqrt{6.625} \approx 2.574 \le 3.162$$!
   Ánh xạ $$\operatorname{prox}_H$$ thực sự co khoảng cách lại trong đúng hình học chuẩn $$H$$.

---

**Phương pháp Newton proximal** có thể được viết lại dưới dạng hoàn toàn tương đồng với **proximal gradient descent** nhờ khái niệm ánh xạ proximal có tỉ lệ.

## Ánh xạ proximal có tỉ lệ
Với ma trận xác định dương $$H \succ 0$$, **ánh xạ proximal có tỉ lệ (scaled proximal map)** ứng với hàm $$h$$ được định nghĩa là:

> \begin{align}
\text{prox}_{H}(x) = \underset{z}{\text{argmin}} \ \frac{1}{2} \parallel x - z \parallel_H^2 + h(z)
\end{align}

trong đó $$\parallel x \parallel_H^2 = x^THx$$ là bình phương chuẩn cảm sinh bởi $$H$$. Khi $$H = \frac{1}{t} I$$, biểu thức này quay về **ánh xạ proximal thông thường**.

Nhìn chung, **ánh xạ proximal có tỉ lệ** giữ nguyên các tính chất tốt của toán tử prox chuẩn:

* **Tính duy nhất:** Nghiệm cực tiểu là duy nhất vì $$H \succ 0$$ làm bài toán con lồi chặt.
* **Tính không giãn (non-expansiveness):** Ánh xạ không làm tăng khoảng cách theo chuẩn $$H$$ (tổng quát hóa trực tiếp tính không giãn của phép chiếu lên tập lồi).

#### [Ghi chú] Tính không giãn của toán tử chiếu
Với hai điểm $$x, y$$ và toán tử chiếu Euclid $$P_C$$ lên tập lồi $$C$$, tính không giãn có nghĩa là $$\parallel P_C(x) - P_C(y) \parallel_2 \le \parallel x - y \parallel_2$$. Nói cách khác, $$P_C$$ là ánh xạ 1-Lipschitz với mọi tập lồi $$C$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter19/09.01_03_projection_operator.png" alt="[Hình 1] Phép chiếu lên tập lồi C [3]" width="70%">
  <figcaption style="text-align: center;">[Hình 1] Phép chiếu lên tập lồi C [3]</figcaption>
</p>
</figure>

## Biểu diễn cập nhật Newton proximal
Sử dụng **ánh xạ proximal có tỉ lệ**, bài toán con của phương pháp Newton proximal có thể viết gọn lại như sau:

> $$
> \begin{align}
> z^{+} & = \underset{z}{\text{argmin}} \ \nabla g(x)^T (z - x) + \frac{1}{2} (z - x)^T H (z - x) + h(z) \\\\
> & =\underset{z}{\text{argmin}} \ \frac{1}{2} \parallel x - H^{-1} \nabla g(x) - z \parallel_H^2 + h(z)
> \end{align}
> $$

Do đó, phép cập nhật Newton proximal tương đương với:

> $$
> \begin{align}
> z^{(k)} & = \text{prox}_{H^{(k-1)}} ( x^{(k-1)} - (H^{(k-1)})^{-1} \nabla g (x^{(k-1)}) ) \\\\
> x^{(k)} & =x^{(k-1)} + t_k (z^{(k)} - x^{(k-1)} )
> \end{align}
> $$

Về mặt trực giác, thuật toán thực hiện một bước Newton trên phần trơn $$g$$, áp dụng toán tử proximal có tỉ lệ theo ma trận $$H^{(k-1)}$$, rồi di chuyển theo hướng thu được.

Từ công thức trên có thể rút ra ba nhận xét quan trọng:

* Khi $$h(z) = 0$$, toán tử proximal trở thành phép đồng nhất và ta thu lại phương pháp Newton cổ điển.
* Khi thay $$H^{(k-1)}$$ bằng $$\frac{1}{r_k} I$$ và đặt $$t_k = 1$$, ta thu lại proximal gradient descent với kích thước bước $$r_k$$.
* Độ khó tính toán của toán tử prox không chỉ phụ thuộc vào $$h$$ mà còn phụ thuộc mạnh vào cấu trúc của ma trận $$H$$: nếu $$H$$ là ma trận đường chéo hoặc ma trận dải (banded), việc giải bài toán con dễ hơn nhiều so với khi $$H$$ dày đặc (dense).

Như vậy, phương pháp Newton proximal thống nhất cả proximal gradient descent và phương pháp Newton trong cùng một khuôn khổ.
