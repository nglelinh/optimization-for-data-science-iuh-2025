---
layout: post
title: 08-11 Ứng dụng hiện đại của phương pháp subgradient
chapter: '08'
order: 18
owner: Nguyen Le Linh
categories:
- chapter08
lang: vi
lesson_type: optional
---

# Ứng dụng hiện đại của phương pháp subgradient

Chương 08 phân tích vòng lặp $$x^{k+1}=x^k-\alpha_k g^k$$ với $$g^k\in\partial f(x^k)$$, bản chiếu, và bản ngẫu nhiên. Bài tùy chọn này ánh xạ ba khuôn ấy lên các pipeline đã chuẩn hóa khoảng 2022–2026. Chúng ta không chứng lại tốc độ $$O(1/\varepsilon^2)$$; chúng ta chỉ ra vì sao người làm thực hành vẫn chạy một bước subgradient (chiếu, ngẫu nhiên).

## 1. Rủi ro thực nghiệm không trơn: hinge, Huber, và huấn luyện ReLU

Hồi quy logistic có regularizer trong [08-01-05]({% multilang_post_url contents/chapter08/20-03-29-08_01_05_example_regularized_logistic_regression %}) đã là ví dụ phương pháp subgradient. Cùng vòng lặp ấy huấn luyện SVM tuyến tính (hinge), hồi quy bền vững (Huber / phân vị), hoặc lớp cuối của một encoder đóng băng. Với cả mạng ReLU, hàm mất mát không còn lồi, nhưng chiều ngược *được cài* vẫn là một lựa chọn bảo toàn của subgradient (Bolte và Pauwels, 2021). Kết quả hội tụ theo giá trị của họ chính là biện minh cho **SGD không trơn như thư viện chạy**, không phải cho một oracle điểm Clarke lý tưởng.

Trên bài toán tổng hữu hạn lồi, bức tranh dễ chịu hơn: bước giảm dần hoặc bước Polyak của chương này vẫn là bảo đảm sách giáo khoa, và các bước thích nghi / không tham số 2022–2024 (DoG, Polyak restart) là hậu duệ trực tiếp của [08-01-06 Bước Polyak]({% multilang_post_url contents/chapter08/20-03-29-08_01_06_polyak_step_sizes %}).

## 2. PGD chiếu và huấn luyện đối kháng $$\ell_p$$

Huấn luyện đối kháng kiểu Madry, tại mỗi minibatch, giải bài toán trong có ràng buộc

$$
\max_{\|\delta\|_p\le\varepsilon}\ \ell\bigl(h_w(x+\delta),y\bigr)
$$

bằng **leo gradient / subgradient chiếu** trên $$\delta$$ và một bước xuống trên $$w$$. Phép chiếu lên quả cầu $$\ell_\infty$$ hoặc $$\ell_2$$ là toán tử trong [08-01-08 Subgradient chiếu]({% multilang_post_url contents/chapter08/20-03-29-08_01_08_projected_subgradient_method %}). Croce và Hein (2020) chỉ ra rằng PGD trong chỉnh kém *thổi phồng* độ bền vững; ensemble không tham số **AutoAttack** (APGD + FAB + Square) trở thành phép thử mặc định. Croce và cộng sự (2021) đóng gói phép thử ấy thành **RobustBench**, vẫn là bảng xếp hạng công khai cho độ bền $$\ell_\infty$$ và $$\ell_2$$ đến 2025. Câu chuyện chuẩn đối ngẫu (hàm tựa của quả cầu tấn công) thuộc Chương 13; *thuật toán* là phương pháp chiếu của chương này.

## 3. Công bằng và các ràng buộc tỷ lệ

Nhiều ràng buộc sản xuất là **tỷ lệ không trơn**: demographic parity, equalised odds, sàn độ nhạy, trần churn. Chúng trông như $$\mathbb{P}(\hat y=1\mid A=a)\le \alpha$$ — trung bình chỉ báo, do đó từng khúc hằng. Cotter, Jiang, Gupta và đồng tác giả (JMLR 2019) đưa vào trò chơi hai người **proxy-Lagrangian**: một người bước gradient trên surrogate trơn, người kia ép tỷ lệ gốc bằng phương pháp (sub)gradient trên nhân tử. Agarwal, Beygelzimer, Dudík, Langford và Wallach (2018) đưa phân loại công bằng về dãy bài toán cost-sensitive; thư viện **Fairlearn** (Weerts, Dudík, Edgar, Jalali, Lutz và Madaio, 2023, *JMLR*) chuyển reduction ấy thành `ExponentiatedGradient` và là thứ stack sklearn 2024–2026 thực sự gọi.

ERM có trọng số bên trong thường được giải bằng bước subgradient hoặc SGD trên hinge hay logistic. Cập nhật nhân tử bên ngoài là bước subgradient trên phần dư ràng buộc. Đó là thuật toán của chương này, hai lần.

## 4. Ví dụ nhỏ: bước chiếu trên quả cầu $$\ell_\infty$$

```python
import numpy as np

def proj_linf(delta, eps):
    return np.clip(delta, -eps, eps)

def pgd_inner(x, g, eps, alpha=0.01, steps=10):
    delta = np.zeros_like(x)
    for _ in range(steps):
        delta = proj_linf(delta + alpha * g(x + delta), eps)
    return delta
```

Thay `g` bằng gradient minibatch của hàm mất mát thì bạn có vòng trong của huấn luyện đối kháng. Thay quả cầu bằng simplex xác suất hoặc polytope công bằng thì bạn có phương pháp chiếu của mục 08-01-08.

## Cần nhớ

Nếu mục tiêu hoặc ràng buộc là max, $$\ell_1$$, hinge, hoặc tỷ lệ thực nghiệm, huấn luyện bậc nhất *chính là* phương pháp subgradient (có thể chiếu, có thể ngẫu nhiên). Tăng tốc và prox (Chương 09) là nâng cấp khi cấu trúc tổng hợp đã hiện; chúng không thay vòng lặp này trên một ràng buộc tỷ lệ thô.

**Câu hỏi.** Vì sao bước cố định về lý thuyết khó chịu với ràng buộc tỷ lệ lồi không trơn, và vì sao các reduction công bằng vẫn dùng một bước như vậy trong thực hành?

## Nguồn

- Bolte, J., & Pauwels, E. (2021). Conservative set valued fields, automatic differentiation, stochastic gradient methods and deep learning. *Mathematical Programming*, 188, 19–51.
- Croce, F., & Hein, M. (2020). Reliable evaluation of adversarial robustness with an ensemble of diverse parameter-free attacks. *ICML*, PMLR 119.
- Croce, F., Andriushchenko, M., Sehwag, V., Debenedetti, E., Flammarion, N., Chiang, M., Mittal, P., & Hein, M. (2021). RobustBench: A standardized adversarial robustness benchmark. *NeurIPS Datasets and Benchmarks*. Bảng: [robustbench.github.io](https://robustbench.github.io/)
- Cotter, A., Jiang, H., Gupta, M., Wang, S., Narayan, T., You, S., & Sridharan, K. (2019). Optimization with non-differentiable constraints with applications to fairness, recall, churn, and other goals. *JMLR*, 20(172).
- Agarwal, A., Beygelzimer, A., Dudík, M., Langford, J., & Wallach, H. (2018). A reductions approach to fair classification. *ICML*, PMLR 80.
- Weerts, H., Dudík, M., Edgar, R., Jalali, A., Lutz, R., & Madaio, M. (2023). Fairlearn: Assessing and improving fairness of AI systems. *JMLR*, 24(257). [https://fairlearn.org](https://fairlearn.org)
