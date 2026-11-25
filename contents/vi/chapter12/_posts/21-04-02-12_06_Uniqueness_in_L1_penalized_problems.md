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

Trong hồi quy tuyến tính cổ điển với $$p > n$$ (nhiều biến đặc trưng hơn số mẫu quan sát — chuyện thường ngày trong di truyền học hay xử lý ảnh), hệ phương trình bình phương tối thiểu có vô số nghiệm. Người ta thường kỳ vọng khi thêm phạt $$\ell_1$$ (bài toán Lasso), nghiệm $$\hat{\beta}$$ sẽ trở nên duy nhất. Nhưng thực tế thú vị hơn thế nhiều: **ngay cả khi $$\lambda > 0$$, Lasso vẫn có thể có vô số nghiệm $$\hat{\beta}$$ khác nhau!**

Tuy nhiên, một định lý tuyệt đẹp của Ryan Tibshirani (2013) chứng minh bằng **điều kiện KKT của Lasso** cho thấy điều kỳ diệu sau: dù có nhiều vector trọng số $$\hat{\beta}$$ khác nhau, **giá trị dự đoán $$X\hat{\beta}$$ luôn duy nhất tuyệt đối**; mọi nghiệm đều có cùng dấu trên tập biến hoạt động; và chỉ cần các cột của ma trận $$X$$ ở *vị trí tổng quát (general position)* (điều xảy ra với xác suất 1 khi dữ liệu rút từ phân phối liên tục!), nghiệm Lasso $$\hat{\beta}$$ lập tức **duy nhất** ngay cả khi $$p \gg n$$!

## Kiến thức cần nhớ: Bốn trụ cột của tính duy nhất trong bài toán phạt $$\ell_1$$

- **Hệ điều kiện KKT của Lasso:** Điểm $$\hat{\beta}$$ tối ưu khi và chỉ khi tồn tại vector dấu $$s \in \partial\|\hat{\beta}\|_1$$ sao cho:
  $$X^T(y - X\hat{\beta}) = \lambda s, \quad \text{với } s_j = \operatorname{sign}(\hat{\beta}_j) \text{ nếu } \hat{\beta}_j \ne 0, \text{ và } |s_j| \le 1 \text{ nếu } \hat{\beta}_j = 0.$$
  Chú ý: vế trái là độ tương quan giữa từng đặc trưng $$X_j$$ với phần dư $$y - X\hat{\beta}$$! Tập các biến đạt cực đại tương quan $$|X_j^T(y - X\hat{\beta})| = \lambda$$ gọi là **tập cân bằng (equicorrelation set)** $$\mathcal{E}$$.
- **Tính duy nhất tuyệt đối của giá trị dự đoán $$X\hat{\beta}$$:** Vì hàm $$\frac{1}{2}\|y - u\|_2^2$$ là hàm **lồi chặt** theo vector dự đoán $$u = X\beta$$, mọi nghiệm tối ưu $$\hat{\beta}^{(1)}, \hat{\beta}^{(2)}$$ bắt buộc phải cho cùng một dự đoán $$X\hat{\beta}^{(1)} = X\hat{\beta}^{(2)}$$, và do đó có cùng phần dư và cùng tập cân bằng $$\mathcal{E}$$!
- **Điều kiện đủ cho tính duy nhất của $$\hat{\beta}$$:** Mọi tọa độ ngoài $$\mathcal{E}$$ đều bắt buộc bằng $$0$$ ($$\hat{\beta}_{-\mathcal{E}} = 0$$). Vì vậy nếu ma trận con $$X_{\mathcal{E}}$$ có hạng cột đầy đủ ($$\operatorname{null}(X_{\mathcal{E}}) = \{0\}$$), thì từ $$X_{\mathcal{E}} \hat{\beta}_{\mathcal{E}}^{(1)} = X_{\mathcal{E}} \hat{\beta}_{\mathcal{E}}^{(2)}$$ suy ngay ra $$\hat{\beta}^{(1)} = \hat{\beta}^{(2)}$$!
- **Vị trí tổng quát (General Position) khi $$p > n$$:** Nếu dữ liệu rút từ phân phối xác suất liên tục trên $$\mathbb{R}^{n \times p}$$, các cột của $$X$$ ở vị trí tổng quát với xác suất 1, bảo đảm $$|\mathcal{E}| \le n$$ và $$X_{\mathcal{E}}$$ luôn đủ hạng cột $$\implies$$ Lasso có nghiệm duy nhất với tối đa $$n$$ hệ số khác $$0$$!

### Giải thích: Ví dụ tính tay khi Lasso có vô số nghiệm $$\hat{\beta}$$ nhưng $$X\hat{\beta}$$ vẫn duy nhất

