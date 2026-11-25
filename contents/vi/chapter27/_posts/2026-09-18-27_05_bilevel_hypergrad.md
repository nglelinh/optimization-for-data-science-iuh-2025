---
layout: post
title: 27-05 Tối ưu hai mức và siêu gradient
chapter: '27'
order: 6
owner: Nguyen Le Linh
categories:
- chapter27
lang: vi
lesson_type: optional
---

Ở các bài trước, ta học cách lấy đạo hàm của hàm mất mát theo trọng số $$w$$ với tốc độ học $$\eta$$ và hệ số phạt $$\lambda$$ cố định. Nhưng câu hỏi lớn tiếp theo trong thực hành học máy là: *làm sao tự động tối ưu chính các siêu tham số $$\lambda$$ (như hệ số chính quy hóa, trọng số dữ liệu, hay kiến trúc mạng) bằng gradient thay vì mò mẫm bằng tìm kiếm lưới (grid search)?*

Đó chính là thế giới của **Tối ưu hai mức (Bilevel Optimization)** và **Siêu gradient (Hypergradient)**: bản thân nghiệm tối ưu $$w^\star(\lambda)$$ của bài toán huấn luyện bên trong lại là một hàm số phụ thuộc vào $$\lambda$$, và ta cần kéo đạo hàm của hàm mất mát kiểm định bên ngoài *xuyên qua* cả một quy trình tối ưu hóa bên trong!

## Kiến thức cần nhớ: Ba trụ cột của Tối ưu hai mức và Siêu gradient

Hai phương pháp tính siêu gradient trong bài học này dựa trên ba trụ cột toán học sâu sắc:

- **Cấu trúc lồng nhau (Upper-Level vs. Lower-Level):** Bài toán ngoài cực tiểu hóa rủi ro kiểm định $$F(w^\star(\lambda), \lambda)$$ theo siêu tham số $$\lambda$$, bị ràng buộc bởi điều kiện $$w^\star(\lambda) \in \arg\min_w L(w, \lambda)$$ của bài toán huấn luyện trong. Tổng đạo hàm gồm hai nhánh: tác động trực tiếp $$\nabla_\lambda F$$ và tác động gián tiếp $$\bigl(\frac{\partial w^\star}{\partial \lambda}\bigr)^T \nabla_w F$$.
- **Vi phân ẩn bằng Định lý Hàm ẩn (Implicit Differentiation):** Tại nghiệm tối ưu trong, $$\nabla_w L(w^\star(\lambda), \lambda) = 0$$. Lấy đạo hàm hai vế theo $$\lambda$$ cho ta hệ phương trình tuyến tính $$\nabla_{ww}^2 L \cdot \frac{\partial w^\star}{\partial \lambda} + \nabla_{w\lambda}^2 L = 0$$. Điểm kỳ diệu là ta **không cần lưu lịch sử vòng lặp huấn luyện trong** — chỉ cần giải hệ tuyến tính (bằng Conjugate Gradient + HVP) ngay tại điểm hội tụ $$w^\star$$!
- **Trải phẳng vòng lặp (Unrolling / Differentiating through Optimization):** Nếu bài toán trong chỉ chạy $$K$$ bước SGD/GD, ta coi cả $$K$$ bước đó như một đồ thị tính toán lớn rồi chạy AD chiều nghịch xuyên qua tất cả $$K$$ bước. Dễ cài bằng PyTorch/JAX khi $$K$$ nhỏ (như MAML trong meta-learning), nhưng bộ nhớ tăng tuyến tính theo $$K$$ và dễ mất ổn định khi $$K$$ lớn.

### Giải thích: Tính tay Siêu gradient bằng Định lý Hàm ẩn cho Hồi quy Ridge

Xét bài toán hai mức 1 chiều cực kỳ trong sáng: chọn hệ số phạt $$\lambda > 0$$ để cực tiểu hóa mất mát kiểm định (ngoài) $$F(w) = \frac{1}{2}(w - 2)^2$$, trong khi bài toán huấn luyện (trong) là hồi quy Ridge:

