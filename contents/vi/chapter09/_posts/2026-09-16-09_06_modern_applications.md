---
layout: post
title: 09-06 Ứng dụng hiện đại của proximal GD và tăng tốc
chapter: '09'
order: 11
owner: Nguyen Le Linh
categories:
- chapter09
lang: vi
lesson_type: optional
---

# Ứng dụng hiện đại của proximal GD và tăng tốc

Chương 09 nghiên cứu bài toán tối ưu tổng hợp $$\min_x g(x)+h(x)$$ với $$g$$ trơn và $$h$$ có toán tử gần kề dễ tính, cùng vòng lặp gradient gần kề và kỹ thuật tăng tốc Nesterov / FISTA. Bài đọc tùy chọn này chỉ ra cách khuôn mẫu đó được ứng dụng trong tái tạo ảnh y sinh, mô hình tuyến tính tổng quát thưa, và các mạng nơ-ron *trải phẳng thuật toán (algorithm unrolling)* giai đoạn 2022–2026.

Nhắc lại cặp công thức cập nhật FISTA trong [09-05-03]({% multilang_post_url contents/chapter09/20-01-08-09_05_03_example_FISTA %}) (với kích thước bước $$\alpha \le 1/L$$ và dãy hệ số động lượng $$t_k$$):

$$
y^{k}=x^{k-1}+\frac{t_{k-1}-1}{t_k}(x^{k-1}-x^{k-2}),\qquad
x^{k}=\operatorname{prox}_{\alpha h}\bigl(y^{k}-\alpha\nabla g(y^{k})\bigr).
$$

Khi $$h=\lambda\|\cdot\|_1$$, toán tử gần kề chính là phép ngưỡng mềm (soft-thresholding) — cùng ánh xạ đã gặp ở Chương 07.

## 1. Tái tạo ảnh MRI / CT: từ FISTA đến PnP-FISTA

Bài toán tái tạo MRI nén và CT góc thưa có dạng bình phương tối thiểu kết hợp thành phần chính quy hóa thưa hoặc biến phân toàn phần (total variation). FISTA cổ điển (Beck và Teboulle, 2009) vẫn là thuật toán cơ sở trên CPU/GPU trong nhiều hệ thống nghiên cứu y sinh. Bài tổng quan trên *IEEE SPM* năm 2023 của Kamilov, Bouman, Buzzard và Wohlberg phân tích lý do các phòng thí nghiệm **thay toán tử gần kề của $$h$$ bằng một bộ khử nhiễu học được**, trong khi vẫn giữ nguyên bước gradient của phần trung thực dữ liệu $$g$$ (mô hình vật lý thuận). Phương pháp lai này được gọi là **plug-and-play (PnP)**; Thuật toán 4 trong bài báo của họ chính là **PnP-FISTA**. Các lĩnh vực ứng dụng được khảo sát gồm kính hiển vi sinh học, chụp CT, MRI và chụp cắt lớp ptycho-tomography.

Thành phần trung thực dữ liệu đóng vai trò hàm trơn $$g$$ của chương này, còn bộ khử nhiễu đảm nhiệm vai trò $$\operatorname{prox}_{\alpha h}$$. Do đó, việc nắm vững vòng lặp gradient gần kề là bước cần thiết trước khi tích hợp mạng nơ-ron.

## 2. Trải phẳng thuật toán (Algorithm Unrolling): FISTA-Net và pFISTA-DR

Kỹ thuật trải phẳng thuật toán (Monga, Li và Eldar, 2021) chuyển một số bước lặp cố định của proximal gradient / FISTA thành một kiến trúc mạng nơ-ron, trong đó kích thước bước, ngưỡng co và thậm chí cả toán tử gần kề đều có thể học từ dữ liệu. Xiang, Dong và Yang (2021) giới thiệu **FISTA-Net** trên *IEEE TMI*: một chuỗi các khối gồm mô-đun gradient, mô-đun gần kề và mô-đun động lượng, được đánh giá trên chụp cắt lớp điện từ và CT tia X. Qu, Zhang, Kang, Lin, Lin, She, Wu, Wang và Zheng (2024) trải phẳng **FISTA có chiếu** cho ảnh MRI quét hướng kính (**pFISTA-DR**), ghi nhận thời gian tái tạo giảm từ khoảng 48 giây/lát xuống 0,55 giây/lát trên dữ liệu lâm sàng. Zhang, Chen, Xiong và Zhang (2023) tổng hợp hướng nghiên cứu này dưới tên gọi *cảm biến nén lấy cảm hứng vật lý (physics-inspired compressed sensing)*: khung thuật toán ISTA/FISTA được giữ nguyên, còn các ánh xạ tuyến tính và bộ lọc được học từ dữ liệu.

**Liên hệ với giáo trình.** Nếu không nắm được công thức lặp FISTA trên giấy, các mạng trải phẳng sẽ chỉ là một hộp đen. Điểm cốt lõi của chương này là các kết nối tắt (skip connection) và động lượng trong mạng thực chất tương ứng với dãy hệ số $$t_k$$ của Nesterov.

## 3. Elastic net và hoàn thiện ma trận trong các bộ giải thực tế

