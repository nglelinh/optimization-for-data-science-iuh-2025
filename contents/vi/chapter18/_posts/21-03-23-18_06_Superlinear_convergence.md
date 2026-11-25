---
layout: post
title: 18-06 Hội tụ Siêu tuyến tính
chapter: '18'
order: '7'
owner: Hooncheol Shin
categories:
- chapter18
lang: vi
---

Phương pháp Quasi-Newton không hề tính đạo hàm bậc hai, vậy tại sao nó lại có thể bỏ xa hạ gradient (hội tụ tuyến tính) và tiến gần sát tốc độ của phương pháp Newton (hội tụ bậc hai)? Câu trả lời nằm ở **hội tụ siêu tuyến tính (superlinear convergence)** và một định lý kiệt tác của Dennis và Moré (1974): để đạt hội tụ siêu tuyến tính, ta **không cần** ma trận xấp xỉ $$B_k$$ phải hội tụ về toàn bộ Hessian thực $$G(x^\star)$$ — ta chỉ cần $$B_k$$ xấp xỉ chính xác $$G(x^\star)$$ **dọc theo hướng bước đi $$p_k$$** là đủ!

## Kiến thức cần nhớ: Bốn mảnh ghép của lý thuyết hội tụ siêu tuyến tính

Để đọc hiểu các giả thiết và Định lý Dennis–Moré trong bài, hãy đặt bốn khái niệm này vào đúng vị trí của chúng:

- **Hệ thang tốc độ hội tụ (Linear → Superlinear → Quadratic):** Hội tụ tuyến tính giữ tỉ số sai số $$\|e_{k+1}\| / \|e_k\| \le c < 1$$ không đổi; hội tụ siêu tuyến tính đưa tỉ số đó về $$0$$ khi $$k \to \infty$$; còn hội tụ bậc hai đòi hỏi $$\|e_{k+1}\| \le M\|e_k\|^2$$ (gấp đôi số chữ số đúng sau mỗi bước).
- **Tính liên tục Lipschitz của Hessian:** Đảm bảo độ cong thực không biến đổi đột ngột quanh nghiệm $$x^\star$$, nhờ đó thông tin secant thu thập từ các bước gần nhất phản ánh trung thực ma trận $$G(x^\star)$$.
- **Điều kiện Wolfe hai vế (Armijo + Độ cong):** Đảm bảo đồng thời hai mục tiêu quan trọng: giá trị hàm giảm đủ (không nhảy quá lố) và $$y_k^T s_k > 0$$ (không dừng quá non và giữ $$B_k \succ 0$$), đồng thời chấp nhận độ dài bước đơn vị $$t_k = 1$$ khi đủ gần $$x^\star$$.
- **Định lý Dennis–Moré:** Khẳng định rằng bước $$x_{k+1} = x_k + p_k$$ hội tụ siêu tuyến tính khi và chỉ khi $$\lim_{k \to \infty} \frac{\|(B_k - G(x^\star)) p_k\|}{\|p_k\|} = 0$$ — tức $$B_k$$ chỉ cần khớp $$G(x^\star)$$ trên đúng hướng mà thuật toán đang đi!

### Giải thích: So sánh tốc độ giảm sai số bằng số thực và kiểm tra tỉ số Dennis–Moré

Hãy quan sát sự khác biệt kịch tính giữa ba tốc độ hội tụ cùng xuất phát từ sai số ban đầu $$e_0 = 0.5$$ sau 5 vòng lặp:

| Vòng lặp $$k$$ | Tuyến tính ($$e_{k+1} = 0.5 e_k$$) | Siêu tuyến tính ($$e_{k+1} = e_k^{1.5}$$) | Bậc hai ($$e_{k+1} = e_k^2$$) |
| :---: | :---: | :---: | :---: |
| $$0$$ | $$0.500000$$ | $$0.500000$$ | $$0.500000$$ |
| $$1$$ | $$0.250000$$ | $$0.353553$$ | $$0.250000$$ |
| $$2$$ | $$0.125000$$ | $$0.210224$$ | $$0.062500$$ |
| $$3$$ | $$0.062500$$ | $$0.096385$$ | $$0.003906$$ |
| $$4$$ | $$0.031250$$ | $$0.029924$$ | $$1.5 \times 10^{-5}$$ |
| $$5$$ | $$0.015625$$ | $$0.005177$$ | $$2.3 \times 10^{-10}$$ |

