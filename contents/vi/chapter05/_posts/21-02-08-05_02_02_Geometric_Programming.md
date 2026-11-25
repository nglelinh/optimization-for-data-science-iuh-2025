---
layout: post
title: 05-02-02 Quy Hoạch Hình Học
chapter: '05'
order: 6
owner: Copilot
categories:
- chapter05
lang: vi
---

Khi thiết kế một vi mạch điện tử hay một cánh máy bay, kỹ sư thường xuyên gặp các công thức vật lý dạng định luật lũy thừa: diện tích tỷ lệ với $$w \cdot h$$, điện trở tỷ lệ với $$L \cdot w^{-1}$$, công suất tiêu thụ tỷ lệ với $$C \cdot V^2 \cdot f$$. Nhìn vào những biểu thức nhân chia lũy thừa ấy, bài toán trông hoàn toàn **phi lồi**!

Thế nhưng vào những năm 1960, Duffin, Peterson và Zener phát hiện ra một lớp bài toán kỳ diệu mang tên **Quy hoạch Hình học (Geometric Programming - GP)**: miễn là mọi biến đều dương ($$x_i > 0$$), các ràng buộc bất đẳng thức là **đa thức dương (posynomial)** và các ràng buộc đẳng thức là **đơn thức dương (monomial)**, thì chỉ qua phép đổi biến logarit $$y_i = \log x_i$$, toàn bộ bài toán lập tức biến hình thành một bài toán tối ưu hóa lồi trơn tru giải được đến độ chính xác tuyệt đối!

## Bản đồ kiến thức nền: Từ đơn thức dương đến bài toán lồi Log-Sum-Exp

Ba trụ cột dưới đây giải mã trọn vẹn cấu trúc của Quy hoạch Hình học:

- **Đơn thức dương (Monomial) & Đa thức dương (Posynomial):** Đơn thức dương có dạng $$c x_1^{a_1} \cdots x_n^{a_n}$$ với $$c > 0$$ và số mũ $$a_i \in \mathbb{R}$$ bất kỳ (có thể âm hoặc phân số!). Đa thức dương là tổng của nhiều đơn thức dương (hệ số dương, tuyệt đối không có dấu trừ giữa các số hạng!).
- **Phép đổi biến Logarit $$x_i = e^{y_i}$$:** Dưới phép đổi biến này, mỗi đơn thức dương trở thành hàm mũ $$e^{a^T y + b}$$ (với $$b = \log c$$). Lấy $$\log$$ hai vế biến:
  - Ràng buộc đẳng thức đơn thức $$h(x) = 1$$ thành **đẳng thức affine** $$a^T y + b = 0$$.
  - Ràng buộc bất đẳng thức đa thức dương $$\sum_k c_k x^{a_k} \le 1$$ thành **bất đẳng thức log-sum-exp** $$\log\left(\sum_k e^{a_k^T y + b_k}\right) \le 0$$ — luôn lồi!
- **Tại sao đẳng thức phải là Monomial chứ không được là Posynomial?** Vì $$\log$$ của một tổng hàm mũ (log-sum-exp) là hàm lồi phi affine, nên nếu đặt dấu `=` thì ràng buộc đẳng thức sẽ mất tính lồi!

### Khung giải thích (nên đọc chậm): Thiết kế hộp chữ nhật thể tích lớn nhất bằng Quy hoạch Hình học

Tìm kích thước dương $$(w, h, d) > 0$$ của một chiếc hộp không nắp có diện tích mặt đáy và mặt bên giới hạn:
$$\max_{w, h, d > 0} \; w \cdot h \cdot d \quad \text{thỏa mãn} \quad w d + 2 w h + 2 h d \le 12.$$

1. **Bước 1 — Đưa về dạng chuẩn GP:**
   - Cực đại hóa $$w h d$$ tương đương cực tiểu hóa đơn thức dương $$f_0(w, h, d) = w^{-1} h^{-1} d^{-1}$$.
   - Chia hai vế ràng buộc cho $$12$$: $$\frac{1}{12} w d + \frac{1}{6} w h + \frac{1}{6} h d \le 1$$ (một đa thức dương!).
