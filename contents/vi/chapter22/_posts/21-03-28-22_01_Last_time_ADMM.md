---
layout: post
title: '22-01 Nhắc lại: ADMM'
chapter: '22'
order: 2
owner: YoungJae Choung
categories:
- chapter22
lang: vi
---

Trước khi chuyển sang phương pháp gradient có điều kiện (Frank–Wolfe), bài học này đóng vai trò như một trạm trung chuyển chiến lược: dừng lại nhìn về **ADMM (Alternating Direction Method of Multipliers)** — công cụ chủ lực của Chương 21 — để thấy rõ điểm tương đồng và khác biệt giữa hai triết lý lớn của tối ưu hiện đại.

Nếu Frank–Wolfe chọn cách giữ nguyên ràng buộc tập lồi $$x \in C$$ rồi tuyến tính hóa hàm mục tiêu, thì ADMM lại chọn con đường tách đôi một bài toán khó thành hai bài toán con dễ hơn thông qua biến phụ $$z$$ và ràng buộc đẳng thức $$Ax + Bz = c$$. Điều kỳ diệu của ADMM là ở chỗ nó ghép sức mạnh ổn định của hàm phạt bậc hai (Augmented Lagrangian) với khả năng giải tách biệt từng biến giống như Dual Decomposition, biến những bài toán khổng lồ thành chuỗi cập nhật luân phiên cực kỳ thân thiện với tính toán phân tán.

## Kiến thức cần nhớ: Ba trụ cột đằng sau ADMM

Khi đọc lại ba dòng cập nhật ngắn gọn của ADMM, hãy nhớ rằng đằng sau chúng là sự hòa quyện của ba ý tưởng lớn trong giải tích lồi:

- **Hàm Lagrangian tăng cường (Augmented Lagrangian):** Cộng thêm số hạng phạt bậc hai $$\frac{\rho}{2}\|Ax + Bz - c\|_2^2$$ vào Lagrangian cổ điển không làm thay đổi nghiệm tối ưu của bài toán gốc, nhưng giúp hàm đối ngẫu trở nên trơn hơn và loại bỏ yêu cầu hàm mục tiêu phải lồi chặt mới hội tụ.
- **Tách biến luân phiên (Gauss–Seidel Splitting):** Thay vì cực tiểu hóa đồng thời theo cặp $$(x, z)$$ — vốn phá vỡ cấu trúc tách biệt — ADMM cập nhật $$x$$ trước (giữ $$z$$ cố định) rồi mới cập nhật $$z$$ (dùng $$x$$ vừa tính), giống hệt tinh thần phương pháp Gauss–Seidel trong đại số tuyến tính số.
- **Biến đối ngẫu chuẩn hóa (Scaled Dual Variable):** Đặt $$w = u / \rho$$ không chỉ giúp viết gọn hai số hạng tuyến tính và bậc hai thành một bình phương hoàn chỉnh $$\frac{\rho}{2}\|Ax + Bz - c + w\|_2^2$$, mà còn cho thấy trực giác rõ ràng: $$w^{(k)}$$ chính là *tổng tích lũy* của mọi sai số vi phạm ràng buộc (primal residuals) từ đầu thuật toán tới bước $$k$$.

### Giải thích: Tính tay 2 vòng lặp ADMM dạng chuẩn hóa

Để cảm nhận cách biến đối ngẫu $$w$$ "kéo" hai biến tách rời $$x$$ và $$z$$ lại gần nhau, hãy giải bài toán đồng thuận 1 chiều:

$$
\min_{x, z \in \mathbb{R}}\ \frac{1}{2}(x - 4)^2 + \frac{1}{2}z^2 \qquad \text{thỏa mãn } x - z = 0.
$$

Nghiệm đúng bằng mắt thường là $$x^\star = z^\star = 2$$ (trung bình cộng của $$4$$ và $$0$$). Hãy chọn $$\rho = 1$$, khởi tạo $$z^{(0)} = 0$$ và $$w^{(0)} = 0$$ (ở đây $$A = 1, B = -1, c = 0$$):

