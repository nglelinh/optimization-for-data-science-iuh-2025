---
layout: post
title: 05-01-01 Quy Hoạch Tuyến Tính - Thuật Toán Simplex
chapter: '05'
order: 9
owner: Hooncheol Shin
categories:
- chapter05
lang: vi
lesson_type: required
---

Bài [quy hoạch tuyến tính]({% multilang_post_url contents/chapter05/21-02-08-05_01_Linear_Programming_(LP) %}) ở tiết trước có tập khả thi là một đa diện. Một sự thật hình học làm cho LP đặc biệt: **nếu tồn tại nghiệm tối ưu hữu hạn thì có ít nhất một điểm tối ưu nằm tại đỉnh**. Thuật toán simplex đi từ đỉnh này sang đỉnh kề, cải thiện hàm mục tiêu, cho đến khi không còn đỉnh láng giềng nào tốt hơn.

Bảng simplex tương tác: [demo simplex](https://github.com/nglelinh/interactive_math/blob/main/linear-programming/simplex_optimization_demo.html) trong `nglelinh/interactive_math`.

<div class="content-box insight-box">
<strong>Ý tưởng then chốt:</strong> các phương pháp gradient đi trong phần trong của miền. Simplex bám trên bộ xương của đa diện và chỉ đánh giá các góc. Đó là lý do một thuật toán những năm 1950 vẫn giải được nhiều LP phía sau bài toán pha trộn, định tuyến, và đối ngẫu SVM.
</div>

## Dạng chuẩn

Hầu hết giáo trình cài simplex trên dạng đẳng thức với biến không âm:

$$
\begin{align}
\underset{x}{\text{minimize}} \quad & c^\top x \\
\text{subject to} \quad & Ax = b, \\
& x \succeq 0,
\end{align}
$$

với $$A \in \mathbb{R}^{m \times n}$$ có hạng hàng đủ $$m$$, $$b \succeq 0$$, và $$n > m$$. Ràng buộc bất đẳng thức $$Gx \preceq h$$ được chuyển bằng cách thêm biến **bù** (slack) không âm. Biến tự do được tách thành hiệu của hai biến không âm.

Một **cơ sở** (basis) là một tập $$m$$ cột độc lập tuyến tính của $$A$$. Viết $$A = [A_B \; A_N]$$ sau khi hoán vị cột, và tách $$x = (x_B, x_N)$$. **Nghiệm cơ sở** tương ứng là

$$
x_B = A_B^{-1} b, \qquad x_N = 0.
$$

Nếu $$x_B \succeq 0$$ thì điểm đó là **nghiệm khả thi cơ sở (BFS)** — về hình học, một đỉnh của đa diện khả thi.

## Chi phí rút gọn và một bước xoay (pivot)

Từ $$Ax = b$$ ta khử các biến cơ sở:

$$
x_B = A_B^{-1}b - A_B^{-1}A_N x_N.
$$

Thế vào hàm mục tiêu:

$$
c^\top x = c_B^\top A_B^{-1}b + \bar{c}_N^\top x_N, \qquad \bar{c}_N^\top := c_N^\top - c_B^\top A_B^{-1}A_N.
$$

Vector $$\bar{c}_N$$ chứa **chi phí rút gọn** (reduced costs). Vì $$x_N \succeq 0$$:

- nếu $$\bar{c}_N \succeq 0$$, không thể tăng một biến ngoài cơ sở mà làm giảm mục tiêu — BFS là **tối ưu**;
- nếu có $$\bar{c}_j < 0$$, ta có thể tăng tọa độ ngoài cơ sở đó (biến **vào** cơ sở) và đưa một biến cơ sở về không (biến **ra**). Kiểm định tỉ số chọn chỉ số ra sao cho $$x_B$$ vẫn không âm.

Một phép đổi chỗ như vậy gọi là **pivot**. Sau hữu hạn bước (nếu có quy tắc chống tuần hoàn, ví dụ Bland), simplex hoặc báo tối ưu, hoặc phát hiện tia không bị chặn ($$Ax = 0$$, $$x \succeq 0$$, $$c^\top x < 0$$).

## Ví dụ hai biến

Tối đa hóa $$3x_1 + 2x_2$$ (tương đương tối thiểu hóa $$-3x_1-2x_2$$) với

$$
\begin{align}
x_1 + x_2 &\le 4, \\
2x_1 + x_2 &\le 6, \\
x_1, x_2 &\ge 0.
\end{align}
$$

Các đỉnh của đa giác khả thi là $$(0,0)$$, $$(3,0)$$, $$(2,2)$$, và $$(0,4)$$. Giá trị mục tiêu: $$0$$, $$9$$, $$10$$, $$8$$. Simplex có thể xuất phát từ gốc, xoay tới $$(3,0)$$ rồi $$(2,2)$$, nơi mọi chi phí rút gọn đều không âm. Hình học cho cùng kết luận: các đường mức của $$3x_1+2x_2$$ chạm đa giác lần cuối tại $$(2,2)$$.

## Vì sao vẫn dạy simplex trong khoa học dữ liệu

- **Kiểm tra mô hình.** Nếu viết được bài toán về dạng chuẩn LP, bạn đã biết nó lồi và tồn tại nghiệm tại đỉnh.
- **Lót đường cho đối ngẫu.** Chi phí rút gọn chính là slack đối ngẫu. Bù trừ bù (complementary slackness) ở [Chương 12]({% multilang_post_url contents/chapter12/21-04-02-12_00_KKT_conditions %}) là chứng chỉ tối ưu mà simplex đang tìm.
- **Bộ giải.** Mã sản xuất (HiGHS, Gurobi, `scipy.optimize.linprog`) dùng simplex cải tiến và/hoặc điểm trong. Bạn ít khi tự lập bảng, nhưng cần phân biệt trả về không khả thi với không bị chặn.

**Ghi chú độ phức tạp.** Các khối Klee–Minty cho thấy một số quy tắc xoay có thể mất số bước hàm mũ trong trường hợp xấu nhất. Thực tế simplex thường nhanh; phương pháp điểm trong (Chương 15–17) có đảm bảo đa thức và thắng trên một số LP thưa lớn. Với mô hình *đã là* LP hoặc QP — bài toán khẩu phần, đối ngẫu SVM lề cứng, basis pursuit — bạn thường gọi lớp mô hình hóa như CVXPY (xem lab DCP trong chương này) thay vì xoay bảng bằng tay.

## Bài tập

1. Chuyển $$x_1 - x_2 \le 3$$, $$x_1 \ge 0$$, $$x_2$$ tự do về dạng chuẩn.
2. Xuất phát từ $$(0,0)$$ trong ví dụ trên, xác định biến vào đầu tiên nếu luôn chọn chi phí rút gọn âm nhất.
3. Cho một LP 2-D khả thi và không bị chặn; giải thích vì sao kiểm định tỉ số thất bại.

Đọc thêm: Boyd & Vandenberghe, Phụ lục B; Nocedal & Wright, Ch. 13; ghi chú bài toán chuẩn của CMU được liên kết từ [README]({{ site.baseurl }}/).