2. **Bước 2 — Đổi biến logarit:** Đặt $$w = e^{y_1},\; h = e^{y_2},\; d = e^{y_3}$$ và lấy $$\log$$:
   $$\min_{y \in \mathbb{R}^3} \; (-y_1 - y_2 - y_3) \quad \text{s.t.} \quad \log\left(\frac{1}{12} e^{y_1 + y_3} + \frac{1}{6} e^{y_1 + y_2} + \frac{1}{6} e^{y_2 + y_3}\right) \le 0.$$
   Đây là bài toán tối ưu hóa lồi 100%!
3. **Bước 3 — Giải nhanh bằng đối xứng & bất đẳng thức AM-GM:**
   Với $$w d + 2wh + 2hd \le 12$$, theo AM-GM cho 3 số dương:
   $$12 \ge wd + 2wh + 2hd \ge 3\sqrt[3]{(wd)(2wh)(2hd)} = 3\sqrt[3]{4(whd)^2}.$$
   Dấu bằng xảy ra khi ba số hạng bằng nhau và cùng bằng $$12/3 = 4$$:
   $$wd = 4,\quad 2wh = 4 \implies wh = 2,\quad 2hd = 4 \implies hd = 2.$$
4. **Bước 4 — Khôi phục nghiệm gốc:**
   Nhân cả ba: $$(whd)^2 = 4 \cdot 2 \cdot 2 = 16 \implies whd = 4$$. Suy ra $$h^\star = \frac{4}{wd} = 1$$, $$w^\star = \frac{2}{h^\star} = 2$$, $$d^\star = \frac{2}{h^\star} = 2$$.
   Kiểm tra: diện tích $$2(2) + 2(2)(1) + 2(1)(2) = 12$$, thể tích cực đại $$V^\star = 4$$!

---

Phần này giới thiệu một lớp bài toán tối ưu ban đầu trông không lồi khi nhìn vào hàm mục tiêu và các ràng buộc gốc, nhưng có thể chuyển đổi tương đương về dạng bài toán tối ưu hóa lồi nhờ phép đổi biến thích hợp.

Trước tiên, ta cần hai định nghĩa cơ bản:

## 1. Đơn thức dương và Đa thức dương

Một hàm $$f: \mathbb{R}^n \to \mathbb{R}$$ xác định trên miền $$\text{dom } f = \mathbb{R}^n_{++}$$ (mọi thành phần đều dương chặt) có dạng:

$$f(x) = c x_1^{a_1} x_2^{a_2} \ldots x_n^{a_n} \quad \quad (24)$$

trong đó $$c > 0$$ và $$a_i \in \mathbb{R}$$, được gọi là **hàm đơn thức dương** (monomial).

Tổng của các đơn thức dương:

$$f(x) = \sum_{k=1}^K c_k x_1^{a_{1k}} x_2^{a_{2k}} \ldots x_n^{a_{nk}} \quad \quad (25)$$

với $$c_k > 0$$, được gọi là **hàm đa thức dương** (posynomial).

## 2. Bài toán Quy hoạch Hình học

Một bài toán tối ưu có dạng:

$$\begin{align}
x &= \arg\min_x f_0(x) \\
\text{subject to: } &f_i(x) \leq 1, \quad i = 1, 2, \ldots, m \quad \quad (26) \\
&h_j(x) = 1, \quad j = 1, 2, \ldots, p
\end{align}$$

trong đó $$f_0, f_1, \ldots, f_m$$ là các đa thức dương và $$h_1, \ldots, h_p$$ là các đơn thức dương, được gọi là **bài toán Quy hoạch Hình học (Geometric Programming - GP)**. Điều kiện $$x \succ 0$$ luôn được ngầm hiểu.

Lưu ý rằng nếu $$f$$ là một đa thức dương và $$h$$ là một đơn thức dương, thì thương $$f/h$$ cũng là một đa thức dương.

**Ví dụ:**

