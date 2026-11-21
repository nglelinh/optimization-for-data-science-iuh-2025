---
layout: post
title: '14-05 Phân tích hội tụ'
chapter: '14'
order: 9
owner: Minjoo Lee
categories:
- chapter14
lang: vi
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
    });
</script>

Cho đến nay, chúng ta đã xem xét phương pháp Newton thuần túy, chỉ có tính chất hội tụ cục bộ, và phương pháp Newton có giảm chấn (phương pháp Newton với tìm kiếm đường backtracking), áp dụng tìm kiếm đường backtracking để đảm bảo hội tụ toàn cục khi lồi.

Trong chương này, chúng ta phân tích tốc độ hội tụ của phương pháp Newton có giảm chấn. Đối với phương pháp Newton có giảm chấn, chúng ta xem xét các cận hội tụ được chia thành hai giai đoạn: giai đoạn mà backtracking được áp dụng (giai đoạn giảm chấn: tiến bộ chậm) và giai đoạn hội tụ cục bộ mà backtracking không còn cần thiết (giai đoạn thuần túy: hội tụ bậc hai).


## Các điều kiện của $$f$$ cho phân tích hội tụ
Giả sử $$f$$ lồi, khả vi hai lần, có $$dom(f)=\mathbb{R}^{n}$$ và thỏa mãn ba điều kiện sau:

1. $$\nabla f$$ liên tục Lipschitz với tham số L.
>$$\begin{align}
>\|\nabla f(x) - \nabla f(y)\|_{2} \leq L\|x-y\|_{2} \quad \forall x,y.
>\end{align}$$

