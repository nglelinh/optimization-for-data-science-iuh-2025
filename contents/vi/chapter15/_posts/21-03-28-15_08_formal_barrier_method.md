---
layout: post
title: '15-08 Phương pháp chắn chính thức'
chapter: "15"
categories:
- chapter16
order: 14
owner: "Minjoo Lee"
lang: vi
---

Ở các mục trước, ta đã xây dựng phương pháp chắn dựa trên hàm chắn logarit cho ràng buộc vô hướng $$h_i(x) \le 0$$. Nhưng nếu bài toán là **Quy hoạch nón bậc hai (SOCP)** hay **Quy hoạch nửa xác định (SDP)** (nơi biến là ma trận $$X \succeq 0$$, ràng buộc không phải là $$m$$ bất đẳng thức vô hướng mà là một nón lồi tổng quát), thì toàn bộ lý thuyết có còn đứng vững không?

Mục 15-08 đưa phương pháp chắn lên tầm khái quát cao nhất của tối ưu lồi hiện đại nhờ định nghĩa **hàm chắn tự hài hòa với tham số $$\nu$$ ($$\nu$$-self-concordant barrier)** của Nesterov và Nemirovskii. Chỉ cần hàm chắn $$\phi$$ thỏa hai bất đẳng thức gọn nhẹ (tự hài hòa và bình phương Newton decrement $$\lambda_\phi(x)^2 \le \nu$$), toàn bộ định lý hội tụ thời gian đa thức $$O\bigl(\sqrt{\nu}\log(\nu/(\epsilon t^{(0)}))\bigr)$$ tự động áp dụng cho **mọi lớp bài toán lồi**: LP, QP, SOCP và SDP!

## Kiến thức cần nhớ: Bốn mảnh ghép của Phương pháp chắn chính thức

