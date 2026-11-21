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

Trong chương này chúng ta học các cách giải bài toán bằng đối ngẫu: phương pháp dual subgradient, phương pháp dual decomposition và phương pháp augmented Lagrangian, đồng thời tìm hiểu sơ lược ý tưởng của phương pháp hướng luân phiên của các nhân tử (Alternating Direction Method of Multipliers, ADMM).

Trước hết, hãy ôn lại ngắn gọn hai chủ đề từ các chương trước: phương pháp Newton proximal và hàm liên hợp (conjugate function).

## Ôn tập: phương pháp Newton proximal
Xét bài toán
>\begin{equation}
\min_x g(x) + h(x)
\end{equation}

Ở đây $$g$$ và $$h$$ là các hàm lồi, $$g$$ khả vi hai lần và $$h$$ đơn giản.

Phương pháp Newton proximal bắt đầu từ điểm ban đầu $$x^{(0)} \in \mathbb{R}^n$$. Trước hết, ta tìm một hướng tốt cho cả $$g$$ và $$h$$:
>\begin{alignat}{1}
v^{(k)} & = \arg \min_v \nabla g({x^{(k-1)}})^T v +  \frac{1}{2} v^T \nabla^2 g(x^{(k-1)}) v + h(x^{(k-1)} + v) 
\end{alignat}

Sau đó cập nhật điểm tiếp theo theo hướng này:
>\begin{equation}
x^{(k)} = x^{(k-1)} + t_k v^{(k)}, \quad k=1,2,3,\dots 
\end{equation}

Ở đây $$t_k$$ là kích thước bước, được xác định bằng backtracking.

Hai bước này được lặp lại.

> * Mỗi vòng lặp rất đắt (việc tính $$v^{(k)}$$ nói chung rất khó).
* Tuy nhiên, dưới các điều kiện thích hợp, chỉ cần rất ít vòng lặp để hội tụ, và phương pháp có tốc độ hội tụ bậc hai cục bộ.


## Ôn tập: hàm liên hợp (conjugate function)
Với $$f: \mathbb{R}^n \to \mathbb{R}$$, hàm liên hợp được định nghĩa là
>\begin{equation}
f^*(y) = \max_x y^Tx - f(x)
\end{equation}

(1) Hàm liên hợp có thể được viết như sau, đây là một dạng thường xuất hiện trong các bài toán đối ngẫu.
>\begin{equation}
-f^{\ast}(y) = \min_x f(x) - y^Tx
\end{equation}

(2) Nếu $$f$$ đóng và lồi thì $$f^{**} = f$$. Hơn nữa,
>\begin{equation}
x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x) \Longleftrightarrow x \in \arg\min_z f(z) - y^Tz
\end{equation}
#### Chứng minh ####
Trước hết ta chứng minh $$x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x)$$.

#### Bước 1: $$y \in \partial f(x) \Longrightarrow x \in \partial f^{\ast}(y)$$
>
Giả sử $$y \in \partial f(x)$$. Khi đó $$x$$ thuộc tập $$M_y$$ các điểm cực đại hóa $$z \mapsto y^Tz - f(z)$$, tức là $$x \in M_y$$. <br> Do đó $$f^{\ast}(y) = y^Tx - f(x)$$, và với mọi $$w$$ ta có $$f^{\ast}(w) \ge w^Tx - f(x) = f^{\ast}(y) + x^T(w - y)$$. Điều này chính là $$x \in \partial f^{\ast}(y)$$.

####  Bước 2: $$x \in \partial f^{\ast}(y) \Longrightarrow y \in \partial f(x)$$
>
Áp dụng Bước 1 cho $$f^{\ast}$$, nếu $$x \in  \partial f^{\ast}(y)$$ thì $$y \in \partial f^{\ast\ast}(x)$$. Vì $$f^{\ast\ast}=f$$ nên ta có $$y \in \partial f(x)$$.

Bước 1 và 2 chứng minh $$x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x)$$.
#### Bước 3: $$x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x) \Longleftrightarrow x \in \arg\min_z f(z) - y^Tz$$
>
Cuối cùng, $$y \in \partial f(x) \Longleftrightarrow x \in \arg\min_z f(z) - y^Tz$$ suy ra trực tiếp từ định nghĩa của subgradient. <br>
Kết hợp với các phần trên, ta chứng minh được $$x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x) \Longleftrightarrow x \in \arg\min_z f(z) - y^Tz$$.


(3) Nếu $$f$$ lồi chặt thì
> $$
> \begin{equation}
> \nabla f^{\ast}(y) = \arg\min_z f(z) - y^T z
> \end{equation}
> $$

#### Chứng minh

>Nếu $$f$$ lồi chặt thì $$f(z)-y^Tz$$ có một điểm cực tiểu $$z$$ duy nhất,
>và theo chứng minh của (2) ở trên, điểm cực tiểu này phải là $$\nabla f^{\ast}(y)$$.

Nói cách khác, nếu $$f$$ lồi chặt thì dưới vi phân của $$f^{\ast}$$ chỉ gồm một phần tử, chính là gradient. Do đó $$f^{\ast}$$ là hàm khả vi.
