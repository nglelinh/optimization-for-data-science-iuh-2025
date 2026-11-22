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

## Bài tập

1. Chuyển hệ ràng buộc $$x_1 - x_2 \le 3$$, $$x_1 \ge 0$$, $$x_2$$ tự do về dạng chuẩn.
2. Xuất phát từ $$(0,0)$$ trong ví dụ trên, xác định biến vào đầu tiên nếu luôn chọn biến có chi phí rút gọn âm nhất.
3. Xây dựng một bài toán LP hai chiều khả thi nhưng không bị chặn và giải thích vì sao phép kiểm định tỉ số không tìm được biến ra.

Đọc thêm: Boyd & Vandenberghe, Phụ lục B; Nocedal & Wright, Chương 13; tài liệu bài toán chuẩn của CMU được liên kết tại [README]({{ site.baseurl }}/).