- **Định nghĩa $$\nu$$-self-concordant barrier:** Hàm lồi $$\phi$$ trên miền mở $$D$$ thỏa hai điều kiện:
  1. $$\phi$$ là hàm tự hài hòa ($$\vert g'''(0) \vert \le 2(g''(0))^{3/2}$$ dọc mọi đường thẳng).
  2. $$\nabla \phi(x)^T (\nabla^2 \phi(x))^{-1} \nabla \phi(x) \le \nu$$ với mọi $$x \in D$$ (bình phương Newton decrement của riêng $$\phi$$ bị chặn đều bởi tham số độ phức tạp $$\nu$$!).
- **Tham số $$\nu$$ cho các nón chuẩn:**
  - Nón không âm $$\mathbb{R}_+^m$$ với $$\phi(x) = -\sum_{i=1}^m \log x_i$$: $$\nu = m$$.
  - Nón bậc hai $$\{(x, t) : \|x\|_2 \le t\}$$ với $$\phi(x, t) = -\log(t^2 - \|x\|_2^2)$$: $$\nu = 2$$ (độc lập với số chiều $$n$$!).
  - Nón ma trận nửa xác định dương $$\mathbb{S}_+^n$$ với $$\phi(X) = -\log\det X$$: $$\nu = n$$.
- **Định lý độ phức tạp thời gian đa thức:** Với bước tăng ngắn $$\mu = 1 + \frac{c}{\sqrt{\nu}}$$, sau mỗi lần tăng $$t \leftarrow \mu t$$, chỉ cần đúng **1 bước Newton** để quay lại gần đường trung tâm, dẫn tới tổng số bước Newton là $$O\bigl(\sqrt{\nu}\log(\nu / (\epsilon t^{(0)}))\bigr)$$!

### Giải thích: Tính tay tham số $$\nu$$ cho hàm chắn logarit 2 biến $$\phi(x_1, x_2) = -\log x_1 - \log x_2$$

Ta kiểm chứng trực tiếp rằng $$\phi(x_1, x_2) = -\log x_1 - \log x_2$$ trên $$x_1 > 0, x_2 > 0$$ là một hàm chắn tự hài hòa với tham số $$\nu = 2$$ (tức $$m = 2$$):

1. **Tính gradient và Hessian của $$\phi$$:**
   $$\nabla \phi(x) = \begin{bmatrix} -1/x_1 \\ -1/x_2 \end{bmatrix}, \qquad \nabla^2 \phi(x) = \begin{bmatrix} 1/x_1^2 & 0 \\ 0 & 1/x_2^2 \end{bmatrix}.$$
2. **Tính nghịch đảo Hessian:**
   $$(\nabla^2 \phi(x))^{-1} = \begin{bmatrix} x_1^2 & 0 \\ 0 & x_2^2 \end{bmatrix}.$$
3. **Tính bình phương Newton decrement $$\lambda_\phi(x)^2 = \nabla \phi(x)^T (\nabla^2 \phi(x))^{-1} \nabla \phi(x)$$:**
   $$\lambda_\phi(x)^2 = \left(-\frac{1}{x_1}\right) x_1^2 \left(-\frac{1}{x_1}\right) + \left(-\frac{1}{x_2}\right) x_2^2 \left(-\frac{1}{x_2}\right) = 1 + 1 = 2.$$
   Giá trị này bằng đúng $$\nu = 2$$ tại **mọi điểm** $$(x_1, x_2) > 0$$! Tương tự, với $$m$$ ràng buộc tuyến tính độc lập, $$\lambda_\phi(x)^2 = m$$, giải thích vì sao tham số độ phức tạp của quy hoạch tuyến tính chính là $$\nu = m$$!

---

Một hàm lồi $$\phi : D \to \mathbb{R}$$ xác định trên tập lồi mở $$D \subset \mathbb{R}^n$$ được gọi là **hàm chắn tự hài hòa (self-concordant barrier)** với tham số $$\nu$$ nếu thỏa mãn hai điều kiện:

* $$\phi$$ là hàm tự hài hòa (self-concordant).
* Với mọi $$x \in D$$, bình phương đại lượng giảm Newton (Newton decrement) của $$\phi$$ bị chặn bởi $$\nu$$:

> $$\lambda(x)^2 = \nabla \phi(x)^T (\nabla^2 \phi(x))^{-1} \nabla \phi(x) \le \nu$$

Xét bài toán quy hoạch tuyến tính (LP) sau, với $$\bar{D}$$ là bao đóng của miền $$D$$:
>
$$\begin{align}
&\min_{x} \           && c^Tx \\
&\text{subject to } \ && x \in \bar{D}  \\
\end{align}$$

Bài toán này được xấp xỉ bởi bài toán chắn không ràng buộc:
>
$$\begin{align}
&\min_{x} && tc^Tx + \phi(x) \\
\end{align}$$

Đặt $$\phi_t(x) := tc^Tx + \phi(x)$$ và gọi $$\lambda_t(x)$$ là đại lượng giảm Newton tương ứng của $$\phi_t$$.

Nhận xét quan trọng: khi tăng tham số lên $$t^+ > t$$, ta có bất đẳng thức:
>
$$\begin{align}
\lambda_{t^+}(x) \le & \frac{t^+}{t}\lambda_t(x) + \left ( \frac{t^+}{t} -1 \right ) \sqrt{\nu}  \\\
\end{align}$$

## Định lý

>$$
>\begin{align}
>& \text{nếu} \quad \lambda_t(x) \le \frac{1}{9} \quad \text{và} \quad \frac{t^+}{t} \le 1 + \frac{1}{8 \sqrt{\nu}} \quad \text{thì} \quad \lambda_{t^+}(x^+) \le \frac{1}{9}  \\
>& \qquad \qquad \text{với} \quad x^+ = x - (\nabla^2 \phi_{t^+}(x))^{-1} \nabla \phi_{t^+}(x)
>\end{align}
>$$

Kết quả này cho thấy nếu xuất phát từ $$x^{(0)}, t^{(0)}$$ thỏa $$\lambda_{t^{(0)}}(x^{(0)}) \lt \frac{1}{9}$$ và chọn hệ số tăng $$\mu := 1 + \frac{1}{8 \sqrt{\nu}}$$, thì mỗi bước định tâm chỉ cần đúng một bước Newton là đủ duy trì điều kiện bám đường trung tâm.
