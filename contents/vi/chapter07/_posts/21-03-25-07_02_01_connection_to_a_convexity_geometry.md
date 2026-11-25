---
layout: post
title: 07-02-01 Liên hệ với hình học tập lồi
chapter: '07'
order: 4
owner: Kyeongmin Woo
categories:
- chapter07
lang: vi
---

Làm thế nào để biến một bài toán tối ưu **có ràng buộc** $$\min_{x \in C} f(x)$$ thành một bài toán **hoàn toàn không ràng buộc** trên toàn không gian $$\mathbb{R}^n$$ mà không mất đi bất kỳ thông tin nào? Câu trả lời kinh điển của giải tích lồi chỉ cần đúng một hàm số kỳ lạ nhưng cực kỳ lợi hại: **hàm chỉ thị (indicator function)** $$I_C(x)$$, nhận giá trị $$0$$ nếu $$x \in C$$ và nhảy vọt lên $$+\infty$$ ngay khi $$x$$ bước ra ngoài $$C$$!

Khi viết lại bài toán thành $$\min_{x \in \mathbb{R}^n} \big(f(x) + I_C(x)\big)$$, một câu hỏi tuyệt đẹp lập tức hiện ra: *vi phân dưới $$\partial I_C(x)$$ của hàm chỉ thị trông như thế nào?* Bổ đề trong bài học này chứng minh một kết nối hình học ngoạn mục: **$$\partial I_C(x)$$ chính xác là Nón pháp tuyến (Normal Cone) $$N_C(x)$$ của tập lồi $$C$$ tại $$x$$**!

## Kiến thức cần nhớ: Nhịp cầu giữa Giải tích Subgradient và Hình học Tập lồi

Ba trụ cột dưới đây giải thích trọn vẹn sức mạnh của đẳng thức $$\partial I_C(x) = N_C(x)$$:

- **Hàm chỉ thị $$I_C(x)$$ là hàm lồi mở rộng:** Tập trên đồ thị $$\operatorname{epi}(I_C) = C \times [0, \infty)$$ là một hình trụ lồi trên đáy $$C$$, nên $$I_C$$ là hàm lồi khi và chỉ khi $$C$$ là tập lồi!
- **Định nghĩa Nón pháp tuyến $$N_C(x)$$:** Tại một điểm $$x \in C$$, nón pháp tuyến là tập tất cả các vector $$g$$ hướng ra ngoài $$C$$ sao cho $$g^T(y - x) \le 0$$ với mọi $$y \in C$$ (tức góc giữa $$g$$ và mọi hướng đi vào $$C$$ đều $$\ge 90^\circ$$):
  - Nếu $$x \in \operatorname{int}(C)$$ (bên trong $$C$$): không có vector khác 0 nào vuông góc/tù với mọi hướng $$\implies N_C(x) = \{0\}$$.
  - Nếu $$x$$ nằm trên biên trơn của $$C$$: $$N_C(x)$$ là **tia pháp tuyến hướng ra ngoài**.
  - Nếu $$x$$ nằm ở góc nhọn (đỉnh đa giác) của $$C$$: $$N_C(x)$$ là một **hình quạt (nón) rộng** chứa mọi tia pháp tuyến hướng ra ngoài!
- **Đẳng thức $$\partial I_C(x) = N_C(x)$$:** Viết định nghĩa subgradient cho $$I_C$$ tại $$x \in C$$ (nơi $$I_C(x) = 0$$):
  $$I_C(y) \ge 0 + g^T(y - x) \; \forall y \in \mathbb{R}^n.$$
  Với $$y \notin C$$, vế trái là $$+\infty$$ nên luôn đúng; với $$y \in C$$, vế trái là $$0$$ nên điều kiện rút gọn thành $$g^T(y - x) \le 0 \; \forall y \in C$$ — chính xác là định nghĩa $$g \in N_C(x)$$!

### Giải thích: Tính tường minh Nón pháp tuyến $$N_C(x) = \partial I_C(x)$$ trên hình vuông đơn vị

Xét tập lồi $$C = [0, 1] \times [0, 1] \subset \mathbb{R}^2$$ (hình vuông đơn vị):