2. $$f$$ lồi mạnh với tham số m. (Quan hệ giữa cận trên $$L$$ và tính liên tục Lipschitz: [nguồn](https://xingyuzhou.org/blog/notes/strong-convexity), [giáo trình này: 06-03-05]({% multilang_post_url contents/chapter06/21-03-20-06_03_05_look_at_the_conditions_and_practicalities %}))
>$$\begin{align}
>mI\preceq\nabla^{2}f(x)\preceq LI.
>\end{align}$$
3. $$\nabla^{2} f$$ liên tục Lipschitz với tham số M.
>$$\begin{align}
>\|\nabla^{2}f(x)-\nabla^{2}f(y)\|_{2} \leq M\|x-y\|_{2} \quad \forall x,y.
>\end{align}$$

## Phân tích hội tụ
Nếu ba điều kiện trên được thỏa mãn, với $$\eta, \gamma$$ thỏa $$0<\eta \leq m^{2}/M$$ và $$\gamma>0$$, sự hội tụ ở mỗi giai đoạn có thể thu được như sau:

>Giai đoạn I: Giai đoạn "giảm chấn" (damped), $$\|\nabla f(x^{(k)})\|_{2} \geq \eta$$,
>
>$$\begin{align}
>f(x^{(k+1)})-f(x^{(k)}) \leq -\gamma
>\end{align}$$
>
>Giai đoạn II: Giai đoạn "thuần túy" (pure), $$\|\nabla f(x^{(k)})\|_{2}<\eta$$, backtracking chọn $$t = 1$$
>
>$$\begin{align}
>\frac{M}{2m^{2}}\|\nabla f(x^{(k+1)})\|_{2} \leq \bigg( \frac{M}{2m^{2}}\|\nabla f(x^{(k)})\|_{2} \bigg)^{2}.
>\end{align}$$

Lưu ý rằng một khi vào giai đoạn thuần túy, tức là khi điều kiện $$\|\nabla f(x^{(k)})\|_{2}<\eta$$ lần đầu tiên được thỏa mãn ở vòng lặp thứ $$k$$, thì điều kiện này luôn được thỏa mãn ở các vòng lặp sau.

## Phân tích hội tụ theo giá trị tối ưu
Bây giờ ta muốn so sánh sự hội tụ của từng giai đoạn theo hiệu so với giá trị tối ưu.

Với Giai đoạn I, nếu thực hiện $$k$$ vòng lặp bắt đầu từ $$x^{(0)}$$, ta có thể sắp xếp phương trình của từng bước và biểu diễn như sau:

>$$\begin{align}
>\require{cancel}
>& &\cancel{f(x^{(1)})}-f(x^{(0)}) \leq -\gamma \\\\
>& &\cancel{f(x^{(2)})}-\cancel{f(x^{(1)})} \leq -\gamma \\\\
>& &\vdots \\\\
>&+ &f(x^{(k)})-\cancel{f(x^{(k-1)})} \leq -\gamma \\\\
>&= &f(x^{(k)})-f(x^{(0)})\leq -k\gamma.
>\end{align}$$

Trừ $$f^{\star}$$ ở cả hai vế, ta thu được kết quả sau. Gọi $$k_{0}$$ là $$k$$ đầu tiên thỏa $$\|\nabla f(x^{(k)})\|_{2}<\eta$$ (các vòng lặp $$k \le k_0$$ thuộc giai đoạn giảm chấn).
>$$\begin{align}
>f(x^{(k)})-f^{\star} \leq (f(x^{(0)})-f^{\star})-\gamma k \qquad \text{if }k \leq k_{0}
>\end{align}$$

Với Giai đoạn II, giả sử lặp bắt đầu từ $$k_{0}$$ và tiến hành $$k-k_{0}$$ bước. Ngoài ra, dùng $$\|\nabla f(x^{(k_0)})\|_2<\eta \leq m^{2}/M$$ ở trên và tính lồi mạnh, ta có thể sắp xếp phương trình như sau (đặt $$a_k = \frac{M}{2m^{2}}\|\nabla f(x^{(k)})\|_{2}$$, khi đó $$a_{k_0} \leq \frac{1}{2}$$):
>$$\begin{align}
>& &a_{k+1} \leq a_{k}^{2}\\\\
>&\Rightarrow &a_{k} \leq a_{k_0}^{2^{k-k_{0}}} \leq \Big(\frac{1}{2}\Big)^{2^{k-k_{0}}}\\\\
>&\Rightarrow &\|\nabla f(x^{(k)})\|_{2} \leq \frac{2m^{2}}{M}\Big(\frac{1}{2}\Big)^{2^{k-k_{0}}}.
>\end{align}$$

Từ tính lồi mạnh, $$f(y)\geq f(x)+\nabla f(x)^{T}(y-x)+\frac{m}{2}\|y-x\|^{2}_{2}\geq f(x)-\frac{1}{2m}\|\nabla f(x)\|^{2}_{2}$$ với mọi $$y$$, nên
>$$\begin{align}
>f(x^{(k)})-f^{\star} \leq \frac{1}{2m}\|\nabla f(x^{(k)})\|_{2}^{2}\leq \frac{2m^{3}}{M^{2}}\Big(\frac{1}{2}\Big)^{2^{k-k_{0}+1}}.
>\end{align}$$

Do đó, ta có thể tổng hợp sự hội tụ theo từng bước, lấy vòng lặp thứ $$k_{0}$$ làm điểm rẽ nhánh, như sau:

>Định lý: Phương pháp Newton dùng backtracking line search có cận hội tụ hai giai đoạn.
>$$\begin{align}
>&f(x^{(k)})-f^{\star} \leq \begin{cases} (f(x^{(0)})-f^{\star})-\gamma k \qquad &\text{if }k\leq k_{0}\\\\
\frac{2m^{3}}{M^{2}}(\frac{1}{2})^{2^{k-k_{0}+1}} \qquad &\text{if }k>k_{0}.
\end{cases}
>\end{align}$$

>Ở đây, $$\gamma = \frac{\alpha \beta \eta^{2}m}{L^{2}}$$, $$\eta = \min\{1, 3(1-2\alpha)\}\frac{m^{2}}{M}$$, và $$k_{0}$$ là bước mà điều kiện $$\|\nabla f(x^{(k_0)})\|_{2}<\eta$$ bắt đầu được thỏa mãn.

## Chứng minh 1. Giai đoạn giảm chấn (Damped phase)
Trước hết, ta suy ra giai đoạn giảm chấn thỏa $$\|\nabla f(x)\|_{2} \geq \eta$$. Ta suy ra sự hội tụ của giai đoạn giảm chấn thông qua cận dưới của kích thước bước được xác định bởi quá trình backtracking line search. Quan hệ của Newton decrement được dùng thường xuyên trong quá trình chứng minh.

>Ta bắt đầu từ phương trình sau, trong đó đặt $$y=x+t\Delta x_{nt}$$ trong xấp xỉ Taylor của $$f$$ và áp dụng cận trên từ điều kiện Lipschitz.
>
>$$\begin{align}
>f(x+t\Delta x_{nt}) \leq f(x)+t\nabla f(x)^{T}\Delta x_{nt} + \frac{L \|\Delta x_{nt} \|^{2}_{2} }{2}t^{2},
>\end{align}$$
>
Dùng quan hệ giữa Newton decrement, bước cập nhật và ma trận Hessian cùng với tính lồi mạnh, ta có thể triển khai như sau.
>
>$$\begin{align}
>&\text{Vì }\lambda(x)^{2}=\Delta x_{nt}^{T} \nabla^{2} f(x) \Delta x_{nt} \geq m\|\Delta x_{nt}\|^{2}_{2}\text{ và }\nabla f(x)^{T}\Delta x_{nt} = -\lambda(x)^{2},\\\\
>&f(x)+t\nabla f(x)^{T}\Delta x_{nt} + \frac{L \|\Delta x_{nt} \|^{2}_{2} }{2}t^{2} \leq f(x)-t\lambda(x)^{2} + \frac{L}{2m}t^{2}\lambda(x)^{2},
>\end{align}$$
>
>Khi đó, để thỏa điều kiện của backtracking line search, ta xét $$t$$ thỏa bất đẳng thức sau.
>
>$$\begin{align}
>f(x+t\Delta x_{nt}) \leq f(x)-(1-\frac{L}{2m}t)t \lambda(x)^{2}, \qquad \text{ trong đó }0<1-\frac{L}{2m}t \leq \frac{1}{2}
>\end{align}$$
>
>Gọi giá trị lớn nhất của $$t$$ thỏa điều kiện trên là $$\hat{t}$$, ta có $$\hat{t} = \frac{m}{L}$$, và thay vào phương trình gốc ta được:
>
>$$\begin{align}
>f(x+\hat{t}\Delta x_{nt})\leq f(x)-\frac{m}{2L}\lambda(x)^{2} \leq f(x) -\alpha \hat{t} \lambda(x)^{2},
>\end{align}$$
>
>(bất đẳng thức cuối đúng vì $$\alpha < 1/2$$). Vì $$0<\beta\leq 1$$ trong backtracking line search, ta có $$t\geq \beta \frac{m}{L}$$, và sắp xếp lại ta suy ra kết quả cuối cùng.
>
>$$\begin{align}
>f(x^{+})-f(x) &\leq -\alpha t \lambda(x)^{2}\\\\
> &\leq -\alpha\beta \frac{m}{L}\lambda(x)^{2}\\\\
> &\leq -\alpha\beta \frac{m}{L^{2}}\|\nabla f(x)\|^{2}_{2}\\\\
> &\leq -\alpha\beta \eta^{2}\frac{m}{L^{2}},\\\\
> &\gamma = \alpha\beta \eta^{2}\frac{m}{L^{2}}.
>\end{align}$$

(Ở bước thứ ba ta dùng $$\lambda(x)^{2} = \nabla f(x)^{T}\nabla^{2}f(x)^{-1}\nabla f(x) \geq \|\nabla f(x)\|_2^2 / L$$.)

## Chứng minh 2. Giai đoạn thuần túy (Pure phase)
Bây giờ giả sử $$\|\nabla f(x)\|_{2} < \eta$$ và xem xét giai đoạn thuần túy (giai đoạn hội tụ bậc hai). Chứng minh gồm hai phần: chỉ ra rằng không cần cập nhật $$t$$ trong backtracking line search, và chỉ ra rằng tốc độ hội tụ là bậc hai.

>Từ backtracking line search, ta có bất đẳng thức sau.
>
>$$\begin{align}
>\eta \leq 3(1-2\alpha)\frac{m^{2}}{M}.
>\end{align}$$
>
>Ngoài ra, theo điều kiện Lipschitz, với $$t \geq 0$$ thì các điều kiện sau thỏa mãn.
>
>$$\begin{align}
>\|\nabla^{2}f(x+t\Delta x_{nt})-\nabla^{2}f(x)\|_{2} \leq tM \|\Delta x_{nt} \|_{2},\\\\
>| \Delta x_{nt}^{T} \big( \nabla^{2}f(x+t\Delta x_{nt})-\nabla^{2}f(x) \big) \Delta x_{nt}| \leq tM \|\Delta x_{nt} \|_{2}^{3}.
>\end{align}$$
>
>Đặt $$\tilde{f}(t) = f(x+t\Delta x_{nt})$$, khi đó $$\tilde{f}''(t) = \Delta x_{nt}^{T} \nabla^{2}f(x+t\Delta x_{nt})\Delta x_{nt}$$, và thay vào.
>
>$$\begin{align}
>\tilde{f}''(t) \leq \tilde{f}''(0)+tM\|\Delta x_{nt}\|^{3}_{2}
>\end{align}$$
>
>Dùng $$\tilde{f}''(0) = \lambda(x)^{2}$$ và $$\lambda(x)^{2} \geq m\|\Delta x_{nt}\|_{2}^{2}$$ (nên $$\|\Delta x_{nt}\|_2^3 \le \lambda(x)^3/m^{3/2}$$), rồi gộp các bất đẳng thức. Vì $$\tilde{f}'(0) = -\lambda(x)^{2}$$ nên ta có thể sắp xếp như sau.
>
>$$\begin{align}
>\tilde{f}''(t) &\leq \lambda(x)^{2} + t\frac{M}{m^{3/2}}\lambda(x)^{3}, \\\\
>\tilde{f}'(t) &\leq \tilde{f}'(0)+t\lambda(x)^{2} +t^{2}\frac{M}{2m^{3/2}}\lambda(x)^{3}\\\\
>&= -\lambda(x)^{2}+t\lambda(x)^{2} + t^{2}\frac{M}{2m^{3/2}}\lambda(x)^{3}.
>\end{align}$$
>
>Bây giờ lấy tích phân hai vế.
>
>$$\begin{align}
>\tilde{f}(t) \leq \tilde{f}(0) - t\lambda(x)^{2} + t^{2} \frac{1}{2}\lambda(x)^{2} + t^{3}\frac{M}{6m^{3/2}}\lambda(x)^{3}.
>\end{align}$$
>
>Đặt $$t = 1$$, ta thu được kết quả sau.
>
>$$\begin{align}
>f(x+\Delta x_{nt}) \leq f(x) -\frac{1}{2}\lambda(x)^{2} + \frac{M}{6m^{3/2}}\lambda(x)^{3}.
>\end{align}$$
>
>Bây giờ giả sử $$\|\nabla f(x)\|_{2}\leq \eta \leq 3(1-2\alpha)\frac{m^{2}}{M}$$. Do tính lồi mạnh, $$\lambda(x) \leq \|\nabla f(x)\|_{2}/m^{1/2} \leq 3(1-2\alpha)m^{3/2}/M$$. Thay vào bất đẳng thức trên ta suy ra kết quả sau.
>
>$$\begin{align}
>f(x+\Delta x_{nt}) &\leq f(x) - \lambda(x)^{2}( \frac{1}{2}- \frac{M\lambda(x)}{6m^{3/2}} ) \\\\
> &\leq f(x) -\alpha \lambda(x)^{2} \\\\
> &= f(x) + \alpha \nabla f(x)^{T} \Delta x_{nt},
>\end{align}$$
>
>Kết quả này có nghĩa là khi $$t=1$$, điều kiện của backtracking line search luôn được thỏa mãn, nên $$t$$ không bị giảm.

Bây giờ ta chứng minh tốc độ hội tụ giảm theo bậc hai.
>Dùng $$\Delta x_{nt} = -(\nabla^{2}f(x))^{-1}\nabla f(x)$$, rồi dùng tính chất của tích phân $$\nabla f(x+\Delta x_{nt}) - \nabla f(x) = \int^{1}_{0}{\nabla^{2}f(x+t\Delta x_{nt})\Delta x_{nt}\, dt}$$, áp dụng điều kiện Lipschitz của Hessian vào biểu thức tích phân và sắp xếp. Cuối cùng áp dụng điều kiện lồi mạnh thì chứng minh hoàn tất. Quá trình được biểu diễn bằng công thức như sau.
>
>$$\begin{align}
>\| \nabla f(x^{+}) \| _{2} &= \| \nabla f(x+\Delta x_{nt}) - \nabla f(x) - \nabla^{2}f(x)\Delta x_{nt} \|_{2}\\\\
>&=\| \int^{1}_{0}{ \big( \nabla^{2}f(x+t\Delta x_{nt})-\nabla^{2} f(x) \big) \Delta x_{nt} dt } \|_{2}\\\\
> & \leq \frac{M}{2}\|\Delta x_{nt} \|^{2}_{2}\\\\
> & = \frac{M}{2}\|\nabla^{2}f(x)^{-1}\nabla f(x)\|^{2}_{2}\\\\
> & \leq \frac{M}{2m^{2}}\|\nabla f(x)\|^{2}_{2}.
>\end{align}$$

Tóm lại, khi $$\eta = \min \{1, 3(1-2\alpha)\}\frac{m^{2}}{M}$$, trong điều kiện $$\|\nabla f(x^{(k)}) \|_{2}<\eta$$ thì phương pháp Newton không còn cần cập nhật trong backtracking line search nữa và hội tụ bậc hai.

## Ước lượng độ phức tạp tổng thể
Bây giờ ta có thể ước lượng độ phức tạp của toàn bộ quá trình, nói cách khác là cận của số vòng lặp cần để đi từ giá trị khởi tạo đến giá trị tối ưu.
Trước hết, ở giai đoạn Newton giảm chấn ở trên, $$f$$ giảm tối thiểu $$\gamma$$ ở mỗi vòng lặp, nên tổng số bước Newton giảm chấn không vượt quá giá trị của biểu thức sau.
>$$\begin{align}
>\frac{f(x^{(0)})-p^{\star}}{\gamma}.
>\end{align}$$

Ta cũng có thể tính cận cho số vòng lặp ở giai đoạn Newton thuần túy. Đặt $$f(x)-p^{\star}\leq \epsilon$$ và $$\epsilon_{0} = \frac{2m^{3}}{M^{2}}$$ trong công thức trên rồi rút gọn theo số vòng lặp, ta tính được giá trị sau.
>$$\begin{align}
>& &\epsilon = \epsilon_{0} (\frac{1}{2})^{2^{k-k_{0}+1}}\\\\
>&\Leftrightarrow &\frac{\epsilon_{0}}{\epsilon} = 2^{2^{k-k_{0}+1}}\\\\
>&\Leftrightarrow &k-k_{0}+1 = \log_{2}\log_{2}(\frac{\epsilon_{0}}{\epsilon})
>\end{align}$$

Do đó số vòng lặp ở giai đoạn Newton thuần túy bị chặn bởi $$\log \log(\frac{\epsilon_{0}}{\epsilon})$$.

Cộng hai kết quả này, ta có thể định nghĩa cận trên của số vòng lặp cần thiết để thu được nghiệm có độ chính xác mong muốn bằng phương pháp Newton.
>$$\begin{align}
>\frac{f(x^{(0)})-p^{\star}}{\gamma} + \log_2 \log_2 (\frac{\epsilon_{0}}{\epsilon}).
>\end{align}$$

So với sự thay đổi của độ chính xác $$\epsilon$$ yêu cầu khi giải bài toán, số hạng thứ hai ở vế phải thay đổi rất ít, nên trong ứng dụng thực tế người ta coi nó là hằng số khi ước lượng. Thông thường, người ta biết rằng 6 vòng lặp cho độ chính xác $$\epsilon \approx 5\cdot 10^{-20}\epsilon_{0}$$.

Nói chung, số vòng lặp cần thiết để cực tiểu hóa hàm mục tiêu $$f$$ là:
>$$\begin{align}
>\frac{f(x^{(0)})-p^{\star}}{\gamma} + 6.
>\end{align}$$
