---
layout: post
title: '22-04 Tính chất và các biến thể'
chapter: '22'
order: 5
owner: YoungJae Choung
categories:
- chapter22
lang: vi
---

Nếu bạn từng chạy Frank–Wolfe tiêu chuẩn trên một đa diện và vẽ quỹ đạo điểm lặp, bạn sẽ sớm bắt gặp một cảnh tượng vừa thú vị vừa sốt ruột: khi nghiệm tối ưu $$x^\star$$ nằm trên một cạnh biên thay vì ở đỉnh, thuật toán bắt đầu **đi zíc-zắc** qua lại giữa hai đỉnh hai bên, bước ngày càng ngắn lại và mãi không chịu chạm đích. Đây chính là lý do định lý cổ điển của Wolfe (1970) chứng minh tốc độ $$O(1/k)$$ là chặn dưới chặt — không thể cải thiện chỉ bằng cách chọn kích thước bước khéo hơn.

Để phá vỡ bức tường $$O(1/k)$$ và đạt hội tụ tuyến tính (nhanh theo hàm mũ $$O(e^{-\rho k})$$) cho các hàm lồi mạnh trên đa diện, cộng đồng tối ưu đã sáng tạo ra một ý tưởng cực kỳ trực giác: bên cạnh việc *bước về phía một đỉnh tốt*, hãy cho phép thuật toán **lùi ra xa khỏi một đỉnh xấu** đang còn dư âm trong tập hoạt động!

## Kiến thức cần nhớ: Bốn trụ cột nâng cấp Frank–Wolfe

Bài học này mở rộng thuật toán Frank–Wolfe cơ bản sang các biến thể thực chiến thông qua bốn ý tưởng nền tảng:

- **Tìm kiếm đường thẳng và Hiệu chỉnh toàn phần (Line Search & Fully Corrective):** Thay bước cố định $$2/(k+1)$$ bằng tối ưu 1 chiều theo $$\gamma \in [0, 1]$$, hoặc cực tiểu hóa lại toàn bộ $$f$$ trên bao lồi của tập đỉnh đã gặp. Cách này giảm hàm mục tiêu rất mạnh ở các vòng đầu, nhưng đánh đổi bằng chi phí giải bài toán con lớn hơn.
- **Biểu diễn tập hoạt động và Bước rời xa (Active Set & Away Steps):** Mọi điểm lặp đều là tổ hợp lồi $$x^{(k)} = \sum_{v \in \mathcal{S}_k} \alpha_v v$$ của một tập hữu hạn các đỉnh hoạt động $$\mathcal{S}_k$$. Bước rời xa tìm đỉnh $$v \in \mathcal{S}_k$$ kém nhất (tích vô hướng với gradient lớn nhất) rồi giảm trọng số $$\alpha_v$$ — thậm chí xóa hẳn $$v$$ khỏi $$\mathcal{S}_k$$ (gọi là *drop step*).
- **Hình học đa diện và Độ rộng kim tự tháp (Pyramidal Width):** Định lý Lacoste-Julien & Jaggi (2013) chứng minh Away-Step Frank–Wolfe hội tụ tuyến tính nhờ hằng số hình học của đa diện (độ rộng kim tự tháp), đảm bảo hướng di chuyển luôn tạo một góc đủ nhọn với hướng giảm gradient âm dù nghiệm nằm sát mặt biên.
- **Bám theo đường nghiệm (Path Following):** Khi giải họ bài toán ràng buộc với tham số $$t$$ tăng dần (ví dụ chuỗi nghiệm Lasso), nghiệm của bài toán trước là điểm khởi tạo nóng (warm start) tuyệt vời cho bài toán tiếp theo, giúp giảm mạnh tổng số lần gọi LMO.

### Giải thích: Một bước Away-Step triệt tiêu đỉnh xấu ngay lập tức

Hãy xem tại sao Away-Step lại "nhảy thẳng tới đích" ở nơi Frank–Wolfe tiêu chuẩn phải đi zíc-zắc. Xét tam giác $$C = \operatorname{conv}\{v_1=(0,0),\; v_2=(1,0),\; v_3=(0,1)\}$$ và hàm mục tiêu lồi mạnh $$f(x_1, x_2) = \frac{1}{2}(x_1 - 0.5)^2 + \frac{1}{2}x_2^2$$, có nghiệm tối ưu nằm trên cạnh đáy tại $$x^\star = (0.5, 0)$$.

Giả sử ta đang ở điểm $$x = 0.4 v_1 + 0.4 v_2 + 0.2 v_3 = (0.4,\; 0.2)$$ với tập hoạt động $$\mathcal{S} = \{v_1, v_2, v_3\}$$ và gradient $$\nabla f(x) = (-0.1,\; 0.2)$$.

