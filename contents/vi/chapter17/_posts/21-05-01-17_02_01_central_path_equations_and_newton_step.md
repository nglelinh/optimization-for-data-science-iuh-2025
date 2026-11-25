---
layout: post
title: '17-02-01 Phương trình đường trung tâm và bước Newton'
chapter: '17'
order: 4
owner: Minjoo Lee
categories:
- chapter17
lang: vi
---

Mọi thuật toán Newton đều bắt đầu bằng một câu hỏi cốt lõi: *hệ phương trình phi tuyến cần giải là gì, và ma trận Jacobi của nó trông như thế nào?* Khi gom cả điều kiện dừng đối ngẫu, điều kiện bù chặt bị nhiễu và ràng buộc đẳng thức gốc vào một vector phần dư duy nhất $$r_\tau(x, u, v) = 0$$, ta thu được một hệ phương trình khối cực kỳ cân đối. Giải hệ tuyến tính hóa của nó chính là trái tim của mỗi vòng lặp PD-IPM.

## Bản đồ kiến thức nền: Giải phẫu hệ phương trình Newton gốc–đối ngẫu

Trước khi nhìn vào ma trận khối $$3 \times 3$$ trong bài học, hãy nắm rõ bốn mảnh ghép giải tích và đại số tuyến tính tạo nên nó:

- **Ánh xạ phần dư $$r_\tau(x, u, v)$$:** Ghép ba nhóm phương trình của điều kiện KKT bị nhiễu thành một ánh xạ vector từ $$\mathbb{R}^{n+m+p}$$ vào $$\mathbb{R}^{n+m+p}$$. Điểm trên đường trung tâm ứng với $$\tau$$ chính là không điểm của ánh xạ này.
- **Khai triển Taylor bậc nhất cho hệ vector:** Xấp xỉ $$r_\tau(w + \Delta w) \approx r_\tau(w) + Dr_\tau(w)\Delta w = 0$$ biến bài toán giải hệ phi tuyến thành bài toán giải một hệ phương trình tuyến tính $$Dr_\tau(w)\Delta w = -r_\tau(w)$$.
- **Cấu trúc ma trận Jacobi theo khối:** Hàng thứ nhất chứa Hessian của hàm Lagrange $$\nabla^2 f(x) + \sum_{i=1}^m u_i \nabla^2 h_i(x)$$; hàng thứ hai chứa ma trận đường chéo $$U = \operatorname{diag}(u)$$ và $$\operatorname{diag}(h(x))$$; hàng thứ ba chứa ma trận ràng buộc tuyến tính $$A$$.
- **Khử khối (Schur Complement):** Vì khối $$\operatorname{diag}(h(x))$$ là ma trận đường chéo khả nghịch (do $$h_i(x) < 0$$), ta có thể khử biến $$\Delta u$$ ngay lập tức bằng phép chia từng phần tử, thu gọn hệ về ma trận đối xứng nhỏ hơn chỉ theo $$(\Delta x, \Delta v)$$.

### Khung giải thích (nên đọc chậm): Giải tay hệ Newton gốc–đối ngẫu $$2 \times 2$$ từng con số

Xét bài toán lồi 1 biến (không có ràng buộc đẳng thức $$Ax = b$$):

$$\min_{x} \; f(x) = \frac{1}{2}x^2 \qquad \text{với điều kiện} \qquad h(x) = 1 - x \le 0.$$

Ta có $$\nabla f(x) = x$$, $$\nabla^2 f(x) = 1$$, $$\nabla h(x) = -1$$, $$\nabla^2 h(x) = 0$$. Hệ điều kiện KKT bị nhiễu với tham số $$\tau$$ là:

$$r_{\text{dual}}(x, u) = x - u = 0, \qquad r_{\text{cent}}(x, u) = u(1 - x) + \tau = 0.$$

Hãy tính chính xác một bước Newton từ điểm hiện tại $$(x, u) = (2, 1)$$ với $$\tau = 0.2$$:

1. **Tính vector phần dư $$r_\tau(2, 1)$$:**
   - $$r_{\text{dual}} = 2 - 1 = 1$$.
   - $$r_{\text{cent}} = 1 \cdot (1 - 2) + 0.2 = -0.8$$.
2. **Lập ma trận Jacobi $$Dr_\tau(x, u)$$ tại $$(2, 1)$$:**
   - Đạo hàm của $$r_{\text{dual}} = x - u$$ theo $$(x, u)$$ là $$[1, \; -1]$$.
   - Đạo hàm của $$r_{\text{cent}} = u(1 - x) + \tau$$ theo $$(x, u)$$ là $$[-u, \; 1 - x] = [-1, \; -1]$$.
3. **Giải hệ phương trình tuyến tính $$Dr_\tau \Delta w = -r_\tau$$:**
   $$\begin{bmatrix} 1 & -1 \\ -1 & -1 \end{bmatrix} \begin{bmatrix} \Delta x \\ \Delta u \end{bmatrix} = -\begin{bmatrix} 1 \\ -0.8 \end{bmatrix} = \begin{bmatrix} -1 \\ 0.8 \end{bmatrix}.$$
   Cộng hai phương trình: $$-2\Delta u = -0.2 \implies \Delta u = 0.1$$. Thay lại vào phương trình đầu: $$\Delta x = \Delta u - 1 = -0.9$$.
