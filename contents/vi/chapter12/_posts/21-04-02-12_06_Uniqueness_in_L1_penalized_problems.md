---
layout: post
title: 12-06 Tính duy nhất trong các bài toán phạt L1
chapter: '12'
order: 7
owner: Wontak Ryu
categories:
- chapter12
lang: vi
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

Bài toán hồi quy tuyến tính có phạt $$L1$$ sau đây cũng được biết đến rộng rãi như bài toán lasso.

>$$
>\begin{align}
>&&&\hat{\beta} \in \text{argmin}_{\beta \in \mathbb{R}^p} \frac{1}{2} \| y - X\beta \|^2_2 + \lambda \|\beta\|_1, \qquad \\\\
>&& \text{ --- (1) } &\text{cho trước } y \in \mathbb{R}^n, \\\\
>&&& \text{ một ma trận } X \in \mathbb{R}^{n \text{ x } p} \ \text{ của các biến dự đoán,} \\\\
>&&& \text{và tham số điều chỉnh} \lambda \ge 0.
>\end{align}
>$$

Bài toán Lasso ở trên có một nghiệm duy nhất khi nó là lồi chặt chẽ, tức là, khi $$rank(X) = p$$. Mặt khác, khi $$rank(X) < p$$ (khi nó không lồi chặt chẽ), nó có thể có vô số nghiệm (Tham khảo: [Hệ thống thiếu xác định](https://en.wikipedia.org/wiki/Underdetermined_system)). - Lưu ý rằng nếu số biến (p) lớn hơn số quan sát (n), thì $$rank(X)$$ nhất thiết nhỏ hơn p.<br/>
Thú vị là, trong một số trường hợp đặc biệt, bài toán Lasso được đảm bảo có một nghiệm duy nhất bất kể chiều của $$X$$ [13].

>**Định lý:** Khi hàm $$f$$ khả vi và lồi chặt chẽ, $$\lambda > 0$$, và $$X \in \mathbb{R}^{n \times p}$$ tuân theo một phân phối xác suất liên tục nào đó trên $$\mathbb{R}^{np}$$, bài toán tối ưu hóa sau luôn có một nghiệm duy nhất. Hơn nữa, nghiệm bao gồm nhiều nhất $$min\{n,p\}$$ thành phần khác không. Không có hạn chế nào về chiều của $$X$$. (Tức là, nó hợp lệ ngay cả khi p >> n)

## Các sự thật cơ bản và các điều kiện KKT

> **Bổ đề 1.** Đối với $$y, X, \lambda \ge 0$$ tùy ý, bài toán lasso (1) có các tính chất sau.
> 
> 1. Nó có hoặc một nghiệm duy nhất hoặc vô số nghiệm.
> 2. Tất cả các nghiệm lasso $$\hat{\beta}$$ có cùng giá trị $$X\hat{\beta}$$.
>3. Khi $$\lambda > 0$$, tất cả các nghiệm lasso $$\hat{\beta}$$ có cùng chuẩn $$l_1$$ ($$\|\hat{\beta}\|_1$$).

$$\text{ }$$

> **Chứng minh.**<br/>
> 1. Nếu (1) có hai nghiệm $$\hat{\beta}^{(1)}$$, $$\hat{\beta}^{(2)}$$, thì với bất kỳ $$0 < \alpha < 1$$, $$\alpha \hat{\beta}^{(1)} + (1 - \alpha) \hat{\beta}^{(2)}$$ cũng là một nghiệm, vì vậy tồn tại vô số nghiệm.<br/>
> 2. & 3. Giả sử có hai nghiệm $$\hat{\beta}^{(1)}$$, $$\hat{\beta}^{(2)}$$. Gọi giá trị tối ưu là $$c^\star$$. Khi đó với bất kỳ nghiệm $$\alpha \hat{\beta}^{(1)} + (1 - \alpha) \hat{\beta}^{(2)}$$ ($$0 < \alpha < 1$$), đẳng thức sau phải luôn được giữ.
> 
> $$
>\begin{align}
> &\frac{1}{2} \| y - X(\alpha \hat{\beta}^{(1)} + (1 - \alpha) \hat{\beta}^{(2)}) \|_2^2 + \lambda \| \alpha \hat{\beta}^{(1)} + (1 - \alpha) \hat{\beta}^{(2)} \|_1 \\
> & = \alpha c^\star + (1-\alpha) c^\star = c^\star
>\end{align}
>$$
>
> Để thỏa mãn đẳng thức này, $$X\hat{\beta}$$ phải luôn có cùng giá trị cho bất kỳ nghiệm $$\hat{\beta}$$, và khi $$\lambda > 0$$, $$\|\hat{\beta}\|_1$$ cũng phải luôn giống nhau.


Trở lại ban đầu, các điều kiện KKT cho bài toán lasso (1) như sau.
>$$
>\begin{align}
>&&X^T (y - X\hat{\beta}) = \lambda \gamma, \qquad \text{ --- (2)} \\\\
>&&\gamma_i \in 
> \begin{cases}
> \{ sign(\hat{\beta_i}) \} & \text{nếu } \hat{\beta_i} \neq 0 \\\\
> [-1, 1] & \text{nếu } \hat{\beta_i} = 0,
> \end{cases} \\\\
> &&\text{với } i = 1, \dots, p. \text{ --- (3)} \\\\
> &&\text{Ở đây } \gamma \in \mathbb{R}^p \text{ được gọi là subgradient của hàm } \\
> &&f(x) = \| x \|_1 \text{ được đánh giá tại } x = \hat{\beta}.
>\end{align}
>$$

Tức là, nghiệm $$\hat{\beta}$$ của (1) thỏa mãn (2) và (3) cho một $$\gamma$$ nào đó. 

Hãy dùng các điều kiện KKT thu được ở trên để biến đổi điều kiện cho nghiệm lasso về dạng tường minh hơn. Trong phần tiếp theo, để việc suy diễn gọn hơn, ta giả sử $$\lambda > 0$$. Trước hết, định nghĩa tập equicorrelation $$\mathcal{E}$$ như sau. $$\mathcal{E}$$ là tập chứa mọi chỉ số $$i$$ có $$\hat{\beta}_i \neq 0$$ và mọi chỉ số $$j$$ có $$\hat{\beta}_j = 0$$ nhưng $$\vert\gamma_j\vert = 1$$.

$$
\mathcal{E} = \{ i \in \{1, \dots, p \}  : \vert X_i^T (y - X\hat{\beta}) \vert = \lambda \}. \qquad \text{ --- (4)}
$$

Tiếp theo, định nghĩa dấu equicorrelation $$s$$ như sau. Ở đây $$X_\mathcal{E}$$ là ma trận gồm các cột $$i \in \mathcal{E}$$ của $$X$$.

$$
s = sign(X^T_\mathcal{E} (y -X\hat{\beta})). \qquad \text{ --- (5)}
$$

$$\mathcal{E}, s$$ có thể biểu diễn qua $$\gamma$$ như sau: $$\mathcal{E} = \{i \in \{1, \dots, p \} : \vert \gamma_i \vert = 1 \}$$ và $$s = \gamma_{\mathcal{E}}$$. Hơn nữa, theo Bổ đề 1 (mục 2), $$X\hat{\beta}$$ có giá trị duy nhất, nên $$\mathcal{E}$$ và $$s$$ cũng duy nhất.

Theo định nghĩa của subgradient $$\gamma$$ trong (3), với mọi nghiệm lasso $$\hat{\beta}$$ ta có $$\hat{\beta}_{-\mathcal{E}} = 0$$. Do đó, viết (2) cho khối $$\mathcal{E}$$ ta được:

$$
X^T_\mathcal{E} ( y - X_\mathcal{E} \hat{\beta_\mathcal{E}} ) = \lambda \gamma_\mathcal{E}=  \lambda s. \qquad \text{ --- (6)}
$$

Nhân hai vế của (6) với $$(X^T_\mathcal{E})^+$$ (giả nghịch đảo của $$X^T_\mathcal{E}$$), và dùng $$(X^T_\mathcal{E})^+ X^T_\mathcal{E} = X_\mathcal{E} X_\mathcal{E}^+$$ (phép chiếu lên không gian cột của $$X_\mathcal{E}$$) ta được:

$$
\begin{align}
& X_\mathcal{E} X_\mathcal{E}^+ X_\mathcal{E} \hat{\beta_\mathcal{E}} = X_\mathcal{E} X_\mathcal{E}^+ ( y - (X^T_\mathcal{E})^+  \lambda s) \\\\
\Leftrightarrow
& X_\mathcal{E} \hat{\beta_\mathcal{E}} = X_\mathcal{E} X_\mathcal{E}^+ ( y - (X^T_\mathcal{E})^+  \lambda s).
\end{align}
$$

Vì $$X\hat{\beta} = X_\mathcal{E} \hat{\beta_\mathcal{E}}$$ nên đẳng thức trên chính là

$$
X \hat{\beta} = X_\mathcal{E} X_\mathcal{E}^+ ( y - (X^T_\mathcal{E})^+  \lambda s), \qquad \text{ --- (7)}
$$

và mọi nghiệm lasso $$\hat{\beta}$$ có dạng

$$
\begin{align}
& \hat{\beta_{-\mathcal{E}}} = 0 \text{ và } \hat{\beta_{\mathcal{E}}} = X_\mathcal{E}^+ ( y - (X^T_\mathcal{E})^+ \lambda s) + b, \qquad \text{ --- (8)} \\\\
& \text{với } b \in null(X_\mathcal{E}).
\end{align}
$$

## Điều kiện đủ cho tính duy nhất

Để $$\hat{\beta_{\mathcal{E}}}$$ trong (8) là duy nhất thì phải có $$b=0$$ (vì $$X_\mathcal{E}^+ ( y - (X^T_\mathcal{E})^+ \lambda s)$$ là duy nhất). Từ yêu cầu $$b=0$$ và đẳng thức (8), ta thu được kết luận sau.

>**Bổ đề 2.** Với mọi $$y, X, \lambda > 0$$, nếu $$null(X_\mathcal{E}) = \{0\}$$, hay $$rank(X_\mathcal{E}) = \vert\mathcal{E}\vert$$ ([tham khảo](https://www.quora.com/When-the-null-space-of-a-matrix-is-the-zero-vector-the-matrix-is-invertible-Why/answer/Alexander-Farrugia)), thì nghiệm lasso là duy nhất, và tương đương với

>$$
>\begin{align}
>&& \hat{\beta_{-\mathcal{E}}} = 0 \text{ và } \hat{\beta_{\mathcal{E}}} = (X^T_\mathcal{E}X_\mathcal{E})^{-1} ( X^T_\mathcal{E} y - \lambda s), \qquad \text{ --- (9)} \\\\
>&& \text{trong đó } \mathcal{E} \text{ và } s \text{ là tập equicorrelation và các dấu được định nghĩa trong (4) và (5)}.
>\end{align}
>$$

Lưu ý rằng nghiệm này có nhiều nhất $$min\{n, p\}$$ thành phần khác không.

Bây giờ ta tìm một điều kiện tự nhiên hơn (đối với $$X$$) suy ra $$null(X_\mathcal{E}) = \{0\}$$. Trước hết, giả sử $$null(X_\mathcal{E}) \neq \{0\}$$. Khi đó, với một $$i \in \mathcal{E}$$ nào đó ta có đẳng thức

$$
X_i = \sum_{j \in \mathcal{E} \backslash \{i\} } c_j X_j,\\\\
\text{với } c_j \in \mathbb{R}, j \in \mathcal{E}.
$$

Nhân hai vế với $$s_i$$, và nhân vế phải với $$s_j s_j = 1$$:

$$
s_i X_i = \sum_{j \in \mathcal{E} \backslash \{i\} } (s_i s_j c_j) \cdot (s_j X_j). \qquad \text{ --- (10)}
$$

Định nghĩa phần dư lasso $$r = y - X \hat{\beta}$$; khi đó với mọi $$j \in \mathcal{E}$$ ta có $$X_j^T r = s_j \lambda$$. Nhân $$r$$ vào hai vế của (10) ta được đẳng thức theo $$\lambda$$ (giả sử $$\lambda > 0$$):

$$
\lambda = \sum_{j \in \mathcal{E} \backslash \{i\} } (s_i s_j c_j) \lambda \quad \text{ và } \quad \sum_{j \in \mathcal{E} \backslash \{i\} } (s_i s_j c_j) = 1.
$$

Tức là, nếu $$null(X_\mathcal{E}) \neq \{0\}$$ thì với một $$i \in \mathcal{E}$$ nào đó đẳng thức sau đúng:

$$
s_iX_i = \sum_{j \in \mathcal{E} \backslash \{i\} } a_j \cdot s_j X_j, \text{ với } \sum_{j \in \mathcal{E} \backslash \{i\} } a_j = 1.
$$

Đẳng thức này có nghĩa là $$s_iX_i$$ nằm trong bao affine của các $$s_j X_j, j \in \mathcal{E} \backslash \{i\}$$. Điều này cũng có nghĩa là một tập con gồm $$k+2$$ phần tử như vậy chỉ có thể sinh ra không gian affine có số chiều tối đa là $$k$$.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter12/l1_uniqueness.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 1] 4 phần tử trong không gian affine 2 chiều [3]</figcaption>
</p>
</figure>

Điều ta muốn là ma trận $$X \in \mathbb{R}^{n \text{ x } p}$$ thỏa mãn $$null(X_\mathcal{E}) = \{0\}$$; điều này tương đương với việc các cột của $$X$$ ở [vị trí tổng quát (general position)](https://en.wikipedia.org/wiki/General_position). Nói cách khác, không có không gian con affine $$k$$ chiều nào chứa nhiều hơn $$k+1$$ phần tử của tập.

>**Bổ đề 3.** Nếu các cột của ma trận $$X$$ ở vị trí tổng quát thì với mọi $$y$$ và $$\lambda > 0$$, nghiệm lasso là duy nhất và nghiệm này thỏa mãn (9).

Vậy những ma trận $$X$$ nào luôn thỏa mãn điều kiện trên? Kết luận như sau.

>**Bổ đề 4.** Nếu mọi phần tử của ma trận $$X \in \mathbb{R}^{n \text{ x } p}$$ tuân theo một phân phối xác suất liên tục trên $$\mathbb{R}^{np}$$ thì với mọi $$y$$ và $$\lambda > 0$$, nghiệm lasso là duy nhất và luôn thỏa mãn (9).

Lý do là khi tuân theo phân phối xác suất liên tục, các vector cột (với xác suất 1) ở vị trí tổng quát, nên các tập con cột liên quan độc lập tuyến tính. ([tham khảo](https://math.stackexchange.com/questions/432447/probability-that-n-vectors-drawn-randomly-from-mathbbrn-are-linearly-ind?rq=1))

## Hàm mất mát lồi tổng quát

Điều tương tự cũng áp dụng cho bài toán lasso tổng quát hơn [13].

$$
\hat{\beta} \in \text{argmin}_{\beta \in \mathbb{R}^p} f(X\beta) + \lambda \|\beta\|_1, \qquad \text{ --- (11) }
$$

>**Bổ đề 5.** Nếu mọi phần tử của ma trận $$X \in \mathbb{R}^{n \text{ x } p}$$ tuân theo một phân phối xác suất liên tục trên $$\mathbb{R}^{np}$$, thì với mọi hàm khả vi và lồi chặt $$f$$ và mọi $$\lambda > 0$$, bài toán (11) luôn có nghiệm duy nhất. Nghiệm này có nhiều nhất $$min\{n,p\}$$ thành phần khác không.
