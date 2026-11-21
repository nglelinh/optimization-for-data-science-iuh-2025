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

Trong phần này, hãy xem các ví dụ khác nhau tương ứng với quy hoạch nguyên và tìm hiểu cách chúng được sử dụng.

## Bài toán cái túi (Knapsack)
Bài toán cái túi là một bài toán tối ưu tổ hợp kinh điển, trong đó thể tích có thể bỏ vào túi bị giới hạn, tức tổng kích thước các đồ vật chứa được trong túi bị ràng buộc. Với ràng buộc này, bài toán nhằm chọn các đồ vật có tổng giá trị lớn nhất. Bài toán có thể biểu diễn bằng các biến nhị phân $$x$$, trong đó $$x_{j}$$ nhận giá trị 0 hoặc 1 tùy theo đồ vật thứ $$j$$ có được chọn hay không.

> $$
> \begin{align}
> &\max_{x} && c^\intercal x \\\\
> &\text{subject to } && a^\intercal x \leq b \\\\
> &&&x_{j} \in {0, 1}, j = 1, \dotsc , n
> \end{align}
> $$

$$c_{j}, a_{j}$$ lần lượt biểu diễn giá trị và kích thước (thể tích) của đồ vật thứ $$j$$.

## Bài toán phân công (Assignment)
Giả sử có $$n$$ người và $$n$$ công việc. Mỗi người được giao đúng một công việc. Ở đây, $$c_{ij}$$ là chi phí để người $$i$$ thực hiện công việc $$j$$. Bài toán phân công nhằm giao $$n$$ người cho $$n$$ công việc với chi phí nhỏ nhất. Để tối ưu các điều kiện này, công thức toán học như sau:

> $$
> \begin{align}
> &\min_{x} &&\sum_{i = 1}^{n} \sum_{j = 1}^{n} c_{ij} x_{ij} \\\\
> &\text{subject to } &&\sum_{i = 1}^{n} x_{ij} = 1, j = 1 \dotsc n \\\\
> &&&\sum_{j = 1}^{n} x_{ij} = 1, i = 1 \dotsc n \\\\
> &&&x_{ij} \in \lbrace 0, 1\rbrace \quad i = 1 \dotsc n, \quad j = 1 \dotsc n
> \end{align}
> $$


## Bài toán đặt cơ sở (Facility location)
Bài toán đặt cơ sở nhằm cực tiểu hóa chi phí vận chuyển từ các cơ sở cụ thể đến khách hàng.<br>

Giả sử có các kho $$N = \lbrace 1, \dotsc, n \rbrace$$ và khách hàng $$M = \lbrace 1, \dotsc, m \rbrace$$.<br>
Chi phí cố định $$f_{j}$$ gắn với việc sử dụng kho $$j$$.
Chi phí vận chuyển $$c_{ij}$$ là chi phí phát sinh khi hàng giao cho khách hàng $$i$$ được vận chuyển từ kho $$j$$.<br>

Các quyết định cần đưa ra ở đây là kho nào nên hoạt động và khách hàng nào nhận hàng từ mỗi kho, với mục tiêu cực tiểu hóa cả chi phí cố định lẫn chi phí vận chuyển bằng cách lập và giải công thức toán học.

> $$
> \begin{align}
> &\min_{x, y} && \sum_{j = 1}^{n} f_{j} y_{j} + \sum_{i = 1}^{m} \sum_{j = 1}^{n} c_{ij} x_{ij} \\\\
> &\text{subject to } && \sum_{j = 1}^{n} x_{ij} = 1,  \quad i = 1 \dotsc m \\\\
> &&& x_{ij} \leq y_{j},  \quad i = 1 \dotsc m,  \quad j = 1 \dotsc n \\\\
> &&& x_{ij} \in \lbrace 0, 1\rbrace \quad i = 1 \dotsc m, \quad j = 1 \dotsc n \\\\
> &&& y_{j} \in \lbrace 0, 1\rbrace \quad j = 1 \dotsc n
> \end{align}
> $$

Ràng buộc đầu tiên nghĩa là mỗi khách hàng nhận hàng từ đúng một kho. Ràng buộc thứ hai nói rằng kho $$j$$ phải hoạt động thì khách hàng $$i$$ mới nhận hàng từ đó. Vì cả $$x_{ij}$$ và $$y_{j}$$ đều nhị phân, ta có $$mn$$ ràng buộc. Điều này cũng có thể biểu diễn ở dạng "gộp" (marginalized) bằng ràng buộc sau:

> $$ \sum_{i = 1}^{m} x_{ij} \leq m y_{j}, \quad j = 1 \dotsc n $$

Phản ánh điều này, có thể thay bằng công thức toán học sau:

> $$
> \begin{align}
> &\min_{x, y} &&\sum_{j = 1}^{n} f_{j} y_{j} + \sum_{i = 1}^{m} \sum_{j = 1}^{n} c_{ij} x_{ij} \\\\
> &\text{subject to } &&\sum_{j = 1}^{n} x_{ij} = 1,  \quad i = 1 \dotsc m \\\\
> &&& \sum_{i = 1}^{m} x_{ij} \leq m y_{j}, \quad j = 1 \dotsc n \\\\
> &&& x_{ij} \in \lbrace 0, 1\rbrace \quad i = 1 \dotsc m, \quad j = 1 \dotsc n \\\\
> &&& y_{j} \in \lbrace 0, 1\rbrace \quad j = 1 \dotsc n
> \end{align}
> $$


