---
layout: post
title: 06-04 Gradient boosting
chapter: '06'
order: 16
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
---

Trong các cuộc thi dữ liệu dạng bảng (tabular data) như Kaggle, hay trong các hệ thống chấm điểm tín dụng, xếp hạng tìm kiếm và dự báo nhu cầu của các tập đoàn công nghệ lớn, thuật toán thống trị suốt nhiều năm qua không phải mạng nơ-ron sâu mà là **XGBoost, LightGBM và CatBoost** — tất cả đều là con đẻ của **Gradient Boosting**!

Điều thú vị đến bất ngờ là: Gradient Boosting thực chất chính là **Gradient Descent**, nhưng không chạy trong không gian tham số $$\mathbb{R}^p$$ mà chạy trực tiếp trong **không gian các hàm số**! Ở mỗi bước lặp, thay vì cập nhật một vector trọng số $$w \leftarrow w - \eta \nabla L(w)$$, ta cộng thêm một cây quyết định nhỏ $$h_m(x)$$ được huấn luyện để xấp xỉ đúng **âm gradient (pseudo-residual)** của hàm mất mát hiện tại!

## Bản đồ kiến thức nền: Từ Gradient Descent trong $$\mathbb{R}^p$$ sang Không gian Hàm

Ba trụ cột sau làm sáng tỏ bản chất tối ưu hóa của Gradient Boosting:

- **Hạ Gradient trong Không gian Hàm (Functional Gradient Descent):** Coi bộ dự đoán hiện tại $$F = (F(x_1), \dots, F(x_n))$$ như một điểm trong $$\mathbb{R}^n$$. Hướng giảm nhanh nhất cho hàm mất mát $$\sum_{i=1}^n L(y_i, F(x_i))$$ chính là vector âm gradient $$r_i^{(m)} = -\left.\frac{\partial L(y_i, F)}{\partial F}\right|_{F = F_{m-1}(x_i)}$$.
- **Pseudo-Residual (Phần dư giả):**
  - Với hàm mất mát bình phương $$L(y, F) = \frac{1}{2}(y - F)^2$$: âm gradient chính là phần dư thông thường $$r_i = y_i - F(x_i)$$!
  - Với hàm mất mát trị tuyệt đối $$L(y, F) = |y - F|$$: âm gradient là $$\operatorname{sign}(y_i - F(x_i))$$!
  - Với hàm mất mát Cross-Entropy (phân loại): âm gradient là $$y_i - \hat{p}_i$$!
- **Khớp cây yếu & Tốc độ học (Shrinkage $$\eta$$):** Vì không thể lưu riêng từng số $$r_i$$ cho dữ liệu mới chưa gặp, ta huấn luyện một cây quyết định nông $$h_m(x)$$ khớp với $$r_i^{(m)}$$, rồi cập nhật $$F_m(x) = F_{m-1}(x) + \eta h_m(x)$$. Hệ số $$\eta \in (0, 1)$$ đóng vai trò hệt như tốc độ học trong GD để chống quá khớp!

### Khung giải thích (nên đọc chậm): Tự tay chạy 2 vòng lặp Gradient Boosting cho bài toán hồi quy 3 mẫu

Cho 3 mẫu dữ liệu $$(x_i, y_i)$$: $$(1, 10),\; (2, 12),\; (3, 20)$$, dùng hàm mất mát bình phương $$L(y, F) = \frac{1}{2}(y - F)^2$$ và tốc độ học $$\eta = 0.5$$:

1. **Khởi tạo $$F_0(x)$$ bằng hằng số tối ưu (trung bình của $$y$$):**
   $$F_0(x) = \frac{10 + 12 + 20}{3} = 14.$$
   Tổng sai số bình phương ban đầu: $$\frac{1}{2}[(10-14)^2 + (12-14)^2 + (20-14)^2] = \frac{1}{2}(16 + 4 + 36) = 28$$.
