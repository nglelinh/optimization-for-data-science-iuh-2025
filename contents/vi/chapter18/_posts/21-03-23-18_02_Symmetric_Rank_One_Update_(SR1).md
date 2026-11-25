---
layout: post
title: 18-02 Cập nhật Hạng-một Đối xứng (SR1)
chapter: '18'
order: 3
owner: Hooncheol Shin
categories:
- chapter18
lang: vi
---

Nếu muốn chỉnh sửa ma trận đối xứng $$B$$ theo cách tiết kiệm nhất có thể để nó thỏa mãn phương trình secant $$B^+ s = y$$, lựa chọn tối giản nhất là cộng thêm một ma trận đối xứng **hạng 1** có dạng $$a u u^T$$. Điều kỳ diệu là chỉ riêng yêu cầu đối xứng và hạng 1 đã khóa chặt hoàn toàn công thức cập nhật — chỉ có **duy nhất một** công thức SR1! Dù có điểm yếu chí mạng là có thể làm mất tính xác định dương hoặc chia cho mẫu số gần bằng không, SR1 lại sở hữu một siêu năng lực đặc biệt: nó xấp xỉ rất sát cả những Hessian không xác định (indefinite) trong các phương pháp vùng tin cậy (trust-region).

## Bản đồ kiến thức nền: Ba đặc tính toán học làm nên cá tính của SR1

Trước khi đi vào phép suy diễn đại số của SR1, hãy nắm rõ ba điểm mạnh và giới hạn của công thức hạng-một này:

- **Tính duy nhất của cập nhật đối xứng hạng 1:** Thay $$B^+ = B + auu^T$$ vào $$B^+ s = y$$ ép vector $$u$$ phải song song với vector sai lệch $$y - Bs$$. Khi mẫu số $$(y - Bs)^T s \ne 0$$, công thức $$B^+ = B + \frac{(y-Bs)(y-Bs)^T}{(y-Bs)^T s}$$ là nghiệm duy nhất.
- **Tính bất biến qua phép nghịch đảo (Self-Duality):** Khi áp dụng công thức Sherman–Morrison để lấy nghịch đảo $$H^+ = (B^+)^{-1}$$, công thức cập nhật cho $$H$$ có hình dạng hoàn toàn y hệt công thức cho $$B$$ (chỉ đổi chỗ $$B \leftrightarrow H$$ và $$s \leftrightarrow y$$).
- **Mất tính xác định dương và cơ chế bỏ qua bước (Skipping):** Ngay cả khi $$B \succ 0$$ và $$y^T s > 0$$, mẫu số $$(y - Bs)^T s$$ vẫn có thể âm (làm $$B^+$$ mất tính xác định dương) hoặc gần bằng $$0$$ (làm $$B^+$$ nổ lớn). Trong thực hành, ta bỏ qua cập nhật nếu $$|s^T(y - Bs)| < r \|s\| \|y - Bs\|$$ (thường $$r = 10^{-8}$$), và kết hợp SR1 với vùng tin cậy thay vì line search thuần túy.

### Khung giải thích (nên đọc chậm): Tính tay một bước SR1 trên ma trận $$2 \times 2$$ và kiểm chứng secant

Giả sử ta bắt đầu với xấp xỉ Hessian $$B_0 = I = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$$, và sau một bước tối ưu thu được $$s = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$$, $$y = \begin{bmatrix} 3 \\ 1 \end{bmatrix}$$:

1. **Tính vector sai lệch secant $$v = y - B_0 s$$:**
   $$v = \begin{bmatrix} 3 \\ 1 \end{bmatrix} - \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}\begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 2 \\ 1 \end{bmatrix}.$$
2. **Tính mẫu số $$v^T s$$:**
   $$v^T s = (2)(1) + (1)(0) = 2 \ne 0.$$
   (Mẫu số dương và cách xa $$0$$ nên phép cập nhật hoàn toàn an toàn!).
3. **Tính ma trận hiệu chỉnh hạng 1 và $$B_1$$:**
   $$\frac{vv^T}{v^T s} = \frac{1}{2}\begin{bmatrix} 2 \\ 1 \end{bmatrix}\begin{bmatrix} 2 & 1 \end{bmatrix} = \begin{bmatrix} 2 & 1 \\ 1 & 0.5 \end{bmatrix} \implies B_1 = I + \begin{bmatrix} 2 & 1 \\ 1 & 0.5 \end{bmatrix} = \begin{bmatrix} 3 & 1 \\ 1 & 1.5 \end{bmatrix}.$$