$$
w^\star(\lambda) = \arg\min_{w \in \mathbb{R}}\ L(w, \lambda) = \arg\min_w \left[\frac{1}{2}(w - 4)^2 + \frac{\lambda}{2} w^2\right].
$$

Hãy tính siêu gradient $$\frac{dF(w^\star(\lambda))}{d\lambda}$$ tại điểm thử hiện tại $$\lambda = 3$$ bằng **Định lý Hàm ẩn**:

1. **Giải bài toán trong tại $$\lambda = 3$$:**
   Điều kiện tối ưu bậc nhất $$\nabla_w L(w, \lambda) = (w - 4) + \lambda w = 0 \implies w^\star(\lambda) = \frac{4}{1 + \lambda}$$.
   Tại $$\lambda = 3$$, ta nhận được $$w^\star(3) = \frac{4}{1 + 3} = 1$$.
2. **Tính các đạo hàm bậc hai cục bộ của $$L$$ tại $$(w^\star, \lambda) = (1, 3)$$:**
   - Hessian theo $$w$$: $$\nabla_{ww}^2 L = 1 + \lambda = 1 + 3 = 4$$.
   - Đạo hàm hỗn hợp theo $$w, \lambda$$: $$\nabla_{w\lambda}^2 L = w^\star = 1$$.
3. **Áp dụng Định lý Hàm ẩn tìm độ nhạy $$\frac{dw^\star}{d\lambda}$$:**
   $$\frac{dw^\star}{d\lambda} = -\bigl(\nabla_{ww}^2 L\bigr)^{-1} \nabla_{w\lambda}^2 L = -\frac{1}{4} = -0.25.$$
   (Kiểm tra trực tiếp từ công thức đóng $$w^\star(\lambda) = 4(1+\lambda)^{-1}$$: đạo hàm là $$-4(1+3)^{-2} = -4/16 = -0.25$$ — khớp tuyệt đối!).
4. **Áp dụng quy tắc dây chuyền ra Siêu gradient:**
   Vì $$\nabla_w F(w^\star) = w^\star - 2 = 1 - 2 = -1$$ và $$\nabla_\lambda F = 0$$:
   $$\frac{dF}{d\lambda}\Big|_{\lambda=3} = \nabla_w F(w^\star) \cdot \frac{dw^\star}{d\lambda} = (-1)(-0.25) = +0.25 > 0.$$
   **Ý nghĩa trực giác:** Siêu gradient dương ($$+0.25$$) báo ngay cho ta biết phải **giảm $$\lambda$$** xuống để hạ mất mát kiểm định $$F$$ — hoàn toàn đúng vì giảm $$\lambda$$ từ $$3$$ về $$1$$ sẽ đẩy $$w^\star$$ từ $$1$$ lên đúng đích kiểm định $$w^\star(1) = 2$$!

Các Chương 26–27 xét bài toán huấn luyện mô hình bằng cách lấy đạo hàm một hàm mất mát *đơn* theo vector trọng số. Tuy nhiên, nhiều bài toán học máy hiện đại lại có cấu trúc tối ưu **lồng nhau (hai mức)**: bản thân trọng số $$w^\star(\lambda)$$ là nghiệm của một bài toán tối ưu bên trong phụ thuộc vào siêu tham số $$\lambda$$, và ta cần lấy đạo hàm của mục tiêu *bên ngoài* xuyên qua nghiệm đó. Bài đọc tùy chọn này giới thiệu khuôn khổ tối ưu hai mức (bilevel optimization) và khái niệm **siêu gradient (hypergradient)** — bổ sung ứng dụng cho AD ở các mục 27-01 đến 27-03.

