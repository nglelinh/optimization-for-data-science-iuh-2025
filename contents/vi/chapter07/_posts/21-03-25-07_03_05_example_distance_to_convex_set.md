---
layout: post
title: '07-03-05 Ví dụ: Khoảng cách đến tập lồi'
chapter: '07'
order: 11
owner: Kyeongmin Woo
categories:
- chapter07
lang: vi
---

Trong robot học (tránh va chạm chướng ngại vật), đồ họa máy tính và tối ưu hóa chiếu (projected methods), ta thường xuyên gặp **hàm khoảng cách đến một tập lồi đóng $$C$$**: $$\operatorname{dist}(x, C) = \min_{y \in C} \|x - y\|_2$$. Hàm này luôn lồi, nhưng liệu nó có khả vi không và gradient (hay subgradient) của nó hướng về đâu?

Trực giác hình học cho ta câu trả lời trong tích tắc: nếu bạn đang đứng ở điểm $$x$$ nằm ngoài một hồ nước hình lồi $$C$$, và điểm bờ hồ gần bạn nhất là hình chiếu $$P_C(x)$$, thì hướng khiến bạn **đi ra xa hồ nhanh nhất** chính là tia thẳng nối từ $$P_C(x)$$ qua $$x$$ — tức là vector đơn vị $$g = \frac{x - P_C(x)}{\|x - P_C(x)\|_2}$$! Bài học này chứng minh chặt chẽ kết quả hình học tuyệt đẹp đó bằng đúng công cụ subgradient và điều kiện tối ưu bậc nhất!

## Bản đồ kiến thức nền: Hình học Phép chiếu và Subgradient của Hàm khoảng cách

Ba trụ cột sau tóm gọn toàn bộ chứng minh và ứng dụng của bài học này:

- **Tính duy nhất và đặc trưng của Hình chiếu $$P_C(x)$$:** Vì $$y \mapsto \frac{1}{2}\|x - y\|_2^2$$ là hàm lồi chặt trên tập lồi đóng $$C$$, điểm chiếu $$P_C(x) = \arg\min_{y \in C} \|x - y\|_2$$ luôn **tồn tại duy nhất** và thỏa điều kiện tối ưu bậc nhất (góc tù):
  $$(x - P_C(x))^T (y - P_C(x)) \le 0 \quad \forall y \in C.$$
- **Gradient của $$\operatorname{dist}(x, C)$$ khi $$x \notin C$$:** Khi $$x \notin C$$, ta có $$\operatorname{dist}(x, C) > 0$$ và hàm khả vi với gradient duy nhất có độ dài bằng $$1$$:
  $$\nabla \operatorname{dist}(x, C) = \frac{x - P_C(x)}{\|x - P_C(x)\|_2}.$$
  (Còn hàm *bình phương khoảng cách* $$\frac{1}{2}\operatorname{dist}^2(x, C)$$ thì **khả vi ở mọi nơi** kể cả trên biên và trong $$C$$, với gradient $$x - P_C(x)$$!)
- **Tính chất đối ngẫu của siêu phẳng đỡ:** Trong chứng minh, ta dùng bất đẳng thức $$(x - P_C(x))^T (z - P_C(x)) \le (x - P_C(x))^T (z - P_C(z))$$ cộng với Cauchy-Schwarz để xác nhận $$g^T(z - x) \le \operatorname{dist}(z, C) - \operatorname{dist}(x, C)$$ cho mọi $$z \in \mathbb{R}^n$$!

### Khung giải thích (nên đọc chậm): Tính tay $$P_C(x)$$, $$\operatorname{dist}(x, C)$$ và kiểm chứng subgradient $$g$$

Xét tập lồi đóng là hình tròn đơn vị $$C = \{y \in \mathbb{R}^2 : \|y\|_2 \le 1\}$$ và điểm ngoài $$x = (3, 4)^T$$:

1. **Bước 1 — Tìm hình chiếu $$P_C(x)$$ và khoảng cách $$\operatorname{dist}(x, C)$$:**
   - Chuẩn $$\|x\|_2 = \sqrt{3^2 + 4^2} = 5 > 1$$.
   - Hình chiếu lên hình tròn đơn vị là điểm trên tia $$Ox$$ có độ dài 1:
     $$P_C(x) = \frac{x}{\|x\|_2} = (0.6,\; 0.8)^T.$$
   - Khoảng cách: $$\operatorname{dist}(x, C) = \|x - P_C(x)\|_2 = 5 - 1 = 4$$.
