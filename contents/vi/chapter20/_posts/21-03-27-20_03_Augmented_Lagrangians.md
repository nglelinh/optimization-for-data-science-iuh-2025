---
layout: post
title: '20-03 Augmented Lagrangian'
chapter: '20'
order: 7
owner: Hooncheol Shin
categories:
- chapter20
lang: vi
---

Phương pháp tăng đối ngẫu (dual ascent) có một gót chân Achilles cực kỳ khó chịu: nếu hàm mục tiêu $$f(x)$$ không lồi mạnh (chẳng hạn $$f(x)$$ tuyến tính hoặc có đoạn phẳng), bài toán con $$\min_x (f(x) + u^T Ax)$$ có thể **vô nghiệm (tiến tới $$-\infty$$)** hoặc nhảy loạn xạ không bao giờ hội tụ! Năm 1969, Magnus Hestenes và Michael Powell độc lập đề xuất một cú "cứu nguy" thiên tài: cộng thêm một số hạng phạt bậc hai $$\frac{\rho}{2}\|Ax - b\|_2^2$$ vào hàm mục tiêu. Số hạng này **bằng 0 hoàn toàn** tại mọi điểm khả thi $$Ax = b$$ (nên không làm thay đổi nghiệm tối ưu), nhưng lại biến hàm mục tiêu thành lồi trơn hơn rất nhiều — đó là **phương pháp hàm Lagrange tăng cường (Augmented Lagrangian / Method of Multipliers)**!

## Kiến thức cần nhớ: Bốn trụ cột của Phương pháp Nhân tử (Augmented Lagrangian)

Hiểu bốn điểm sau sẽ giúp bạn nắm trọn cả ưu điểm lẫn cái giá phải trả của Augmented Lagrangian:

- **Tương đương tuyệt đối về nghiệm tối ưu:** Vì ràng buộc $$Ax = b$$ vẫn được giữ nguyên, việc thêm $$\frac{\rho}{2}\|Ax - b\|_2^2$$ không gây ra sai số xấp xỉ như phương pháp phạt thuần túy (penalty method — vốn phải đẩy $$\rho \to \infty$$ gây suy biến số học). Ở đây, chỉ cần một hằng số $$\rho > 0$$ hữu hạn là đủ đạt nghiệm chính xác!
- **Bước học tự nhiên $$t_k = \rho$$:** Điều kiện dừng của bước gốc $$0 \in \partial f(x^{(k)}) + A^T\big(u^{(k-1)} + \rho(Ax^{(k)} - b)\big)$$ cho thấy nếu đặt $$u^{(k)} = u^{(k-1)} + \rho(Ax^{(k)} - b)$$, thì cặp $$(x^{(k)}, u^{(k)})$$ **tự động thỏa mãn điều kiện khả thi đối ngẫu** ở ngay mỗi vòng lặp!
- **Hội tụ vững chắc dưới điều kiện rất nhẹ:** Không còn yêu cầu $$f$$ phải lồi chặt hay hữu hạn ở mọi nơi; chỉ cần $$f$$ lồi đóng và bài toán có nghiệm là phương pháp nhân tử hội tụ bền bỉ.
- **Nhược điểm duy nhất — đánh mất tính phân rã:** Số hạng $$\frac{\rho}{2}\|\sum_i A_i x_i - b\|_2^2$$ khi bình phương lên sẽ sinh ra các tích chéo $$x_i^T A_i^T A_j x_j$$ trói chặt mọi khối biến lại với nhau — chính nhược điểm này sẽ khai sinh ra ADMM ở bài tiếp theo!

### Giải thích: Cứu một bài toán mà Dual Ascent thất bại hoàn toàn chỉ trong 2 bước

Xét bài toán tối ưu tuyến tính 1 biến đơn giản nhất có thể:

$$\min_{x \in \mathbb{R}} \; f(x) = x \qquad \text{với điều kiện} \qquad x = 2.$$

Nghiệm hiển nhiên là $$x^\star = 2, u^\star = -1$$. Hãy so sánh hai phương pháp cùng khởi tạo từ $$u^{(0)} = 0$$:

1. **Thử chạy Dual Ascent thường:**
   - Bước gốc phải giải $$\min_x (x + 0 \cdot x) = \min_x x = -\infty$$! Thuật toán **sập ngay ở vòng lặp đầu tiên** vì $$f(x) = x$$ không lồi chặt.
