---
layout: post
title: '24-02 Các ví dụ về quy hoạch nguyên'
chapter: '24'
order: 3
owner: YoungJae Choung
categories:
- chapter24
lang: vi
---

Sức mạnh thật sự của quy hoạch nguyên hỗn hợp không nằm ở sự cầu kỳ của công thức, mà ở khả năng **dịch những bài toán tưởng như chẳng liên quan gì đến nhau về cùng một ngôn ngữ toán học chung**. Dù bạn đang xếp hành lý vào chiếc ba-lô, ghép cặp nhân viên với công việc, chọn nơi đặt kho hàng, phân cụm dữ liệu bằng K-medoids hay chọn tập đặc trưng tốt nhất cho hồi quy, tất cả đều quy về cùng một bộ khung MIP.

Bài học này giống như một cuốn từ điển mẫu (modeling cookbook): đọc kỹ sáu bài toán kinh điển dưới đây sẽ giúp bạn nhận ra ngay các "mẫu câu" ràng buộc quen thuộc khi đối mặt với một bài toán thực tế hoàn toàn mới.

## Bản đồ kiến thức nền: Bốn khuôn mẫu mô hình hóa MIP cốt lõi

Sáu ví dụ trong bài thực chất xoay quanh bốn khuôn mẫu tư duy mô hình hóa quan trọng nhất của vận trù học và thống kê:

- **Khuôn mẫu Chọn lọc có ngân sách (Knapsack & Best Subset):** Dùng $$\sum_j x_j \le k$$ hoặc $$\sum_j a_j x_j \le b$$ để giới hạn số lượng hoặc tổng tài nguyên, kết hợp liên kết $$|\beta_j| \le M z_j$$ khi muốn gắn biến nhị phân với biến liên tục.
- **Khuôn mẫu Ghép cặp 1–1 (Assignment):** Ma trận biến $$x_{ij} \in \{0, 1\}$$ có tổng mỗi hàng và tổng mỗi cột bằng $$1$$. Điểm đặc biệt kỳ diệu là ma trận ràng buộc của bài toán phân công có tính *hoàn toàn đơn mô-đun (totally unimodular)*, nên nghiệm nới lỏng LP luôn tự động là số nguyên!
- **Khuôn mẫu Liên kết Mở–Phục vụ (Facility Location & K-medoids):** Tách quyết định "mở địa điểm/chọn tâm cụm $$j$$" (biến $$y_j$$) khỏi quyết định "gán khách hàng/điểm dữ liệu $$i$$ vào $$j$$" (biến $$x_{ij}$$) qua ràng buộc liên kết $$x_{ij} \le y_j$$ (dạng chặt, tốt hơn nhiều so với dạng gộp $$\sum_i x_{ij} \le n y_j$$).
- **Khuôn mẫu Chọn phân vị/ngoại lai (Least Median of Squares):** Dùng biến nhị phân $$z_i$$ để "tắt" phần dư của một tỷ lệ điểm dữ liệu (các điểm ngoại lai) thông qua big-$$M$$, biến hàm mục tiêu trung vị phi lồi thành một MILP giải được chính xác.

### Khung giải thích (nên đọc chậm): Tính tay bài toán cái túi 0–1 — khi thuật toán tham lam thất bại

Xét bài toán cái túi 0–1 với sức chứa tối đa $$b = 6$$ kg và 3 món đồ:
- Món 1: giá trị $$c_1 = 10$$, khối lượng $$a_1 = 3$$ (tỷ số $$c_1/a_1 \approx 3.33$$).
- Món 2: giá trị $$c_2 = 10$$, khối lượng $$a_2 = 3$$ (tỷ số $$c_2/a_2 \approx 3.33$$).
- Món 3: giá trị $$c_3 = 14$$, khối lượng $$a_3 = 4$$ (tỷ số $$c_3/a_3 = 3.50$$ — cao nhất!).

