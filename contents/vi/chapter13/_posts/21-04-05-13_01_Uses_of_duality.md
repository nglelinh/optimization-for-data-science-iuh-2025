---
layout: post
title: 13-01 Ứng dụng của đối ngẫu
chapter: '13'
order: 2
owner: Wontak Ryu
categories:
- chapter13
lang: vi
---

Trong thực tế chạy thuật toán tối ưu, câu hỏi khiến kỹ sư đau đầu nhất không phải lúc nào cũng là "làm sao đi bước tiếp theo", mà là **"khi nào thì đủ tốt để dừng lại?"**. Nếu chỉ nhìn vào độ lớn gradient hay sự thay đổi nhỏ giữa hai vòng lặp liên tiếp $$\|x^{(k+1)} - x^{(k)}\|$$, bạn rất dễ bị đánh lừa bởi một thung lũng phẳng dài nơi thuật toán bò chậm nhưng vẫn còn cách đáy rất xa.

Lý thuyết đối ngẫu giải quyết dứt điểm nỗi lo này bằng một cơ chế kiểm chứng toán học tuyệt đối: **khoảng cách đối ngẫu (duality gap)**. Thay vì đoán mò mình còn cách nghiệm tối ưu $$f^\star$$ bao xa, bạn xây dựng song song một điểm khả thi đối ngẫu $$(u, v)$$ để tạo ra một "sàn cứng" $$g(u, v) \le f^\star \le f(x)$$. Khi trần và sàn khép sát nhau dưới ngưỡng $$\epsilon$$, bạn có thể dừng máy với sự đảm bảo 100% về độ chính xác.

## Kiến thức cần nhớ: Vì sao đối ngẫu sinh ra tiêu chí dừng và đường tắt giải toán?

- **Tính đối ngẫu yếu như một chặn dưới phổ quát:** Bất kể bài toán gốc có lồi hay không, với mọi điểm khả thi nguyên thủy $$x$$ và mọi điểm khả thi đối ngẫu $$(u, v)$$, ta luôn có $$g(u, v) \le f^\star \le f(x)$$. Vì vậy $$f(x) - g(u, v)$$ luôn là chặn trên chắc chắn cho sai số thực $$f(x) - f^\star$$.
- **Khoảng cách đối ngẫu (Duality Gap) vs. Độ lệch tối ưu (Suboptimality):** Ta không bao giờ biết giá trị $$f^\star$$ khi thuật toán đang chạy, nên không thể tính trực tiếp $$f(x) - f^\star$$. Nhưng ta tính được cả $$f(x)$$ lẫn $$g(u, v)$$, biến một đại lượng ẩn thành tiêu chí dừng đo được trực tiếp.
- **Bắc cầu từ bài toán khó sang bài toán dễ:** Khi đối ngẫu mạnh thỏa mãn, việc giải bài toán đối ngẫu (thường có ít biến hơn hoặc cấu trúc ràng buộc đơn giản hơn) rồi khôi phục $$x^\star$$ giúp giảm mạnh chi phí tính toán.

### Giải thích: Tính khoảng cách đối ngẫu làm tiêu chí dừng bằng tay

Xét bài toán quy hoạch bậc hai đơn giản:

$$\min_{x \in \mathbb{R}^2} \frac{1}{2}(x_1^2 + x_2^2) \qquad \text{với điều kiện } x_1 + x_2 = 4.$$

1. **Tìm hàm đối ngẫu $$g(v)$$:** Lập hàm Lagrange $$L(x, v) = \frac{1}{2}(x_1^2 + x_2^2) + v(4 - x_1 - x_2)$$. Lấy đạo hàm theo $$x_1, x_2$$ bằng $$0$$ ta được $$x_1 = v, x_2 = v$$. Thay lại vào $$L$$ thu được:
   $$g(v) = \frac{1}{2}(v^2 + v^2) + v(4 - 2v) = 4v - v^2.$$
