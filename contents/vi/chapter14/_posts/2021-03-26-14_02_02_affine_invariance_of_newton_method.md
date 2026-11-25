---
layout: post
title: 14-02-02 Tính bất biến affine của phương pháp Newton
chapter: '14'
order: 7
owner: Minjoo Lee
categories:
- chapter14
lang: vi
---

Trong học máy, một trong những quy tắc đầu tiên bạn được dặn khi chạy Gradient Descent là: *"Hãy chuẩn hóa (standardize) các đặc trưng về cùng thang đo!"* Lý do rất đơn giản: nếu một biến đo bằng kilômét còn biến kia đo bằng milimét, đường đồng mức sẽ bị kéo dẹt thành một khe nứt hẹp, khiến Gradient Descent lê lết hàng nghìn bước.

Thế nhưng, nếu bạn dùng **Phương pháp Newton**, bạn có thể đổi đơn vị từ mét sang nanômét, xoay trục tọa độ hay kéo xiên hệ trục bằng bất kỳ phép biến đổi affine khả nghịch $$x = Ay$$ nào — và **quỹ đạo hội tụ của phương pháp Newton không hề thay đổi dù chỉ một phần tỷ**! Tính chất đáng kinh ngạc này gọi là **tính bất biến affine (affine invariance)**.

## Kiến thức cần nhớ: Vì sao phép đổi hệ tọa độ không làm phương pháp Newton nao núng?

- **Quy tắc dây chuyền cho gradient và Hessian:** Khi đặt $$x = Ay$$ và xét hàm $$g(y) = f(Ay)$$, ta có $$\nabla g(y) = A^T \nabla f(Ay)$$ và $$\nabla^2 g(y) = A^T \nabla^2 f(Ay) A$$.
- **Sự triệt tiêu kỳ diệu của ma trận $$A$$:** Khi lấy nghịch đảo Hessian của $$g$$ nhân với gradient của $$g$$:
  $$(\nabla^2 g(y))^{-1}\nabla g(y) = A^{-1} (\nabla^2 f(Ay))^{-1} (A^T)^{-1} A^T \nabla f(Ay) = A^{-1}(\nabla^2 f(x))^{-1}\nabla f(x).$$
  Do đó $$y^+ = y - A^{-1}\Delta x_{\text{nt}} \implies Ay^+ = x - \Delta x_{\text{nt}} = x^+$$!
- **Tại sao Gradient Descent thất bại:** Trong GD, bước cập nhật $$y^+ = y - t A^T \nabla f(Ay)$$ khi nhân ngược với $$A$$ trở thành $$Ay^+ = x - t (A A^T) \nabla f(x)$$, bị méo đi bởi ma trận $$A A^T$$ trừ khi $$A$$ là ma trận trực giao.

### Giải thích: Kiểm chứng số tính bất biến affine dưới phép kéo giãn trục 10 lần

Xét hàm 1 chiều $$f(x) = e^x - 2x$$ tại $$x^{(0)} = 1$$, và thực hiện phép đổi đơn vị kéo giãn 10 lần $$x = 10y$$ (tức $$A = 10$$, điểm khởi tạo tương ứng $$y^{(0)} = 0.1$$). Hàm mới là $$g(y) = f(10y) = e^{10y} - 20y$$.

1. **Bước Newton trong không gian gốc $$x$$ (tại $$x^{(0)} = 1$$):**
   - $$f'(1) = e - 2 \approx 0.71828$$, $$f''(1) = e \approx 2.71828$$.
   - $$x^{(1)} = 1 - \frac{e - 2}{e} = \frac{2}{e} \approx 0.73576$$.
2. **Bước Newton trong không gian đổi đơn vị $$y$$ (tại $$y^{(0)} = 0.1$$):**
   - $$g'(0.1) = 10e^{1} - 20 = 10(e - 2)$$.
   - $$g''(0.1) = 100e^{1}$$.
   - $$y^{(1)} = 0.1 - \frac{10(e - 2)}{100e} = 0.1 - \frac{e - 2}{10e} = \frac{2}{10e} \approx 0.073576$$.
   - Đổi ngược sang không gian $$x$$: $$10 y^{(1)} = \frac{2}{e} = x^{(1)}$$ — **khớp tuyệt đối!**