1. **Tính hướng Frank–Wolfe tiêu chuẩn ($$d_{\text{FW}}$$):**
   Tính $$\langle \nabla f(x), v \rangle$$ tại ba đỉnh: tại $$v_1$$ bằng $$0$$, tại $$v_2$$ bằng $$-0.1$$, tại $$v_3$$ bằng $$+0.2$$.
   Đỉnh cực tiểu là $$s_{\text{FW}} = v_2 = (1, 0)$$, nên $$d_{\text{FW}} = v_2 - x = (0.6,\; -0.2)$$.
   Mức giảm tuyến tính: $$\langle -\nabla f(x), d_{\text{FW}} \rangle = (0.1)(0.6) + (-0.2)(-0.2) = 0.10$$.
2. **Tính hướng rời xa ($$d_{\text{away}}$$):**
   Trong tập hoạt động $$\mathcal{S}$$, đỉnh có tích vô hướng lớn nhất (tệ nhất) là $$v_{\text{away}} = v_3 = (0, 1)$$ (giá trị $$+0.2$$).
   Hướng rời xa là $$d_{\text{away}} = x - v_3 = (0.4,\; -0.8)$$.
   Mức giảm tuyến tính: $$\langle -\nabla f(x), d_{\text{away}} \rangle = (0.1)(0.4) + (-0.2)(-0.8) = -0.04 + 0.16 = 0.12$$.
3. **So sánh và thực hiện Drop Step:**
   Vì $$0.12 > 0.10$$, thuật toán chọn hướng rời xa $$d_{\text{away}}$$! Để giữ các trọng số tổ hợp lồi không âm, bước tối đa cho phép là $$\gamma_{\max} = \frac{\alpha_3}{1 - \alpha_3} = \frac{0.2}{0.8} = 0.25$$.
   Cập nhật với $$\gamma = 0.25$$:
   $$x^+ = (0.4,\; 0.2) + 0.25(0.4,\; -0.8) = (0.5,\; 0.0) = x^\star!$$
   Đỉnh gây nhiễu $$v_3$$ bị loại sạch khỏi tập hoạt động ($$\alpha_3^+ = 0$$), và thuật toán chạm đúng nghiệm tối ưu chỉ trong một nước đi — thay vì phải kéo dài hàng chục bước zíc-zắc về phía $$v_1$$ và $$v_2$$!

## Một số biến thể

Dưới đây là một số biến thể phổ biến của phương pháp gradient có điều kiện:

* **Tìm kiếm đường thẳng (Line search)**: Thay vì dùng kích thước bước cố định $$\gamma_k=2/(k+1)$$ ($$k=1,2,3,\ldots$$), ta dùng tìm kiếm đường thẳng chính xác (exact line search) tại mỗi vòng lặp:
> $$\gamma_k = \arg\min_{\gamma\in[0,1]} f\Bigl( x^{(k−1)} + \gamma\bigl(s^{(k−1)} − x^{(k−1)} \bigr) \Bigr)$$

Ngoài ra cũng có thể dùng backtracking line search.

* **Hiệu chỉnh toàn phần (Fully corrective)**: Cập nhật bằng cách cực tiểu hóa trực tiếp hàm mục tiêu trên bao lồi của tất cả các đỉnh đã tìm được cho đến bước hiện tại:
> $$x^{(k)} = \arg\min_y f(y) \: \text{ subject to } y \in \text{conv}\{ x^{(0)}, s^{(0)}, \ldots, s^{(k−1)} \}$$

Biến thể này thường giảm giá trị hàm mục tiêu nhanh hơn nhiều sau mỗi vòng lặp, nhưng chi phí giải bài toán con cao hơn đáng kể.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter22/away_steps.png" alt="[Hình 3] Động lực của away step [3]">
  <figcaption style="text-align: center;">[Hình 3] Động lực của away step [3]</figcaption>
</p>
</figure>
<br>


## Biến thể bước rời xa (Away steps)

Để khắc phục hiện tượng hội tụ chậm (đi zíc-zắc gần biên), hãy xét bài toán cực tiểu hóa minh họa ở [Hình 3], trong đó nghiệm tối ưu là $$(0, 0)$$. Phương pháp Frank-Wolfe tiêu chuẩn gặp khó khăn khi rời khỏi ảnh hưởng của điểm khởi tạo $$(0, 1)$$. Với bước rời xa (away step), thuật toán không chỉ di chuyển về phía các đỉnh triển vọng mà còn có thể lùi ra xa khỏi các đỉnh kém triển vọng đang nằm trong tập hoạt động.

Giả sử tập ràng buộc là bao lồi $$C = \text{conv}(A)$$ với tập nguyên tử (atom) $$A$$. Khi đó mọi điểm $$x \in C$$ có thể biểu diễn tường minh dưới dạng tổ hợp lồi của các phần tử thuộc $$A$$:
> $$x = \sum_{a\in A} \lambda_a(x) a$$

Thuật toán gradient có điều kiện với bước rời xa:

1. Chọn $$x^{(0)} = a^{(0)} \in A$$.
2. Với $$k = 1, 2, 3, \ldots$$:
   * $$s^{(k−1)} \in \arg\min_{a\in A} \nabla f(x^{(k−1)})^T a$$
   * $$a^{(k−1)} \in \arg\max_{a\in A,\; \lambda_a(x^{(k−1)})>0} \nabla f(x^{(k−1)})^T a$$
   * Chọn hướng $$v = s^{(k−1)} − x^{(k−1)}$$ (bước Frank-Wolfe) hoặc $$v = x^{(k−1)} − a^{(k−1)}$$ (bước rời xa) tùy hướng nào cho độ giảm tuyến tính tốt hơn.
   * Cập nhật $$x^{(k)} = x^{(k−1)} + \gamma_k v$$.