1. **Vòng lặp $$k = 1$$:**
   - *Cập nhật $$x^{(1)}$$:* Cực tiểu hóa $$\frac{1}{2}(x - 4)^2 + \frac{1}{2}(x - 0 + 0)^2$$. Lấy đạo hàm bằng $$0$$: $$(x - 4) + x = 0 \Rightarrow x^{(1)} = 2$$.
   - *Cập nhật $$z^{(1)}$$:* Cực tiểu hóa $$\frac{1}{2}z^2 + \frac{1}{2}(2 - z + 0)^2$$. Lấy đạo hàm bằng $$0$$: $$z - (2 - z) = 0 \Rightarrow z^{(1)} = 1$$.
   - *Cập nhật biến đối ngẫu $$w^{(1)}$$:* $$w^{(1)} = w^{(0)} + (x^{(1)} - z^{(1)}) = 0 + (2 - 1) = 1$$.
2. **Vòng lặp $$k = 2$$:**
   - *Cập nhật $$x^{(2)}$$:* Cực tiểu hóa $$\frac{1}{2}(x - 4)^2 + \frac{1}{2}(x - 1 + 1)^2 = \frac{1}{2}(x-4)^2 + \frac{1}{2}x^2 \Rightarrow x^{(2)} = 2$$.
   - *Cập nhật $$z^{(2)}$$:* Cực tiểu hóa $$\frac{1}{2}z^2 + \frac{1}{2}(2 - z + 1)^2 = \frac{1}{2}z^2 + \frac{1}{2}(3 - z)^2$$. Đạo hàm bằng $$0$$: $$z - (3 - z) = 0 \Rightarrow z^{(2)} = 1.5$$.
   - *Cập nhật biến đối ngẫu $$w^{(2)}$$:* $$w^{(2)} = 1 + (2 - 1.5) = 1.5$$.
3. **Quan sát trực giác:** Sai số ràng buộc $$x^{(k)} - z^{(k)}$$ giảm một nửa sau mỗi bước ($$1 \to 0.5 \to 0.25 \to \dots$$), còn $$w^{(k)}$$ tích lũy dần $$0 \to 1 \to 1.5 \to 1.75 \to 2$$, đóng vai trò như lực lò xo bù trừ để kéo $$z^{(k)}$$ tiến mượt về đúng $$2$$ mà không cần đặt $$\rho \to \infty$$!

## Nhắc lại: ADMM

Xét bài toán tối ưu có ràng buộc đẳng thức sau:
> $$\begin{align}
> &\min_{x,z} &&f(x) + g(z)\\\\
> &\text{ subject to } &&Ax + Bz = c 
> \end{align}$$

Với tham số $$\rho > 0$$, hàm Lagrangian tăng cường (Augmented Lagrangian) tương ứng có dạng:
> $$ L_\rho(x, z, u) = f(x) + g(z) + u^T(Ax + Bz − c) + \frac{\rho}{2} \| Ax + Bz − c \|^2_2$$

Việc bổ sung số hạng phạt bậc hai $$\frac{\rho}{2} \| Ax + Bz − c \|^2_2$$ giúp cải thiện điều kiện hội tụ của bài toán, đồng thời ADMM vẫn duy trì khả năng tách biến thuận tiện cho tính toán song song thông qua các bước cập nhật luân phiên sau (chứng minh chi tiết đã trình bày ở chương trước).

Các bước lặp ADMM với $$k = 1, 2, 3, \ldots$$:
> $$x^{(k)} = \arg\min_{x} L_\rho(x, z^{(k−1)}, u^{(k−1)})$$
> $$z^{(k)} = \arg\min_{z} L_\rho(x^{(k)}, z, u^{(k−1)})$$
> $$u^{(k)} = u^{(k−1)} + \rho(Ax^{(k)} + Bz^{(k)} − c)$$

## ADMM dạng chuẩn hóa (scaled form)

Đặt biến đối ngẫu chuẩn hóa $$w = u/\rho$$, các bước cập nhật ADMM được viết gọn như sau:

> $$x^{(k)} = \arg\min_{x} f(x) + \frac{\rho}{2} \| Ax + Bz^{(k−1)} − c + w^{(k−1)} \|^2_2$$
> $$z^{(k)} = \arg\min_{z} g(z) + \frac{\rho}{2} \| Ax^{(k)} + Bz − c + w^{(k−1)} \|^2_2$$ 
> $$w^{(k)} = w^{(k−1)} + Ax^{(k)} + Bz^{(k)} − c$$