3. **So sánh với Gradient Descent (cùng bước $$t = 0.1$$):**
   - Trong không gian $$x$$: $$x^{(1)}_{\text{GD}} = 1 - 0.1(0.71828) = 0.92817$$.
   - Trong không gian $$y$$: $$y^{(1)}_{\text{GD}} = 0.1 - 0.1(7.1828) = -0.61828 \implies 10y^{(1)}_{\text{GD}} = -6.1828$$ (bay vọt ra rất xa, khác hẳn $$0.92817$$!).

---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

Một tính chất quan trọng của phương pháp Newton là tính bất biến affine: hướng cập nhật không phụ thuộc vào các phép biến đổi affine của hệ tọa độ. Ngược lại, gradient descent không có tính chất này nên tốc độ hội tụ thay đổi tùy theo hệ tọa độ được chọn.

Trang này chứng minh tính chất bất biến affine của phương pháp Newton.

## Chứng minh tính bất biến affine
Cho $$f:\mathbb{R}^{n}\rightarrow \mathbb{R}$$ khả vi hai lần và ma trận không suy biến $$A\in \mathbb{R}^{n\times n}$$. Định nghĩa hàm $$g(y) := f(Ay)$$, tức là hàm $$g$$ tại $$y$$ có cùng giá trị với hàm $$f$$ tại điểm biến đổi affine $$Ay$$. Để tránh nhầm lẫn về ký hiệu và đối số của gradient, ta đặt $$x := Ay$$.

Áp dụng quy tắc chuỗi để lấy đạo hàm bậc nhất và bậc hai của $$g$$, ta thu được:

>$$
>\begin{align}
>\nabla g(y) &= A^{T} \nabla f(x)\\\\
>\nabla^{2} g(y) &= A^{T}\nabla^{2}f(x)A,
>\end{align}
>$$

Bước Newton của $$g$$ theo biến $$y$$ là:

>$$
>\begin{align}
>y^{+}  = y-(\nabla^{2}g(y))^{-1}\nabla g(y).
>\end{align}
>$$

Biểu diễn bước cập nhật này theo $$f$$ và $$x$$, ta suy ra bước Newton cho $$f$$ tại $$x$$:

>$$
>\begin{align}
>y^{+} &= y-(A^{T}\nabla^{2}f(x)A)^{-1}A^{T} \nabla f(x)\\\\
>\Leftrightarrow y^{+} &= y-A^{-1}(\nabla^{2}f(x))^{-1}(A^{T})^{-1}A^{T} \nabla f(x)\\\\
>\Leftrightarrow Ay^{+} &= Ay-(\nabla^{2}f(x))^{-1}\nabla f(x)\\\\
>\Leftrightarrow x^{+} &= x - \nabla^{2}f(x)^{-1}\nabla f(x).
>\end{align}
>$$

Kết quả này cho thấy bước Newton bất biến affine: các bước cập nhật trong hệ tọa độ đã biến đổi bởi ma trận không suy biến $$A$$ hoàn toàn tương đương với các bước cập nhật trong hệ tọa độ gốc.

Thực hiện kiểm tra tương tự cho gradient descent, ta thu được:

>$$
>\begin{align}
>y^{+} &= y-t_{k}\cdot \nabla g(y)\\\\
>\Leftrightarrow y^{+} &= y-t_{k}\cdot A^{T}\nabla f(x)\\\\
>\Leftrightarrow x^{+} &= x - t_{k}\cdot AA^{T}\nabla f(x). 
>\end{align}
>$$

Với gradient descent, do ma trận Hessian được xấp xỉ bởi $$\frac{1}{t}I$$, hướng cập nhật bị thay đổi khi áp dụng phép biến đổi affine lên hệ tọa độ (trừ trường hợp đặc biệt $$AA^T$$ tỉ lệ với ma trận đơn vị).