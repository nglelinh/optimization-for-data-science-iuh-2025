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


Các bài 29-01 đến 29-03 đã trình bày SGD song song dữ liệu, **FedAvg** và sự khác biệt với ADMM. Bài đọc tùy chọn này mở rộng sang các phương pháp và ứng dụng học liên kết giai đoạn 2020–2026: xử lý dữ liệu non-IID giữa các máy khách (FedProx, SCAFFOLD), đưa bộ tối ưu thích nghi lên máy chủ (FedOpt) và ứng dụng thực tế trong y tế liên viện.

## 1. FedProx: bổ sung số hạng proximal hạn chế trôi cục bộ

Li, Sahu, Zaheer, Sanjabi, Talwalkar và Smith (*Federated Optimization in Heterogeneous Networks*, MLSys 2020, [proceedings.mlsys.org](https://proceedings.mlsys.org/paper_files/paper/2020/hash/1f5fe83998a09396ebe6477d9475ba0c-Abstract.html)) thay hàm mục tiêu cục bộ $$F_c(w)$$ bằng:

$$
F_c(w)+\frac{\mu}{2}\|w-w_t\|_2^2.
$$

Số hạng phạt bậc hai này kéo nghiệm cục bộ không đi quá xa khỏi mô hình toàn cục $$w_t$$ vừa nhận — có ý tưởng gần với số hạng phạt trong Lagrangian tăng cường nhưng không có biến đối ngẫu. FedProx là phương pháp mở rộng phổ biến ngay sau FedAvg khi hệ thống có sự không đồng nhất cả về dữ liệu (non-IID) lẫn phần cứng (máy khách thực hiện số bước cục bộ không đều hoặc ngắt kết nối). Tuy nhiên, FedProx **không** phải ADMM vì không có bước cập nhật đối ngẫu hay phần dư kiểm chứng đồng thuận như đã phân biệt ở mục 29-03.

## 2. SCAFFOLD: biến kiểm soát triệt tiêu trôi máy khách

Karimireddy, Kale, Mohri, Reddi, Stich và Suresh (*SCAFFOLD: Stochastic Controlled Averaging for Federated Learning*, ICML 2020, [PMLR v119](https://proceedings.mlr.press/v119/karimireddy20a.html)) duy trì các *biến kiểm soát (control variates)* trên máy chủ và trên từng máy khách để hiệu chỉnh trực tiếp độ lệch gradient cục bộ $$(\nabla F_c-\nabla F)$$ trong mỗi bước SGD cục bộ. Chi phí truyền thông mỗi vòng tăng thêm một vector tham số, nhưng đổi lại tốc độ hội tụ không bị suy giảm theo số bước cục bộ $$E$$. Nếu FedAvg chỉ lấy trung bình các mô hình đã bị trôi, SCAFFOLD chủ động trừ đi thành phần trôi ước lượng — cùng cơ chế biến kiểm soát như trong SVRG/SAGA ở mục 26-05.

## 3. FedOpt / FedAdam: dùng bộ tối ưu thích nghi ở phía máy chủ

Reddi, Charles, Zaheer, Garrett, Rush, Konečný, Kumar và McMahan (*Adaptive Federated Optimization*, ICLR 2021, [OpenReview](https://openreview.net/forum?id=LkFG3lB13U5)) xem độ chênh lệch trung bình của các máy khách $$w_t-\bar w_{t+1}$$ như một *giả gradient (pseudo-gradient)* và áp dụng các bộ tối ưu thích nghi (Adam, Yogi, AdaGrad) ngay **tại máy chủ**. Nhờ đó, máy khách chỉ cần chạy SGD đơn giản với bộ nhớ thấp, còn trạng thái mô-men $$\hat m, \hat v$$ của tiền điều kiện thích nghi được lưu ở máy chủ. Khi kết hợp với bước cục bộ kiểu FedAvg, biến thể này thường được gọi là **FedAdam**.

## 4. Y tế liên viện: ứng dụng thực tế nổi bật của học liên kết

Các bài toán chẩn đoán ảnh y khoa và hồ sơ bệnh án điện tử (EHR) liên bệnh viện (cross-silo) là lĩnh vực đưa học liên kết vượt ra ngoài bài toán dự đoán gõ phím trên điện thoại. Guan, Yap, Bozoki và Liu (*Federated learning for medical image analysis: A survey*, *Pattern Recognition* 151:110424, 2024, [doi:10.1016/j.patcog.2024.110424](https://doi.org/10.1016/j.patcog.2024.110424)) hệ thống hóa các bài toán phân đoạn khối u, ảnh X-quang ngực và dữ liệu đa phương thức. Các bài khảo sát của Nguyen và cộng sự (*Federated Learning for Smart Healthcare: A Survey*, *ACM Comput. Surv.* 55(3), 2022) cùng bài tổng quan trên *CSBJ* 2025 (hơn 250 công trình giai đoạn 2019–2024, [doi:10.1016/j.csbj.2025.06.009](https://doi.org/10.1016/j.csbj.2025.06.009)) tổng hợp kiến trúc hệ thống, phân hoạch ngang/dọc và các bộ tổng hợp được triển khai thực tế: FedAvg vẫn là lựa chọn khởi đầu phổ biến nhất; FedProx và SCAFFOLD được dùng khi phân phối lớp giữa các bệnh viện lệch mạnh; còn bảo vệ quyền riêng tư hình thức (DP-SGD, tổng hợp an toàn) được kết hợp ở tầng bảo mật riêng như đã nêu ở mục 29-02.

| Phương pháp | Cơ chế bổ sung | Chi phí truyền thông thêm | Khi nào nên thử |
|-------------|----------------|---------------------------|-----------------|
| FedAvg (29-02) | trung bình trọng số sau $$E$$ bước cục bộ | 1 mô hình / vòng | chuẩn đối chiếu, dữ liệu gần IID |
| FedProx | số hạng proximal $$\mu$$ kéo về $$w_t$$ | tương đương FedAvg | thiết bị không đồng đều, non-IID vừa |
| SCAFFOLD | biến kiểm soát máy khách / máy chủ | $$+1$$ vector / máy khách | trôi cục bộ mạnh (non-IID cao) |
| FedAdam | áp dụng Adam lên giả gradient tại máy chủ | tương đương FedAvg (+ bộ nhớ máy chủ) | muốn cập nhật thích nghi ở máy chủ, máy khách nhẹ |
| FedADMM (21-07) | phần dư đối ngẫu | cùng bậc với FedAvg | cần theo dõi phần dư gốc–đối ngẫu |

**Bài tập.** Dùng lại cách chia dữ liệu MNIST (hoặc hỗn hợp Gaussian 2 chiều) cho 3 máy khách, mỗi máy khách một lớp từ mục 29-02. Chạy $$E=5$$ bước cục bộ với: (i) FedAvg, (ii) FedProx tại hai giá trị $$\mu$$ khác nhau, và (iii) một phiên bản đơn giản của SCAFFOLD trừ trung bình trượt của gradient cục bộ. Vẽ độ chính xác kiểm tra toàn cục theo *số vòng truyền thông* (không theo số bước cục bộ) và nhận xét phương pháp nào làm giảm dao động rõ nhất so với mục 29-02.

## Nguồn

- H. B. McMahan et al., AISTATS 2017 — FedAvg (đã bắt buộc).
- T. Li et al., MLSys 2020 — FedProx.
- S. P. Karimireddy et al., ICML 2020 — SCAFFOLD.
- S. Reddi et al., ICLR 2021 — FedOpt / FedAdam.
- H. Guan et al., *Pattern Recognition* 151:110424, 2024 — FL ảnh y khoa.
- D. C. Nguyen et al., *ACM Comput. Surv.* 55(3), 2022 — FL y tế thông minh.
- Khảo sát CSBJ 2025, [doi:10.1016/j.csbj.2025.06.009](https://doi.org/10.1016/j.csbj.2025.06.009) — rà hệ thống 2019–2024.