1. **Cách giải tham lam (Greedy theo tỷ số giá trị/khối lượng):**
   Tham lam chọn món có tỷ số cao nhất trước là Món 3 ($$x_3 = 1$$, nặng $$4$$ kg, giá trị $$14$$). Dung tích còn lại là $$6 - 4 = 2$$ kg — không nhét vừa Món 1 hay Món 2! Tổng giá trị tham lam dừng ở **$$14$$**.
2. **Giải bài toán nới lỏng LP (cho phép cắt nhỏ món đồ, $$x_j \in [0, 1]$$):**
   Chọn trọn Món 3 ($$x_3 = 1$$, dùng $$4$$ kg) cộng thêm $$\frac{2}{3}$$ Món 1 ($$x_1 = \frac{2}{3}$$, dùng $$2$$ kg). Tổng giá trị LP là $$14 + \frac{2}{3}(10) = 20.67$$ — đây là **cận trên** cho mọi nghiệm nguyên.
3. **Nghiệm tối ưu quy hoạch nguyên 0–1:**
   Bỏ qua món "hấp dẫn nhất" là Món 3, ta chọn cả Món 1 và Món 2: $$x^\star = (1, 1, 0)$$. Tổng khối lượng $$3 + 3 = 6 \le 6$$, tổng giá trị đạt **$$20$$** — vượt xa tham lam ($$14$$) và rất sát cận trên LP ($$20.67$$)!

Mục này giới thiệu một số bài toán kinh điển có thể mô hình hóa bằng quy hoạch nguyên và quy hoạch nguyên hỗn hợp.

## Bài toán cái túi (Knapsack)

Bài toán cái túi là một ví dụ kinh điển trong tối ưu tổ hợp: cho một chiếc túi có dung tích tối đa $$b$$ và $$n$$ đồ vật, mỗi đồ vật thứ $$j$$ có giá trị $$c_j$$ và kích thước $$a_j$$. Mục tiêu là chọn tập đồ vật có tổng giá trị lớn nhất sao cho tổng kích thước không vượt quá $$b$$. Dùng biến nhị phân $$x_j \in \{0, 1\}$$ biểu thị việc có chọn đồ vật thứ $$j$$ hay không, ta có:

> $$
> \begin{align}
> &\max_{x} && c^\intercal x \\\\
> &\text{subject to } && a^\intercal x \leq b \\\\
> &&&x_{j} \in \{0, 1\}, \quad j = 1, \dotsc , n
> \end{align}
> $$

## Bài toán phân công (Assignment)

Giả sử có $$n$$ người và $$n$$ công việc, mỗi người đảm nhận đúng một công việc và mỗi công việc được giao cho đúng một người. Gọi $$c_{ij}$$ là chi phí để người $$i$$ thực hiện công việc $$j$$. Bài toán phân công cực tiểu hóa tổng chi phí được phát biểu là:

> $$
> \begin{align}
> &\min_{x} &&\sum_{i = 1}^{n} \sum_{j = 1}^{n} c_{ij} x_{ij} \\\\
> &\text{subject to } &&\sum_{i = 1}^{n} x_{ij} = 1, \quad j = 1, \dotsc, n \\\\
> &&&\sum_{j = 1}^{n} x_{ij} = 1, \quad i = 1, \dotsc, n \\\\
> &&&x_{ij} \in \lbrace 0, 1\rbrace, \quad i = 1, \dotsc, n, \quad j = 1, \dotsc, n
> \end{align}
> $$

## Bài toán đặt cơ sở (Facility location)

Bài toán đặt cơ sở nhằm đồng thời quyết định những kho nào cần mở và phân bổ khách hàng về các kho đó sao cho tổng chi phí cố định và chi phí vận chuyển là nhỏ nhất.

Giả sử có tập các vị trí kho ứng viên $$N = \lbrace 1, \dotsc, n \rbrace$$ và tập khách hàng $$M = \lbrace 1, \dotsc, m \rbrace$$. Mỗi kho $$j$$ có chi phí mở cố định $$f_{j}$$, còn chi phí vận chuyển hàng từ kho $$j$$ đến khách hàng $$i$$ là $$c_{ij}$$. Mô hình quy hoạch nguyên được viết như sau:

> $$
> \begin{align}
> &\min_{x, y} && \sum_{j = 1}^{n} f_{j} y_{j} + \sum_{i = 1}^{m} \sum_{j = 1}^{n} c_{ij} x_{ij} \\\\
> &\text{subject to } && \sum_{j = 1}^{n} x_{ij} = 1,  \quad i = 1, \dotsc, m \\\\
> &&& x_{ij} \leq y_{j},  \quad i = 1, \dotsc, m,  \quad j = 1, \dotsc, n \\\\
> &&& x_{ij} \in \lbrace 0, 1\rbrace, \quad i = 1, \dotsc, m, \quad j = 1, \dotsc, n \\\\
> &&& y_{j} \in \lbrace 0, 1\rbrace, \quad j = 1, \dotsc, n
> \end{align}
> $$

Ràng buộc thứ nhất đảm bảo mỗi khách hàng được phục vụ bởi đúng một kho. Ràng buộc thứ hai yêu cầu kho $$j$$ phải được mở ($$y_j = 1$$) thì mới có thể giao hàng cho khách hàng $$i$$ ($$x_{ij} = 1$$). Hệ ràng buộc $$x_{ij} \leq y_j$$ gồm $$mn$$ bất đẳng thức, và cũng có thể viết lại ở dạng gộp (aggregated) chỉ còn $$n$$ bất đẳng thức:

> $$ \sum_{i = 1}^{m} x_{ij} \leq m y_{j}, \quad j = 1, \dotsc, n $$

Khi đó bài toán có dạng tương đương trên miền nguyên:

> $$
> \begin{align}
> &\min_{x, y} &&\sum_{j = 1}^{n} f_{j} y_{j} + \sum_{i = 1}^{m} \sum_{j = 1}^{n} c_{ij} x_{ij} \\\\
> &\text{subject to } &&\sum_{j = 1}^{n} x_{ij} = 1,  \quad i = 1, \dotsc, m \\\\
> &&& \sum_{i = 1}^{m} x_{ij} \leq m y_{j}, \quad j = 1, \dotsc, n \\\\
> &&& x_{ij} \in \lbrace 0, 1\rbrace, \quad i = 1, \dotsc, m, \quad j = 1, \dotsc, n \\\\
> &&& y_{j} \in \lbrace 0, 1\rbrace, \quad j = 1, \dotsc, n
> \end{align}
> $$

## Phân cụm K-means và K-medoids

Phân cụm là quá trình phân hoạch tập dữ liệu $$\{1, \dotsc, n\}$$ thành $$K$$ nhóm tương đồng $$S_{1} \cup \dotsc \cup S_{K} = \lbrace 1, \dotsc, n \rbrace$$. Thuật toán K-means cực tiểu hóa tổng bình phương khoảng cách từ các điểm dữ liệu tới tâm cụm (centroid):

$$ \sum_{i = 1}^{K} \sum_{j \in S_{i}} \| x^{(j)} - \mu^{(i)} \|^{2} $$

trong đó $$\mu^{(i)} := \frac{1}{| S_{i} |} \sum_{j \in S_{i}} x^{(j)}$$ là trung bình cộng (tâm) của cụm $$i$$.

Một phương pháp ít nhạy cảm với điểm ngoại lai hơn là phân cụm K-medoids: thay vì lấy trung bình cộng làm tâm cụm, K-medoids yêu cầu tâm cụm $$y^{(i)}$$ phải là một điểm dữ liệu thực tế trong tập dữ liệu sao cho tổng khoảng cách là nhỏ nhất:

>$$\sum_{i = 1}^{K} \sum_{j \in S_{i}} \| x^{(j)} - y^{(i)} \|^{2} $$
>$$\text{với } y^{(i)} \in \lbrace x^{(j)} : j \in S_{i} \rbrace $$

