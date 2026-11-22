---
layout: post
title: 10-05 Trò chơi ma trận
chapter: '10'
order: 6
owner: Wontak Ryu
categories:
- chapter10
lang: vi
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

Trong bài này, chúng ta xét bài toán chiến lược hỗn hợp (mixed strategy) trong trò chơi ma trận — một ví dụ tiêu biểu về cặp bài toán LP gốc và đối ngẫu trong lý thuyết trò chơi. Xét trò chơi gồm hai người chơi $$J$$ và $$R$$ cùng một ma trận chi trả $$P$$.

## Thiết lập trò chơi

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter10/matrix_game.png" alt="Thiết lập trò chơi" width="70%">
  <figcaption style="text-align: center;">[Hình 1] Thiết lập trò chơi [3]</figcaption>
</p>
</figure>

Phần tử $$P_{ij}$$ của ma trận chi trả biểu thị số tiền mà $$J$$ phải trả cho $$R$$ khi $$J$$ chọn chiến lược $$i$$ (hàng) và $$R$$ chọn chiến lược $$j$$ (cột). Nếu $$P_{ij} > 0$$, $$J$$ trả cho $$R$$ một khoản bằng $$P_{ij}$$; nếu $$P_{ij} < 0$$, $$R$$ trả cho $$J$$ một khoản bằng $$|P_{ij}|$$.

Đây là trò chơi tổng bằng không (zero-sum): gọi phần thưởng của $$R$$ là $$r_R$$ và của $$J$$ là $$r_J$$, thì ở mọi ván đấu ta luôn có $$r_R = -r_J$$, tức tổng phần thưởng của hai người chơi bằng $$0$$.

Giả sử cả hai người chơi đều sử dụng chiến lược hỗn hợp, nghĩa là lựa chọn của mỗi người được rút ngẫu nhiên theo một phân phối xác suất:

>$$
>\begin{align}
>x : P(\text{J chooses i}) = x_{i}, \qquad i=1,...m\\\\
>y : P(\text{R chooses j}) = y_{j}, \qquad j=1,...n.\\\\
>\end{align}
>$$

Khi biết phân phối xác suất của đối phương, mỗi người chơi có thể tính được chi trả kỳ vọng (expected payout):

>$$
>\begin{align}
>\sum_{i=1}^{m}\sum_{j=1}^{n}x_{i}y_{j}P_{ij} = x^{T}Py.\\\\
>\end{align}
>$$

Vì $$P_{ij}$$ là khoản tiền $$J$$ trả cho $$R$$, nên $$J$$ muốn cực tiểu hóa chi trả kỳ vọng, còn $$R$$ muốn cực đại hóa chi trả kỳ vọng.

Bây giờ, ta xét bài toán từ góc nhìn của từng người chơi với giả định cả hai đều hành động tối ưu. Ta sẽ lập bài toán tối ưu cho từng phía, rồi chỉ ra rằng theo định lý minimax của von Neumann, hai giá trị tối ưu thu được bằng nhau.

## Cực tiểu hóa chi trả kỳ vọng: góc nhìn của J

Trước hết, giả sử $$R$$ biết trước chiến lược $$x$$ của $$J$$. Khi đó $$R$$ sẽ chọn $$y$$ để cực đại hóa chi trả kỳ vọng $$x^T P y$$:

>$$
>\begin{align}
>\max\{x^{T}Py : y\geq0, 1^{T}y = 1\} = \max_{j=1,...,n}(P^{T}x)_{j}.\\\\
>\end{align}
>$$

Theo biểu thức trên, chiến lược tối ưu của $$R$$ là chọn chỉ số $$j$$ làm cực đại $$(P^T x)_j$$ (tức đặt $$y_j = 1$$ tại chỉ số đó và bằng $$0$$ ở các chỉ số còn lại).

Biết rằng $$R$$ sẽ phản ứng tối ưu như vậy, $$J$$ chọn phân phối $$x$$ nhằm giải bài toán:

>$$
>\begin{align}
>& \min_{x}
>& &\max_{j=1,...,n} (P^{T}x)_{j}\\\\
>& \text{thỏa mãn}
>& & x\geq 0, 1^{T}x =1.\\\\
>\end{align}
>$$

Vì cực đại theo từng điểm của các hàm tuyến tính là một hàm lồi, đây là một bài toán tối ưu lồi. Ta gọi giá trị tối ưu của bài toán này là $$f_1^*$$. Lưu ý rằng giả định mọi người chơi đều hành động tối ưu là giả định cơ bản của mô hình trò chơi hai người tổng bằng không.

## Cực đại hóa chi trả kỳ vọng: góc nhìn của R

Ngược lại, giả sử $$J$$ biết trước chiến lược $$y$$ của $$R$$. Khi đó $$J$$ sẽ chọn $$x$$ để cực tiểu hóa chi trả kỳ vọng:

>$$
>\begin{align}
>\min \{x^{T}Py : x\geq0, 1^{T}x = 1\} = \min_{i=1,...,m}(Py)_{i}.\\\\
>\end{align}
>$$

