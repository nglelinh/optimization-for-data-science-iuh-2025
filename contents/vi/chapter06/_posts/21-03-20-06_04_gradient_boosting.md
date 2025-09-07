---
layout: post
title: 06-04 Gradient boosting
chapter: '06'
order: 14
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
---

# Gradient boosting

**Gradient boosting** là một phương pháp sử dụng gradient descent để tạo ra các cây một cách tuần tự, đồng thời bù đắp cho các lỗi của các cây trước đó khi cố gắng dự đoán kết quả với một mô hình ensemble bao gồm nhiều cây. **Gradient Boosting** có thể được sử dụng cho cả hồi quy và phân lớp.

* Để biết thêm thông tin chi tiết, tham khảo blog [Gradient Boosting from scratch](https://medium.com/mlreview/gradient-boosting-from-scratch-1e317ae4587d)


### [Tham khảo] Thuật toán functional gradient descent
**Gradient boosting** được giới thiệu như một thuật toán functional gradient descent bởi Llew Mason, Jonathan Baxter, Peter Bartlett và Marcus Frean. Thuật toán functional gradient descent tối ưu hóa hàm mất mát trên không gian hàm bằng cách liên tục lựa chọn các hàm có hướng âm của gradient, do đó thực hiện gradient descent.

* Để biết thêm thông tin chi tiết, tham khảo [Gradient Boosting](https://en.wikipedia.org/wiki/Gradient_boosting)

### [Tham khảo] Boosting vs Bagging
**Boosting** là một kỹ thuật ensemble tạo ra các weak learner một cách tuần tự để dự đoán kết quả. Learner giai đoạn tiếp theo học từ dữ liệu mà learner giai đoạn trước đó đã dự đoán sai, và kết quả của các learner được tạo ra tuần tự được kết hợp để tạo ra kết quả cuối cùng.

**Bagging** là một kỹ thuật ensemble tạo ra các weak learner độc lập với nhau để dự đoán kết quả. Do đó, mỗi learner chạy song song và kết quả của chúng được kết hợp để tạo ra kết quả cuối cùng.

* Để biết thêm thông tin chi tiết, tham khảo blog [What is the difference between Bagging and Boosting?](https://quantdare.com/what-is-the-difference-between-bagging-and-boosting/)
## Gradient Boosting
Hãy xem xét nền tảng về cách **Gradient Boosting** được phát triển.

Giả sử có một mô hình ensemble bao gồm các cây được sử dụng cho phân lớp. Mô hình này sẽ muốn dự đoán kết quả sao cho tối thiểu hóa lỗi với các giá trị quan sát được. Gọi các giá trị quan sát được là $$y_i$$, $$i=1,\dots,n$$, dữ liệu đầu vào là $$x_i, i=1,\dots,n$$, và các giá trị dự đoán là $$u_i$$, $$i=1,\dots,n$$.

Như được hiển thị trong hình dưới đây, mỗi cây thuộc ensemble nhận $$x_i \in R^p$$ làm đầu vào và đưa ra kết quả theo các điều kiện phân nhánh trong các nút của cây.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter06/06_04_tree_O9zyAlk.png" alt="tree_O9zyAlk" width="80%" height="80%">
  <figcaption style="text-align: center;">$$\text{[Fig 1] Example of Tree }T_j\text{ [3]}$$</figcaption>
</p>
</figure>

Giá trị dự đoán $$u_i$$ của mô hình ensemble có thể được tính toán bằng tổng có trọng số của kết quả của mỗi cây. (Ở đây, $$T_j(x_i)$$ là kết quả được đưa ra bởi cây $$j$$ khi nó nhận $$x_i$$ làm đầu vào.)

>
$$ \begin{equation}
u_i = \sum_{j=1}^M \beta_j T_j(x_i)
\end{equation} $$

Đối với hàm mất mát, nó có thể được định nghĩa là $$L=(y_i,u_i)=(y_i - u_i)^2$$ dưới dạng tổng bình phương sai số để tối thiểu hóa lỗi giữa các giá trị quan sát và dự đoán.
>
$$ \begin{equation}
\min_{\beta} \sum_{i=1}^n L\left(y_i, \sum_{j=1}^M \beta_j T_j(x_i)\right)
\end{equation} $$

Thông thường, khi xây dựng cây trong các mô hình ensemble, nhiều cây nhỏ với độ sâu cố định được tạo ra. Điều này là bởi vì việc làm cho cây nhỏ hơn sử dụng ít bộ nhớ hơn và cho phép dự đoán nhanh hơn, và khi số lượng cây tăng lên, hiệu suất của ensemble cải thiện. Thông thường, độ sâu của cây được cố định ở mức 5 hoặc ít hơn.

Do đó, trong bài toán này, các điều kiện nút được định nghĩa trong mỗi cây rất đa dạng và kết quả của rất nhiều cây được kết hợp tuyến tính, làm cho không gian cây khá lớn. Vì vậy, có thể nói rằng đây là một bài toán rất khó để tối ưu hóa.

Để giải quyết vấn đề này, bài toán tối ưu hóa phải được chuyển đổi thành một bài toán dễ hơn. Bài toán tối ưu hóa ban đầu là tìm $$M$$ trọng số $$\beta_j$$ để tối thiểu hóa hàm mất mát. Hãy nghĩ về bài toán này như một bài toán tối thiểu hóa $$\min_{u} f(u)$$ của hàm $$f(u)$$ đối với các giá trị dự đoán $$u$$. Nếu hàm $$f(u)$$ là hàm mất mát $$L(y,u)$$, thì việc tìm $$u$$ để tối thiểu hóa hàm mất mát có thể được coi là một bài toán được định nghĩa lại một cách dễ dàng. (Ở đây, $$n$$ là số lượng điểm dữ liệu.)

**Gradient boosting** đề cập đến kỹ thuật giải quyết bài toán tối thiểu hóa được định nghĩa lại $$\min_{u} f(u)$$ sử dụng gradient descent.

## Thuật toán
Thuật toán **Gradient boosting** thực hiện gradient descent theo cách sau để tìm ra nghiệm tối ưu $$u^*$$ của $$\min_u L(y, u)$$.

1. Đặt giá trị ban đầu là kết quả của một cây tùy ý: $$u^{(0)}=T_0$$. Sau đó lặp lại các bước 2~4 sau đây.

2. Tính toán gradient âm cho $$u^{(k-1)}$$, là giá trị dự đoán gần nhất cho $$n$$ điểm dữ liệu.
>
$$ \begin{equation}
d_i = - \left . \left[ \frac{\partial L(y_i,u_i)}{\partial u_i} \right] \right|_{u_i = u_i^{(k-1)}}, i=1,\dots,n
\end{equation} $$

3. Tìm cây $$T_k$$ có kết quả $$T(x_i)$$ giống nhất với các gradient $$d_i$$ cho $$n$$ điểm dữ liệu.
>
$$ \begin{equation}
\min_{\text{trees } T} \sum_{i=1}^n (d_i-T(x_i))^2
\end{equation} $$

4. Tính toán kích thước bước $$a_k$$ và cập nhật các giá trị dự đoán sử dụng $$T_k$$ được tìm thấy ở trên.
>
$$u^{(k)}=u^{(k-1)} + \alpha_k T_k$$

Thuật toán này tìm gradient $$d$$ đối với $$u$$ để tìm nghiệm tối ưu $$u^*$$ thông qua gradient descent, tìm $$T_k$$ gần nhất với $$d$$, và thay thế $$T_k$$ thay vì gradient trong phương trình cập nhật để tìm vị trí tiếp theo.

Giá trị dự đoán cuối cùng $$u^*$$ thu được theo cách này có thể được thấy là giống hệt với tổng có trọng số của kết quả cây được định nghĩa trước đó. (Tức là, nếu chúng ta mở rộng phương trình cập nhật đệ quy $$u^{(k)}=u^{(k-1)} + \alpha_k T_k$$ trở lại $$k=0$$, chúng ta nhận được $$u^* = \sum_{k=1}^n \alpha_k T_k$$, có thể được biến thành dạng tổng có trọng số của kết quả cây.)