## Phân cụm K-means và K-medoids
Phân cụm là quá trình chia dữ liệu thành các nhóm tương tự nhau. Thuật toán K-means nhằm tìm $$K$$ cụm bằng cách tìm $$K$$ giá trị tâm (centroid) cực tiểu hóa khoảng cách trung bình giữa các điểm dữ liệu trong cụm. Mục tiêu là tìm một phân hoạch $$S_{1} \cup \dotsc \cup S_{K} = \lbrace 1, \dotsc, n \rbrace$$ cho dữ liệu đã cho. Khi đó biểu thức sau được cực tiểu hóa:

$$ \sum_{i = 1}^{K} \sum_{j \in S_{i}} \| x^{(j)} - \mu^{(i)} \|^{2} $$

trong đó $$ \mu^{(i)} :  = \frac{1}{| S_{i} |} \sum_{j \in S_{i}} x^{(j)} $$,
$$ \mu^{(i)} $$ biểu diễn tâm của cụm $$i$$.

Một phương pháp bền vững (robust) hơn với các điểm ngoại lai so với việc tính tâm bằng trung bình (K-means) là phân cụm K-medoids: thay vì tính giá trị tâm của $$K$$ cụm bằng trung bình cộng, nó đặt tâm là điểm dữ liệu gần tâm cụm nhất.
Nghĩa là, phân cụm K-medoids là phương pháp xem mỗi điểm dữ liệu ($$y^{(i)}$$) là một điểm tâm ứng viên và chọn điểm dữ liệu cho giá trị nhỏ nhất làm tâm.

>$$\sum_{i = 1}^{K} \sum_{j \in S_{i}} \| x^{(j)} - y^{(i)} \|^{2} $$
>$$\text{where } y^{(i)} \in \lbrace x^{(j)} : j \in S_{i} \rbrace $$

<br>
Bài toán này có thể được biến đổi và biểu diễn thành một quy hoạch nguyên.
Trước hết, ta định nghĩa $$ d_{ij} = \| x^{(i)} - x^{(j)} \|^2 $$ và hai biến nhị phân sau:

$$\begin{align}
&w_{i} =\begin{cases}1 && \text{nếu chọn } x^{(i)} \text{ làm tâm} \\\\
0 && \text{ngược lại.} \end{cases}\\\\
&z_{ji} =\begin{cases}1 && \text{nếu } x^{(j)} \text{ thuộc cụm có tâm } x^{(i)} \\\\
0 && \text{ngược lại.} \end{cases}
\end{align}$$

<br>

Bài toán K-medoids có thể được định nghĩa như một bài toán tối ưu như sau:

> $$
> \begin{align}
> &\min_{w, z} && \sum_{i = 1}^{n} \sum_{j = 1}^{n} d_{ij} z_{ji} \\\\
> &\text{subject to } && z_{ji} \leq w_{i} \\\\
> &&& \sum_{i = 1}^{n} z_{ji} = 1, \quad j = 1 \dotsc n \\\\
> &&& \sum_{i = 1}^{n} w_{i} = K \\\\
> &&& w_{i} \in \lbrace 0, 1 \rbrace \quad i = 1 \dotsc n \\\\
> &&& z_{ji} \in \lbrace 0, 1 \rbrace \quad j, i = 1 \dotsc n
> \end{align}
> $$

Ràng buộc đầu tiên nghĩa là sau khi tâm được xác định, ta sẽ xác định $$x_{j}$$ có thuộc về $$x_{i}$$ hay không. Ràng buộc thứ hai bảo đảm mỗi điểm thuộc đúng một cụm.

## Chọn tập con tốt nhất (Best subset selection)
Khi cho $$X = [x^{1} \quad \dotsc \quad x^{p}] \in \mathbb{R}^{n×p}, \quad y \in \mathbb{R}^{n}$$, bài toán chọn tập con tốt nhất như sau:

> $$
> \begin{align}
> &\min_{\beta} &&\frac{1}{2} \| y - X\beta \|^{2} \\\\
> &\text{subject to } &&\| \beta \|_{0} \leq k\\\\
> \end{align}$$
> $$\begin{align}
> \text{trong đó}  \| \beta \|_{0}  :  = \text{ số phần tử khác không của } \beta.
> \end{align}
> $$

Vì $$ \| \beta \|_{0} $$ là ràng buộc không lồi, bài toán có thể được giải dễ hơn bằng cách biến đổi thành quy hoạch nguyên.

> $$
> \begin{align}
> &\min_{\beta, z} && \frac{1}{2} \| y - X\beta \|^{2} \\\\
> &\text{subject to } && | \beta_{i} | \leq Mz_{i} \quad i = 1 \dotsc p \\\\
> &&&z_{i} \in \lbrace 0, 1 \rbrace \quad i = 1 \dotsc p \\\\
> &&&\sum_{i = 1}^{p} z_{i} \leq k
> \end{align}
> $$

Ở đây $$M$$ là một hằng số đủ lớn (big-M) sao cho $$|\beta_i| \leq M$$ tại nghiệm tối ưu.

## Hồi quy bình phương trung vị nhỏ nhất (Least median of squares)
Khi cho $$X = [x^{1} \quad \dotsc \quad x^{p}] \in \mathbb{R}^{n×p}, \quad y \in \mathbb{R}^{n}$$ và $$\beta \in \mathbb{R}^{p}$$, nếu định nghĩa $$r : = y - X\beta$$, bài toán hồi quy bình phương trung vị nhỏ nhất như sau:

> $$\beta_{LMS} : = \arg\min_{\beta} (median | r_{i} | ).$$
