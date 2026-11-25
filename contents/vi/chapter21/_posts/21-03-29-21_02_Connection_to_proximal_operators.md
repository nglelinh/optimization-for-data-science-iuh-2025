---
layout: post
title: '21-02 Mối liên hệ với toán tử proximal'
chapter: '21'
order: 3
owner: Hooncheol Shin
categories:
- chapter21
lang: vi
---

Ở Chương 9, ta giải bài toán tổng hai hàm $$\min_x f(x) + g(x)$$ bằng **proximal gradient descent**, nhưng phương pháp đó đòi hỏi ít nhất một trong hai hàm (ví dụ $$f$$) phải khả vi trơn. Điều gì xảy ra nếu **cả $$f$$ và $$g$$ đều không khả vi** (chẳng hạn $$f(x) = \|Ax - b\|_1$$ và $$g(x) = \lambda\|x\|_1$$, hoặc tổng hai hàm chỉ thị tập lồi)? Chỉ cần tách biến thành $$\min f(x) + g(z) \text{ s.t. } x = z$$, ADMM dạng chuẩn hóa lập tức biến thành **một thuật toán hoàn toàn đối xứng chỉ dùng hai toán tử proximal** $$\operatorname{prox}_{f, 1/\rho}$$ và $$\operatorname{prox}_{g, 1/\rho}$$ — mà không cần bất kỳ đạo hàm nào!

## Kiến thức cần nhớ: Ba điểm nối sâu sắc giữa ADMM và toán tử proximal

Để nắm vững sức mạnh của cách viết proximal ADMM trong bài học này, hãy ghi nhớ ba mối liên hệ cốt lõi:

- **Đối xứng hoàn toàn giữa $$f$$ và $$g$$:** Bước cập nhật $$x^{(k)} = \operatorname{prox}_{f, 1/\rho}(z^{(k-1)} - w^{(k-1)})$$ và $$z^{(k)} = \operatorname{prox}_{g, 1/\rho}(x^{(k)} + w^{(k-1)})$$ cho phép giải tổng của **hai hàm đều không trơn**, miễn là mỗi hàm có toán tử proximal dễ tính!
- **Tương đương với thuật toán Douglas–Rachford:** Biến đổi đại số ngắn cho thấy ADMM áp dụng trên bài toán tách biến $$x = z$$ thực chất tương đương với phương pháp tách toán tử Douglas–Rachford nổi tiếng trong giải tích lồi (và nếu áp dụng ADMM trên bài toán đối ngẫu thì tương đương với Douglas–Rachford trên bài toán gốc).
- **Ý nghĩa của tham số $$1/\rho$$:** Trong $$\operatorname{prox}_{f, 1/\rho}(v) = \arg\min_x \left(f(x) + \frac{\rho}{2}\|x - v\|_2^2\right)$$, tham số $$1/\rho$$ đóng vai trò hệt như bước học $$t$$ trong proximal gradient: $$\rho$$ lớn giữ $$x^{(k)}$$ bám sát $$z^{(k-1)} - w^{(k-1)}$$, còn $$\rho$$ nhỏ cho phép $$x^{(k)}$$ tiến sâu hơn về cực tiểu riêng của $$f$$.

### Giải thích: Chạy tay 3 vòng lặp Proximal ADMM và thấy vì sao cả hai phần dư đều quan trọng

Xét bài toán $$\min_x \underbrace{\frac{1}{2}(x - 4)^2}_{f(x)} + \underbrace{|x|}_{g(x)}$$ (nghiệm chính xác là $$x^\star = 3$$ vì $$(3 - 4) + 1 = 0$$). Chọn $$\rho = 1$$ (nên $$1/\rho = 1$$), ta tính sẵn hai toán tử proximal:
- $$\operatorname{prox}_{f, 1}(v) = \arg\min_x \left(\frac{1}{2}(x - 4)^2 + \frac{1}{2}(x - v)^2\right) = \frac{v + 4}{2}$$.
- $$\operatorname{prox}_{g, 1}(v) = S_1(v)$$ (ngưỡng mềm với ngưỡng $$1$$).

Khởi tạo $$z^{(0)} = 0, w^{(0)} = 0$$:

1. **Vòng 1:**
   - $$x^{(1)} = \operatorname{prox}_{f, 1}(0 - 0) = \frac{0 + 4}{2} = 2.0$$.
   - $$z^{(1)} = S_1(2.0 + 0) = 1.0$$.
   - $$w^{(1)} = 0 + 2.0 - 1.0 = 1.0$$.