2. **Chạy Augmented Lagrangian với $$\rho = 1$$:**
   Hàm Lagrange tăng cường là $$L_1(x, u) = x + u(x - 2) + \frac{1}{2}(x - 2)^2$$.
   - **Vòng 1 ($$u^{(0)} = 0$$):**
     - Bước gốc: $$x^{(1)} = \arg\min_x \left(x + \frac{1}{2}(x - 2)^2\right)$$. Đạo hàm $$1 + (x - 2) = 0 \implies x^{(1)} = 1$$ (hữu hạn và duy nhất!).
     - Bước đối ngẫu (dùng bước học $$t = \rho = 1$$): $$u^{(1)} = 0 + 1(1 - 2) = -1$$.
   - **Vòng 2 ($$u^{(1)} = -1$$):**
     - Bước gốc: $$x^{(2)} = \arg\min_x \left(x - (x - 2) + \frac{1}{2}(x - 2)^2\right) = \arg\min_x \left(2 + \frac{1}{2}(x - 2)^2\right) = 2 = x^\star$$!
     - Phần dư ràng buộc $$x^{(2)} - 2 = 0$$, nhân tử $$u^{(2)} = -1 = u^\star$$ — **đạt nghiệm tối ưu chính xác chỉ sau 2 vòng lặp** mà không cần đẩy $$\rho \to \infty$$!

---

Nhược điểm lớn của phương pháp tăng đối ngẫu (dual ascent) là đòi hỏi điều kiện mạnh — chẳng hạn $$f$$ phải lồi mạnh — để đảm bảo hội tụ. **Phương pháp hàm Lagrange tăng cường (Augmented Lagrangian)**, còn gọi là **phương pháp nhân tử (method of multipliers)**, khắc phục hạn chế này.

Ta viết lại bài toán gốc bằng cách cộng thêm một số hạng phạt bậc hai vào hàm mục tiêu:
>\begin{equation}
\min_x f(x) + \frac{\rho}{2} \lVert Ax - b \rVert _2^2 \quad \text{ subject to } \quad Ax = b
\end{equation}

trong đó $$\rho > 0$$. Nếu $$A$$ có hạng cột đầy đủ, hàm mục tiêu mới trở nên lồi mạnh. Bài toán này hoàn toàn tương đương với bài toán ban đầu vì số hạng phạt $$\frac{\rho}{2}\lVert Ax - b \rVert_2^2$$ bằng $$0$$ tại mọi điểm khả thi $$Ax = b$$.

## Phương pháp Augmented Lagrangian
Áp dụng **dual gradient ascent** cho bài toán đã biến đổi, ta thu được các bước lặp với $$k = 1, 2, 3, \dots$$:
> $$
> \begin{alignat}{1}
> x^{(k)} & \in \arg\min_x f(x) + (u^{(k-1)})^T A x + \frac{\rho}{2} \lVert Ax - b \rVert_2^2  \\
> u^{(k)} & = u^{(k-1)} + \rho (A x^{(k)} - b)
> \end{alignat}
> $$

Ở đây, tham số phạt $$\rho$$ đồng thời được chọn làm độ dài bước cập nhật đối ngẫu ($$t_k = \rho$$).

#### Vì sao chọn độ dài bước $$t_k = \rho$$?

Vì $$x^{(k)}$$ là nghiệm cực tiểu của $$f(x) + (u^{(k-1)})^T Ax + \frac{\rho}{2} \lVert Ax - b\rVert _2^2$$, điều kiện tối ưu bậc nhất cho ta:

> $$
> \begin{alignat}{1}
> 0 & \in \partial f(x^{(k)}) + A^T \left( u^{(k-1)} + \rho (A x^{(k)} -b) \right)  \\
>   & = \partial f(x^{(k)}) + A^T u^{(k)}
> \end{alignat}
> $$

Như vậy, với quy tắc cập nhật $$u^{(k)} = u^{(k-1)} + \rho (A x^{(k)} - b)$$, điểm $$x^{(k)}$$ luôn thỏa mãn điều kiện dừng đối ngẫu $$0 \in \partial f(x^{(k)}) + A^T u^{(k)}$$ ở mọi vòng lặp. Dưới các giả thiết rất nhẹ, phần dư $$Ax^{(k)} - b$$ tiến về $$0$$, các điều kiện KKT dần được thỏa mãn và $$(x^{(k)}, u^{(k)})$$ hội tụ về nghiệm tối ưu.

Ưu điểm của **phương pháp augmented Lagrangian** là tính hội tụ ổn định và vững chắc hơn nhiều so với dual ascent; tuy nhiên, nhược điểm là số hạng bậc hai $$\frac{\rho}{2}\lVert Ax - b \rVert_2^2$$ làm các khối biến liên kết với nhau, phá vỡ tính khả phân (decomposability) của bài toán.