Biết rằng $$J$$ sẽ phản ứng tối ưu như vậy, $$R$$ chọn phân phối $$y$$ để giải bài toán:

>$$
>\begin{align}
>& \max_{y}  
>& & \min_{i=1,...,m} (Py)_{i}\\\\
>&\text{thỏa mãn}
>& &y\geq 0, 1^{T}y =1.\\\\
>\end{align}
>$$

Gọi giá trị tối ưu của bài toán này là $$f_2^*$$. Vì ở góc nhìn thứ nhất $$R$$ có lợi thế biết trước chiến lược của $$J$$, ta dễ thấy $$f_1^* \geq f_2^*$$.

## Định lý minimax của von Neumann

Theo định lý minimax của von Neumann, dấu bằng thực sự xảy ra: $$f_1^* = f_2^*$$. Định lý được phát biểu như sau:

>$$
>\begin{align}
>&\text{Cho } X\subset \mathbb{R}^{m} \text{ và }Y\subset \mathbb{R}^{n} \text{ là các tập lồi compact. }\\\\
> &\text{Nếu } f:X\times Y\rightarrow \mathbb{R} \text{ là hàm liên tục lồi-lõm, tức là}\\\\
> &\qquad f(\cdot, y): X\rightarrow\mathbb{R} \text{ lồi với } y \text{ cố định, và}\\\\
> &\qquad f(x, \cdot): Y\rightarrow\mathbb{R} \text{ lõm với } x \text{ cố định.}\\\\
> &\text{Khi đó ta có} \\\\ 
>&\min_{x\in X} \max_{y\in Y} f(x,y) = \max_{y\in Y} \min_{x\in X} f(x,y).\\\\
>\end{align}
>$$

Phần chứng minh định lý này được lược bỏ.

## Chứng minh hai góc nhìn tạo thành cặp bài toán gốc – đối ngẫu

Ta sẽ chứng minh hai bài toán trên là cặp bài toán LP gốc – đối ngẫu của nhau; khi kết hợp với định lý minimax của von Neumann ($$f_1^* = f_2^*$$), điều này cho thấy tính đối ngẫu mạnh được thỏa mãn.

Trước hết, viết lại bài toán từ góc nhìn của $$J$$ dưới dạng LP bằng cách đưa thêm biến phụ $$t$$ biểu thị giá trị lớn nhất của các thành phần trong $$P^T x$$:

>$$
>\begin{align}
>& \min_{x} \max_{j=1,...,n} 
>& &(P^{T}x)_{j}\\\\
>&\text{thỏa mãn } 
>& &x\geq 0, 1^{T}x = 1\\\\
>\end{align}
>$$
>
>$$
>\begin{align}
>\Leftrightarrow{} \\\\
>& \min_{x,t}
>& & t \\\\
>&\text{thỏa mãn } 
>& &x\geq0, 1^{T}x = 1, P^{T}x \preceq t. \\\\
>\end{align}
>$$

Áp dụng phương pháp Lagrangian đã học ở bài 10-04 để lập hàm Lagrange và hàm đối ngẫu $$g(u, v, y)$$ (với $$u \geq 0, y \geq 0$$):

>$$
>\begin{align}
>&L(x, t, u, v, y) &&= t-u^{T}x+v(1-1^{T}x)+y^{T}(P^{T}x-t1)\\\\
>&g(u, v, y) &&= \min_{x,t} \quad L(x, t, u, v, y)\\\\
>&&&= \begin{cases} v \qquad &\text{if } 1-1^{T}y = 0, Py-u-v1=0\\\\
-\infty \qquad &\text{trường hợp khác.} \end{cases}
>\end{align}
>$$

Khử biến bù $$u \geq 0$$ từ điều kiện $$Py - u - v\mathbf{1} = 0$$ (tức $$Py \geq v\mathbf{1}$$), ta thu được bài toán đối ngẫu:

>$$
>\begin{align}
>&\max_{y,v} \qquad \quad && v\\\\
>&\text{thỏa mãn }\quad && y\geq0, 1^{T}y = 1\\\\
>&&& Py\geq v.
>\end{align}
>$$

Đây chính là dạng LP tương đương với bài toán từ góc nhìn của $$R$$. Như vậy, hai góc nhìn của trò chơi ma trận tạo thành một cặp bài toán gốc – đối ngẫu và có cùng giá trị tối ưu (đối ngẫu mạnh).

Tổng quát đối với quy hoạch tuyến tính (sẽ được trình bày kỹ hơn ở Chương 11), chỉ cần bài toán gốc hoặc bài toán đối ngẫu khả thi thì tính đối ngẫu mạnh luôn được bảo đảm.

### Trò chơi ma trận trong 18 giây

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/matrix-game_vi.mp4"></video>
</div>

$$J$$ cực tiểu hóa đường cao nhất, $$R$$ cực đại hóa đường thấp nhất, và cả hai đạt cùng một giá trị: định lý minimax chính là đối ngẫu LP.

### Tự tay thử: trò chơi nhìn từ hai phía

<div class="opx-explainer" data-opx="mgame" data-lang="vi"></div>