Tài liệu tham khảo chính gồm bài tổng quan của Chen, Chen, Jiang, Ye, Wang, Yang, Poor và Wang (*A Whole New World, but How? A Survey of Bilevel Optimization and Applications*, [arXiv:2405.04996](https://arxiv.org/abs/2405.04996), 2024), bài báo nền tảng về định lý hàm ẩn của Bengio (*Gradient-Based Optimization of Hyperparameters*, 2000) và cách tiếp cận cho học sâu của Franceschi, Frasconi, Salzo, Grazzi và Pontil (ICML 2018).

## Khuôn khổ bài toán lồng nhau

Một bài toán tối ưu **hai mức (bilevel)** có dạng tổng quát:

$$
\begin{align}
\min_{\lambda}\quad & F\bigl(w^\star(\lambda),\lambda\bigr)\\
\text{s.t.}\quad & w^\star(\lambda)\in\arg\min_w\, L(w,\lambda).
\end{align}
$$

Bài toán **bên trong** tương ứng với quá trình huấn luyện thông thường: $$L$$ là hàm mất mát huấn luyện, $$w$$ là trọng số mô hình, còn $$\lambda$$ là siêu tham số tác động vào bài toán trong (tốc độ học, hệ số suy giảm trọng số, trọng số mẫu dữ liệu hoặc điểm khởi tạo cho vài bước cập nhật). Hàm mục tiêu **bên ngoài** $$F$$ thường là hàm mất mát trên tập kiểm định (validation loss), tiêu chí công bằng hoặc mất mát trên tác vụ mới. Đạo hàm toàn phần $$\nabla_\lambda F(w^\star(\lambda),\lambda)$$ được gọi là **siêu gradient (hypergradient)**.

Cấu trúc này xuất hiện dưới nhiều tên gọi quen thuộc:

* **Tối ưu siêu tham số (HPO):** $$\lambda$$ là hệ số chính quy hóa hoặc tốc độ học; $$F$$ là hàm mất mát kiểm định. Tìm kiếm lưới (grid search) không lấy đạo hàm xuyên qua $$w^\star$$, còn phương pháp siêu gradient tối ưu trực tiếp theo $$\lambda$$.
* **Học siêu cấp (Meta-learning / MAML):** Mỗi tác vụ thực hiện vài bước SGD bên trong xuất phát từ điểm khởi tạo chung $$\lambda$$; hàm mất mát ngoài đo hiệu năng sau các bước thích nghi đó (Finn, Abbeel & Levine, ICML 2017).
* **Chưng cất dữ liệu và học bộ tối ưu:** Vòng trong chạy vài bước gradient descent; biến ngoài là tập dữ liệu tổng hợp hoặc chính tham số của bộ tối ưu.
* **Các lớp ẩn (Implicit layers):** Nghiệm cân bằng $$w=\Phi(w,\lambda)$$ là một điểm bất động bên trong; mô hình Deep Equilibrium (DEQ) lấy đạo hàm xuyên qua điểm bất động này bằng tích vector–Jacobian.

## Hai cách tính siêu gradient

**Khai triển vòng lặp (Unrolling).** Thay nghiệm chính xác $$w^\star(\lambda)$$ bằng kết quả sau $$T$$ bước của một bộ giải khả vi, $$w_{t+1}=w_t-\eta\nabla_w L(w_t,\lambda)$$, rồi lan truyền ngược qua toàn bộ chuỗi $$T$$ bước đó. AD chiều nghịch (27-03) tính $$\nabla_\lambda F$$ với chi phí thời gian và bộ nhớ tăng tuyến tính theo $$T$$ (tương tự lan truyền ngược theo thời gian trong RNN). Với $$T$$ nhỏ (chẳng hạn bài toán học ít mẫu kiểu MAML), khai triển vòng lặp rất trực tiếp và hiệu quả.

**Vi phân ẩn (Implicit differentiation).** Nếu bài toán trong trơn và ma trận Hessian $$H=\nabla_{ww}^2 L(w^\star,\lambda)$$ khả nghịch tại nghiệm $$w^\star$$, định lý hàm ẩn cho:

$$
\frac{\mathrm{d}w^\star}{\mathrm{d}\lambda}
=-H^{-1}\nabla_{w\lambda}^2 L(w^\star,\lambda),
$$

suy ra siêu gradient có dạng:

$$
\nabla_\lambda F
=\nabla_\lambda F\big|_{\text{tường minh}}
-\bigl(\nabla_{w\lambda}^2 L\bigr)^\top H^{-1}\nabla_w F.
$$

Trong thực tế, ta không tạo tường minh ma trận nghịch đảo $$H^{-1}$$ mà giải hệ tuyến tính $$H\,v=\nabla_w F$$ bằng phương pháp gradient liên hợp (dùng tích Hessian–vector qua AD thuận-trên-nghịch ở mục 27-03), sau đó nhân với đạo hàm riêng hỗn hợp $$\nabla_{w\lambda}^2 L$$. Lorraine, Vicol và Duvenaud (ICML 2020, *Optimizing Millions of Hyperparameters by Implicit Differentiation*) áp dụng cách này cho bài toán HPO quy mô lớn. Giả thiết $$H$$ khả nghịch tại nghiệm tối ưu chính xác là điều kiện cần lưu ý: nó phù hợp với bài toán trong lồi mạnh giải đến hội tụ, còn với mạng nơ-ron không lồi thường dừng sớm sau ít bước, khai triển vòng lặp phản ánh trung thực hơn quy trình thực tế đã chạy.

Các kỹ thuật vi phân ẩn xấp xỉ (như gradient liên hợp cắt cụt hoặc chuỗi Neumann) nằm trung gian giữa hai cách tiếp cận trên.

<div class="content-box insight-box">
<strong>Khi nào dùng khai triển vòng lặp, khi nào dùng vi phân ẩn.</strong>
Khi vòng trong ngắn, không lồi, hoặc bản thân thuật toán tối ưu là một phần của mô hình (MAML, học bộ tối ưu): dùng khai triển vòng lặp.
Khi vòng trong dài, lồi mạnh và số lượng siêu tham số lớn: dùng vi phân ẩn kết hợp gradient liên hợp.
Không nên vi phân xuyên qua toàn bộ quá trình tiền huấn luyện AdamW của một mô hình ngôn ngữ lớn bằng cả hai cách trên; hãy dùng bài toán đại diện nhẹ hơn (tinh chỉnh ngắn, lớp tuyến tính trên cùng hoặc tập con dữ liệu).
</div>

## Ví dụ: siêu gradient theo tốc độ học sau một bước

Ví dụ đơn giản nhất là bài toán trong dạng bậc hai với siêu tham số vô hướng là tốc độ học $$\lambda=\eta$$. Một bước gradient descent từ $$w_0$$ cho $$w_1(\eta)=w_0-\eta\nabla L(w_0)$$. Với hàm mất mát ngoài $$F(w_1)=\tfrac12\|w_1-w_{\mathrm{val}}\|_2^2$$, ta tính được siêu gradient $$\mathrm{d}F/\mathrm{d}\eta$$ trực tiếp bằng quy tắc dây chuyền:

```python
import numpy as np

def one_step_hypergrad(A, b, w0, eta, w_val):
    """Trong: một bước GD trên 0.5 w^T A w - b^T w. Ngoài: 0.5 ||w1 - w_val||^2."""
    g = A @ w0 - b
    w1 = w0 - eta * g
    # d w1 / d eta = -g ; hypergrad = (w1 - w_val)^T dw1/deta
    hyper = (w1 - w_val) @ (-g)
    return w1, hyper

A = np.diag([1.0, 10.0])
b = np.array([1.0, 1.0])
w0 = np.zeros(2)
w_val = np.linalg.solve(A, b)          # lấy nghiệm tối ưu làm mục tiêu kiểm định
w1, dF = one_step_hypergrad(A, b, w0, eta=0.05, w_val=w_val)
print(w1, "siêu gradient dF/deta", dF)
```

Giá trị siêu gradient âm cho biết hàm mất mát kiểm định sẽ giảm nếu ta *tăng* $$\eta$$. Khi $$T>1$$ hoặc khi $$L$$ là mạng nơ-ron, AD chiều nghịch (PyTorch hoặc JAX) tự động thực hiện đúng cùng phép tính quy tắc dây chuyền này dọc theo băng tính toán.

Nếu xét nghiệm tối ưu *chính xác* của bài toán hồi quy ridge $$L(w,\lambda)=\tfrac12\|Xw-y\|_2^2+\frac{\lambda}{2}\|w\|_2^2$$ với hàm mất mát ngoài trên tập kiểm định, vi phân ẩn dẫn tới hệ tuyến tính $$(X^\top X+\lambda I)v=\nabla_w F$$ — chính là hệ phương trình tuyến tính quen thuộc của hồi quy ridge ở Chương 05.

## Mục tiêu cần nắm

Sau bài này, bạn cần: (i) viết được dạng tối ưu hai mức cho HPO và MAML một bước; (ii) giải thích được vì sao AD chiều nghịch trên vòng trong khai triển cho ra siêu gradient; (iii) viết được công thức vi phân ẩn và nhận diện hệ phương trình tuyến tính chứa Hessian; và (iv) nhận thức được giới hạn chi phí để không áp dụng khai triển cho quá trình tiền huấn luyện mô hình lớn. Tài liệu đọc thêm (không kiểm tra): Maclaurin, Duvenaud & Adams (2015) về đảo ngược SGD cho HPO; Rajeswaran, Finn, Kakade & Levine (ICML 2019) về MAML ẩn; khảo sát Chen và cộng sự (2024).

**Bài tập 1.** Suy ra $$\mathrm{d}w_1/\mathrm{d}\eta=-\nabla L(w_0)$$ cho một bước GD và tính siêu gradient của $$F(w_1)=\tfrac12\|w_1-w_{\mathrm{val}}\|_2^2$$. Sau đó tự tính cho hai bước ($$T=2$$) và đối chiếu với `torch.autograd` trên cùng hàm bậc hai.

**Bài tập 2.** Với bài toán hồi quy ridge $$L(w,\lambda)=\tfrac12\|Xw-y\|_2^2+\frac{\lambda}{2}\|w\|_2^2$$ và hàm mất mát ngoài trên tập kiểm định, hãy viết biểu thức siêu gradient ẩn và tính nó bằng cách giải $$(X^\top X+\lambda I)v=\nabla_w F$$. So sánh kết quả này với siêu gradient khai triển sau *một* bước GD: khi nào hai giá trị sai lệch, và giá trị nào phản ánh đúng quy trình chỉ chạy $$T$$ bước?

**Câu hỏi.** AD chế độ hỗn hợp ở mục 27-03 tính tích Hessian–vector với chi phí tương đương một lượt tính gradient. Phép tính đó xuất hiện ở *vị trí nào* trong công thức siêu gradient ẩn, và vì sao nó cho phép Lorraine và cộng sự mở rộng lên hàng triệu siêu tham số?

## Nguồn

- Y. Bengio, “Gradient-Based Optimization of Hyperparameters,” *Neural Computation*, 2000.
- L. Franceschi, P. Frasconi, S. Salzo, R. Grazzi, and M. Pontil, “Bilevel Programming for Hyperparameter Optimization and Meta-Learning,” ICML 2018.
- J. Lorraine, P. Vicol, and D. Duvenaud, “Optimizing Millions of Hyperparameters by Implicit Differentiation,” ICML 2020.
- C. Finn, P. Abbeel, and S. Levine, “Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks,” ICML 2017.
- C. Chen et al., “A Whole New World, but How?,” [arXiv:2405.04996](https://arxiv.org/abs/2405.04996), 2024.
