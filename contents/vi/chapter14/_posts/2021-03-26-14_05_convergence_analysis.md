---
layout: post
title: '14-05 Phân tích hội tụ'
chapter: '14'
order: 11
owner: Minjoo Lee
categories:
- chapter14
lang: vi
---

Khi ghép phương pháp Newton với tìm kiếm đường backtracking, một câu hỏi lớn đặt ra cho lý thuyết hội tụ: *liệu ta có thể đảm bảo thuật toán hội tụ từ MỌI điểm xuất phát $$x^{(0)}$$, và tổng số vòng lặp để đạt sai số $$\epsilon$$ là bao nhiêu?*

Câu trả lời là một trong những định lý đẹp nhất của tối ưu lồi cổ điển: hành trình của Newton có giảm chấn luôn chia làm **hai giai đoạn tách biệt rõ ràng**. Trong **giai đoạn giảm chấn (damped phase)** khi gradient còn lớn, mỗi vòng lặp đảm bảo cắt giảm giá trị hàm mục tiêu ít nhất một hằng số dương $$\gamma$$ (hội tụ tuyến tính chắc chắn). Ngay khi gradient tụt xuống dưới một ngưỡng tới hạn $$\eta$$, thuật toán bước vào **giai đoạn thuần túy (pure phase)** — bước $$t = 1$$ luôn được chấp nhận và sai số rơi theo hàm mũ kép $$2^{2^k}$$, nghĩa là chỉ cần thêm $$\log_2\log_2(1/\epsilon)$$ vòng lặp (thực tế hầu như không bao giờ quá 6 bước!) để đạt độ chính xác máy tính.

## Kiến thức cần nhớ: Giải phẫu hai giai đoạn hội tụ toàn cục của Newton

- **Ba giả thiết tiêu chuẩn:** Hàm $$f$$ khả vi hai lần, lồi mạnh với tham số $$m > 0$$ ($$\nabla^2 f(x) \succeq mI$$), gradient Lipschitz $$L$$ ($$\nabla^2 f(x) \preceq LI$$), và Hessian Lipschitz $$M$$ ($$\|\nabla^2 f(x) - \nabla^2 f(y)\|_2 \le M\|x-y\|_2$$).
- **Pha 1 — Giai đoạn giảm chấn ($$\|\nabla f(x)\|_2 \ge \eta$$):** Thuật toán có thể cần $$t < 1$$, nhưng mỗi vòng lặp luôn giảm $$f(x)$$ ít nhất một lượng hằng số $$\gamma > 0$$. Do đó số vòng lặp ở Pha 1 bị chặn trên bởi $$\frac{f(x^{(0)}) - f^\star}{\gamma}$$.
- **Pha 2 — Giai đoạn thuần túy ($$\|\nabla f(x)\|_2 < \eta$$):** Ngay khi vượt ngưỡng $$\eta$$, bước $$t = 1$$ luôn thỏa Armijo và sai số giảm bình phương sau mỗi bước, nên chỉ cần thêm tối đa $$\log_2\log_2(\epsilon_0/\epsilon)$$ vòng lặp.
- **Ý nghĩa thực tế của $$\log_2\log_2(1/\epsilon)$$:** Ngay cả khi bạn đòi hỏi độ chính xác cực khắt khe $$\epsilon = 10^{-15}$$, giá trị $$\log_2\log_2(10^{15}) \approx \log_2(50) \approx 5.6$$ — tức là một khi đã vào vùng bậc hai, **tối đa 6 bước Newton là xong!**

### Giải thích: Đếm số vòng lặp qua từng pha bằng con số cụ thể

Giả sử một bài toán lồi mạnh có giá trị ban đầu $$f(x^{(0)}) - f^\star = 20$$, mức giảm đảm bảo mỗi bước ở Pha 1 là $$\gamma = 2$$, và ngưỡng chuyển pha tương ứng sai số mục tiêu $$\epsilon_0 = 0.5$$. Hãy tính tổng số vòng lặp tối đa để đạt hai mức độ chính xác khác nhau: $$\epsilon = 10^{-4}$$ và $$\epsilon = 10^{-16}$$:

