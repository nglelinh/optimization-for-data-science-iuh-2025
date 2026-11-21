---
layout: post
title: 10-09 Ứng dụng hiện đại của đối ngẫu LP
chapter: '10'
order: 10
owner: Nguyen Le Linh
categories:
- chapter10
lang: vi
lesson_type: optional
---

# Ứng dụng hiện đại của đối ngẫu LP

Chương 10 xây đối ngẫu của quy hoạch tuyến tính, đối ngẫu yếu/mạnh, bù, và các ví dụ max-flow / min-cut cùng trò chơi ma trận. Bài tùy chọn này chỉ ra bốn chỗ *cùng* các chứng chỉ ấy được dùng trong hệ thống CS và khoa học dữ liệu khoảng 2022–2026.

Một LP gốc $$\min\{c^\top x:Ax=b,\,Gx\le h\}$$ và đối ngẫu của nó vẫn có nghĩa: mọi cặp đối ngẫu khả thi $$(u,v)$$ là một **cận dưới**, và tại tối ưu cận khít và các bất đẳng thức không dùng có nhân tử không.

## 1. Kiểm chứng mạng nơ-ron như một LP (rồi LP có cắt)

Hỏi liệu một bộ phân loại có đổi nhãn trong hộp $$\ell_\infty$$ là bài toán không lồi theo các kích hoạt ReLU. Nới chuẩn thay mỗi ReLU bằng xấp xỉ ngoài tam giác / LP (Ehlers; Wong và Kolter). Biến đối ngẫu của LP ấy là **nhân tử lan truyền cận**. Zhang, Wang, Xu, Li, Li, Jana, Hsieh và Kolter (NeurIPS 2022) thêm **mặt cắt tổng quát** vào đối ngẫu ấy (GCP-CROWN) và gấp vào **$$\alpha,\beta$$-CROWN**, công cụ thắng cuộc thi International Verification of Neural Networks các năm 2021, 2022, 2023, 2024 và 2025. Phần kỹ thuật là lan truyền cận trên GPU; chứng chỉ vẫn là “đối ngẫu của LP đã siết nằm trên không, nên không tồn tại ví dụ đối kháng.”

Đây là đối ngẫu yếu của Chương 10 dùng như **chứng minh an toàn**, không phải câu chuyện định giá.

## 2. Thị trường điện: LP khớp lệnh và giá bóng

Thị trường năng lượng ngày-tới khớp một quy hoạch tuyến tính (hỗn hợp nguyên): cực tiểu chi phí chào giá với cân bằng công suất và giới hạn đường dây. Đối ngẫu của nới *tuyến tính* là vector **giá biên theo vị trí** (LMP). Sau cú sốc giá châu Âu 2022, đối ngẫu ấy không còn là tranh minh họa sách: nó là số trên hóa đơn. Liang và Dvorkin (ACM e-Energy 2023) dùng tối ưu nghịch trên lịch và LMP công bố để khôi phục giá chào của nhà máy — họ đảo ánh xạ KKT / đối ngẫu của LP khớp lệnh. Các bài 2022–2023 về đấu giá ngày-tới châu Âu viết giá theo vùng tường minh như đối ngẫu của LP phúc lợi có ràng buộc lưới.

**Nối với giáo trình.** Bù nói rằng chỉ đường dây tắc ($$Gx=h$$) mới mang được giá tắc $$v$$ khác không. Câu ấy là chương này, áp lên một lưới.

## 3. Max-flow / min-cut sau 2022

Định lý trong [10-03]({% multilang_post_url contents/chapter10/21-03-22-10_03_Max_flow_and_min_cut %}) vẫn là cặp đối ngẫu sau phân đoạn ảnh, phát hiện cộng đồng, và cắt độ tin cậy trong mạng truyền thông. Các bộ giải quy mô lớn hiện đại (Gurobi, HiGHS, OR-Tools) đưa đối ngẫu ra như vector hạng nhất; một workflow khoa học dữ liệu “phân bổ băng thông” hoặc “cắt đồ thị thành nguồn/đích” đang đọc vector ấy. Cách dùng CS *mới* thường là dung lượng **học được** (GNN dự đoán trọng số cạnh) rồi một đối ngẫu max-flow cổ điển như một lớp — cùng cặp với tối ưu khả vi ở Chương 12, nhưng bài toán trong là LP.

## 4. Vận chuyển tối ưu như một LP khổng lồ

Bài toán Kantorovich

$$
\min_{\pi\ge 0}\ \langle C,\pi\rangle\quad\text{s.t.}\quad \pi\mathbf{1}=a,\ \pi^\top\mathbf{1}=b
$$

là một LP. Đối ngẫu là $$\max_{f,g} f^\top a+g^\top b$$ với $$f_i+g_j\le C_{ij}$$ — các **thế Kantorovich**. Peyré và Cuturi (2019) là chuyên khảo tính toán; thích nghi miền, chưng cất dữ liệu, và căn chỉnh đơn bào 2022–2026 vẫn giải bản có regularizer (Sinkhorn) hoặc không, rồi đọc đối ngẫu như một khớp mềm. Đối ngẫu yếu là khẳng định không khớp nào rẻ hơn mọi cặp thế khả thi.

## Cần nhớ

Đối ngẫu LP là một **chứng chỉ**: của bất khả thi (kiểm chứng), của một giá (thị trường), của một cắt (mạng), hoặc của chi phí khớp (vận chuyển). Nếu viết được gốc và đưa ra một đối ngẫu khả thi cùng giá trị mục tiêu, bạn xong — đó là đối ngẫu mạnh cho LP, và đó là thứ bốn ứng dụng kia tính.

**Câu hỏi.** Trong GCP-CROWN, vì sao *thêm* một mặt cắt vào LP gốc chỉ *nâng* cận dưới đối ngẫu? Định lý nào của chương này là điều đó?

## Nguồn

- Zhang, H., Wang, S., Xu, K., Li, L., Li, B., Jana, S., Hsieh, C.-J., & Kolter, J. Z. (2022). General cutting planes for bound-propagation-based neural network verification. *NeurIPS*. [arXiv:2208.05740](https://arxiv.org/abs/2208.05740). Công cụ: [α,β-CROWN](https://github.com/Verified-Intelligence/alpha-beta-CROWN) (vô địch VNN-COMP 2021–2025).
- Liang, Z., & Dvorkin, Y. (2023). Data-driven inverse optimization for marginal offer price recovery in electricity markets. *ACM e-Energy ’23*.
- Peyré, G., & Cuturi, M. (2019). Computational optimal transport. *Foundations and Trends in Machine Learning*, 11(5–6). (tham chiếu LP/đối ngẫu chuẩn vẫn dùng trong pipeline OT 2022–2026)
- Boyd, S., & Vandenberghe, L. (2004). *Convex Optimization*, Ch. 5 (đối ngẫu LP và giá bóng).
