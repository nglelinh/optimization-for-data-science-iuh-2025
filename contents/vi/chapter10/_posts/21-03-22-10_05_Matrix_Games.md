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

Trong bài này, chúng ta xét các chiến lược hỗn hợp (mixed strategy) của trò chơi ma trận, một ví dụ về LP gốc và LP đối ngẫu trong lý thuyết trò chơi. Thiết lập gồm hai người chơi, J và R, và một ma trận chi trả $$P$$.

## Thiết lập trò chơi

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter10/matrix_game.png" alt="Thiết lập trò chơi" width="70%">
  <figcaption style="text-align: center;">[Hình 1] Thiết lập trò chơi [3]</figcaption>
</p>
</figure>

Ma trận chi trả là số tiền thưởng mà J phải trả cho R khi J chọn chiến lược $$i$$ (hàng) và R chọn chiến lược $$j$$ (cột) ($$P_{ij}$$). Nếu giá trị này dương, J trả cho R một khoản bằng độ lớn của phần tử tương ứng; nếu âm, R trả cho J một khoản bằng độ lớn đó.

Thiết lập này còn gọi là trò chơi tổng bằng không (zero-sum): nếu phần thưởng R nhận được (hoặc phải trả) là $$r_{R}$$ và phần thưởng của J là $$r_{J}$$, thì trong mỗi ván $$r_{R} = - r_{J}$$, và tổng hai phần thưởng luôn bằng 0.

Ngoài ra, ta giả sử cả hai người chơi đều dùng chiến lược hỗn hợp. Chiến lược hỗn hợp là giả định rằng lựa chọn của mỗi người chơi tuân theo một phân phối xác suất nhất định (hay được lấy mẫu từ một phân phối xác suất nhất định).

>$$
>\begin{align}
>x : P(\text{J chooses i}) = x_{i}, \qquad i=1,...m\\\\
>y : P(\text{R chooses j}) = y_{j}, \qquad j=1,...n.\\\\
>\end{align}
>$$

Nếu mỗi người chơi biết chiến lược hỗn hợp (tức phân phối xác suất) của đối phương, họ có thể tính khoản chi trả mà mình kỳ vọng nhận được, tức chi trả kỳ vọng (expected payout).

>$$
>\begin{align}
>\sum_{i=1}^{m}\sum_{j=1}^{n}x_{i}y_{j}P_{ij} = x^{T}Py.\\\\
>\end{align}
>$$

Vì dấu của ma trận chi trả được định nghĩa là số tiền J trả cho R, J sẽ cố gắng cực tiểu hóa chi trả kỳ vọng này vì J muốn trả cho R càng ít càng tốt, còn R sẽ cố gắng cực đại hóa chi trả kỳ vọng này vì R muốn nhận từ J càng nhiều càng tốt.

Bây giờ, đứng ở vị trí của từng người chơi, mỗi người xét chiến lược hỗn hợp của đối phương để cực đại hóa (R) hoặc cực tiểu hóa (J) chi trả kỳ vọng này. Với giả định hai bên đều hành động tối ưu đối với nhau, ta sẽ tìm chiến lược tối ưu suy ra từ hai góc nhìn, và cuối cùng xác nhận rằng theo định lý minimax của Von Neumann, hai kết quả này bằng nhau.

## Cực tiểu hóa chi trả kỳ vọng: góc nhìn của J
Trước hết, giả sử R biết chiến lược $$x$$ của J. R sẽ muốn cực đại hóa chi trả kỳ vọng $$x^{T}Py$$.

>$$
>\begin{align}
>\max\{x^{T}Py : y\geq0, 1^{T}y = 1\} = \max_{j=1,...,n}(P^{T}x)_{j}.\\\\
>\end{align}
>$$

Khi đó, như công thức cho thấy, R tìm chỉ số $$j$$ ứng với giá trị lớn nhất trong các $$(P^{T}x)_{j}$$; chiến lược đặt $$y_{j} = 1$$ cho chỉ số đó và bằng 0 cho các chỉ số còn lại chính là chiến lược cực đại hóa chi trả kỳ vọng của R.

Khi biết R hành động tối ưu như trên, chiến lược tối ưu của J là phân phối $$x$$ thỏa mãn bài toán sau.

>$$
>\begin{align}
>& \min_{x}
>& &\max_{j=1,...,n} (P^{T}x)_{j}\\\\
>& \text{thỏa mãn}
>& & x\geq 0, 1^{T}x =1.\\\\
>\end{align}
>$$