1. **Số vòng lặp ở Pha 1 (giảm chấn):**
   $$k_1 \le \frac{f(x^{(0)}) - f^\star}{\gamma} = \frac{20}{2} = 10 \text{ bước}.$$
   Lưu ý $$k_1$$ **không hề phụ thuộc vào $$\epsilon$$**!
2. **Số vòng lặp ở Pha 2 (hội tụ bậc hai) khi $$\epsilon = 10^{-4}$$:**
   Ta cần $$k_2 \approx \log_2\log_2\left(\frac{0.5}{10^{-4}}\right) = \log_2\log_2(5000) \approx \log_2(12.29) \approx 3.62 \implies 4 \text{ bước}.$$
   Tổng: $$10 + 4 = 14$$ bước.
3. **Số vòng lặp ở Pha 2 khi siết chặt sai số lên gấp một nghìn tỷ lần ($$\epsilon = 10^{-16}$$):**
   Ta cần $$k_2 \approx \log_2\log_2\left(\frac{0.5}{10^{-16}}\right) = \log_2\log_2(5 \times 10^{15}) \approx \log_2(52.15) \approx 5.70 \implies 6 \text{ bước}.$$
   Tổng: $$10 + 6 = 16$$ bước!
   **So sánh ấn tượng:** Để tăng độ chính xác từ $$10^{-4}$$ lên $$10^{-16}$$ (tốt hơn $$10^{12}$$ lần!), phương pháp Newton chỉ cần thêm đúng **2 vòng lặp**, trong khi Gradient Descent cần tăng gấp **4 lần** số vòng lặp!

---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
    });
</script>

Đến đây, ta đã xét phương pháp Newton thuần túy (chỉ đảm bảo hội tụ cục bộ) và phương pháp Newton có giảm chấn (kết hợp tìm kiếm đường backtracking nhằm đảm bảo hội tụ toàn cục với hàm lồi).

Mục này phân tích tốc độ hội tụ của phương pháp Newton có giảm chấn. Cận hội tụ được tách thành hai giai đoạn: giai đoạn cần thu nhỏ bước bằng backtracking (giai đoạn giảm chấn, tiến bộ chậm hơn) và giai đoạn hội tụ cục bộ khi backtracking luôn chấp nhận $$t = 1$$ (giai đoạn thuần túy, hội tụ bậc hai).

## Các điều kiện của $$f$$ cho phân tích hội tụ
Giả sử $$f$$ lồi, khả vi hai lần, có $$\text{dom}(f)=\mathbb{R}^{n}$$ và thỏa mãn ba điều kiện sau:

1. $$\nabla f$$ liên tục Lipschitz với hằng số $$L$$:
>$$
>\begin{align}
>\|\nabla f(x) - \nabla f(y)\|_{2} \leq L\|x-y\|_{2} \quad \forall x,y.
>\end{align}
>$$

