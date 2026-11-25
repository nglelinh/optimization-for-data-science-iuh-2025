---
layout: post
title: 05-01-01 Quy Hoạch Tuyến Tính - Thuật Toán Simplex
chapter: '05'
order: 3
owner: Hooncheol Shin
categories:
- chapter05
lang: vi
lesson_type: required
---

Một khối đa diện LP với 50 biến và 100 ràng buộc có thể sở hữu số đỉnh lớn hơn $$\binom{100}{50} \approx 10^{29}$$ — liệt kê hết các đỉnh là bất khả thi ngay cả với siêu máy tính nhanh nhất thế giới. Vậy mà **thuật toán Simplex** do George Dantzig phát minh năm 1947 lại thường tìm ra đỉnh tối ưu chỉ sau vài trăm bước nhảy!

Bí quyết nằm ở đâu? Thay vì thử mù quáng mọi đỉnh, Simplex hành xử như một người leo núi thông minh trên khung cạnh của đa diện: đứng tại một đỉnh (nghiệm cơ sở khả thi), thuật toán nhìn dọc theo các cạnh xuất phát từ đỉnh đó, chọn một cạnh làm giảm hàm mục tiêu (chi phí rút gọn âm), rồi trượt thẳng sang đỉnh kề tốt hơn. Khi mọi cạnh xuất phát đều làm tăng hàm mục tiêu, ta biết chắc mình đã đứng ở đỉnh tối ưu toàn cục!

## Kiến thức cần nhớ: Động cơ đại số bên trong thuật toán Simplex

Để không bao giờ bị lạc trong các bảng tính (tableau) của Simplex, hãy nắm vững bốn trụ cột:

- **Nghiệm cơ sở khả thi (Basic Feasible Solution - BFS):** Với hệ $$Ax = b$$ ($$m$$ phương trình, $$n$$ biến, $$m < n$$), mỗi đỉnh của đa diện tương ứng với việc chọn $$m$$ biến **cơ sở** $$x_B$$ (tương ứng ma trận con khả nghịch $$B$$) và đặt $$n - m$$ biến **phi cơ sở** $$x_N = 0$$, sao cho $$x_B = B^{-1} b \ge 0$$.
- **Chi phí rút gọn (Reduced Cost):** Khi tăng một biến phi cơ sở $$x_j$$ từ $$0$$ lên $$\theta > 0$$, tốc độ thay đổi ròng của hàm mục tiêu là $$\bar{c}_j = c_j - c_B^T B^{-1} A_j$$. Nếu mọi $$\bar{c}_j \ge 0$$, không hướng nào cải thiện được nữa — ta dừng và kết luận tối ưu!
- **Phép xoay trục & Quy tắc tỉ số nhỏ nhất (Pivot & Minimum Ratio Test):** Khi chọn biến vào $$x_j$$ có $$\bar{c}_j < 0$$, ta tăng $$x_j$$ tối đa đến mức nào để các biến cơ sở $$x_B = B^{-1}b - \theta (B^{-1}A_j)$$ không bị âm? Đúng bằng $$\theta^\star = \min_{i : d_i > 0} \frac{(B^{-1}b)_i}{d_i}$$ với $$d = B^{-1}A_j$$. Biến cơ sở chạm $$0$$ đầu tiên sẽ rời cơ sở!
- **Độ phức tạp thực tế vs. Trường hợp xấu nhất:** Dù về lý thuyết Klee–Minty chứng minh Simplex có thể tốn số bước hàm mũ trong trường hợp bệnh lý, trong thực tế Simplex chạy gần như tuyến tính $$O(m)$$ bước xoay và vẫn là bộ giải chuẩn cho các bài LP lớn cần khởi động ấm (warm-start).

### Giải thích: Chạy tay trọn vẹn 2 bước xoay Simplex trên một bài LP

