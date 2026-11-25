---
layout: post
title: '23-02 Ví dụ: hồi quy tuyến tính'
chapter: '23'
order: 3
owner: Jinwoo Park
categories:
- chapter23
lang: vi
---

Trong hồi quy tuyến tính bình phương tối thiểu, ai cũng biết công thức nghiệm đóng $$\hat{\beta} = (X^T X)^{-1} X^T y$$. Nhưng khi số đặc trưng $$p$$ lên tới hàng chục nghìn, việc nhân ma trận $$X^T X$$ tốn $$O(np^2)$$ và nghịch đảo tốn $$O(p^3)$$ trở nên bất khả thi. Ta buộc phải dùng các phương pháp lặp bậc nhất — và đây là lúc một kết quả thực nghiệm đáng kinh ngạc xuất hiện.

Trên cùng một bài toán hồi quy tuyến tính, khi so sánh từng chu trình hạ theo tọa độ (CD) với từng bước gradient descent (GD) hay thậm chí gradient tăng tốc Nesterov (AGD), đường hội tụ của CD thường lao dốc nhanh hơn hẳn — trong khi tổng số phép tính của **một chu trình CD lại bằng đúng một bước GD**! Bí mật nằm ở hai chỗ: CD luôn dùng ngay thông tin tọa độ vừa cập nhật (hiệu ứng Gauss–Seidel) và tự động chọn kích thước bước tối ưu riêng cho từng tọa độ mà không bị chặn bởi trị riêng lớn nhất toàn cục.

## Bản đồ kiến thức nền: Ba trụ cột tạo nên tốc độ của CD cho hồi quy tuyến tính

Để hiểu cả công thức cập nhật lẫn lý do so sánh chi phí giữa CD và GD là hoàn toàn công bằng, hãy nắm ba trụ cột sau:

- **Chiếu từng phần dư (Partial Residual Regression):** Khi giữ cố định $$\beta_{-i}$$, phần dư chưa được giải thích bởi các đặc trưng khác là $$r^{(-i)} = y - X_{-i}\beta_{-i}$$. Cập nhật $$\beta_i = \frac{X_i^T r^{(-i)}}{\|X_i\|_2^2}$$ chính là hồi quy tuyến tính 1 biến đơn giản của phần dư đó lên cột $$X_i$$.
- **Bảo trì phần dư trong $$O(n)$$ (Incremental Residual Update):** Nếu mỗi lần cập nhật $$\beta_i$$ ta tính lại $$X_{-i}\beta_{-i}$$ từ đầu thì tốn $$O(np)$$, khiến cả chu trình tốn $$O(np^2)$$. Nhưng bằng cách giữ vector phần dư chung $$r = y - X\beta$$, ta tính $$r^{(-i)} = r + \beta_i^{\text{old}} X_i$$, cập nhật $$\beta_i^{\text{new}}$$, rồi sửa $$r \leftarrow r - (\beta_i^{\text{new}} - \beta_i^{\text{old}}) X_i$$ — chỉ tốn $$O(n)$$ mỗi tọa độ, nên cả chu trình $$p$$ tọa độ chỉ tốn đúng $$O(np)$$, ngang bằng 1 bước GD!
- **Tự động thích nghi độ cong từng trục (Coordinate-wise Lipschitz Adaptation):** GD phải dùng chung một bước $$t \le 1/L$$ bị chi phối bởi hướng cong mạnh nhất của $$X^T X$$. Ngược lại, CD chia riêng cho $$\|X_i\|_2^2$$ trên từng trục — tương đương với việc tự động tiền điều kiện theo đường chéo (*diagonal preconditioning*).

### Khung giải thích (nên đọc chậm): Tính tay 1 chu trình CD có bảo trì phần dư

Xét bài toán $$\min_{\beta \in \mathbb{R}^2} \frac{1}{2}\|y - X\beta\|_2^2$$ với ma trận đặc trưng và vector nhãn:

$$
X = \begin{pmatrix} 1 & 1 \\ 1 & -1 \\ 0 & 1 \end{pmatrix}, \qquad y = \begin{pmatrix} 3 \\ 1 \\ 1 \end{pmatrix}.
$$

Ta tính sẵn bình phương chuẩn các cột: $$\|X_1\|_2^2 = 1^2 + 1^2 + 0^2 = 2$$ và $$\|X_2\|_2^2 = 1^2 + (-1)^2 + 1^2 = 3$$. Khởi tạo $$\beta^{(0)} = (0, 0)$$, nên vector phần dư ban đầu là $$r = y - X\beta^{(0)} = (3, 1, 1)^T$$.

1. **Cập nhật tọa độ $$i = 1$$:**
   - Vì $$\beta_1^{\text{old}} = 0$$, phần dư riêng $$r^{(-1)} = r = (3, 1, 1)^T$$.
   - Tích vô hướng $$X_1^T r^{(-1)} = 1(3) + 1(1) + 0(1) = 4$$.
   - Suy ra $$\beta_1^{(1)} = \frac{4}{2} = 2$$.
   - Cập nhật phần dư ngay tại chỗ (chỉ tốn $$O(n)$$):
     $$r \leftarrow (3, 1, 1)^T - (2 - 0)(1, 1, 0)^T = (1,\; -1,\; 1)^T.$$