Cực đại (theo từng điểm) của các hàm lồi cũng là một hàm lồi. Ta gọi đây là bài toán của góc nhìn thứ nhất, và gọi nghiệm của bài toán tối ưu này là chi trả kỳ vọng tối ưu $$f^{*}_{1}$$. Một điểm cần lưu ý nữa là giả định tất cả người chơi đều hành động tối ưu là giả định cơ bản trong cách hình thức hóa trò chơi dạng đơn giản nhất.

## Cực đại hóa chi trả kỳ vọng: góc nhìn của R
Ở góc nhìn thứ hai, giả sử J biết chiến lược $$y$$ của R. J sẽ muốn cực tiểu hóa chi trả kỳ vọng.

>$$
>\begin{align}
>\min \{x^{T}Py : x\geq0, 1^{T}x = 1\} = \min_{i=1,...,m}(Py)_{i}.\\\\
>\end{align}
>$$

Theo lập luận tương tự, khi biết J hành động tối ưu như trên, chiến lược tối ưu của R là phân phối $$y$$ thỏa mãn bài toán sau.

>$$
>\begin{align}
>& \max_{y}  
>& & \min_{i=1,...,m} (Py)_{i}\\\\
>&\text{thỏa mãn}
>& &y\geq 0, 1^{T}y =1.\\\\
>\end{align}
>$$

Tương tự, ta gọi đây là bài toán của góc nhìn thứ hai và gọi nghiệm của nó là $$f^{*}_{2}$$. Vì người chơi R muốn cực đại hóa chi trả kỳ vọng, nên dễ dự đoán rằng chi trả kỳ vọng $$f^{*}_{1}$$ của góc nhìn thứ nhất (R biết trước chiến lược của J) sẽ lớn hơn hoặc bằng chi trả của góc nhìn thứ hai. ($$f^{*}_{1}\geq f^{*}_{2}$$)
  
## Định lý minimax của Von Neumann
Tuy nhiên, theo định lý minimax của Von Neumann thì $$f^{*}_{1} = f^{*}_{2}$$. Định lý minimax phát biểu như sau.
  
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

## Chứng minh hai góc nhìn là cặp bài toán gốc - đối ngẫu
Bây giờ ta sẽ chỉ ra rằng chi trả kỳ vọng của hai góc nhìn trên, xét như các bài toán LP, là cặp bài toán gốc - đối ngẫu của nhau, và nhờ định lý minimax của Von Neumann hai kết quả bằng nhau nên đối ngẫu mạnh được thỏa mãn.

Trước hết, bài toán của góc nhìn thứ nhất có thể viết lại như sau.

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

Ta đã viết lại bài toán sao cho $$t$$ bằng giá trị lớn nhất trong các thành phần của $$P^{T}x$$.

Bây giờ, áp dụng cách thứ hai của đối ngẫu đã học là lập hàm Lagrange và tìm hàm đối ngẫu Lagrange $$g$$, ta được

>$$
>\begin{align}
>&L(x, t, u, v, y) &&= t-u^{T}x+v(1-1^{T}x)+y^{T}(P^{T}x-t1)\\\\
>&g(u, v, y) &&= \min_{x,t} \quad L(x, t, u, v, y)\\\\
>&&&= \begin{cases} v \qquad &\text{if } 1-1^{T}y = 0, Py-u-v1=0\\\\
-\infty \qquad &\text{trường hợp khác.} \end{cases}
>\end{align}
>$$

Vì $$u$$ là biến bù (slack variable), loại bỏ nó và sắp xếp lại ta được:

>$$
>\begin{align}
>&\max_{y,v} \qquad \quad && v\\\\
>&\text{thỏa mãn }\quad && y\geq0, 1^{T}y = 1\\\\
>&&& Py\geq v.
>\end{align}
>$$

Đây chính là bài LP gốc của góc nhìn thứ hai. Do đó hai góc nhìn có quan hệ đối ngẫu và giá trị tối ưu của hai bài toán bằng nhau, nên đối ngẫu mạnh được thỏa mãn.

Nói chung với bài toán LP (sẽ được đề cập ở các phần sau), chỉ cần một trong hai bài toán gốc hoặc đối ngẫu khả thi thì đối ngẫu mạnh đã thỏa mãn.

### Trò chơi ma trận trong 18 giây

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/matrix-game_vi.mp4"></video>
</div>

J cực tiểu hóa đường cao nhất, R cực đại hóa đường thấp nhất, và cả hai đạt cùng một giá trị: định lý minimax, chính là đối ngẫu LP.

### Tự tay thử: trò chơi nhìn từ hai phía

<div class="opx-explainer" data-opx="mgame" data-lang="vi"></div>