Xét bài toán Lasso với $$n = 1$$ mẫu quan sát $$y = 4$$ và $$p = 2$$ đặc trưng giống hệt nhau (cộng tuyến hoàn hảo, vi phạm vị trí tổng quát!):
$$X = \begin{pmatrix} 1 & 1 \end{pmatrix}, \quad \lambda = 1 \implies \min_{\beta_1, \beta_2} \; \frac{1}{2}(4 - \beta_1 - \beta_2)^2 + |\beta_1| + |\beta_2|.$$

1. **Giải điều kiện KKT của Lasso:**
   Đặt $$u = X\beta = \beta_1 + \beta_2$$. Điều kiện KKT cho cả hai cột giống nhau đòi:
   $$1 \cdot (4 - u) = 1 \cdot s_1 = 1 \cdot s_2, \quad s_1 \in \partial|\beta_1|, \; s_2 \in \partial|\beta_2|.$$
   Nếu $$\beta_1, \beta_2 \ge 0$$ và không đồng thời bằng $$0$$, ta cần $$s_1 = s_2 = 1 \implies 4 - u = 1 \implies u^* = \beta_1^* + \beta_2^* = 3$$!
2. **Quan sát tập nghiệm vô hạn nhưng chung một dự đoán duy nhất:**
   - $$\hat{\beta}^{(1)} = (3, 0)^T \implies X\hat{\beta}^{(1)} = 3$$, hàm mục tiêu $$= \frac{1}{2}(4-3)^2 + 3 = 3.5$$.
   - $$\hat{\beta}^{(2)} = (0, 3)^T \implies X\hat{\beta}^{(2)} = 3$$, hàm mục tiêu $$= \frac{1}{2}(4-3)^2 + 3 = 3.5$$.
   - Mọi tổ hợp lồi $$\hat{\beta}(\theta) = (3\theta,\; 3(1-\theta))^T$$ với $$\theta \in [0, 1]$$ đều là nghiệm tối ưu toàn cục (vô số nghiệm!), vì $$X_{\mathcal{E}} = (1, 1)$$ không đủ hạng cột!
   - Thế nhưng giá trị dự đoán $$X\hat{\beta} = 3$$ và chuẩn $$\|\hat{\beta}\|_1 = 3$$ là **duy nhất tuyệt đối** trên toàn bộ đoạn nghiệm!

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

Bài toán hồi quy tuyến tính có phạt $$L_1$$ dưới đây còn được gọi là bài toán **lasso**:

>$$
>\begin{align}
>&&&\hat{\beta} \in \text{argmin}_{\beta \in \mathbb{R}^p} \frac{1}{2} \| y - X\beta \|^2_2 + \lambda \|\beta\|_1, \qquad \\\\
>&& \text{ --- (1) } &\text{cho trước } y \in \mathbb{R}^n, \\\\
>&&& \text{ ma trận } X \in \mathbb{R}^{n \text{ x } p} \ \text{ của các biến dự báo,} \\\\
>&&& \text{và tham số điều chỉnh } \lambda \ge 0.
>\end{align}
>$$

