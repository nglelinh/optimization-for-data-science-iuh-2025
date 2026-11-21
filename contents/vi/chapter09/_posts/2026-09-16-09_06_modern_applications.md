---
layout: post
title: 09-06 Ứng dụng hiện đại của proximal GD và tăng tốc
chapter: '09'
order: 13
owner: Nguyen Le Linh
categories:
- chapter09
lang: vi
lesson_type: optional
---

# Ứng dụng hiện đại của proximal GD và tăng tốc

Chương 09 nghiên cứu bài toán tổng hợp $$\min_x g(x)+h(x)$$ với $$g$$ trơn và $$h$$ thân thiện với prox, vòng proximal-gradient, và tăng tốc Nesterov / FISTA. Bài tùy chọn này ở lại khuôn ấy và chỉ ra nơi nó chạy trong tạo ảnh, GLM thưa, và mạng *unroll* từ 2022 đến 2026.

Nhắc cặp FISTA đã có trong [09-05-03]({% multilang_post_url contents/chapter09/20-01-08-09_05_03_example_FISTA %}):

$$
y^{k}=x^{k-1}+\frac{t_{k-1}-1}{t_k}(x^{k-1}-x^{k-2}),\qquad
x^{k}=\operatorname{prox}_{t_k h}\bigl(y^{k}-t_k\nabla g(y^{k})\bigr).
$$

Khi $$h=\lambda\|\cdot\|_1$$ thì prox là soft-thresholding — cùng ánh xạ với Chương 07.

## 1. Tái tạo MRI / CT: FISTA, rồi PnP-FISTA

MRI nén và CT góc thưa là bình phương tối thiểu tổng hợp cộng regularizer thưa hoặc biến phân toàn phần. FISTA cổ điển (Beck và Teboulle, 2009) vẫn là đường cơ sở CPU/GPU trong mã nghiên cứu bệnh viện. Bài hướng dẫn IEEE SPM 2023 của Kamilov, Bouman, Buzzard và Wohlberg giải thích vì sao phòng thí nghiệm **thay prox của $$h$$ bằng bộ khử nhiễu học được** và giữ bước gradient của $$g$$ (mô hình vật lý thuận). Lai đó là **plug-and-play (PnP)**; Algorithm 4 của họ đúng là **PnP-FISTA**. Ứng dụng họ khảo sát gồm kính hiển vi sinh học, CT, MRI, và ptycho-tomography.

Mảnh trung thành dữ liệu là $$g$$ trơn của chương này; bộ khử nhiễu đóng vai $$\operatorname{prox}_{t h}$$. Bạn phải viết được vòng lặp trước khi bàn mạng nơ-ron.

## 2. Unrolling thuật toán: FISTA-Net và pFISTA-DR

Unrolling (Monga, Li và Eldar, 2021) biến một số bước proximal-gradient / FISTA cố định thành kiến trúc nơ-ron mà bước, ngưỡng, thậm chí prox được huấn luyện. Xiang, Dong và Yang (2021) công bố **FISTA-Net** trên *IEEE TMI*: cascade gồm module gradient, proximal, và momentum, đánh giá trên tomography điện từ và CT tia X. Qu, Zhang, Kang, Lin, Lin, She, Wu, Wang và Zheng (2024) unroll **FISTA chiếu** cho MRI hướng kính (**pFISTA-DR**) và báo thời gian tái tạo giảm từ khoảng 48 s/lát xuống 0,55 s/lát trên dữ liệu lâm sàng. Zhang, Chen, Xiong và Zhang (2023) khảo sát cùng ý tưởng dưới tên *compressed sensing lấy cảm hứng vật lý*: khung ISTA/FISTA ở lại, các ánh xạ tuyến tính trở thành học được.

**Nối với giáo trình.** Nếu không viết được FISTA trên giấy, mạng unroll chỉ là một hộp đen khác. Điểm của chương này là liên kết skip / momentum *chính là* dãy $$t_k$$ của Nesterov.

## 3. Elastic net và hoàn thiện ma trận trong bộ giải sản xuất