Bài toán K-medoids có thể phát biểu trực tiếp dưới dạng quy hoạch nguyên. Đặt $$d_{ij} = \| x^{(i)} - x^{(j)} \|^2$$ và định nghĩa hai nhóm biến nhị phân:

$$\begin{align}
&w_{i} =\begin{cases}1 && \text{nếu chọn } x^{(i)} \text{ làm tâm cụm} \\\\
0 && \text{ngược lại,} \end{cases}\\\\
&z_{ji} =\begin{cases}1 && \text{nếu } x^{(j)} \text{ được gán vào cụm có tâm } x^{(i)} \\\\
0 && \text{ngược lại.} \end{cases}
\end{align}$$

Khi đó bài toán tối ưu K-medoids trở thành:

> $$
> \begin{align}
> &\min_{w, z} && \sum_{i = 1}^{n} \sum_{j = 1}^{n} d_{ij} z_{ji} \\\\
> &\text{subject to } && z_{ji} \leq w_{i}, \quad j, i = 1, \dotsc, n \\\\
> &&& \sum_{i = 1}^{n} z_{ji} = 1, \quad j = 1, \dotsc, n \\\\
> &&& \sum_{i = 1}^{n} w_{i} = K \\\\
> &&& w_{i} \in \lbrace 0, 1 \rbrace, \quad i = 1, \dotsc, n \\\\
> &&& z_{ji} \in \lbrace 0, 1 \rbrace, \quad j, i = 1, \dotsc, n
> \end{align}
> $$

Ràng buộc đầu tiên đảm bảo điểm $$x^{(j)}$$ chỉ có thể thuộc cụm có tâm $$x^{(i)}$$ nếu $$x^{(i)}$$ được chọn làm tâm; ràng buộc thứ hai đảm bảo mỗi điểm thuộc đúng một cụm; ràng buộc thứ ba ấn định đúng $$K$$ tâm cụm.

## Chọn tập con tốt nhất (Best subset selection)

Cho ma trận đặc trưng $$X = [x^{1} \quad \dotsc \quad x^{p}] \in \mathbb{R}^{n \times p}$$ và vector phản hồi $$y \in \mathbb{R}^{n}$$, bài toán chọn tập con tốt nhất có dạng:

> $$
> \begin{align}
> &\min_{\beta} &&\frac{1}{2} \| y - X\beta \|^{2} \\\\
> &\text{subject to } &&\| \beta \|_{0} \leq k
> \end{align}$$
> $$\begin{align}
> \text{trong đó } \| \beta \|_{0} := \text{ số phần tử khác không của } \beta.
> \end{align}
> $$

Vì ràng buộc $$\|\beta\|_0 \leq k$$ không lồi, ta có thể biểu diễn lại bài toán thành quy hoạch nguyên hỗn hợp bằng kỹ thuật hằng số lớn (big-M):

> $$
> \begin{align}
> &\min_{\beta, z} && \frac{1}{2} \| y - X\beta \|^{2} \\\\
> &\text{subject to } && | \beta_{i} | \leq Mz_{i}, \quad i = 1, \dotsc, p \\\\
> &&&z_{i} \in \lbrace 0, 1 \rbrace, \quad i = 1, \dotsc, p \\\\
> &&&\sum_{i = 1}^{p} z_{i} \leq k
> \end{align}
> $$

ở đây $$M$$ là hằng số đủ lớn sao cho $$|\beta_i| \leq M$$ tại nghiệm tối ưu.

## Hồi quy bình phương trung vị nhỏ nhất (Least median of squares)

Cho $$X = [x^{1} \quad \dotsc \quad x^{p}] \in \mathbb{R}^{n \times p}$$, $$y \in \mathbb{R}^{n}$$ và $$\beta \in \mathbb{R}^{p}$$, đặt vector phần dư $$r := y - X\beta$$. Bài toán hồi quy bình phương trung vị nhỏ nhất được định nghĩa là:

> $$\beta_{LMS} := \arg\min_{\beta} (\text{median} | r_{i} | ).$$