$$\begin{align}
(x, y, z) &= \arg\min_{x,y,z} x/y \\
\text{subject to: } &1 \leq x \leq 2 \\
&x^3 + 2y/z \leq \sqrt{y} \\
&x/y = z
\end{align}$$

Bài toán này có thể viết lại về dạng chuẩn của GP:

$$\begin{align}
(x, y, z) &= \arg\min_{x,y,z} xy^{-1} \\
\text{subject to: } &x^{-1} \leq 1 \\
&(1/2)x \leq 1 \\
&x^3 y^{-1/2} + 2y^{1/2}z^{-1} \leq 1 \\
&xy^{-1}z^{-1} = 1
\end{align}$$

Ở dạng gốc này, bài toán không phải là bài toán lồi vì hàm mục tiêu và các ràng buộc đều không lồi.

## 3. Chuyển đổi GP về dạng lồi

Ta có thể chuyển đổi bài toán GP về dạng lồi bằng phép đổi biến logarit như sau:

Đặt $$y_i = \log(x_i)$$, tức là $$x_i = \exp(y_i)$$. Nếu $$f$$ là một đơn thức dương theo $$x$$, thì:

$$f(x) = c(\exp(y_1))^{a_1} \ldots (\exp(y_n))^{a_n} = \exp(a^T y + b)$$

trong đó $$b = \log(c)$$. Hàm $$g(y) = \exp(a^T y + b)$$ là một hàm lồi theo $$y$$ (vì hợp thành của một hàm lồi với một hàm affine luôn bảo toàn tính lồi; ở đây hàm $$\exp$$ là hàm lồi và $$a^T y + b$$ là hàm affine).

Tương tự, đa thức dương trong phương trình (25) được viết lại thành:

$$f(x) = \sum_{k=1}^K \exp(a_k^T y + b_k)$$

trong đó $$a_k = [a_{1k}, \ldots, a_{nk}]^T$$ và $$b_k = \log(c_k)$$. Biểu thức này là tổng các hàm mũ của hàm affine nên là hàm lồi theo $$y$$.

Bài toán GP (26) do đó được viết lại thành:

$$\begin{align}
y &= \arg\min_y \sum_{k=1}^{K_0} \exp(a_{0k}^T y + b_{0k}) \\
\text{subject to: } &\sum_{k=1}^{K_i} \exp(a_{ik}^T y + b_{ik}) \leq 1, \quad i = 1, \ldots, m \quad \quad (27) \\
&\exp(g_j^T y + h_j) = 1, \quad j = 1, \ldots, p
\end{align}$$

trong đó $$a_{ik} \in \mathbb{R}^n$$ ($$i = 0, 1, \ldots, m$$) và $$g_j \in \mathbb{R}^n$$ ($$j = 1, \ldots, p$$).

Áp dụng phép biến đổi đơn điệu tăng $$\log(\cdot)$$ cho hàm mục tiêu và hai vế của các ràng buộc, đồng thời sử dụng tính chất hàm $$\log \sum_{k} \exp(a_k^T y + b_k)$$ (log-sum-exp) là hàm lồi, ta viết lại bài toán (27) về dạng lồi:

**Bài toán GP ở dạng lồi:**

$$\begin{align}
\text{minimize}_y \quad &\tilde{f}_0(y) = \log\left(\sum_{k=1}^{K_0} \exp(a_{0k}^T y + b_{0k})\right) \\
\text{subject to: } &\tilde{f}_i(y) = \log\left(\sum_{k=1}^{K_i} \exp(a_{ik}^T y + b_{ik})\right) \leq 0, \quad i = 1, \ldots, m \quad \quad (28) \\
&\tilde{h}_j(y) = g_j^T y + h_j = 0, \quad j = 1, \ldots, p
\end{align}$$

Như vậy, bài toán GP tương đương với một bài toán tối ưu hóa lồi, vì hàm mục tiêu và các hàm ràng buộc bất đẳng thức trong (28) đều là hàm lồi, còn các ràng buộc đẳng thức là hàm affine. Dạng (28) thường được gọi là **bài toán quy hoạch hình học ở dạng lồi** để phân biệt với dạng gốc (26).