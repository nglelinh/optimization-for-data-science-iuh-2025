---
layout: post
title: 29-04 Ứng dụng liên federated hiện đại
chapter: '29'
order: 5
owner: Nguyen Le Linh
categories:
- chapter29
lang: vi
lesson_type: optional
---


Các bài 29-01 đến 29-03 đã sở hữu SGD song song dữ liệu, **FedAvg**, và tương phản ADMM. Ghi chú tùy chọn này là lớp *ứng dụng* 2020–2026: làm gì khi client non-IID (FedProx, SCAFFOLD), bước server thích nghi vào thế nào (FedOpt), và phương pháp thực sự chạy ở đâu (y tế xuyên kho). Nó không suy diễn lại vòng ba bước FedAvg.

## 1. FedProx: dây proximal trên trôi cục bộ

Li, Sahu, Zaheer, Sanjabi, Talwalkar và Smith, *Federated Optimization in Heterogeneous Networks*, MLSys 2020, [proceedings.mlsys.org](https://proceedings.mlsys.org/paper_files/paper/2020/hash/1f5fe83998a09396ebe6477d9475ba0c-Abstract.html), thay mục tiêu cục bộ $$F_c(w)$$ bằng

$$
F_c(w)+\frac{\mu}{2}\|w-w_t\|_2^2.
$$

Đó là số hạng proximal về mô hình toàn cục vừa phát — cùng *ý tưởng* với phạt Lagrangian tăng cường, không có biến đối ngẫu. FedProx là bài đầu tiên đọc sau FedAvg khi hệ thống client rớt và dữ liệu cục bộ non-IID. Nó **không** phải ADMM (không nâng đối ngẫu, không chứng nhận phần dư); Chương 29-03 đã làm sắc phân biệt đó. Dùng $$\mu>0$$ như núm bền, không như chứng minh bạn đã có đồng thuận.

## 2. SCAFFOLD: biến kiểm soát cho trôi client

Karimireddy, Kale, Mohri, Reddi, Stich và Suresh, *SCAFFOLD: Stochastic Controlled Averaging for Federated Learning*, ICML 2020, [PMLR v119](https://proceedings.mlr.press/v119/karimireddy20a.html), giữ một *biến kiểm soát* trên server và trên mỗi client để SGD cục bộ được hiệu chỉnh bởi ước lượng chệch gradient client $$(\nabla F_c-\nabla F)$$. Truyền thông mỗi vòng tăng một vector; phần thưởng là tốc độ không nổ theo số bước cục bộ $$E$$. Nếu FedAvg là “hy vọng trung bình các mô hình đã trôi vẫn ổn,” SCAFFOLD là “trừ trôi ước lượng.” Sinh viên giảm phương sai (26-05) sẽ nhận ra nước đi.

## 3. FedOpt / FedAdam: server được phép là Adam

Reddi, Charles, Zaheer, Garrett, Rush, Konečný, Kumar và McMahan, *Adaptive Federated Optimization*, ICLR 2021, [OpenReview](https://openreview.net/forum?id=LkFG3lB13U5), coi *pseudo-gradient* $$w_t-\bar w_{t+1}$$ (delta client đã trung bình) như một quan sát và áp Adam / Yogi / Adagrad **trên server**. Client có thể ở lại SGD; tiền điều kiện thích nghi sống nơi bộ nhớ rẻ. Kết hợp với bước cục bộ kiểu FedAvg thường gọi là FedAdam. Đây là bộ tối ưu Chương 26, nâng một tầng trong phân cấp — câu hỏi thi hữu ích: *ai* giữ $$\hat m,\hat v$$?

## 4. Y tế: ứng dụng khiến FL bắt buộc

Dự đoán ảnh y khoa xuyên kho và EHR là lý do phương pháp liên federated rời bài bàn phím di động. Guan, Yap, Bozoki và Liu, *Federated learning for medical image analysis: A survey*, *Pattern Recognition* 151:110424, 2024, [doi:10.1016/j.patcog.2024.110424](https://doi.org/10.1016/j.patcog.2024.110424), là bản đồ ảnh (phân đoạn u, X-quang ngực, modality thiếu). Nguyen et al., *Federated Learning for Smart Healthcare: A Survey*, *ACM Comput. Surv.* 55(3), 2022, và khảo sát CSBJ 2025 (hơn 250 bài, 2019–2024, [doi:10.1016/j.csbj.2025.06.009](https://doi.org/10.1016/j.csbj.2025.06.009)) liệt kê kiến trúc hệ thống, phân hoạch ngang/dọc, và aggregator nào (FedAvg / FedProx / SCAFFOLD / FedAdam) triển khai thực sự dùng. Bài học tối ưu điềm tĩnh: FedAvg vẫn là *hiện thực* mặc định; FedProx và SCAFFOLD là *câu trả lời* mặc định khi cân bằng lớp của một bệnh viện không khớp bệnh viện khác; riêng tư hình thức (DP-SGD, tổng hợp an toàn) là môn khác, như 29-02 đã cảnh báo.

| Phương pháp | Ý thêm | Truyền thông thêm | Khi nào thử |
|-------------|--------|-------------------|-------------|
| FedAvg (29-02) | trung bình trọng số sau $$E$$ bước cục bộ | một mô hình / vòng | baseline, gần IID |
| FedProx | proximal $$\mu$$ về $$w_t$$ | như FedAvg | rớt mạng, non-IID vừa |
| SCAFFOLD | biến kiểm soát client/server | $$+1$$ vector / client | trôi client mạnh |
| FedAdam | Adam trên pseudo-gradient server | như FedAvg (+ trạng thái server) | server thích nghi, client rẻ |
| FedADMM (21-08) | phần dư đối ngẫu | cùng bậc | khi muốn chứng nhận gốc–đối ngẫu |

**Bài tập.** Tái sử dụng phân hoạch MNIST 3 client, mỗi client một lớp (hoặc hỗn hợp Gauss 2-D) từ 29-02. Chạy $$E=5$$ bước cục bộ với (i) FedAvg, (ii) FedProx ở hai $$\mu$$, (iii) SCAFFOLD *hoạt họa* trừ trung bình chạy của gradient mỗi client khỏi bước cục bộ. Vẽ độ chính xác kiểm tra toàn cục theo vòng, không theo bước cục bộ. Viết bốn câu về phương pháp nào thu nhỏ dao động bạn thấy ở 29-02.

## Nguồn

- H. B. McMahan et al., AISTATS 2017 — FedAvg (đã bắt buộc).
- T. Li et al., MLSys 2020 — FedProx.
- S. P. Karimireddy et al., ICML 2020 — SCAFFOLD.
- S. Reddi et al., ICLR 2021 — FedOpt / FedAdam.
- H. Guan et al., *Pattern Recognition* 151:110424, 2024 — FL ảnh y khoa.
- D. C. Nguyen et al., *ACM Comput. Surv.* 55(3), 2022 — FL y tế thông minh.
- Khảo sát CSBJ 2025, [doi:10.1016/j.csbj.2025.06.009](https://doi.org/10.1016/j.csbj.2025.06.009) — rà hệ thống 2019–2024.