4. **Kiểm tra điểm mới với bước đầy đủ $$\theta = 1$$:**
   $$x^+ = 2 - 0.9 = 1.1 > 1 \quad (h(x^+) = -0.1 < 0), \qquad u^+ = 1 + 0.1 = 1.1 > 0.$$
   Tính lại phần dư tại $$(1.1, 1.1)$$: $$r_{\text{dual}}^+ = 1.1 - 1.1 = 0$$, còn $$r_{\text{cent}}^+ = 1.1(-0.1) + 0.2 = +0.09$$ (giảm mạnh từ $$-0.8$$ xuống $$+0.09$$!). Chỉ sau một bước tuyến tính hóa, cả phần dư đối ngẫu lẫn phần dư trung tâm đều co rút ngoạn mục.

---

**Phương pháp điểm trong gốc-đối ngẫu (Primal-dual interior-point method)** tìm nghiệm tối ưu bằng cách bám theo đường trung tâm tương tự phương pháp chắn. Để làm điều này, thuật toán biểu diễn các điều kiện KKT bị nhiễu (perturbed KKT conditions) dưới dạng hàm phần dư và tìm nghiệm làm triệt tiêu các phần dư đó. Phần này trình bày chi tiết cách tiếp cận này.

## Phương trình đường trung tâm
Chuyển toàn bộ vế phải sang vế trái trong hệ phương trình đường trung tâm đã nêu ở [17-01 Điều kiện tối ưu]({% multilang_post_url contents/chapter17/21-05-01-17_01_barrier_method_duality_optimality_revisited %}), ta thu được hệ điều kiện KKT bị nhiễu:
> $$
> \begin{array}{rcl}
> \nabla f(x) +\nabla h(x)u + A^Tv & = & 0 \\\
>  Uh(x) + \tau\mathbb{1}  & = & 0 \\\
> Ax-b & = & 0 \\\
> u,-h(x)  & > & 0
> \end{array}
> $$

Lưu ý sự khác biệt giữa điều kiện KKT của bài toán gốc và điều kiện KKT bị nhiễu: ở bài toán gốc ta có điều kiện bù chặt $$Uh(x) = 0$$ và $$u, -h(x) \ge 0$$, còn ở điều kiện KKT bị nhiễu ta có $$Uh(x) = -\tau\mathbb{1}$$ và $$u, -h(x) \gt 0$$.

Hệ phương trình phi tuyến này có thể được giải xấp xỉ ở mỗi bước bằng cách tuyến tính hóa nó thông qua phiên bản tìm nghiệm (root-finding) của phương pháp Newton.

## Bước Newton
Ta định nghĩa hệ ba phương trình đầu tiên là hàm phần dư $$r(x, u, v) = 0$$ (gọi là phần dư vì các đại lượng này cần tiến về $$0$$ tại nghiệm tối ưu):

> $$r(x,u,v) :=
> \begin{bmatrix}
> \nabla f(x) +\nabla h(x)u + A^Tv \\\
> Uh(x) + \tau\mathbb{1} \\\
> Ax-b
> \end{bmatrix}, H(x) = \text{Diag}(h(x))$$

Áp dụng khai triển Taylor bậc nhất để xấp xỉ tuyến tính phương trình $$r(x + \Delta x, u + \Delta u, v + \Delta v) = 0$$ (xem chi tiết tại [14-02-01 Tìm nghiệm]({% multilang_post_url contents/chapter14/2021-03-26-14_01_newton_method %})):
>$$\begin{align}
0 & = r(x + \Delta x, u + \Delta u, v + \Delta v)  \\\\
  & \approx r(x, u, v) + \nabla r(x, u, v) 
\begin{pmatrix}
\Delta x \\\\
\Delta u \\\\
\Delta v \\\\
\end{pmatrix} \\\\
\end{align}$$

Suy ra hệ phương trình tuyến tính xác định bước Newton:

>$$\begin{align}
\nabla r(x, u, v) 
\begin{pmatrix}
\Delta x \\\\
\Delta u \\\\
\Delta v \\\\
\end{pmatrix} = -r(x, u, v) \\\\
\end{align}$$

Tính ma trận Jacobi $$\nabla r(x, u, v)$$ bằng cách lấy đạo hàm riêng của $$r(x, u, v)$$ theo $$x, u, v$$ rồi thay vào hệ trên, ta thu được:
> $$\begin{bmatrix}
> \nabla^2f(x) + \sum_i u_i \nabla^2h_i(x) & \nabla h(x) & A^T \\\
>  U \nabla  h(x)^T & H(x) & 0 \\\
> A & 0 & 0
> \end{bmatrix}
> \begin{bmatrix}
> \Delta x \\\
> \Delta u \\\
> \Delta v
> \end{bmatrix} = -r(x,u,v)$$
> trong đó
> $$r(x,u,v) :=
> \begin{bmatrix}
> \nabla f(x) +\nabla h(x)u + A^Tv \\\
> Uh(x) + \tau\mathbb{1} \\\
> Ax-b
> \end{bmatrix}, H(x) = \text{Diag}(h(x))$$

Nghiệm $$(\Delta x, \Delta u, \Delta v)$$ của hệ tuyến tính này chính là hướng cập nhật cho cả biến gốc và biến đối ngẫu. Chính vì thuật toán cập nhật đồng thời biến gốc và biến đối ngẫu thông qua hàm phần dư nên nó được gọi là phương pháp điểm trong **gốc-đối ngẫu (Primal-Dual)**.