2. **Đánh giá ở vòng lặp thứ nhất:** Giả sử thuật toán đang đứng tại điểm khả thi $$x^{(1)} = (3, 1)$$ (thỏa $$3 + 1 = 4$$) và ước lượng đối ngẫu $$v^{(1)} = 1.5$$.
   - Giá trị nguyên thủy: $$f(x^{(1)}) = \frac{1}{2}(9 + 1) = 5.0$$.
   - Giá trị đối ngẫu: $$g(v^{(1)}) = 4(1.5) - (1.5)^2 = 6 - 2.25 = 3.75$$.
   - Khoảng cách đối ngẫu: $$\Delta_1 = 5.0 - 3.75 = 1.25$$. Ta chắc chắn $$f(x^{(1)}) - f^\star \le 1.25$$ (thực tế $$f^\star = 4$$, sai số thật là $$1.0 \le 1.25$$).
3. **Đánh giá ở vòng lặp sau:** Thuật toán tiến tới $$x^{(2)} = (2.1, 1.9)$$ và $$v^{(2)} = 1.95$$.
   - $$f(x^{(2)}) = \frac{1}{2}(4.41 + 3.61) = 4.01$$.
   - $$g(v^{(2)}) = 4(1.95) - (1.95)^2 = 7.8 - 3.8025 = 3.9975$$.
   - Khoảng cách đối ngẫu: $$\Delta_2 = 4.01 - 3.9975 = 0.0125$$. Nếu ngưỡng dừng là $$\epsilon = 0.02$$, thuật toán dừng ngay và đảm bảo chắc chắn giá trị mục tiêu chỉ sai khác đáy tối đa $$0.0125$$.

---

### Hai ứng dụng chính của đối ngẫu

Hãy cùng điểm lại hai tính chất ứng dụng chính của lý thuyết đối ngẫu đã giới thiệu ở Chương 11.

* **Khoảng cách đối ngẫu làm tiêu chí dừng:** Khi $$x$$ khả thi nguyên thủy và $$(u, v)$$ khả thi đối ngẫu, hiệu giữa giá trị mục tiêu nguyên thủy $$f(x)$$ và giá trị hàm đối ngẫu $$g(u, v)$$ được gọi là **khoảng cách đối ngẫu** (duality gap) giữa $$x$$ và $$(u, v)$$:

> $$f(x) - f^{\star} \le f(x) - g(u, v)$$

Khi khoảng cách đối ngẫu bằng $$0$$ (zero duality gap), nghiệm nguyên thủy và nghiệm đối ngẫu đều đạt tối ưu. Ngoài ra, giá trị hàm đối ngẫu $$g(u, v)$$ luôn là một **cận dưới** của giá trị tối ưu $$f^{\star}$$ (tức $$g(u, v) \le f^{\star}$$); xem lại chi tiết tại [[Chương 11]]({% multilang_post_url contents/chapter11/21-03-24-11_00_Duality_in_General_Programs %}). Từ đó ta có suy dẫn sau:

#### Chứng minh
> $$\begin{align*}
> f^{\star} &\ge g(u, v) \\
> -f^{\star} &\le -g(u, v) \\
> f(x)-f^{\star} &\le \underbrace{f(x)-g(u, v)}_{\text{khoảng cách đối ngẫu}}\\
> g^{\star}-g(u, v) &\le \underbrace{f(x)-g(u, v)}_{\text{khoảng cách đối ngẫu}}\\
> \end{align*}$$

Nhờ chặn trên sai số tối ưu này, khoảng cách đối ngẫu thường được dùng trực tiếp làm tiêu chí dừng cho các thuật toán tối ưu hóa.

* **Tìm nghiệm nguyên thủy thông qua nghiệm đối ngẫu:** Khi tính đối ngẫu mạnh được thỏa mãn và ta đã biết nghiệm đối ngẫu tối ưu $$(u^{\star}, v^{\star})$$, nghiệm nguyên thủy tối ưu $$x^{\star}$$ phải cực tiểu hóa hàm Lagrangian $$L(x, u^{\star}, v^{\star})$$ theo $$x$$ (tức thỏa mãn điều kiện dừng). Tính chất này cho phép suy ra nghiệm nguyên thủy từ nghiệm đối ngẫu.