Bài toán elastic net $$\tfrac12\|X\beta-y\|_2^2+\lambda\bigl(\alpha\|\beta\|_1+(1-\alpha)\tfrac12\|\beta\|_2^2\bigr)$$ có thể giải bằng phương pháp gradient gần kề (hoặc giảm theo tọa độ trên hàm bậc hai cộng chuẩn $$\ell_1$$) với **toán tử ngưỡng mềm có điều chỉnh Ridge**. Tay, Narasimhan và Hastie (2023) đưa đường chính quy hóa này thành lựa chọn mặc định cho mọi họ GLM trong `glmnet` — phục vụ phân tích hệ gene, dự báo tỷ lệ nhấp chuột và mô hình sống còn Cox. Ví dụ hoàn thiện ma trận ở bài [09-03]({% multilang_post_url contents/chapter09/20-01-08-09_03_example_matrix_completion %}) cũng tuân theo đúng khuôn mẫu tổng hợp (số hạng sai số dữ liệu trơn cộng toán tử gần kề của chuẩn hạt nhân là ngưỡng mềm trên giá trị kỳ dị), hiện vẫn là nền tảng cho nhiều hệ thống gợi ý và bài toán điền khuyết dữ liệu đơn bào.

ISTA và FISTA không phải lúc nào cũng là thuật toán chạy *CPU* nhanh nhất cho Lasso (giảm theo tọa độ kết hợp quy tắc sàng lọc biến thường nhanh hơn; xem Chương 13), nhưng chúng đặc biệt thuận tiện để **triển khai song song trên GPU, trải phẳng thành mạng nơ-ron, hoặc thay thế toán tử gần kề**. Đó là lý do các lĩnh vực tái tạo ảnh và lập trình khả vi chuẩn hóa dựa trên họ thuật toán này.

## 4. Một bước lặp ISTA tối giản

```python
import numpy as np

def soft_threshold(z, t):
    return np.sign(z) * np.maximum(np.abs(z) - t, 0.0)

def ista_step(x, A, b, lam, t):
    # t < 1 / ||A||^2 với g(x) = 0.5 ||Ax - b||^2
    return soft_threshold(x - t * A.T @ (A @ x - b), t * lam)
```

FISTA chỉ thay đổi *điểm* tính gradient $$\nabla g$$ bằng cách dùng bước ngoại suy động lượng ở bài 09-05. PnP-FISTA thay `soft_threshold` bằng một bộ khử nhiễu (`denoiser`), còn FISTA-Net cho phép học trực tiếp cả bước `t` lẫn bộ khử nhiễu đó.

## Tóm lược

Cấu trúc tổng hợp (hàm mất mát trơn cộng thành phần chính quy hóa có toán tử gần kề tính được) là lý do ra đời của phương pháp gradient gần kề, còn kỹ thuật tăng tốc là một lịch trình hệ số $$t_k$$ chứ không làm thay đổi mô hình bài toán. Trong giai đoạn 2022–2026, cùng một lịch trình này vừa đóng vai trò (i) bộ giải tối ưu chuẩn, (ii) khung plug-and-play bao quanh các mạng CNN khử nhiễu, và (iii) kiến trúc mạng nơ-ron thu được khi trải phẳng từ 10 đến 40 bước lặp.

**Câu hỏi.** Khi nào nên giữ nguyên toán tử gần kề giải tích (như ngưỡng mềm, SVT) thay vì thay bằng bộ khử nhiễu học được — và trong trường hợp PnP, những bảo đảm lý thuyết nào của Chương 09 vẫn còn giữ được?

## Nguồn

- Beck, A., & Teboulle, M. (2009). A fast iterative shrinkage-thresholding algorithm for linear inverse problems. *SIAM J. Imaging Sciences*, 2(1), 183–202. (FISTA cổ điển)
- Kamilov, U. S., Bouman, C. A., Buzzard, G. T., & Wohlberg, B. (2023). Plug-and-play methods for integrating physical and learned models in computational imaging. *IEEE Signal Processing Magazine*, 40(1), 85–97.
- Monga, V., Li, Y., & Eldar, Y. C. (2021). Algorithm unrolling: Interpretable, efficient deep learning for signal and image processing. *IEEE Signal Processing Magazine*, 38(2), 18–44.
- Xiang, J., Dong, Y., & Yang, Y. (2021). FISTA-Net: Learning a fast iterative shrinkage thresholding network for inverse problems in imaging. *IEEE Transactions on Medical Imaging*, 40(5), 1329–1339.
- Qu, B., Zhang, J., Kang, T., Lin, J., Lin, M., She, H., Wu, Q., Wang, M., & Zheng, G. (2024). Radial magnetic resonance image reconstruction with a deep unrolled projected fast iterative soft-thresholding network. *Computers in Biology and Medicine*, 168, 107707.
- Zhang, J., Chen, B., Xiong, R., & Zhang, Y. (2023). Physics-inspired compressive sensing: Beyond deep unrolling. *IEEE Signal Processing Magazine*, 40(1), 58–72.
- Tay, J. K., Narasimhan, B., & Hastie, T. (2023). Elastic net regularization paths for all generalized linear models. *Journal of Statistical Software*, 106(1).