Và đây là phép kiểm tra trực giác cho **Định lý Dennis–Moré**: giả sử $$G(x^\star) = \begin{bmatrix} 2 & 0 \\ 0 & 10 \end{bmatrix}$$, ma trận xấp xỉ $$B_k = \begin{bmatrix} 2 + 10^{-3} & 0 \\ 0 & 99 \end{bmatrix}$$ (sai lệch khổng lồ ở thành phần thứ hai: $$99$$ so với $$10$$!), nhưng hướng bước đi hiện tại là $$p_k = (1, \; 10^{-5})^T$$:

1. **Tính tử số:** $$(B_k - G(x^\star))p_k = \begin{bmatrix} 10^{-3} & 0 \\ 0 & 89 \end{bmatrix}\begin{bmatrix} 1 \\ 10^{-5} \end{bmatrix} = \begin{bmatrix} 10^{-3} \\ 8.9 \times 10^{-4} \end{bmatrix}$$, có chuẩn $$\approx 1.34 \times 10^{-3}$$.
2. **Chia cho $$\|p_k\| \approx 1$$:** Tỉ số Dennis–Moré chỉ khoảng $$0.00134 \ll 1$$! Dù $$B_k$$ ước lượng sai hoàn toàn độ cong dọc trục $$x_2$$, thuật toán vẫn thực hiện một bước đi gần như hoàn hảo giống bước Newton vì $$p_k$$ hầu như nằm dọc trục $$x_1$$ — nơi $$B_k$$ đã học chính xác!

---

# Giả thiết 1:
> Ma trận Hessian $$G$$ liên tục Lipschitz tại $$x^*$$, nghĩa là tồn tại hằng số dương $$L$$ sao cho:
> $$\| G(x) - G(x^*) \| \le L \| x - x^* \|$$
với mọi $$x$$ đủ gần $$x^*$$.

# Giả thiết 2: Điều kiện Wolfe
> Giả sử độ dài bước $$t$$ được chọn (thông qua tìm kiếm theo đường thẳng) sao cho thỏa mãn đồng thời hai bất đẳng thức:
> $$
f(x + tp) \le f(x) + \alpha_1 t \nabla f(x)^T p
>$$
và
> $$
\nabla f(x + tp)^T p \ge \alpha_2 \nabla f(x)^T p
>$$
với $$0 < \alpha_1 < \alpha_2 < 1$$.

* Điều kiện Wolfe thứ nhất (điều kiện giảm đủ) đảm bảo độ dài bước $$t$$ không quá lớn.
* Điều kiện Wolfe thứ hai (điều kiện độ cong) đảm bảo độ dài bước $$t$$ không quá nhỏ.

Dưới hai giả thiết trên, cả DFP và BFGS đều đạt tốc độ hội tụ siêu tuyến tính (tham khảo: [Tốc độ hội tụ trên Wikipedia](https://en.wikipedia.org/wiki/Rate_of_convergence)):

>$$
>\lim_{k \rightarrow \infty} \frac{ \| x^{k+1} - x^\ast \| }{ \| x^k - x^\ast \| } = 0.
>$$

# Định lý Dennis–Moré

Định lý Dennis–Moré cung cấp điều kiện đủ (và cần) cho hướng tìm kiếm của phương pháp Quasi-Newton đạt hội tụ siêu tuyến tính khi hướng đó tiệm cận đủ sát hướng Newton gần nghiệm [14]:

> Giả sử $$f$$ khả vi liên tục hai lần, dãy $$x^k \rightarrow x^\ast$$ với $$\nabla f(x^\ast) = 0$$ và $$\nabla^2 f(x^\ast)$$ xác định dương. Xét điều kiện:
>
>$$
\lim_{k \rightarrow \infty} \frac{\| \nabla f(x^k) + \nabla^2 f(x^k) p^k \| }{\| p^k \|} = 0.
>$$
>
> Nếu hướng tìm kiếm $$p^k$$ thỏa mãn điều kiện trên, thì tồn tại chỉ số $$k_0$$ sao cho:
>
> 1. Với mọi $$k \ge k_0$$, độ dài bước đơn vị $$t_k = 1$$ thỏa mãn điều kiện Wolfe.
> 2. Khi chọn $$t_k = 1$$ với mọi $$k \ge k_0$$, dãy $$x^k$$ hội tụ siêu tuyến tính về $$x^\ast$$.