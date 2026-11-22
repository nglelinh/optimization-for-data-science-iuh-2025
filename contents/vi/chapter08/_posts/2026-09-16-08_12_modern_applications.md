---
layout: post
title: 08-12 Ứng dụng hiện đại của phương pháp subgradient
chapter: '08'
order: 20
owner: Nguyen Le Linh
categories:
- chapter08
lang: vi
lesson_type: optional
---

# Ứng dụng hiện đại của phương pháp subgradient

Chương 08 phân tích vòng lặp $$x^{k+1}=x^k-\alpha_k g^k$$ với $$g^k\in\partial f(x^k)$$, cùng hai biến thể quan trọng là bản có chiếu và bản ngẫu nhiên. Bài đọc tùy chọn này liên hệ ba khuôn mẫu thuật toán đó với các quy trình thực tế đã được chuẩn hóa trong giai đoạn 2022–2026. Chúng ta không chứng minh lại tốc độ hội tụ $$O(1/\varepsilon^2)$$, mà làm rõ vì sao các bước cập nhật subgradient (có chiếu hoặc ngẫu nhiên) vẫn được sử dụng rộng rãi trong thực hành.

## 1. Tối ưu rủi ro thực nghiệm không trơn: hinge, Huber và huấn luyện ReLU

Hồi quy logistic có chính quy hóa trong [08-01-05]({% multilang_post_url contents/chapter08/20-03-29-08_01_05_example_regularized_logistic_regression %}) là một ví dụ trực tiếp của phương pháp subgradient. Cùng cấu trúc vòng lặp đó được dùng để huấn luyện SVM tuyến tính (hàm mất mát hinge), hồi quy bền vững (hàm Huber hoặc phân vị), hay lớp phân loại cuối của một bộ mã hóa đã đóng băng trọng số. Với mạng ReLU nhiều lớp, hàm mất mát không còn lồi, nhưng lan truyền ngược *trong các thư viện thực tế* vẫn tính ra một lựa chọn bảo toàn của subgradient (Bolte và Pauwels, 2021). Kết quả hội tụ của họ cung cấp cơ sở lý thuyết trực tiếp cho **SGD không trơn đúng như cách các thư viện hiện hành triển khai**, chứ không phụ thuộc vào một oracle vi phân Clarke lý tưởng.

Trên các bài toán tổng hữu hạn lồi, phân tích còn rõ ràng hơn: bước giảm dần và bước Polyak trong chương này vẫn là nền tảng tiêu chuẩn, còn các thuật toán chọn bước thích nghi hoặc không cần siêu tham số giai đoạn 2022–2024 (như DoG, Polyak restart) là sự kế thừa trực tiếp từ [08-01-06 Kích thước bước Polyak]({% multilang_post_url contents/chapter08/20-03-29-08_01_06_polyak_step_sizes %}).

## 2. PGD có chiếu và huấn luyện đối kháng theo chuẩn $$\ell_p$$

Trong huấn luyện đối kháng theo cách tiếp cận của Madry, tại mỗi minibatch ta giải bài toán bên trong có ràng buộc:

$$
\max_{\|\delta\|_p\le\varepsilon}\ \ell\bigl(h_w(x+\delta),y\bigr)
$$

bằng **bước tăng gradient / subgradient có chiếu** theo nhiễu $$\delta$$, xen kẽ với bước giảm theo tham số $$w$$. Phép chiếu lên quả cầu $$\ell_\infty$$ hoặc $$\ell_2$$ chính là toán tử trong [08-01-08 Phương pháp subgradient có chiếu]({% multilang_post_url contents/chapter08/20-03-29-08_01_08_projected_subgradient_method %}). Croce và Hein (2020) chỉ ra rằng vòng lặp PGD bên trong nếu tinh chỉnh kém sẽ *đánh giá quá cao* độ bền vững của mô hình; từ đó, bộ tổ hợp không tham số **AutoAttack** (gồm APGD + FAB + Square) trở thành chuẩn kiểm thử mặc định. Croce và cộng sự (2021) đóng gói quy trình này thành **RobustBench**, vốn vẫn là bảng xếp hạng công khai chuẩn cho độ bền đối kháng $$\ell_\infty$$ và $$\ell_2$$ đến năm 2025. Khía cạnh chuẩn đối ngẫu (hàm tựa của quả cầu tấn công) sẽ được đề cập ở Chương 13, còn *thuật toán* cốt lõi chính là phương pháp có chiếu của chương này.

## 3. Tính công bằng và các ràng buộc theo tỷ lệ

