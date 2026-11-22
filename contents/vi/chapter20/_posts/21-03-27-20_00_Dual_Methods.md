---
layout: post
title: '20 Các phương pháp đối ngẫu (Dual Methods)'
chapter: '20'
order: 1
owner: Hooncheol Shin
categories:
- chapter20
lang: vi
---

Trong chương này, chúng ta tìm hiểu các phương pháp giải bài toán tối ưu thông qua bài toán đối ngẫu: phương pháp hạ dưới vi phân đối ngẫu (dual subgradient), phân rã đối ngẫu (dual decomposition), hàm Lagrange tăng cường (augmented Lagrangian), đồng thời giới thiệu sơ lược ý tưởng của phương pháp nhân tử hướng luân phiên (Alternating Direction Method of Multipliers — ADMM).

Trước hết, hãy ôn lại ngắn gọn hai nội dung nền tảng từ các chương trước: phương pháp Newton proximal và hàm liên hợp (conjugate function).

## Ôn tập: phương pháp Newton proximal
Xét bài toán tổng hợp:
>\begin{equation}
\min_x g(x) + h(x)
\end{equation}

trong đó $$g$$ và $$h$$ là các hàm lồi, $$g$$ khả vi hai lần và $$h$$ có cấu trúc đơn giản.

Bắt đầu từ điểm khởi tạo $$x^{(0)} \in \mathbb{R}^n$$, ở mỗi vòng lặp $$k = 1, 2, 3, \dots$$, phương pháp Newton proximal tìm hướng cập nhật $$v^{(k)}$$:
>\begin{alignat}{1}
v^{(k)} & = \arg \min_v \nabla g({x^{(k-1)}})^T v +  \frac{1}{2} v^T \nabla^2 g(x^{(k-1)}) v + h(x^{(k-1)} + v) 
\end{alignat}

sau đó cập nhật điểm lặp với độ dài bước $$t_k$$ (xác định bằng backtracking line search):
>\begin{equation}
x^{(k)} = x^{(k-1)} + t_k v^{(k)}, \quad k=1,2,3,\dots 
\end{equation}

> * Chi phí mỗi vòng lặp cao (việc giải bài toán con tìm $$v^{(k)}$$ nói chung khó).
> * Tuy nhiên, dưới các giả thiết thích hợp, phương pháp chỉ cần rất ít vòng lặp và đạt tốc độ hội tụ bậc hai cục bộ.


## Ôn tập: hàm liên hợp (conjugate function)
Với hàm $$f: \mathbb{R}^n \to \mathbb{R}$$, hàm liên hợp $$f^*$$ được định nghĩa là:
>\begin{equation}
f^*(y) = \max_x y^Tx - f(x)
\end{equation}

(1) Hàm liên hợp thường xuất hiện trong các bài toán đối ngẫu dưới dạng tương đương:
>\begin{equation}
-f^{\ast}(y) = \min_x f(x) - y^Tx
\end{equation}

(2) Nếu $$f$$ là hàm lồi và đóng, thì $$f^{**} = f$$. Hơn nữa:
>\begin{equation}
x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x) \Longleftrightarrow x \in \arg\min_z f(z) - y^Tz
\end{equation}

#### Chứng minh
Trước hết, ta chứng minh $$x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x)$$.

#### Bước 1: $$y \in \partial f(x) \Longrightarrow x \in \partial f^{\ast}(y)$$
> Giả sử $$y \in \partial f(x)$$. Khi đó $$x$$ cực đại hóa hàm $$z \mapsto y^Tz - f(z)$$, nên $$f^{\ast}(y) = y^Tx - f(x)$$. Với mọi $$w$$, ta có $$f^{\ast}(w) \ge w^Tx - f(x) = f^{\ast}(y) + x^T(w - y)$$, điều này chứng tỏ $$x \in \partial f^{\ast}(y)$$.

#### Bước 2: $$x \in \partial f^{\ast}(y) \Longrightarrow y \in \partial f(x)$$
> Áp dụng Bước 1 cho hàm $$f^{\ast}$$: nếu $$x \in \partial f^{\ast}(y)$$ thì $$y \in \partial f^{\ast\ast}(x)$$. Vì $$f^{\ast\ast} = f$$ nên suy ra $$y \in \partial f(x)$$.

#### Bước 3: $$x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x) \Longleftrightarrow x \in \arg\min_z f(z) - y^Tz$$
> Tương đương $$y \in \partial f(x) \Longleftrightarrow x \in \arg\min_z f(z) - y^Tz$$ suy trực tiếp từ định nghĩa dưới vi phân ($$0 \in \partial(f(x) - y^Tx)$$). Kết hợp với Bước 1 và Bước 2, ta thu được điều phải chứng minh.


(3) Nếu $$f$$ lồi chặt thì:
> $$
> \begin{equation}
> \nabla f^{\ast}(y) = \arg\min_z f(z) - y^T z
> \end{equation}
> $$

#### Chứng minh

> Nếu $$f$$ lồi chặt thì hàm $$z \mapsto f(z) - y^Tz$$ có điểm cực tiểu duy nhất. Theo tính chất (2) ở trên, dưới vi phân $$\partial f^{\ast}(y)$$ chỉ gồm đúng một phần tử — đó chính là gradient $$\nabla f^{\ast}(y)$$. Do đó $$f^{\ast}$$ là hàm khả vi.