2. $$f$$ lồi mạnh với tham số $$m$$ (xem thêm quan hệ giữa cận trên $$L$$ và tính liên tục Lipschitz tại [nguồn](https://xingyuzhou.org/blog/notes/strong-convexity), [giáo trình này: 06-03-05]({% multilang_post_url contents/chapter06/21-03-20-06_03_05_look_at_the_conditions_and_practicalities %})):
>$$
>\begin{align}
>mI\preceq\nabla^{2}f(x)\preceq LI.
>\end{align}
>$$

3. $$\nabla^{2} f$$ liên tục Lipschitz với hằng số $$M$$:
>$$
>\begin{align}
>\|\nabla^{2}f(x)-\nabla^{2}f(y)\|_{2} \leq M\|x-y\|_{2} \quad \forall x,y.
>\end{align}
>$$

## Phân tích hội tụ
Khi ba điều kiện trên được thỏa mãn, tồn tại $$\eta, \gamma$$ với $$0<\eta \leq m^{2}/M$$ và $$\gamma>0$$ sao cho ở mỗi giai đoạn ta có:

>Giai đoạn I: Giai đoạn "giảm chấn" (damped), $$\|\nabla f(x^{(k)})\|_{2} \geq \eta$$,
>
>$$
>\begin{align}
>f(x^{(k+1)})-f(x^{(k)}) \leq -\gamma
>\end{align}
>$$
>
>Giai đoạn II: Giai đoạn "thuần túy" (pure), $$\|\nabla f(x^{(k)})\|_{2}<\eta$$, backtracking chọn $$t = 1$$:
>
>$$
>\begin{align}
>\frac{M}{2m^{2}}\|\nabla f(x^{(k+1)})\|_{2} \leq \bigg( \frac{M}{2m^{2}}\|\nabla f(x^{(k)})\|_{2} \bigg)^{2}.
>\end{align}
>$$

Lưu ý rằng một khi thuật toán bước vào giai đoạn thuần túy — tức điều kiện $$\|\nabla f(x^{(k)})\|_{2}<\eta$$ lần đầu được thỏa mãn tại vòng lặp $$k$$ — thì điều kiện này tiếp tục được giữ nguyên ở mọi vòng lặp sau đó.

## Phân tích hội tụ theo giá trị tối ưu
Tiếp theo, ta biểu diễn cận hội tụ của từng giai đoạn theo hiệu so với giá trị tối ưu $$f^{\star}$$.

Với Giai đoạn I, cộng dồn bất đẳng thức qua $$k$$ vòng lặp từ $$x^{(0)}$$, ta thu được:

>$$
>\begin{align}
>\require{cancel}
>& &\cancel{f(x^{(1)})}-f(x^{(0)}) \leq -\gamma \\\\
>& &\cancel{f(x^{(2)})}-\cancel{f(x^{(1)})} \leq -\gamma \\\\
>& &\vdots \\\\
>&+ &f(x^{(k)})-\cancel{f(x^{(k-1)})} \leq -\gamma \\\\
>&= &f(x^{(k)})-f(x^{(0)})\leq -k\gamma.
>\end{align}
>$$

Trừ $$f^{\star}$$ ở cả hai vế và gọi $$k_{0}$$ là chỉ số đầu tiên thỏa mãn $$\|\nabla f(x^{(k)})\|_{2}<\eta$$ (các bước $$k \le k_0$$ thuộc giai đoạn giảm chấn):
>$$
>\begin{align}
>f(x^{(k)})-f^{\star} \leq (f(x^{(0)})-f^{\star})-\gamma k \qquad \text{if }k \leq k_{0}
>\end{align}
>$$

Với Giai đoạn II, xét $$k - k_{0}$$ bước kể từ $$k_{0}$$. Đặt $$a_k = \frac{M}{2m^{2}}\|\nabla f(x^{(k)})\|_{2}$$. Từ $$\|\nabla f(x^{(k_0)})\|_2 < \eta \leq m^{2}/M$$ ta có $$a_{k_0} \leq \frac{1}{2}$$, nên:
>$$
>\begin{align}
>& &a_{k+1} \leq a_{k}^{2}\\\\
>&\Rightarrow &a_{k} \leq a_{k_0}^{2^{k-k_{0}}} \leq \Big(\frac{1}{2}\Big)^{2^{k-k_{0}}}\\\\
>&\Rightarrow &\|\nabla f(x^{(k)})\|_{2} \leq \frac{2m^{2}}{M}\Big(\frac{1}{2}\Big)^{2^{k-k_{0}}}.
>\end{align}
>$$

Nhờ tính lồi mạnh, $$f(y)\geq f(x)+\nabla f(x)^{T}(y-x)+\frac{m}{2}\|y-x\|^{2}_{2}\geq f(x)-\frac{1}{2m}\|\nabla f(x)\|^{2}_{2}$$ với mọi $$y$$, suy ra:
>$$
>\begin{align}
>f(x^{(k)})-f^{\star} \leq \frac{1}{2m}\|\nabla f(x^{(k)})\|_{2}^{2}\leq \frac{2m^{3}}{M^{2}}\Big(\frac{1}{2}\Big)^{2^{k-k_{0}+1}}.
>\end{align}
>$$

Gộp hai giai đoạn với mốc chuyển tiếp $$k_{0}$$, ta có định lý sau:

>Định lý: Phương pháp Newton dùng tìm kiếm đường backtracking có cận hội tụ hai giai đoạn:
>$$
>\begin{align}
>&f(x^{(k)})-f^{\star} \leq \begin{cases} (f(x^{(0)})-f^{\star})-\gamma k \qquad &\text{if }k\leq k_{0}\\\\
>\frac{2m^{3}}{M^{2}}(\frac{1}{2})^{2^{k-k_{0}+1}} \qquad &\text{if }k>k_{0}.
>\end{cases}
>\end{align}
>$$
>
>Ở đây, $$\gamma = \frac{\alpha \beta \eta^{2}m}{L^{2}}$$, $$\eta = \min\{1, 3(1-2\alpha)\}\frac{m^{2}}{M}$$, và $$k_{0}$$ là vòng lặp đầu tiên thỏa mãn $$\|\nabla f(x^{(k_0)})\|_{2}<\eta$$.

## Chứng minh 1. Giai đoạn giảm chấn (Damped phase)
Trước hết, xét trường hợp $$\|\nabla f(x)\|_{2} \geq \eta$$. Ta chứng minh mức giảm giá trị hàm trong giai đoạn này thông qua cận dưới của kích thước bước $$t$$ do tìm kiếm đường backtracking chọn, sử dụng các hệ thức của Newton decrement.

>Bắt đầu bằng cách đặt $$y=x+t\Delta x_{nt}$$ vào khai triển Taylor của $$f$$ và áp dụng cận trên từ điều kiện liên tục Lipschitz của gradient:
>
>$$
>\begin{align}
>f(x+t\Delta x_{nt}) \leq f(x)+t\nabla f(x)^{T}\Delta x_{nt} + \frac{L \|\Delta x_{nt} \|^{2}_{2} }{2}t^{2},
>\end{align}
>$$
>
>Kết hợp các hệ thức giữa Newton decrement, bước cập nhật, ma trận Hessian và tính lồi mạnh:
>
>$$
>\begin{align}
>&\text{Vì }\lambda(x)^{2}=\Delta x_{nt}^{T} \nabla^{2} f(x) \Delta x_{nt} \geq m\|\Delta x_{nt}\|^{2}_{2}\text{ và }\nabla f(x)^{T}\Delta x_{nt} = -\lambda(x)^{2},\\\\
>&f(x)+t\nabla f(x)^{T}\Delta x_{nt} + \frac{L \|\Delta x_{nt} \|^{2}_{2} }{2}t^{2} \leq f(x)-t\lambda(x)^{2} + \frac{L}{2m}t^{2}\lambda(x)^{2},
>\end{align}
>$$
>
>Để thỏa mãn điều kiện dừng của backtracking line search, ta xét các giá trị $$t$$ thỏa bất đẳng thức:
>
>$$
>\begin{align}
>f(x+t\Delta x_{nt}) \leq f(x)-(1-\frac{L}{2m}t)t \lambda(x)^{2}, \qquad \text{ trong đó }1-\frac{L}{2m}t \geq \frac{1}{2}
>\end{align}
>$$
>
>Giá trị lớn nhất của $$t$$ thỏa điều kiện trên là $$\hat{t} = \frac{m}{L}$$. Thay $$\hat{t}$$ vào bất đẳng thức, ta được:
>
>$$
>\begin{align}
>f(x+\hat{t}\Delta x_{nt})\leq f(x)-\frac{m}{2L}\lambda(x)^{2} \leq f(x) -\alpha \hat{t} \lambda(x)^{2},
>\end{align}
>$$
>
>(bất đẳng thức cuối đúng vì $$\alpha \leq 1/2$$). Do tham số thu nhỏ bước thỏa $$0<\beta<1$$, bước $$t$$ mà backtracking dừng lại luôn thỏa $$t\geq \beta \frac{m}{L}$$, từ đó suy ra:
>
>$$
>\begin{align}
>f(x^{+})-f(x) &\leq -\alpha t \lambda(x)^{2}\\\\
> &\leq -\alpha\beta \frac{m}{L}\lambda(x)^{2}\\\\
> &\leq -\alpha\beta \frac{m}{L^{2}}\|\nabla f(x)\|^{2}_{2}\\\\
> &\leq -\alpha\beta \eta^{2}\frac{m}{L^{2}},\\\\
> &\gamma = \alpha\beta \eta^{2}\frac{m}{L^{2}}.
>\end{align}
>$$

(Ở bước thứ ba ta dùng bất đẳng thức $$\lambda(x)^{2} = \nabla f(x)^{T}\nabla^{2}f(x)^{-1}\nabla f(x) \geq \|\nabla f(x)\|_2^2 / L$$.)

## Chứng minh 2. Giai đoạn thuần túy (Pure phase)
Bây giờ giả sử $$\|\nabla f(x)\|_{2} < \eta$$. Chứng minh gồm hai phần: chỉ ra rằng bước đầy đủ $$t = 1$$ luôn được chấp nhận bởi backtracking, và chứng minh tốc độ hội tụ là bậc hai.

>Theo cách chọn $$\eta$$, ta có:
>
>$$
>\begin{align}
>\eta \leq 3(1-2\alpha)\frac{m^{2}}{M}.
>\end{align}
>$$
>
>Từ điều kiện liên tục Lipschitz của Hessian, với mọi $$t \geq 0$$:
>
>$$
>\begin{align}
>\|\nabla^{2}f(x+t\Delta x_{nt})-\nabla^{2}f(x)\|_{2} \leq tM \|\Delta x_{nt} \|_{2},\\\\
>| \Delta x_{nt}^{T} \big( \nabla^{2}f(x+t\Delta x_{nt})-\nabla^{2}f(x) \big) \Delta x_{nt}| \leq tM \|\Delta x_{nt} \|_{2}^{3}.
>\end{align}
>$$
>
>Đặt $$\tilde{f}(t) = f(x+t\Delta x_{nt})$$, khi đó $$\tilde{f}''(t) = \Delta x_{nt}^{T} \nabla^{2}f(x+t\Delta x_{nt})\Delta x_{nt}$$, nên:
>
>$$
>\begin{align}
>\tilde{f}''(t) \leq \tilde{f}''(0)+tM\|\Delta x_{nt}\|^{3}_{2}
>\end{align}
>$$
>
>Sử dụng $$\tilde{f}''(0) = \lambda(x)^{2}$$ và $$\lambda(x)^{2} \geq m\|\Delta x_{nt}\|_{2}^{2}$$ (suy ra $$\|\Delta x_{nt}\|_2^3 \le \lambda(x)^3/m^{3/2}$$), đồng thời tích phân từ $$0$$ đến $$t$$ với $$\tilde{f}'(0) = -\lambda(x)^{2}$$:
>
>$$
>\begin{align}
>\tilde{f}''(t) &\leq \lambda(x)^{2} + t\frac{M}{m^{3/2}}\lambda(x)^{3}, \\\\
>\tilde{f}'(t) &\leq \tilde{f}'(0)+t\lambda(x)^{2} +t^{2}\frac{M}{2m^{3/2}}\lambda(x)^{3}\\\\
>&= -\lambda(x)^{2}+t\lambda(x)^{2} + t^{2}\frac{M}{2m^{3/2}}\lambda(x)^{3}.
>\end{align}
>$$
>
>Tiếp tục lấy tích phân hai vế:
>
>$$
>\begin{align}
>\tilde{f}(t) \leq \tilde{f}(0) - t\lambda(x)^{2} + t^{2} \frac{1}{2}\lambda(x)^{2} + t^{3}\frac{M}{6m^{3/2}}\lambda(x)^{3}.
>\end{align}
>$$
>
>Thay $$t = 1$$, ta thu được:
>
>$$
>\begin{align}
>f(x+\Delta x_{nt}) \leq f(x) -\frac{1}{2}\lambda(x)^{2} + \frac{M}{6m^{3/2}}\lambda(x)^{3}.
>\end{align}
>$$
>
>Với giả thiết $$\|\nabla f(x)\|_{2}\leq \eta \leq 3(1-2\alpha)\frac{m^{2}}{M}$$ và tính lồi mạnh, ta có $$\lambda(x) \leq \|\nabla f(x)\|_{2}/m^{1/2} \leq 3(1-2\alpha)m^{3/2}/M$$. Thay vào bất đẳng thức trên:
>
>$$
>\begin{align}
>f(x+\Delta x_{nt}) &\leq f(x) - \lambda(x)^{2}( \frac{1}{2}- \frac{M\lambda(x)}{6m^{3/2}} ) \\\\
> &\leq f(x) -\alpha \lambda(x)^{2} \\\\
> &= f(x) + \alpha \nabla f(x)^{T} \Delta x_{nt},
>\end{align}
>$$
>
>Điều này chứng tỏ điều kiện backtracking luôn thỏa mãn tại $$t = 1$$, nên kích thước bước không bị thu nhỏ.

Tiếp theo, ta chứng minh tốc độ hội tụ là bậc hai.
>Từ $$\Delta x_{nt} = -(\nabla^{2}f(x))^{-1}\nabla f(x)$$ và công thức tích phân $$\nabla f(x+\Delta x_{nt}) - \nabla f(x) = \int^{1}_{0}{\nabla^{2}f(x+t\Delta x_{nt})\Delta x_{nt}\, dt}$$, áp dụng điều kiện liên tục Lipschitz của Hessian cùng tính lồi mạnh, ta thu được:
>
>$$
>\begin{align}
>\| \nabla f(x^{+}) \| _{2} &= \| \nabla f(x+\Delta x_{nt}) - \nabla f(x) - \nabla^{2}f(x)\Delta x_{nt} \|_{2}\\\\
>&=\| \int^{1}_{0}{ \big( \nabla^{2}f(x+t\Delta x_{nt})-\nabla^{2} f(x) \big) \Delta x_{nt} dt } \|_{2}\\\\
> & \leq \frac{M}{2}\|\Delta x_{nt} \|^{2}_{2}\\\\
> & = \frac{M}{2}\|\nabla^{2}f(x)^{-1}\nabla f(x)\|^{2}_{2}\\\\
> & \leq \frac{M}{2m^{2}}\|\nabla f(x)\|^{2}_{2}.
>\end{align}
>$$

Tóm lại, khi $$\eta = \min \{1, 3(1-2\alpha)\}\frac{m^{2}}{M}$$ và $$\|\nabla f(x^{(k)}) \|_{2}<\eta$$, backtracking luôn giữ $$t = 1$$ và phương pháp Newton đạt hội tụ bậc hai.

## Ước lượng độ phức tạp tổng thể
Từ các cận trên, ta ước lượng tổng số vòng lặp cần thiết để đi từ điểm khởi tạo đến độ chính xác mong muốn.
Trong giai đoạn giảm chấn, mỗi bước giảm giá trị hàm ít nhất $$\gamma$$, nên tổng số bước của giai đoạn này không vượt quá:
>$$
>\begin{align}
>\frac{f(x^{(0)})-p^{\star}}{\gamma}.
>\end{align}
>$$

Đối với giai đoạn thuần túy, đặt $$f(x)-p^{\star}\leq \epsilon$$ và $$\epsilon_{0} = \frac{2m^{3}}{M^{2}}$$, giải theo số bước lặp:
>$$
>\begin{align}
>& &\epsilon = \epsilon_{0} (\frac{1}{2})^{2^{k-k_{0}+1}}\\\\
>&\Leftrightarrow &\frac{\epsilon_{0}}{\epsilon} = 2^{2^{k-k_{0}+1}}\\\\
>&\Leftrightarrow &k-k_{0}+1 = \log_{2}\log_{2}(\frac{\epsilon_{0}}{\epsilon})
>\end{align}
>$$

Do đó, số vòng lặp trong giai đoạn Newton thuần túy bị chặn bởi $$\log_{2}\log_{2}(\frac{\epsilon_{0}}{\epsilon})$$.

Cộng hai giai đoạn lại, ta được cận trên cho tổng số vòng lặp để đạt độ chính xác $$\epsilon$$:
>$$
>\begin{align}
>\frac{f(x^{(0)})-p^{\star}}{\gamma} + \log_2 \log_2 (\frac{\epsilon_{0}}{\epsilon}).
>\end{align}
>$$

Vì số hạng thứ hai tăng rất chậm theo độ chính xác $$\epsilon$$ yêu cầu, trong thực hành người ta thường xem nó như một hằng số nhỏ; cụ thể, 6 vòng lặp đã đạt độ chính xác $$\epsilon \approx 5\cdot 10^{-20}\epsilon_{0}$$.

Do đó, tổng số vòng lặp thường được ước lượng là:
>$$
>\begin{align}
>\frac{f(x^{(0)})-p^{\star}}{\gamma} + 6.
>\end{align}
>$$