3. Kết thúc khi đạt tiêu chí dừng.

## Hội tụ tuyến tính

Xét trước bài toán tối ưu không ràng buộc:
> $$\min_x f(x) \: \text{ subject to } x \in \mathbb{R}^n$$

trong đó $$f$$ là $$\mu$$-lồi mạnh và $$\nabla f$$ là $$L$$-Lipschitz. Khi chạy gradient descent $$x^{(k+1)} = x^{(k)} − t_k\nabla f(x^{(k)})$$ với $$t_k = 1/L$$, ta có tốc độ hội tụ tuyến tính:
> $$f(x^{(k)}) − f^{\star} \leq \Bigl( 1 −\frac{\mu}{L} \Bigr)^k \bigl( f(x^{(0)}) − f^{\star} \bigr)$$

Bây giờ xét bài toán có ràng buộc trên đa diện:
> $$\min_x f(x) \: \text{ subject to } x \in \text{conv}(A) \subseteq \mathbb{R}^n$$

### [Định lý (Lacoste-Julien & Jaggi 2013)]

Giả sử $$f$$ là $$\mu$$-lồi mạnh, $$\nabla f$$ là $$L$$-Lipschitz và tập nguyên tử $$A \subseteq \mathbb{R}^n$$ hữu hạn. Với kích thước bước $$\gamma_k$$ phù hợp, thuật toán gradient có điều kiện kết hợp bước rời xa thỏa mãn:
> $$f(x^{(k)}) − f^{\star} \leq (1 − r)^{k/2}(f(x^{(0)}) − f^{\star}), \qquad r = \frac{\mu}{L}\cdot\frac{\Phi(A)^2}{4\,\text{diam}(A)^2}$$
> $$\text{trong đó } \Phi(A) = \min_{F \in \text{faces}(\text{conv}(A))} \text{dist}(F, \text{conv}(A \setminus F))$$

Nếu đa diện có hình dạng dẹt (phẳng), hằng số hình học $$\Phi(A)$$ nhỏ và tốc độ hội tụ sẽ chậm lại.

## Bám theo đường nghiệm (Path following)

Xét họ bài toán ràng buộc theo chuẩn với tham số bán kính $$t \geq 0$$:
> $$\min_x f(x) \: \text{ subject to } \| x \| \leq t$$

Thuật toán Frank-Wolfe có thể dùng cho bài toán **bám theo đường nghiệm (path following)**, tức sinh ra một đường nghiệm xấp xỉ $$\hat{x}(t)$$ với mọi $$t \geq 0$$.

Khởi tạo $$t_0 = 0$$ và $$x^{\star}(0) = 0$$, cố định các tham số $$\epsilon > 0$$ và $$m > 1$$, sau đó lặp với $$k=1,2,3,\ldots$$:

* Tính $$t_k = t_{k−1} + \frac{(1 − 1/m)\epsilon}{\| \nabla f(\hat{x}(t_{k−1}))\|_{∗}}$$ và giữ nguyên $$\hat{x}(t) = \hat{x}(t_{k−1})$$ cho mọi $$t \in (t_{k−1}, t_k)$$.
* Tại $$t = t_k$$, chạy Frank-Wolfe để tìm $$\hat{x}(t_k)$$ và dừng khi khoảng cách đối ngẫu $$\leq \frac{\epsilon}{m}$$.

Chiến lược này giúp đơn giản hóa đáng kể các thuật toán bám đường nghiệm trước đó [Giesen et al. (2012)], đồng thời đảm bảo với mọi giá trị $$t$$ trên đường đi:
> $$f(\hat{x}(t)) − f(x^{\star}(t)) \leq \epsilon$$

tức sai số tối ưu bị chặn đều bởi $$\epsilon$$ trên toàn bộ đường nghiệm.

Cơ sở của đảm bảo này nằm ở dạng tuyến tính theo $$t$$ của khoảng cách đối ngẫu Frank-Wolfe:
> $$g_t(x) = \max_{\|s\|\leq t} \nabla f(x)^T(x − s) = \nabla f(x)^Tx + t\|\nabla f(x)\|_{∗}$$

Do đó, nếu tại $$t$$ ta có $$g_t(x) \leq \frac{\epsilon}{m}$$, thì khi tăng bán kính lên $$t^+ = t + (1 − 1/m)\epsilon/\|\nabla f(x)\|_{∗}$$, ta thu được:

> $$g_{t^+}(x) = \nabla f(x)^Tx + t\|\nabla f(x)\|_{∗} + \epsilon − \epsilon/m \leq \epsilon$$

Điều này chứng tỏ khoảng cách đối ngẫu luôn được duy trì $$\leq \epsilon$$ trên toàn đoạn từ $$t$$ đến $$t^+$$ ngay cả khi giữ nguyên nghiệm $$x$$.