Xét bài toán dạng chuẩn:
$$\min \; -3x_1 - 2x_2 \quad \text{s.t.} \quad \begin{cases} x_1 + x_2 + s_1 = 4 \\ 2x_1 + x_2 + s_2 = 6 \end{cases}, \qquad x_1, x_2, s_1, s_2 \ge 0.$$

1. **Khởi tạo tại đỉnh gốc:** Cơ sở $$B = \{s_1, s_2\}$$, phi cơ sở $$N = \{x_1, x_2\}$$. Nghiệm: $$x_1=0, x_2=0, s_1=4, s_2=6$$, giá trị $$f = 0$$.
   - Chi phí rút gọn: $$\bar{c}_{x_1} = -3 < 0$$, $$\bar{c}_{x_2} = -2 < 0$$. Chọn biến vào là $$x_1$$ (âm nhất).
2. **Bước xoay 1 (đưa $$x_1$$ vào cơ sở):**
   Giữ $$x_2 = 0$$, ta có $$s_1 = 4 - x_1 \ge 0 \implies x_1 \le 4$$ và $$s_2 = 6 - 2x_1 \ge 0 \implies x_1 \le 3$$.
   Tỉ số nhỏ nhất là $$\min(4/1,\; 6/2) = 3$$, nên $$s_2$$ rời cơ sở!
   Từ phương trình 2: $$x_1 = 3 - 0.5x_2 - 0.5s_2$$. Thế vào phương trình 1 và hàm mục tiêu:
   $$s_1 = 1 - 0.5x_2 + 0.5s_2, \qquad f = -9 - 0.5x_2 + 1.5s_2.$$
   Đỉnh hiện tại: $$(x_1, x_2, s_1, s_2) = (3, 0, 1, 0)$$, $$f = -9$$.
3. **Bước xoay 2 (đưa $$x_2$$ vào cơ sở):**
   Nhìn vào $$f = -9 - 0.5x_2 + 1.5s_2$$: chi phí rút gọn $$\bar{c}_{x_2} = -0.5 < 0$$, nên chọn $$x_2$$ vào cơ sở!
   Giữ $$s_2 = 0$$: $$s_1 = 1 - 0.5x_2 \ge 0 \implies x_2 \le 2$$; $$x_1 = 3 - 0.5x_2 \ge 0 \implies x_2 \le 6$$.
   Tỉ số nhỏ nhất là $$2$$, nên $$s_1$$ rời cơ sở! Từ $$s_1 = 1 - 0.5x_2 + 0.5s_2 \implies x_2 = 2 - 2s_1 + s_2$$.
   Thế vào $$x_1$$ và $$f$$:
   $$x_1 = 2 + s_1 - s_2, \qquad f = -10 + s_1 + s_2.$$
4. **Kiểm tra điều kiện dừng:** Mọi chi phí rút gọn của biến phi cơ sở ($$+1$$ cho $$s_1$$, $$+1$$ cho $$s_2$$) đều $$\ge 0$$! Dừng ngay: nghiệm tối ưu là $$x_1^\star = 2, x_2^\star = 2$$ và $$f^\star = -10$$.

---

Bài toán [quy hoạch tuyến tính]({% multilang_post_url contents/chapter05/21-02-08-05_01_Linear_Programming_(LP) %}) ở tiết trước có tập khả thi là một tập đa diện. Một tính chất hình học đặc trưng của LP là: **nếu tồn tại nghiệm tối ưu hữu hạn (và tập khả thi không chứa đường thẳng), thì có ít nhất một điểm tối ưu nằm tại một đỉnh**. Thuật toán đơn hình (Simplex) di chuyển từ đỉnh này sang đỉnh kề sao cho giá trị hàm mục tiêu được cải thiện, cho đến khi không còn đỉnh lân cận nào tốt hơn.