Bài toán lasso (1) có nghiệm duy nhất khi hàm mục tiêu lồi chặt, tức khi $$\text{rank}(X) = p$$. Ngược lại, khi $$\text{rank}(X) < p$$ (hàm mục tiêu không lồi chặt), bài toán có thể có vô số nghiệm (xem thêm: [Hệ thống thiếu xác định](https://en.wikipedia.org/wiki/Underdetermined_system)). Lưu ý rằng nếu số biến $$p$$ lớn hơn số quan sát $$n$$, thì $$\text{rank}(X)$$ chắc chắn nhỏ hơn $$p$$.<br/>
Tuy nhiên, trong một số điều kiện cụ thể, bài toán lasso vẫn có nghiệm duy nhất bất kể tỷ lệ giữa $$n$$ và $$p$$ [13].

>**Định lý:** Khi hàm $$f$$ khả vi và lồi chặt, $$\lambda > 0$$, và các phần tử của $$X \in \mathbb{R}^{n \times p}$$ tuân theo một phân phối xác suất liên tục trên $$\mathbb{R}^{np}$$, bài toán tối ưu hóa tương ứng luôn có nghiệm duy nhất (với xác suất 1). Hơn nữa, nghiệm này có tối đa $$\min\{n,p\}$$ thành phần khác không, mà không cần ràng buộc gì về kích thước của $$X$$ (kể cả khi $$p \gg n$$).

## Các tính chất cơ bản và điều kiện KKT

> **Bổ đề 1.** Với mọi $$y, X$$ và $$\lambda \ge 0$$, bài toán lasso (1) có các tính chất sau:
> 
> 1. Bài toán chỉ có một nghiệm duy nhất hoặc có vô số nghiệm.
> 2. Mọi nghiệm lasso $$\hat{\beta}$$ đều cho cùng giá trị dự báo $$X\hat{\beta}$$.
> 3. Khi $$\lambda > 0$$, mọi nghiệm lasso $$\hat{\beta}$$ đều có cùng chuẩn $$\ell_1$$ ($$\|\hat{\beta}\|_1$$).

$$\text{ }$$

> **Chứng minh.**<br/>
> 1. Vì (1) là bài toán lồi, nếu tồn tại hai nghiệm phân biệt $$\hat{\beta}^{(1)}$$ và $$\hat{\beta}^{(2)}$$, thì với mọi $$0 < \alpha < 1$$, tổ hợp lồi $$\alpha \hat{\beta}^{(1)} + (1 - \alpha) \hat{\beta}^{(2)}$$ cũng là nghiệm, nên bài toán có vô số nghiệm.<br/>
> 2. & 3. Giả sử $$\hat{\beta}^{(1)}$$ và $$\hat{\beta}^{(2)}$$ là hai nghiệm với cùng giá trị tối ưu $$c^\star$$. Khi đó, với mọi $$0 < \alpha < 1$$, tổ hợp lồi $$\alpha \hat{\beta}^{(1)} + (1 - \alpha) \hat{\beta}^{(2)}$$ cũng đạt giá trị tối ưu $$c^\star$$:
> 
> $$
>\begin{align}
> &\frac{1}{2} \| y - X(\alpha \hat{\beta}^{(1)} + (1 - \alpha) \hat{\beta}^{(2)}) \|_2^2 + \lambda \| \alpha \hat{\beta}^{(1)} + (1 - \alpha) \hat{\beta}^{(2)} \|_1 \\
> & = \alpha c^\star + (1-\alpha) c^\star = c^\star
>\end{align}
>$$
>
> Vì hàm $$u \mapsto \frac{1}{2}\|y - u\|_2^2$$ lồi chặt, đẳng thức trên chỉ xảy ra khi $$X\hat{\beta}^{(1)} = X\hat{\beta}^{(2)}$$, tức $$X\hat{\beta}$$ là duy nhất với mọi nghiệm $$\hat{\beta}$$. Khi $$\lambda > 0$$, thay lại vào giá trị tối ưu $$c^\star$$ suy ra $$\|\hat{\beta}\|_1$$ cũng phải bằng nhau đối với mọi nghiệm.


Quay lại bài toán (1), các điều kiện KKT của bài toán lasso có dạng:
>$$
>\begin{align}
>&&X^T (y - X\hat{\beta}) = \lambda \gamma, \qquad \text{ --- (2)} \\\\
>&&\gamma_i \in 
> \begin{cases}
> \{ \text{sign}(\hat{\beta_i}) \} & \text{nếu } \hat{\beta_i} \neq 0 \\\\
> [-1, 1] & \text{nếu } \hat{\beta_i} = 0,
> \end{cases} \\\\
> &&\text{với } i = 1, \dots, p. \text{ --- (3)} \\\\
> &&\text{Ở đây } \gamma \in \mathbb{R}^p \text{ là một dưới gradient (subgradient) của hàm } \\
> &&f(x) = \| x \|_1 \text{ tại } x = \hat{\beta}.
>\end{align}
>$$

Nghiệm $$\hat{\beta}$$ của (1) thỏa mãn (2) và (3) với một vector $$\gamma$$ nào đó.

Ta dùng các điều kiện KKT này để biểu diễn nghiệm lasso ở dạng tường minh hơn. Trong phần dưới đây, giả sử $$\lambda > 0$$. Trước hết, định nghĩa tập tương quan bằng nhau (equicorrelation set) $$\mathcal{E}$$, gồm mọi chỉ số $$i$$ có $$\hat{\beta}_i \neq 0$$ và mọi chỉ số $$j$$ có $$\hat{\beta}_j = 0$$ nhưng $$\vert\gamma_j\vert = 1$$:

$$
\mathcal{E} = \{ i \in \{1, \dots, p \}  : \vert X_i^T (y - X\hat{\beta}) \vert = \lambda \}. \qquad \text{ --- (4)}
$$

Tiếp theo, định nghĩa vector dấu tương quan bằng nhau (equicorrelation signs) $$s$$ như sau, với $$X_\mathcal{E}$$ là ma trận gồm các cột $$i \in \mathcal{E}$$ của $$X$$:

$$
s = \text{sign}(X^T_\mathcal{E} (y -X\hat{\beta})). \qquad \text{ --- (5)}
$$

Theo định nghĩa của $$\gamma$$, ta có $$\mathcal{E} = \{i \in \{1, \dots, p \} : \vert \gamma_i \vert = 1 \}$$ và $$s = \gamma_{\mathcal{E}}$$. Hơn nữa, theo Bổ đề 1 (mục 2), $$X\hat{\beta}$$ là duy nhất, nên $$\mathcal{E}$$ và $$s$$ cũng duy nhất.

Từ (3), với mọi nghiệm lasso $$\hat{\beta}$$ ta có $$\hat{\beta}_{-\mathcal{E}} = 0$$. Viết lại phương trình (2) trên tập chỉ số $$\mathcal{E}$$:

$$
X^T_\mathcal{E} ( y - X_\mathcal{E} \hat{\beta_\mathcal{E}} ) = \lambda \gamma_\mathcal{E}=  \lambda s. \qquad \text{ --- (6)}
$$

Nhân hai vế của (6) với giả nghịch đảo $$(X^T_\mathcal{E})^+$$ và sử dụng đẳng thức $$(X^T_\mathcal{E})^+ X^T_\mathcal{E} = X_\mathcal{E} X_\mathcal{E}^+$$ (phép chiếu vuông góc lên không gian cột của $$X_\mathcal{E}$$), ta được:

$$
\begin{align}
& X_\mathcal{E} X_\mathcal{E}^+ X_\mathcal{E} \hat{\beta_\mathcal{E}} = X_\mathcal{E} X_\mathcal{E}^+ ( y - (X^T_\mathcal{E})^+  \lambda s) \\\\
\Leftrightarrow
& X_\mathcal{E} \hat{\beta_\mathcal{E}} = X_\mathcal{E} X_\mathcal{E}^+ ( y - (X^T_\mathcal{E})^+  \lambda s).
\end{align}
$$

Vì $$X\hat{\beta} = X_\mathcal{E} \hat{\beta_\mathcal{E}}$$, nên:

$$
X \hat{\beta} = X_\mathcal{E} X_\mathcal{E}^+ ( y - (X^T_\mathcal{E})^+  \lambda s), \qquad \text{ --- (7)}
$$

và mọi nghiệm lasso $$\hat{\beta}$$ đều có dạng:

$$
\begin{align}
& \hat{\beta_{-\mathcal{E}}} = 0 \text{ và } \hat{\beta_{\mathcal{E}}} = X_\mathcal{E}^+ ( y - (X^T_\mathcal{E})^+ \lambda s) + b, \qquad \text{ --- (8)} \\\\
& \text{với } b \in \text{null}(X_\mathcal{E}).
\end{align}
$$

## Điều kiện đủ cho tính duy nhất

Để $$\hat{\beta_{\mathcal{E}}}$$ trong (8) là duy nhất, ta cần $$b = 0$$ (vì thành phần $$X_\mathcal{E}^+ ( y - (X^T_\mathcal{E})^+ \lambda s)$$ đã xác định duy nhất). Từ đó suy ra kết quả sau:

>**Bổ đề 2.** Với mọi $$y, X$$ và $$\lambda > 0$$, nếu $$\text{null}(X_\mathcal{E}) = \{0\}$$, tức $$\text{rank}(X_\mathcal{E}) = \vert\mathcal{E}\vert$$ ([tham khảo](https://www.quora.com/When-the-null-space-of-a-matrix-is-the-zero-vector-the-matrix-is-invertible-Why/answer/Alexander-Farrugia)), thì nghiệm lasso là duy nhất và được cho bởi:

>$$
>\begin{align}
>&& \hat{\beta_{-\mathcal{E}}} = 0 \text{ và } \hat{\beta_{\mathcal{E}}} = (X^T_\mathcal{E}X_\mathcal{E})^{-1} ( X^T_\mathcal{E} y - \lambda s), \qquad \text{ --- (9)} \\\\
>&& \text{trong đó } \mathcal{E} \text{ và } s \text{ là tập và vector dấu equicorrelation định nghĩa trong (4) và (5)}.
>\end{align}
>$$

Lưu ý rằng nghiệm này có tối đa $$\min\{n, p\}$$ thành phần khác không.

Tiếp theo, ta tìm một điều kiện trực tiếp trên ma trận $$X$$ đảm bảo $$\text{null}(X_\mathcal{E}) = \{0\}$$. Giả sử phản chứng $$\text{null}(X_\mathcal{E}) \neq \{0\}$$. Khi đó, tồn tại chỉ số $$i \in \mathcal{E}$$ sao cho cột $$X_i$$ biểu diễn tuyến tính qua các cột còn lại trong $$\mathcal{E}$$:

$$
X_i = \sum_{j \in \mathcal{E} \backslash \{i\} } c_j X_j,\\\\
\text{với } c_j \in \mathbb{R}, j \in \mathcal{E}.
$$

Nhân hai vế với $$s_i$$ và chèn $$s_j^2 = 1$$ vào vế phải:

$$
s_i X_i = \sum_{j \in \mathcal{E} \backslash \{i\} } (s_i s_j c_j) \cdot (s_j X_j). \qquad \text{ --- (10)}
$$

Đặt phần dư lasso $$r = y - X \hat{\beta}$$; khi đó với mọi $$j \in \mathcal{E}$$ ta có $$X_j^T r = s_j \lambda$$. Lấy tích vô hướng hai vế của (10) với $$r$$ (với $$\lambda > 0$$), ta thu được:

$$
\lambda = \sum_{j \in \mathcal{E} \backslash \{i\} } (s_i s_j c_j) \lambda \quad \text{ và } \quad \sum_{j \in \mathcal{E} \backslash \{i\} } (s_i s_j c_j) = 1.
$$

Như vậy, nếu $$\text{null}(X_\mathcal{E}) \neq \{0\}$$ thì tồn tại $$i \in \mathcal{E}$$ sao cho:

$$
s_iX_i = \sum_{j \in \mathcal{E} \backslash \{i\} } a_j \cdot s_j X_j, \text{ với } \sum_{j \in \mathcal{E} \backslash \{i\} } a_j = 1.
$$

Điều này có nghĩa là $$s_i X_i$$ nằm trong bao affine của các điểm $$s_j X_j$$ ($$j \in \mathcal{E} \backslash \{i\}$$). Nói cách khác, một tập con gồm $$k+2$$ phần tử như vậy nằm trong một không gian con affine có số chiều không vượt quá $$k$$.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter12/l1_uniqueness.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 1] 4 phần tử trong không gian affine 2 chiều [3]</figcaption>
</p>
</figure>

Để đảm bảo $$\text{null}(X_\mathcal{E}) = \{0\}$$, chỉ cần các cột của ma trận $$X \in \mathbb{R}^{n \text{ x } p}$$ ở [vị trí tổng quát (general position)](https://en.wikipedia.org/wiki/General_position): không có không gian con affine $$k$$ chiều nào chứa quá $$k+1$$ phần tử thuộc tập $$\{\pm X_1, \dots, \pm X_p\}$$ (với mọi $$k < \min\{n, p\}$$).

>**Bổ đề 3.** Nếu các cột của ma trận $$X$$ ở vị trí tổng quát thì với mọi $$y$$ và $$\lambda > 0$$, nghiệm lasso là duy nhất và thỏa mãn (9).

Những ma trận $$X$$ nào thỏa mãn điều kiện vị trí tổng quát? Ta có kết quả sau:

>**Bổ đề 4.** Nếu các phần tử của ma trận $$X \in \mathbb{R}^{n \text{ x } p}$$ tuân theo một phân phối xác suất liên tục trên $$\mathbb{R}^{np}$$ thì với mọi $$y$$ và $$\lambda > 0$$, nghiệm lasso là duy nhất (với xác suất 1) và thỏa mãn (9).

Lý do là khi các phần tử được rút từ phân phối xác suất liên tục, các vector cột ở vị trí tổng quát với xác suất 1, nên các tập con cột liên quan độc lập tuyến tính ([tham khảo](https://math.stackexchange.com/questions/432447/probability-that-n-vectors-drawn-randomly-from-mathbbrn-are-linearly-ind?rq=1)).

## Hàm mất mát lồi tổng quát

Kết quả tương tự cũng đúng cho bài toán phạt $$\ell_1$$ với hàm mất mát lồi tổng quát [13]:

$$
\hat{\beta} \in \text{argmin}_{\beta \in \mathbb{R}^p} f(X\beta) + \lambda \|\beta\|_1, \qquad \text{ --- (11) }
$$

>**Bổ đề 5.** Nếu các phần tử của ma trận $$X \in \mathbb{R}^{n \text{ x } p}$$ tuân theo một phân phối xác suất liên tục trên $$\mathbb{R}^{np}$$, thì với mọi hàm $$f$$ khả vi, lồi chặt và mọi $$\lambda > 0$$, bài toán (11) luôn có nghiệm duy nhất (với xác suất 1). Nghiệm này có tối đa $$\min\{n,p\}$$ thành phần khác không.
