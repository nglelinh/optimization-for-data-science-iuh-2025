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