2. **Bước 2 — Tính subgradient $$g = \frac{x - P_C(x)}{\|x - P_C(x)\|_2}$$:**
   $$x - P_C(x) = (2.4,\; 3.2)^T \implies g = \frac{1}{4}(2.4,\; 3.2)^T = (0.6,\; 0.8)^T.$$
   Kiểm tra độ dài: $$\|g\|_2 = \sqrt{0.36 + 0.64} = 1$$!
3. **Bước 3 — Kiểm chứng bất đẳng thức subgradient $$\operatorname{dist}(z, C) \ge \operatorname{dist}(x, C) + g^T(z - x)$$ tại điểm thử $$z = (0, 2)^T$$:**
   - Vế trái: $$\operatorname{dist}(z, C) = \|(0, 2)\|_2 - 1 = 2 - 1 = 1$$.
   - Vế phải: $$4 + (0.6, 0.8) \cdot (-3, -2)^T = 4 + (-1.8 - 1.6) = 4 - 3.4 = 0.6$$.
   - So sánh: $$1 \ge 0.6$$ — thỏa mãn hoàn hảo!

---

Hàm khoảng cách từ một điểm $$x$$ đến một tập lồi đóng $$C$$ được định nghĩa như sau:
>
\begin{alignat}{1}
dist(x,C) & = \min_{y \in C} \| y-x \|_2 \\
      & = \| x-P_C(x) \|_2 \\
      & \geq 0 
\end{alignat}

Trong đó, $$P_C(x)$$ là phép chiếu Euclid của $$x$$ lên tập $$C$$, tức là điểm trong $$C$$ gần $$x$$ nhất. Với $$x \notin C$$ (nên $$\|x - P_C(x)\|_2 > 0$$), vi phân dưới của hàm khoảng cách là:
>
\begin{equation}
\partial dist(x,C) = \{\frac{x-P_C(x)}{ \| x-P_C(x) \|_2}\}
\end{equation}

### Chứng minh

Đặt $$u=P_C(x)$$. Theo điều kiện tối ưu bậc một cho bài toán chiếu lên tập lồi $$C$$, ta có:
>
\begin{equation}
(x-u)^T(y-u) \leq 0 \ \text{ với mọi } y \in C
\end{equation}

Suy ra tập $$C$$ nằm trong nửa không gian đóng $$H$$:
>
\begin{equation}
C \subseteq H = \{y:(x-u)^T(y-u) \leq 0 \}
\end{equation}

Ta xét hai trường hợp của $$y$$:

(i) Với $$y \in H$$, ta có:
>
\begin{equation}
(x-u)^T(y-u) \leq 0
\end{equation}

Do $$dist(y,C)\geq 0$$, nên hiển nhiên:
>
\begin{equation}
dist(y,C) \geq \frac{(x-u)^T(y-u)}{ \| x-u \|_2} \text{ với mọi } y \in H
\end{equation}

(ii) Với $$y \notin H$$, ta viết:
>
\begin{equation}
(x-u)^T(y-u) = \| x-u \|_2 \| y-u \|_2 \cos\theta,
\end{equation}

trong đó $$\theta$$ là góc giữa hai vector $$x-u$$ và $$y-u$$. Khi đó:
>
$$
\eqalign{
dist(y,C) &\geq dist(y,H) \\
&= \| y-u \|_2 \cos \theta \\
&= \frac{(x-u)^T(y-u)}{ \| x-u \|_2} \text{ với mọi }y \notin H
}
$$

Từ (i) và (ii), bất đẳng thức sau đúng với mọi $$y$$:
>
$$
\eqalign{
dist(y,C) &\geq \frac{(x-u)^T(y-u)}{ \| x-u \|_2} \\
&= \frac{(x-u)^T(y-x+x-u)}{ \| x-u \|_2}\\
& = \| x-u \|_2 + \left(\frac{x-u}{ \| x-u \|_2}\right)^T(y-x)
}
$$

Do đó, tại $$x \notin C$$, hàm $$dist(x,C)$$ có gradient dưới là:
>
$$g=\frac{x-u}{ \| x-u \|_2}=\frac{x-P_C(x)}{ \| x-P_C(x) \|_2} $$

Hơn nữa, vì vi phân dưới $$\partial dist(x,C)$$ tại $$x \notin C$$ chỉ gồm một phần tử duy nhất, hàm $$dist(x,C)$$ khả vi tại $$x$$ và đạo hàm của nó trùng với gradient dưới nói trên.