Elastic net $$\tfrac12\|X\beta-y\|_2^2+\lambda\bigl(\alpha\|\beta\|_1+(1-\alpha)\tfrac12\|\beta\|_2^2\bigr)$$ là proximal gradient (hoặc descent theo tọa độ trên toàn phương cộng $$\ell_1$$) với **soft-threshold chỉnh ridge**. Tay, Narasimhan và Hastie (2023) biến đường ấy thành mặc định cho mọi họ GLM trong glmnet — gồm genomics, dự báo nhấp, và mô hình Cox. Ví dụ hoàn thiện ma trận [09-03]({% multilang_post_url contents/chapter09/20-01-08-09_03_example_matrix_completion %}) là cùng khuôn tổng hợp (số hạng dữ liệu trơn + prox chuẩn hạt nhân = ngưỡng giá trị singular) vẫn nằm dưới pipeline gợi ý và điền dữ liệu đơn bào.

ISTA / FISTA không phải lúc nào cũng là phương pháp *CPU* nhanh nhất cho Lasso (descent tọa độ cộng screening thường thắng; xem Chương 13), nhưng chúng là phương pháp bạn có thể **gói GPU, unroll, hoặc đổi prox**. Đó là lý do tạo ảnh và lập trình khả vi chuẩn hóa trên chúng.

## 4. Một bước ISTA nhỏ

```python
import numpy as np

def soft_threshold(z, t):
    return np.sign(z) * np.maximum(np.abs(z) - t, 0.0)

def ista_step(x, A, b, lam, t):
    # t < 1 / ||A||^2 với g(x) = 0.5 ||Ax - b||^2
    return soft_threshold(x - t * A.T @ (A @ x - b), t * lam)
```

FISTA chỉ đổi *điểm* bạn đánh giá $$\nabla g$$, dùng momentum của mục 09-05. PnP-FISTA đổi `soft_threshold` thành `denoiser`. FISTA-Net làm `t` và bộ khử nhiễu học được.

## Cần nhớ

Cấu trúc tổng hợp (likelihood trơn + regularizer thân thiện prox) là lý do proximal gradient tồn tại. Tăng tốc là lịch $$t_k$$, không phải mô hình khác. Từ 2022 đến 2026 cùng lịch ấy là (i) một bộ giải, (ii) một vỏ plug-and-play quanh CNN khử nhiễu, và (iii) một mạng nơ-ron nhận được khi unroll mười đến bốn mươi bước.

**Câu hỏi.** Khi nào bạn giữ prox thật (soft-threshold, SVT) thay vì thay bằng bộ khử nhiễu học được — và lý thuyết Chương 09 còn bảo đảm gì trong trường hợp PnP?

## Nguồn

- Beck, A., & Teboulle, M. (2009). A fast iterative shrinkage-thresholding algorithm for linear inverse problems. *SIAM J. Imaging Sciences*, 2(1), 183–202. (FISTA cổ điển)
- Kamilov, U. S., Bouman, C. A., Buzzard, G. T., & Wohlberg, B. (2023). Plug-and-play methods for integrating physical and learned models in computational imaging. *IEEE Signal Processing Magazine*, 40(1), 85–97.
- Monga, V., Li, Y., & Eldar, Y. C. (2021). Algorithm unrolling: Interpretable, efficient deep learning for signal and image processing. *IEEE Signal Processing Magazine*, 38(2), 18–44.
- Xiang, J., Dong, Y., & Yang, Y. (2021). FISTA-Net: Learning a fast iterative shrinkage thresholding network for inverse problems in imaging. *IEEE Transactions on Medical Imaging*, 40(5), 1329–1339.
- Qu, B., Zhang, J., Kang, T., Lin, J., Lin, M., She, H., Wu, Q., Wang, M., & Zheng, G. (2024). Radial magnetic resonance image reconstruction with a deep unrolled projected fast iterative soft-thresholding network. *Computers in Biology and Medicine*, 168, 107707.
- Zhang, J., Chen, B., Xiong, R., & Zhang, Y. (2023). Physics-inspired compressive sensing: Beyond deep unrolling. *IEEE Signal Processing Magazine*, 40(1), 58–72.
- Tay, J. K., Narasimhan, B., & Hastie, T. (2023). Elastic net regularization paths for all generalized linear models. *Journal of Statistical Software*, 106(1).
