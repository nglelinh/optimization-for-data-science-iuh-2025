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

Từ năm 2020 đến 2026, học liên kết đã bước ra khỏi phòng thí nghiệm để giải quyết những bài toán mang ý nghĩa nhân văn sâu sắc: hàng chục bệnh viện trên khắp thế giới hợp tác huấn luyện mô hình phân đoạn u não hay phát hiện bệnh lý phổi mà **không một bức ảnh y khoa nào của bệnh nhân phải rời khỏi tường lửa bệnh viện**.

Nhưng để triển khai thành công trong thế giới thực — nơi dữ liệu giữa các bệnh viện cực kỳ không đồng nhất (non-IID) và tốc độ phần cứng mỗi nơi một khác — cộng đồng tối ưu hóa đã phải phát triển ba vũ khí nâng cấp trực tiếp cho FedAvg: **FedProx** (sợi dây neo proximal), **SCAFFOLD** (biến kiểm soát triệt tiêu trôi cục bộ), và **FedAdam / FedOpt** (tách bộ tối ưu thích nghi lên máy chủ).

## Kiến thức cần nhớ: Bốn trụ cột của Học liên kết hiện đại (2020–2026)

Bài đọc cuối khóa này khép lại chuỗi kết nối giữa tất cả các chương tối ưu bạn đã học:

- **FedProx (Sợi dây neo Proximal $$\frac{\mu}{2}\|w - w_t\|_2^2$$):** Thêm số hạng phạt bậc hai vào hàm mục tiêu cục bộ của từng máy khách để ngăn trọng số chạy quá xa mô hình toàn cục $$w_t$$ — cực kỳ đơn giản, không cần lưu trạng thái cục bộ, xử lý tốt cả non-IID lẫn máy khách yếu chỉ chạy kịp ít bước.
- **SCAFFOLD (Biến kiểm soát kiểu SVRG cho Liên kết):** Mượn trực tiếp ý tưởng biến kiểm soát (control variate) của SVRG (Chương 26) và tinh thần đối ngẫu của ADMM (Chương 21): mỗi máy khách giữ ước lượng hướng trôi $$c_i$$, sửa gradient cục bộ thành $$\nabla F_i(w) - c_i + c$$ để **triệt tiêu hoàn toàn client drift** mà không cần bước proximal chính xác.
- **FedOpt / FedAdam (Tối ưu hai cấp máy khách – máy chủ):** Coi hiệu số trung bình $$\Delta_t = w_t - \sum_i p_i w_{t+1}^{(i)}$$ như một "giả gradient" (pseudo-gradient) ở phía máy chủ, rồi áp dụng Momentum hoặc Adam lên $$\Delta_t$$ ở phía máy chủ trong khi máy khách vẫn chạy SGD gọn nhẹ.
- **Liên kết Y tế Cross-Silo (FeTS & OpenFL):** Minh chứng thực tiễn sống động nơi số nút nhỏ (vài chục bệnh viện), mỗi nút ổn định và đủ năng lực tính toán — mảnh đất lý tưởng để áp dụng cả FedProx, SCAFFOLD lẫn các khung mã nguồn mở như Flower và NVFlare.

### Giải thích: Tính tay cách FedProx và SCAFFOLD chữa bệnh Trôi cục bộ

Quay lại đúng bài toán 2 máy khách non-IID xuyên suốt Chương 29: $$F_1(w) = \frac{1}{2}w^2$$ và $$F_2(w) = \frac{3}{2}(w - 4)^2$$ với nghiệm toàn cục $$w^\star = 3.0$$, xuất phát từ $$w_t = 3.0$$ (nhớ rằng FedAvg thuần với $$E \to \infty$$ đã trôi tụt về $$2.0$$, sai số $$1.0$$!).

1. **Dùng FedProx với hệ số neo $$\mu = 2$$ (mỗi máy cực tiểu hóa $$F_i(w) + \frac{2}{2}(w - 3)^2$$):**
   - *Máy khách 1:* $$\nabla\bigl[\frac{1}{2}w^2 + (w - 3)^2\bigr] = w + 2(w - 3) = 0 \implies w^{(1)} = 2.0$$ (được kéo lại gần $$3.0$$ hơn rất nhiều so với $$0.0$$!).
   - *Máy khách 2:* $$\nabla\bigl[\frac{3}{2}(w - 4)^2 + (w - 3)^2\bigr] = 3(w - 4) + 2(w - 3) = 0 \implies 5w = 18 \implies w^{(2)} = 3.6$$ (gần $$3.0$$ hơn $$4.0$$!).
   - *Trung bình máy chủ:* $$w_{t+1}^{\text{FedProx}} = \frac{2.0 + 3.6}{2} = 2.8$$!
   Chỉ với một số hạng neo đơn giản, sai số trôi đã giảm **5 lần** (từ $$1.0$$ xuống còn $$0.2$$)!
2. **Dùng SCAFFOLD (với biến kiểm soát lý tưởng $$c_1 = \nabla F_1(3) = +3,\; c_2 = \nabla F_2(3) = -3$$ và trung bình toàn cục $$c = \frac{3 + (-3)}{2} = 0$$):**
   Tại $$w = 3.0$$, gradient đã hiệu chỉnh của cả hai máy khách đều là:
   - *Máy khách 1:* $$g_1^{\text{corr}} = \nabla F_1(3) - c_1 + c = 3 - 3 + 0 = 0$$!
   - *Máy khách 2:* $$g_2^{\text{corr}} = \nabla F_2(3) - c_2 + c = (-3) - (-3) + 0 = 0$$!
   Cả hai máy đứng yên tại **đúng $$w^\star = 3.0$$** — sai số trôi bằng $$0$$ tuyệt đối! Nhìn lại cả ba bài 29-02 → 29-03 → 29-04 trên cùng một ví dụ số, bạn đã thấy trọn vẹn mạch tiến hóa tuyệt đẹp của tối ưu hóa liên kết hiện đại.

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
