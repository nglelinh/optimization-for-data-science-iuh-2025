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


Các Chương 26–27 huấn luyện mô hình bằng cách vi phân một hàm mất mát *đơn* theo trọng số. Một lượng đáng ngạc nhiên của học máy hiện đại là một cặp tối ưu **lồng nhau**: bản thân trọng số là nghiệm của bài toán trong phụ thuộc siêu tham số, và ta muốn vi phân mục tiêu *ngoài* xuyên qua nghiệm đó. Bài tùy chọn này là một khuôn lồng — tối ưu hai mức và **siêu gradient** (hypergradient) — ở độ sâu IUH. Nó không phải bài autodiff thứ hai (27-01–27-03 đã sở hữu JVP / VJP) và không phải khảo sát mọi thư viện HPO.

Bản đồ để giữ là Chen, Chen, Jiang, Ye, Wang, Yang, Poor và Wang, *A Whole New World, but How? A Survey of Bilevel Optimization and Applications*, [arXiv:2405.04996](https://arxiv.org/abs/2405.04996) (2024), cùng góc nhìn hàm ẩn cổ điển trong Bengio, *Gradient-Based Optimization of Hyperparameters* (2000) và xử lý học sâu hiện đại của Franceschi, Frasconi, Salzo, Grazzi và Pontil (ICML 2018).

## Một khuôn lồng

Một chương trình **hai mức** (bilevel) là

$$
\begin{align}
\min_{\lambda}\quad & F\bigl(w^\star(\lambda),\lambda\bigr)\\
\text{s.t.}\quad & w^\star(\lambda)\in\arg\min_w\, L(w,\lambda).
\end{align}
$$

Bài toán **trong** là huấn luyện thường: $$L$$ là loss huấn luyện, $$w$$ là trọng số, $$\lambda$$ là siêu tham số *đi vào bài trong* (tốc độ học, weight-decay, bộ lọc dữ liệu trọng số kiểm, khởi tạo của vài bước trong). Mục tiêu **ngoài** $$F$$ thường là loss kiểm, một ràng buộc công bằng, hoặc một meta-task. Đối tượng $$\nabla_\lambda F(w^\star(\lambda),\lambda)$$ là **siêu gradient**.

Đây là cùng khuôn dưới vài tên trong giáo trình:

- **Tối ưu siêu tham số (HPO).** $$\lambda$$ là weight decay hoặc kích thước bước; $$F$$ là loss kiểm. Lưới tìm kiếm bình thường không bao giờ vi phân xuyên $$w^\star$$; một phương pháp siêu gradient thì có.
- **Meta-learning / MAML.** Mỗi “tác vụ” là vài bước SGD trong từ một khởi tạo $$\lambda$$ dùng chung; loss ngoài là hiệu năng sau những bước đó. Finn, Abbeel và Levine (ICML 2017) là thuật toán; toán học là bilevel tháo cuộn.
- **Chưng cất dữ liệu / học cách tối ưu.** Bộ giải trong là vài bước GD; biến ngoài là dữ liệu tổng hợp, hoặc chính siêu tham số của bộ tối ưu.
- **Lớp ẩn.** Một cân bằng $$w=\Phi(w,\lambda)$$ là điểm bất động trong; Deep Equilibrium Models vi phân xuyên nó bằng tích vector–Jacobian (họ hàng của 27-02 / 27-03).

Nếu bạn vẽ được cặp lồng và gọi tên gradient nào là siêu gradient, bạn đọc được những bài đó mà không cần một giáo trình lý thuyết mới.

## Hai cách lấy siêu gradient

**Tháo cuộn (unrolling).** Thay $$w^\star(\lambda)$$ bằng $$T$$ bước của một bộ giải trong khả vi, $$w_{t+1}=w_t-\eta\nabla_w L(w_t,\lambda)$$, rồi lan truyền ngược qua băng. Chế độ nghịch (27-03) cho $$\nabla_\lambda F$$ với chi phí tuyến tính theo $$T$$ nhân chi phí một bước trong — đúng câu chuyện bộ nhớ của một RNN tháo dài. Tháo một bước ($$T=1$$) đã đủ để *cảm* quy tắc chuỗi; các phương pháp few-shot kiểu MAML sống ở $$T$$ nhỏ.

**Vi phân ẩn.** Nếu bài trong trơn và Hessian $$H=\nabla_{ww}^2 L(w^\star,\lambda)$$ khả nghịch tại cực tiểu, định lý hàm ẩn nói

$$
\frac{\mathrm{d}w^\star}{\mathrm{d}\lambda}
=-H^{-1}\nabla_{w\lambda}^2 L(w^\star,\lambda),
$$

nên siêu gradient là

$$
\nabla_\lambda F
=\nabla_\lambda F\big|_{\text{tường minh}}
-\bigl(\nabla_{w\lambda}^2 L\bigr)^\top H^{-1}\nabla_w F.
$$

Bạn không bao giờ lập $$H^{-1}$$: bạn giải $$H\,v=\nabla_w F$$ bằng gradient liên hợp (tích Hessian–vector qua AD thuận-trên-nghịch, chế độ hỗn hợp đã nêu ở 27-03) rồi co với đạo hàm riêng hỗn hợp. Lorraine, Vicol và Duvenaud (ICML 2020, *Optimizing Millions of Hyperparameters by Implicit Differentiation*) là khẩu hiệu HPO quy mô xây trên lần giải đó. Giả thiết khả nghịch là cái giá: tại cực tiểu trong thật của một $$L$$ lồi mạnh thì thành thật; trên mạng không lồi mà bạn dừng sớm, tháo cuộn thường là mô hình thành thật hơn về thứ bạn thực sự đã tính.

Vi phân ẩn xấp xỉ (CG cắt cụt, chuỗi Neumann) nằm giữa hai cách. Coi đó là bài seminar, không phải bộ núm bài tập thứ hai.

<div class="content-box insight-box">
<strong>Khi nào tháo, khi nào nghịch.</strong>
Vòng trong ngắn, không lồi, hoặc “thuật toán <em>chính là</em> mô hình” (MAML, bộ tối ưu được học): tháo cuộn.
Vòng trong dài, bài trong lồi mạnh, nhiều siêu tham số (huấn luyện trọng số kiểm, kiến trúc với bộ giải trong lồi): ẩn / CG.
Đừng bao giờ vi phân xuyên một lần tiền huấn luyện AdamW đầy đủ của mô hình ngôn ngữ bằng một trong hai đường — dùng proxy (fine-tune ngắn, đầu tuyến tính, tập con) hoặc đừng nhận là có siêu gradient.
</div>

## Một tốc độ học tháo một bước

Ví dụ thành thật nhỏ nhất là bài trong toàn phương và bước vô hướng $$\lambda=\eta$$. Một bước gradient từ $$w_0$$ cho $$w_1(\eta)=w_0-\eta\nabla L(w_0)$$. Loss ngoài $$F(w_1)=\tfrac12\|w_1-w_{\mathrm{val}}\|_2^2$$ khi đó có siêu gradient sơ cấp $$\mathrm{d}F/\mathrm{d}\eta$$ theo quy tắc chuỗi — không cần thư viện.

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
w_val = np.linalg.solve(A, b)          # giả bộ đích val là cực tiểu
w1, dF = one_step_hypergrad(A, b, w0, eta=0.05, w_val=w_val)
print(w1, "siêu gradient dF/deta", dF)
```

Siêu gradient âm nói “loss kiểm sẽ giảm nếu bạn *tăng* $$\eta$$.” Đó là toàn bộ thông điệp HPO, viết không cần tuner. AD chế độ nghịch (PyTorch hoặc JAX) làm cùng sổ sách khi $$T>1$$ hoặc khi $$L$$ là một mạng; nay bạn biết băng nào bạn đang nhờ nó phát.

Với cực tiểu trong *thật* của cùng toàn phương, vi phân ẩn lấy lại $$\mathrm{d}w^\star/\mathrm{d}\lambda$$ cho mọi siêu tham số đi vào $$A$$ hoặc $$b$$ (ridge $$\lambda$$ là lựa chọn lớp học thường: $$L(w,\lambda)=\tfrac12\|Xw-y\|_2^2+\frac{\lambda}{2}\|w\|_2^2$$, loss ngoài trên một phần kiểm). Hệ tuyến tính là $$(X^\top X+\lambda I)v=\nabla_w F$$ — một lần giải ridge bạn đã gặp ở Chương 05.

## Giáo trình này kỳ vọng gì

Bạn phải (i) viết được cặp lồng cho HPO và cho MAML một bước, (ii) nói vì sao chế độ nghịch trên vòng trong tháo *chính là* siêu gradient, (iii) viết công thức ẩn và gọi tên lần giải Hessian, và (iv) từ chối tháo một lần tiền huấn luyện LLM đầy đủ. AdamW của Chương 26 vẫn là *thuật toán* trong cho các mô hình ta thực sự huấn luyện; trang này là cách một loss kiểm nói lại với siêu tham số mà không cần lưới. Đọc thêm, không kiểm tra: Maclaurin, Duvenaud và Adams (2015) về đảo SGD cho HPO; Rajeswaran, Finn, Kakade và Levine (ICML 2019) về MAML ẩn; khảo sát Chen 2024 cho phân loại.

**Bài tập 1.** Suy ra $$\mathrm{d}w_1/\mathrm{d}\eta=-\nabla L(w_0)$$ cho một bước GD và siêu gradient của $$F(w_1)=\tfrac12\|w_1-w_{\mathrm{val}}\|_2^2$$. Rồi cài hai bước ($$T=2$$) bằng tay và đối chiếu `torch.autograd` trên cùng toàn phương.

**Bài tập 2.** Với ridge $$L(w,\lambda)=\tfrac12\|Xw-y\|_2^2+\frac{\lambda}{2}\|w\|_2^2$$ và loss ngoài trên tập kiểm, viết siêu gradient ẩn và tính nó bằng cách giải $$(X^\top X+\lambda I)v=\nabla_w F$$. So với vi phân *một* bước GD trên cùng $$L$$. Khi nào hai số lệch, và số nào khớp “tôi thực sự chạy $$T$$ bước”?

**Câu hỏi.** AD chế độ hỗn hợp ở 27-03 tính tích Hessian–vector trong thời gian tương đương một gradient. Tích đó xuất hiện *đúng chỗ nào* trong siêu gradient ẩn — và vì sao đó là lý do Lorraine et al. có thể quảng cáo “hàng triệu siêu tham số”?

## Nguồn

- Y. Bengio, “Gradient-Based Optimization of Hyperparameters,” *Neural Computation*, 2000.
- L. Franceschi, P. Frasconi, S. Salzo, R. Grazzi, and M. Pontil, “Bilevel Programming for Hyperparameter Optimization and Meta-Learning,” ICML 2018.
- J. Lorraine, P. Vicol, and D. Duvenaud, “Optimizing Millions of Hyperparameters by Implicit Differentiation,” ICML 2020.
- C. Finn, P. Abbeel, and S. Levine, “Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks,” ICML 2017.
- C. Chen et al., “A Whole New World, but How?,” [arXiv:2405.04996](https://arxiv.org/abs/2405.04996), 2024.