2. **Cập nhật tọa độ $$i = 2$$ (dùng ngay $$r$$ vừa cập nhật!):**
   - Vì $$\beta_2^{\text{old}} = 0$$, phần dư riêng $$r^{(-2)} = r = (1, -1, 1)^T$$.
   - Tích vô hướng $$X_2^T r^{(-2)} = 1(1) + (-1)(-1) + 1(1) = 3$$.
   - Suy ra $$\beta_2^{(1)} = \frac{3}{3} = 1$$.
   - Cập nhật phần dư:
     $$r \leftarrow (1, -1, 1)^T - (1 - 0)(1, -1, 1)^T = (0,\; 0,\; 0)^T!$$
3. **Quan sát:** Chỉ sau **1 chu trình duy nhất** gồm đúng 2 phép tích vô hướng và 2 phép trừ vector, ta đã thu được nghiệm chính xác tuyệt đối $$\beta^\star = (2, 1)$$ với phần dư bằng $$0$$ — minh họa hoàn hảo cho hiệu ứng Gauss–Seidel kết hợp bảo trì phần dư $$O(n)$$.

Xét bài toán hồi quy tuyến tính:

> $$\min_{\beta} \frac{1}{2} \| y - X\beta \|_2^2,$$
> $$\text{với } y \in \mathbb{R}^n \text{ và } X \in \mathbb{R}^{n \times p} \text{ có các cột } X_1, \dots, X_p.$$

Giữ cố định tất cả các thành phần $$\beta_j$$ ($$j \neq i$$), ta tìm $$\beta_i$$ cực tiểu hóa hàm mục tiêu (ký hiệu $$-i$$ chỉ tập các thành phần còn lại trừ $$i$$; tương ứng $$X_{-i}$$ là ma trận gồm các cột của $$X$$ trừ cột thứ $$i$$):

$$\begin{align}
0 &= \nabla_i f(\beta)\\\\
&= X_i^T (X\beta - y)\\\\
&= X_i^T (X_i \beta_i + X_{-i} \beta_{-i} - y)\\\\
\Rightarrow\\\\
&\beta_i = \frac{X_i^T (y - X_{-i} \beta_{-i})}{X_i^T X_i}
\end{align}$$

Thuật toán coordinate descent lặp lại việc cập nhật $$\beta_i$$ theo công thức trên với $$i = 1, 2, \dots, p, 1, 2, \dots$$.

## Thí nghiệm: so sánh tốc độ hội tụ giữa GD, AGD và CD

Đồ thị dưới đây so sánh tốc độ hội tụ của coordinate descent (CD), gradient descent (GD) và accelerated gradient descent (AGD) trên bài toán hồi quy tuyến tính với $$n=100, p=20$$. Trên trục hoành, giá trị $$k$$ biểu diễn một bước lặp (đối với GD, AGD) hoặc một chu trình duyệt đủ $$p$$ tọa độ (đối với CD).

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter23/gd_vs_agd_vs_cd.png" alt="[Hình 1] GD, AGD và CD [3]">
  <figcaption style="text-align: center;">[Hình 1] GD, AGD và CD [3]</figcaption>
</p>
</figure>
<br/>

Kết quả cho thấy coordinate descent hội tụ nhanh hơn đáng kể so với AGD — vốn đạt tốc độ tối ưu trong lớp các phương pháp bậc nhất. Lý do là CD không thuộc lớp phương pháp bậc nhất thuần túy: ở mỗi bước con bên trong một chu trình, nó tận dụng ngay giá trị tọa độ vừa được cập nhật ở bước trước đó.

### Câu hỏi: So sánh một chu trình CD với một bước GD như trên có công bằng không?

**Trả lời: Có.** Công thức cập nhật CD có thể cài đặt với độ phức tạp $$O(n)$$ cho mỗi tọa độ, do đó một chu trình gồm $$p$$ tọa độ tốn $$O(np)$$ phép tính — tương đương chi phí một bước GD:

* **Cập nhật gradient descent:** $$\beta \leftarrow \beta + tX^T(y-X\beta)$$, tốn $$O(np)$$ flops để tính $$X\beta$$ và $$X^T r$$.
* **Cập nhật coordinate descent:** duy trì sẵn vector phần dư $$r = y - X\beta$$; khi đó mỗi bước chỉ cần cập nhật $$\beta_i \leftarrow \beta_i + \frac{X_i^T r}{X_i^T X_i}$$ rồi cập nhật phần dư $$r \leftarrow r - X_i (\beta_i^{\text{new}} - \beta_i^{\text{old}})$$, tốn $$O(n)$$ flops mỗi tọa độ.

### Coordinate descent: mỗi lần một tọa độ (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/coordinate-descent_vi.mp4"></video>
</div>

Coordinate descent cực tiểu hóa chính xác theo từng trục tọa độ, tạo nên quỹ đạo dạng bậc thang; khi các biến có tương quan cao, kích thước mỗi bước đi sẽ thu hẹp lại.

### Tự tay thử: coordinate descent so với gradient descent

<div class="opx-explainer" data-opx="cd" data-lang="vi"></div>