4. **Kiểm chứng phương trình secant và tính xác định dương:**
   - $$B_1 s = \begin{bmatrix} 3 & 1 \\ 1 & 1.5 \end{bmatrix}\begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 3 \\ 1 \end{bmatrix} = y$$ — khớp chính xác!
   - Định thức $$\det(B_1) = (3)(1.5) - 1^2 = 3.5 > 0$$ và vết $$= 4.5 > 0$$, nên trong ví dụ này $$B_1 \succ 0$$.
5. **Thử đổi $$y = (0.5, 1)^T$$ để thấy rủi ro của SR1:** Khi đó $$v = (-0.5, 1)^T$$, $$v^T s = -0.5 < 0$$ dù $$y^T s = 0.5 > 0$$! Ta được $$B_1 = \begin{bmatrix} 0.5 & 1 \\ 1 & -1 \end{bmatrix}$$ có $$\det = -1.5 < 0$$ — **mất tính xác định dương**! Đây chính là động lực để Davidon, Fletcher và Powell nâng cấp lên cập nhật hạng 2 ở bài tiếp theo.

---

Cập nhật hạng-một đối xứng (Symmetric Rank-One — SR1) cộng thêm vào $$B$$ một ma trận đối xứng hạng 1 sao cho $$B^+$$ giữ được tính đối xứng và thỏa mãn phương trình secant. Biểu diễn ma trận đối xứng hạng 1 dưới dạng tích của $$a \in \left\{-1, 1\right\}$$ và vector $$u \in \mathbb{R}^n$$, công thức cập nhật có dạng:

>$$B^+ = B + auu^T.$$

## Quan sát chính
Ta cần chọn $$a$$ và $$u$$ để $$B^+$$ thỏa mãn phương trình secant $$y = B^+s$$. Thay dạng cập nhật trên vào phương trình secant:

>$$y = B^+s \Rightarrow y = Bs + (au^Ts)u. \quad \text{--- (1)}$$

Vì $$au^Ts$$ là một đại lượng vô hướng, vector $$u$$ phải cùng phương với $$y - Bs$$, tức là $$u = \delta(y - Bs)$$ với $$\delta$$ là một số thực khác 0. Thay $$u = \delta(y - Bs)$$ vào (1):

>$$y-Bs = a\delta^2 \big[ s^T(y - Bs) \big] (y -Bs),$$

Để đẳng thức trên đúng (khi $$y - Bs \neq 0$$ và $$s^T(y - Bs) \neq 0$$), ta cần chọn $$a$$ và $$\delta$$ như sau:

>$$a = \text{sign} \big[ s^T (y - Bs) \big], \quad \delta = \pm | s^T(y-Bs) |^{-1/2}. \quad \text{--- (2)}$$

## Công thức cập nhật SR1 duy nhất
Thay $$u = \delta (y - Bs)$$ cùng các giá trị trong (2) vào $$B^+ = B + auu^T$$, ta thu được công thức cập nhật SR1 duy nhất ([14] mục 6.2):

>$$
>B^+ = B + \frac{(y-Bs)(y-Bs)^T}{(y-Bs)^Ts}.
>$$

## Công thức cập nhật cho xấp xỉ nghịch đảo Hessian

Để tính bước cập nhật $$x^+$$, ta cần tác động của $$B^{-1}$$:

>$$x^+ = x + tp = x - tB^{-1}\nabla f(x)$$

Nếu có thể cập nhật trực tiếp $$H = B^{-1}$$ thay vì cập nhật $$B$$ rồi giải hệ tuyến tính, ta sẽ tránh được chi phí nghịch đảo ma trận ở mỗi vòng lặp. Áp dụng [công thức Sherman–Morrison](https://en.wikipedia.org/wiki/Sherman%E2%80%93Morrison_formula), ta thu được công thức cập nhật tương ứng cho $$H = B^{-1}$$ có cấu trúc hoàn toàn tương tự:

>$$
>H^+ = H + \frac{(s-Hy)(s-Hy)^T}{(s-Hy)^Ty}.
>$$

## Nhược điểm của SR1

Dù rất đơn giản, cập nhật SR1 có hai nhược điểm đáng kể:

1. Phép cập nhật có thể mất ổn định hoặc không xác định khi mẫu số $$(y - Bs)^Ts$$ tiến về $$0$$.
2. Không đảm bảo bảo toàn tính xác định dương của $$B$$ và $$H$$ (ngay cả khi điều kiện độ cong $$s^Ty > 0$$ được thỏa mãn).

Các phần tiếp theo sẽ trình bày những công thức cập nhật khắc phục hai hạn chế này của SR1.