Nhiều ràng buộc trong hệ thống thực tế có dạng **tỷ lệ không trơn**: cân bằng nhân khẩu học (demographic parity), cân bằng tỷ lệ sai số (equalised odds), ngưỡng dưới của độ nhạy, hay ngưỡng trên của tỷ lệ rời bỏ (churn). Các ràng buộc này có dạng $$\mathbb{P}(\hat y=1\mid A=a)\le \alpha$$ — là trung bình của hàm chỉ báo, do đó từng khúc hằng và không khả vi. Cotter, Jiang, Gupta và cộng sự (JMLR 2019) đề xuất cách tiếp cận trò chơi hai người **proxy-Lagrangian**: một phía thực hiện bước gradient trên hàm thay thế trơn, phía kia áp đặt ràng buộc tỷ lệ gốc bằng phương pháp (sub)gradient trên nhân tử đối ngẫu. Agarwal, Beygelzimer, Dudík, Langford và Wallach (2018) quy bài toán phân loại công bằng về một dãy bài toán phân loại có trọng số chi phí (cost-sensitive); thư viện **Fairlearn** (Weerts, Dudík, Edgar, Jalali, Lutz và Madaio, 2023, *JMLR*) cài đặt phương pháp quy giảm này qua lớp `ExponentiatedGradient` và là công cụ được dùng phổ biến trong hệ sinh thái scikit-learn giai đoạn 2024–2026.

Bài toán tối ưu rủi ro thực nghiệm có trọng số ở vòng trong thường được giải bằng bước subgradient hoặc SGD trên hàm mất mát hinge hay logistic, còn bước cập nhật nhân tử ở vòng ngoài là bước subgradient theo mức độ vi phạm ràng buộc — tức là thuật toán của chương này xuất hiện ở cả hai tầng.

## 4. Ví dụ ngắn: bước chiếu lên quả cầu $$\ell_\infty$$

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

Khi thay `g` bằng gradient minibatch của hàm mất mát, ta thu được vòng lặp bên trong của huấn luyện đối kháng. Khi thay phép chiếu lên quả cầu bằng phép chiếu lên đơn hình xác suất hoặc đa diện công bằng, ta thu được đúng phương pháp subgradient có chiếu ở mục 08-01-08.

## Tóm lược

Khi hàm mục tiêu hoặc ràng buộc chứa hàm max, chuẩn $$\ell_1$$, mất mát hinge hay các tỷ lệ thực nghiệm, thuật toán bậc nhất cơ bản *chính là* phương pháp subgradient (có thể kèm phép chiếu hoặc lấy mẫu ngẫu nhiên). Các kỹ thuật tăng tốc và toán tử gần kề ở Chương 09 giúp cải thiện đáng kể khi bài toán có cấu trúc tổng hợp rõ ràng, nhưng không thay thế hoàn toàn vòng lặp này đối với các ràng buộc tỷ lệ không trơn.

**Câu hỏi.** Vì sao kích thước bước cố định về mặt lý thuyết gặp khó khăn với ràng buộc tỷ lệ lồi không trơn, và vì sao các phương pháp quy giảm công bằng trong thực hành vẫn sử dụng kiểu bước này?

## Nguồn

- Bolte, J., & Pauwels, E. (2021). Conservative set valued fields, automatic differentiation, stochastic gradient methods and deep learning. *Mathematical Programming*, 188, 19–51.
- Croce, F., & Hein, M. (2020). Reliable evaluation of adversarial robustness with an ensemble of diverse parameter-free attacks. *ICML*, PMLR 119.
- Croce, F., Andriushchenko, M., Sehwag, V., Debenedetti, E., Flammarion, N., Chiang, M., Mittal, P., & Hein, M. (2021). RobustBench: A standardized adversarial robustness benchmark. *NeurIPS Datasets and Benchmarks*. Bảng: [robustbench.github.io](https://robustbench.github.io/)
- Cotter, A., Jiang, H., Gupta, M., Wang, S., Narayan, T., You, S., & Sridharan, K. (2019). Optimization with non-differentiable constraints with applications to fairness, recall, churn, and other goals. *JMLR*, 20(172).
- Agarwal, A., Beygelzimer, A., Dudík, M., Langford, J., & Wallach, H. (2018). A reductions approach to fair classification. *ICML*, PMLR 80.
- Weerts, H., Dudík, M., Edgar, R., Jalali, A., Lutz, R., & Madaio, M. (2023). Fairlearn: Assessing and improving fairness of AI systems. *JMLR*, 24(257). [https://fairlearn.org](https://fairlearn.org)