Minh họa bảng đơn hình tương tác: [demo simplex](https://github.com/nglelinh/interactive_math/blob/main/linear-programming/simplex_optimization_demo.html) trong `nglelinh/interactive_math`.

<div class="content-box insight-box">
<strong>Ý tưởng then chốt:</strong> Trong khi các phương pháp gradient di chuyển bên trong miền khả thi, thuật toán Simplex bám dọc theo các cạnh của tập đa diện và chỉ đánh giá tại các đỉnh. Nhờ đó, dù ra đời từ thập niên 1950, Simplex vẫn được sử dụng rộng rãi để giải nhiều bài toán LP trong phối trộn, định tuyến và bài toán đối ngẫu của SVM.
</div>

## Dạng chuẩn

Phần lớn các giáo trình trình bày thuật toán Simplex trên dạng chuẩn với ràng buộc đẳng thức và biến không âm:

$$
\begin{align}
\underset{x}{\text{minimize}} \quad & c^\top x \\
\text{subject to} \quad & Ax = b, \\
& x \succeq 0,
\end{align}
$$

trong đó $$A \in \mathbb{R}^{m \times n}$$ có hạng hàng đầy đủ bằng $$m$$, $$b \succeq 0$$, và $$n > m$$. Các ràng buộc bất đẳng thức dạng $$Gx \preceq h$$ được chuyển sang đẳng thức bằng cách thêm **biến phụ** (slack variable) không âm, còn các biến tự do được tách thành hiệu của hai biến không âm.

Một **cơ sở** (basis) là một tập gồm $$m$$ cột độc lập tuyến tính của $$A$$. Sau khi hoán vị cột để viết $$A = [A_B \; A_N]$$ và tách tương ứng $$x = (x_B, x_N)$$, **nghiệm cơ sở** được xác định bởi:

$$
x_B = A_B^{-1} b, \qquad x_N = 0.
$$

Nếu $$x_B \succeq 0$$, điểm này được gọi là **nghiệm khả thi cơ sở (Basic Feasible Solution - BFS)** — về mặt hình học, đây chính là một đỉnh của đa diện khả thi.

## Chi phí rút gọn và bước xoay (pivot)

Từ phương trình $$Ax = b$$, ta biểu diễn các biến cơ sở theo các biến ngoài cơ sở:

$$
x_B = A_B^{-1}b - A_B^{-1}A_N x_N.
$$

Thay vào hàm mục tiêu, ta thu được:

$$
c^\top x = c_B^\top A_B^{-1}b + \bar{c}_N^\top x_N, \qquad \bar{c}_N^\top := c_N^\top - c_B^\top A_B^{-1}A_N.
$$

Vectơ $$\bar{c}_N$$ chứa các **chi phí rút gọn** (reduced costs). Do $$x_N \succeq 0$$:

- Nếu $$\bar{c}_N \succeq 0$$, mọi cách tăng biến ngoài cơ sở đều không thể làm giảm hàm mục tiêu — nghiệm khả thi cơ sở hiện tại là **tối ưu**.
- Nếu tồn tại $$\bar{c}_j < 0$$, ta có thể tăng biến ngoài cơ sở tương ứng (biến **vào** cơ sở) cho đến khi một biến cơ sở giảm về 0 (biến **ra** khỏi cơ sở). Quy tắc kiểm định tỉ số (ratio test) chọn biến ra sao cho điều kiện $$x_B \succeq 0$$ vẫn được duy trì.

Mỗi phép thay đổi cơ sở như vậy gọi là một bước **xoay** (pivot). Sau hữu hạn bước (khi áp dụng quy tắc chống lặp vòng, chẳng hạn quy tắc Bland), thuật toán Simplex hoặc dừng tại nghiệm tối ưu, hoặc phát hiện tia không bị chặn ($$Ax = 0$$, $$x \succeq 0$$, $$c^\top x < 0$$).

## Ví dụ hai biến

Xét bài toán tối đa hóa $$3x_1 + 2x_2$$ (tương đương tối thiểu hóa $$-3x_1 - 2x_2$$) với các ràng buộc:

$$
\begin{align}
x_1 + x_2 &\le 4, \\
2x_1 + x_2 &\le 6, \\
x_1, x_2 &\ge 0.
\end{align}
$$

Các đỉnh của đa giác khả thi là $$(0,0)$$, $$(3,0)$$, $$(2,2)$$ và $$(0,4)$$, với giá trị hàm mục tiêu lần lượt là $$0$$, $$9$$, $$10$$ và $$8$$. Xuất phát từ gốc tọa độ $$(0,0)$$, thuật toán Simplex có thể xoay sang $$(3,0)$$ rồi tới $$(2,2)$$, tại đó mọi chi phí rút gọn đều không âm. Quan sát hình học cũng cho cùng kết quả: các đường đồng mức của $$3x_1 + 2x_2$$ tiếp xúc lần cuối với miền khả thi tại $$(2,2)$$.

## Vai trò của Simplex trong khoa học dữ liệu

- **Kiểm tra cấu trúc mô hình:** Khi viết được bài toán về dạng chuẩn LP, ta biết ngay bài toán có tính lồi và có nghiệm tối ưu tại đỉnh (nếu bị chặn).
- **Liên kết trực tiếp với lý thuyết đối ngẫu:** Các chi phí rút gọn chính là các biến phụ đối ngẫu. Điều kiện bù lỏng (complementary slackness) ở [Chương 12]({% multilang_post_url contents/chapter12/21-04-02-12_00_KKT_conditions %}) chính là chứng chỉ tối ưu mà thuật toán Simplex hướng tới.
- **Sử dụng bộ giải thực tế:** Các thư viện giải LP hiện đại (HiGHS, Gurobi, `scipy.optimize.linprog`) kết hợp phương pháp Simplex cải tiến và/hoặc phương pháp điểm trong. Người dùng hiếm khi tự lập bảng bằng tay, nhưng cần hiểu bản chất để phân biệt kết quả *không khả thi* (infeasible) với *không bị chặn* (unbounded).

**Ghi chú về độ phức tạp:** Ví dụ khối Klee–Minty cho thấy một số quy tắc xoay có thể cần số bước hàm mũ trong trường hợp xấu nhất. Dù vậy, trong thực tế Simplex thường chạy rất nhanh; trong khi đó phương pháp điểm trong (Chương 15–17) có đảm bảo độ phức tạp thời gian đa thức và thường chiếm ưu thế trên nhiều bài toán LP thưa quy mô lớn. Khi bài toán đã có dạng LP hoặc QP chuẩn — như bài toán khẩu phần, đối ngẫu SVM biên cứng hay basis pursuit — cách tiếp cận thực tế là mô hình hóa bằng công cụ như CVXPY (xem bài thực hành DCP trong chương này) thay vì xoay bảng thủ công.

### Phương pháp đơn hình trong khoảng 3 phút

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/simplex-pivots_vi.mp4"></video>
</div>

Đi theo các đỉnh của bài LP trong bài: chọn biến vào, kiểm tra tỉ số, xoay bảng, đọc nghiệm đối ngẫu, và một bài không bị chặn.

## Bài tập

1. Chuyển hệ ràng buộc $$x_1 - x_2 \le 3$$, $$x_1 \ge 0$$, $$x_2$$ tự do về dạng chuẩn.
2. Xuất phát từ $$(0,0)$$ trong ví dụ trên, xác định biến vào đầu tiên nếu luôn chọn biến có chi phí rút gọn âm nhất.
3. Xây dựng một bài toán LP hai chiều khả thi nhưng không bị chặn và giải thích vì sao phép kiểm định tỉ số không tìm được biến ra.

Đọc thêm: Boyd & Vandenberghe, Phụ lục B; Nocedal & Wright, Chương 13; tài liệu bài toán chuẩn của CMU được liên kết tại [README]({{ site.baseurl }}/).