2. **Vòng lặp $$m = 1$$:**
   - Tính âm gradient (phần dư) $$r_i^{(1)} = y_i - F_0(x_i)$$:
     $$r^{(1)} = (10 - 14,\; 12 - 14,\; 20 - 14) = (-4,\; -2,\; +6).$$
   - Huấn luyện cây gốc nông (decision stump) chia tại $$x \le 2.5$$:
     - Nhánh trái ($$x \le 2.5$$): trung bình của $$(-4, -2)$$ là $$-3$$.
     - Nhánh phải ($$x > 2.5$$): trung bình của $$(+6)$$ là $$+6$$.
   - Cập nhật $$F_1(x) = F_0(x) + 0.5 h_1(x)$$:
     $$F_1(1) = 14 + 0.5(-3) = 12.5,\quad F_1(2) = 12.5,\quad F_1(3) = 14 + 0.5(6) = 17.$$
   - Sai số mới: $$\frac{1}{2}[(-2.5)^2 + (-0.5)^2 + (3)^2] = \frac{1}{2}(6.25 + 0.25 + 9) = 7.75$$ (giảm từ $$28$$ xuống $$7.75$$ chỉ sau 1 cây!).
3. **Vòng lặp $$m = 2$$:**
   - Phần dư mới: $$r^{(2)} = (10 - 12.5,\; 12 - 12.5,\; 20 - 17) = (-2.5,\; -0.5,\; +3)$$ — nhỏ đi đúng một nửa, và cây tiếp theo lại tiếp tục gọt sạch sai số còn sót lại!

---

# Gradient boosting

**Gradient boosting** là phương pháp học tập hợp (ensemble) sử dụng ý tưởng gradient descent để xây dựng các cây quyết định theo trình tự nối tiếp, trong đó mỗi cây mới học cách bù đắp sai số còn lại của các cây trước đó. Phương pháp này có thể áp dụng cho cả bài toán hồi quy và phân lớp.