2. **Vòng 2:**
   - $$x^{(2)} = \operatorname{prox}_{f, 1}(1.0 - 1.0) = \frac{0 + 4}{2} = 2.0$$.
   - $$z^{(2)} = S_1(2.0 + 1.0) = S_1(3.0) = 2.0$$.
   - $$w^{(2)} = 1.0 + 2.0 - 2.0 = 1.0$$.
   *(Lưu ý cực thú vị: tại Vòng 2, phần dư gốc $$r^{(2)} = x^{(2)} - z^{(2)} = 0$$ đã bằng 0, nhưng phần dư đối ngẫu $$s^{(2)} = z^{(2)} - z^{(1)} = 1.0 \ne 0$$ — nên thuật toán **không** dừng tại $$2.0$$ mà tiếp tục đi!)*
3. **Vòng 3:**
   - $$x^{(3)} = \operatorname{prox}_{f, 1}(2.0 - 1.0) = \frac{1.0 + 4}{2} = 2.5$$.
   - $$z^{(3)} = S_1(2.5 + 1.0) = S_1(3.5) = 2.5$$.
   - $$w^{(3)} = 1.0 + 2.5 - 2.5 = 1.0$$.
   Cứ thế ở vòng $$k \ge 2$$, $$x^{(k)} = z^{(k)} = 3 - 2^{2-k} \to 3 = x^\star$$!

---

# Mối liên hệ với toán tử proximal

Xét bài toán tối ưu một biến với hàm mục tiêu là tổng của hai hàm:
>$$
>\begin{align}
>\min_{x} f(x)+g(x)
>\end{align}
>$$

Ta có thể viết lại bài toán này bằng cách tách biến và thêm một ràng buộc đẳng thức:
>$$
>\begin{align}
>\min_{x, z} f(x)+g(z) \qquad \text{subject to  }x=z
>\end{align}
>$$

## Các bước ADMM dưới dạng proximal

Áp dụng ADMM dạng chuẩn hóa cho bài toán trên, ta thu được các bước cập nhật:
>$$
>\begin{align}
>&x^{(k)} = {\operatorname{prox}}_{f,\frac{1}{\rho}}(z^{(k-1)}-w^{(k-1)})\\\\
>&z^{(k)} = {\operatorname{prox}}_{g,\frac{1}{\rho}}(x^{(k)}+w^{(k-1)})\\\\
>&w^{(k)}=w^{(k-1)}+x^{(k)}-z^{(k)}
>\end{align}
>$$

trong đó $$\operatorname{prox}_{f,\frac{1}{\rho}}$$ và $$\operatorname{prox}_{g,\frac{1}{\rho}}$$ lần lượt là các toán tử proximal của $$f$$ và $$g$$ với tham số $$\frac{1}{\rho}$$.

## Định nghĩa toán tử proximal

Nhắc lại rằng với một hàm lồi $$f$$, [toán tử proximal]({% multilang_post_url contents/chapter19/21-03-24-19_01_01_Reminder:_proximal_gradient_descent %}) được định nghĩa là:
>$$
>\begin{align}
>{\operatorname{prox}}_{f, \lambda}(v) = \underset{x}{\operatorname{argmin}}\left(f(x)+\frac{1}{2\lambda}||x-v||_{2}^{2}\right). 
>\end{align}
>$$

## Suy diễn các bước cập nhật proximal

Gọi $$x^{+}, z^{+}, w^{+}$$ là các giá trị mới của $$x, z, w$$ sau một vòng lặp. Ta suy ra biểu thức proximal của từng bước như sau:

### Cập nhật cho $$x$$:
>$$
>\begin{align}
>x^{+}& = \underset{x}{\operatorname{argmin}}f(x)+\frac{\rho}{2}||x-z+w||^{2}_{2}\\\\
>& =\underset{x}{\operatorname{argmin}}\frac{1}{2\cdot\frac{1}{\rho}}||(z-w)-x||^{2}_{2}+f(x)\\\\
>& ={\operatorname{prox}}_{f,\frac{1}{\rho}}(z-w)
>\end{align}
>$$

### Cập nhật cho $$z$$:
>$$
>\begin{align}
>z^{+}& = \underset{z}{\operatorname{argmin}}g(z)+\frac{\rho}{2}||x^{+}-z+w||^{2}_{2}\\\\
>& =\underset{z}{\operatorname{argmin}}\frac{1}{2\cdot\frac{1}{\rho}}||(x^{+}+w)-z||^{2}_{2}+g(z)\\\\
>& ={\operatorname{prox}}_{g,\frac{1}{\rho}}(x^{+}+w)
>\end{align}
>$$

## Nhận xét chính

Trong bài toán ADMM tổng quát, ràng buộc có dạng $$Ax+Bz = c$$, còn ở đây ràng buộc đơn giản là $$x=z$$. Khi quan hệ tuyến tính giữa $$x$$ và $$z$$ là phép đồng nhất, hai bước cập nhật biến gốc của ADMM trở thành hai phép tính toán tử proximal liên tiếp trên $$f$$ và $$g$$.