1. **Tại điểm bên trong $$x = (0.5, 0.5)$$:**
   Ta có thể đi theo cả 4 hướng $$(\pm 0.1, 0)$$ và $$(0, \pm 0.1)$$ vẫn ở trong $$C$$. Điều kiện $$g^T(y - x) \le 0$$ ép $$g_1 = 0$$ và $$g_2 = 0$$.
   $$\partial I_C(0.5, 0.5) = N_C(0.5, 0.5) = \{(0, 0)\}.$$
2. **Tại điểm trên cạnh phải $$x = (1, 0.5)$$:**
   Mọi $$y = (y_1, y_2) \in C$$ thỏa $$y_1 - 1 \le 0$$ và $$y_2 - 0.5$$ có thể âm hoặc dương.
   Để $$g_1(y_1 - 1) + g_2(y_2 - 0.5) \le 0 \; \forall y \in C$$, bắt buộc $$g_1 \ge 0$$ và $$g_2 = 0$$!
   $$\partial I_C(1, 0.5) = N_C(1, 0.5) = \{(g_1, 0) : g_1 \ge 0\} \quad (\text{tia ngang chỉ sang phải}).$$
3. **Tại đỉnh trên–phải $$x = (1, 1)$$:**
   Mọi $$y \in C$$ thỏa $$y_1 - 1 \le 0$$ và $$y_2 - 1 \le 0$$. Do đó mọi vector có $$g_1 \ge 0$$ và $$g_2 \ge 0$$ đều thỏa $$g_1(y_1 - 1) + g_2(y_2 - 1) \le 0$$!
   $$\partial I_C(1, 1) = N_C(1, 1) = \mathbb{R}_+^2 \quad (\text{cả góc phần tư thứ nhất!}).$$

---

Đối với một tập lồi $$C \subseteq \mathbb{R}^n$$, xét hàm chỉ thị $$I_C: \mathbb{R}^n \to \mathbb{R}$$ được định nghĩa như sau:

>
$$
I_C(x) = I\{x \in C \} =
\begin{cases}
0               &\text{nếu } x \in C \\
\infty         &\text{nếu } x \notin C 
\end{cases}
$$

Vi phân dưới của hàm chỉ thị có ý nghĩa hình học sau:

### Bổ đề
Với mọi $$x \in C$$, vi phân dưới $$\partial I_C(x)$$ trùng với nón pháp tuyến $$\mathcal{N}_C(x)$$ của tập $$C$$ tại $$x$$:

>
\begin{equation}
\mathcal{N}_C(x) = \{g \in \mathbb{R}^n | g^Tx \geq g^Ty \text{  với mọi  } y \in C \}
\end{equation}

### Chứng minh

Theo định nghĩa, một gradient dưới $$g$$ của $$I_C$$ tại $$x$$ phải thỏa mãn:
>
\begin{equation}
I_C(y) \geq I_C(x) + g^T(y-x) \text{ với mọi } y
\end{equation}

Vì $$x \in C$$ nên $$I_C(x)=0$$, do đó bất đẳng thức trên trở thành:
>
\begin{equation}
I_C(y) \geq g^T(y-x) \text{ với mọi } y
\end{equation}

Ta xét hai trường hợp của $$y$$:

Thứ nhất, với mọi $$y \in C$$, ta có $$I_C(y) = 0$$, nên:
>
\begin{equation}
I_C(y) = 0 \geq g^T(y-x)
\end{equation}

Điều này tương đương với $$g^Tx \geq g^Ty$$ với mọi $$y \in C$$.

Thứ hai, với mọi $$y \notin C$$, ta có $$I_C(y) = \infty$$, nên bất đẳng thức
>
$$I_C(y)=\infty \geq g^T(y-x)$$

luôn đúng với mọi vector $$g$$.

Kết hợp cả hai trường hợp, tập hợp tất cả các gradient dưới của $$I_C$$ tại $$x \in C$$ chính là:
>
$$\{g \in \mathbb{R}^n | g^Tx \geq g^Ty \text{ với mọi } y \in C\}$$

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter07/07_02_subgrad-5.png" alt="connection_to_convexity_geometry" width="80%" height="80%">
</p>
  <figcaption style="text-align: center;">[Hình 1] Nón pháp tuyến [1]</figcaption>
</figure>