* Tham khảo thêm: [Gradient Boosting from scratch](https://medium.com/mlreview/gradient-boosting-from-scratch-1e317ae4587d)

### [Tham khảo] Thuật toán Functional Gradient Descent

**Gradient boosting** được Llew Mason, Jonathan Baxter, Peter Bartlett và Marcus Frean diễn giải như một thuật toán *functional gradient descent* (hạ gradient trong không gian hàm). Thuật toán này cực tiểu hóa hàm mất mát trực tiếp trên không gian hàm bằng cách liên tiếp bổ sung các hàm có hướng xấp xỉ hướng ngược chiều gradient.

* Tham khảo thêm: [Gradient Boosting](https://en.wikipedia.org/wiki/Gradient_boosting)

### [Tham khảo] Boosting và Bagging

**Boosting** là kỹ thuật học tập hợp xây dựng các mô hình yếu (weak learner) một cách tuần tự: mỗi mô hình ở giai đoạn sau tập trung khắc phục sai số mà các mô hình trước đó gây ra, rồi kết hợp tất cả thành dự đoán cuối cùng.

**Bagging** là kỹ thuật học tập hợp huấn luyện các mô hình yếu một cách độc lập và song song trên các tập mẫu con khác nhau, sau đó tổng hợp kết quả của chúng.

* Tham khảo thêm: [What is the difference between Bagging and Boosting?](https://quantdare.com/what-is-the-difference-between-bagging-and-boosting/)

## Ý tưởng của Gradient Boosting

Hãy xem xét cách bài toán **Gradient Boosting** được hình thành.

Giả sử ta có một mô hình tập hợp gồm nhiều cây quyết định nhằm dự đoán đầu ra sao cho cực tiểu hóa sai số so với các giá trị quan sát được. Ký hiệu các giá trị thực là $$y_i$$, dữ liệu đầu vào là $$x_i$$, và giá trị dự đoán là $$u_i$$ với $$i=1,\dots,n$$.

Như minh họa trong hình dưới đây, mỗi cây trong tập hợp nhận đầu vào $$x_i \in \mathbb{R}^p$$ và trả về giá trị dự đoán theo các điều kiện phân nhánh tại các nút của cây.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter06/06_04_tree_O9zyAlk.png" alt="tree_O9zyAlk" width="80%" height="80%">
  <figcaption style="text-align: center;">$$\text{[Fig 1] Example of Tree }T_j\text{ [3]}$$</figcaption>
</p>
</figure>

Giá trị dự đoán $$u_i$$ của mô hình tập hợp là tổng có trọng số đầu ra của các cây (trong đó $$T_j(x_i)$$ là đầu ra của cây thứ $$j$$ với đầu vào $$x_i$$):

>
$$ \begin{equation}
u_i = \sum_{j=1}^M \beta_j T_j(x_i)
\end{equation} $$

Chẳng hạn, với hàm mất mát bình phương $$L(y_i, u_i) = (y_i - u_i)^2$$, bài toán tối ưu hóa là cực tiểu hóa tổng mất mát trên tập dữ liệu:
>
$$ \begin{equation}
\min_{\beta} \sum_{i=1}^n L\left(y_i, \sum_{j=1}^M \beta_j T_j(x_i)\right)
\end{equation} $$

Trong thực tế, các mô hình tập hợp thường sử dụng nhiều cây nhỏ có độ sâu cố định (thường từ 5 trở xuống) để tiết kiệm bộ nhớ, tăng tốc độ dự đoán và cải thiện hiệu năng dần khi tăng số lượng cây.

Tuy nhiên, do cấu trúc phân nhánh của từng cây rất đa dạng và số lượng cây kết hợp rất lớn, không gian tìm kiếm trở nên khổng lồ, khiến việc tối ưu trực tiếp trở nên rất khó khăn.

Để giải quyết, ta chuyển bài toán sang một góc nhìn đơn giản hơn: thay vì tối ưu đồng thời $$M$$ trọng số $$\beta_j$$ và cấu trúc cây, hãy xem đây là bài toán cực tiểu hóa $$\min_{u} f(u)$$ theo vector dự đoán $$u \in \mathbb{R}^n$$ với $$f(u) = \sum_{i=1}^n L(y_i, u_i)$$.

**Gradient boosting** chính là kỹ thuật giải bài toán $$\min_{u} f(u)$$ này bằng thuật toán gradient descent trong không gian hàm.

## Thuật toán

Thuật toán **Gradient boosting** thực hiện hạ gradient theo từng bước để tìm dự đoán tối ưu $$u^*$$ cho $$\min_u L(y, u)$$:

1. Khởi tạo dự đoán ban đầu bằng một cây tùy chọn $$u^{(0)} = T_0$$, sau đó lặp các bước 2–4 cho $$k = 1, \dots, M$$.

2. Tính hướng ngược chiều gradient (pseudo-residual) tại dự đoán hiện tại $$u^{(k-1)}$$ cho $$n$$ điểm dữ liệu:
>
$$ \begin{equation}
d_i = - \left . \left[ \frac{\partial L(y_i,u_i)}{\partial u_i} \right] \right|_{u_i = u_i^{(k-1)}}, \quad i=1,\dots,n
\end{equation} $$

3. Tìm cây quyết định $$T_k$$ khớp nhất với vector gradient âm $$d$$ theo nghĩa bình phương tối thiểu:
>
$$ \begin{equation}
\min_{\text{trees } T} \sum_{i=1}^n (d_i - T(x_i))^2
\end{equation} $$

4. Chọn kích thước bước $$\alpha_k$$ và cập nhật giá trị dự đoán bằng cây $$T_k$$ vừa tìm được:
>
$$u^{(k)} = u^{(k-1)} + \alpha_k T_k$$

Như vậy, ở mỗi vòng lặp, thuật toán tính hướng giảm $$d$$ theo $$u$$, xấp xỉ $$d$$ bằng một cây $$T_k$$, rồi dùng $$T_k$$ thay cho gradient trong bước cập nhật.

Khi khai triển ngược công thức truy hồi $$u^{(k)} = u^{(k-1)} + \alpha_k T_k$$ về $$k = 0$$, dự đoán cuối cùng có dạng $$u^{(M)} = T_0 + \sum_{k=1}^M \alpha_k T_k$$, hoàn toàn khớp với dạng tổng có trọng số các cây quyết định đã định nghĩa ở trên.
