---
layout: post
title: 28-04 Nghiên cứu tình huống phong cảnh hiện đại
chapter: '28'
order: 5
owner: Nguyen Le Linh
categories:
- chapter28
lang: vi
lesson_type: optional
---

Nếu ba bài trước là bản đồ lý thuyết của thế giới không lồi, thì bài đọc này đưa bạn vào bảo tàng những **hiện tượng thực nghiệm kỳ lạ nhất của học sâu hiện đại** — những hiện tượng từng khiến giới thống kê cổ điển phải viết lại sách giáo khoa: hai mạng nơ-ron huấn luyện hoàn toàn độc lập có thể nối với nhau bằng một con đường mất mát gần bằng $$0$$ (**mode connectivity**); mạng Transformer sau khi đã đạt $$100\%$$ độ chính xác tập train bỗng nhiên "giác ngộ" trên tập test sau hàng chục nghìn bước tiếp theo (**grokking**); và sai số kiểm tra tăng vọt ở ngưỡng nội suy rồi lại giảm sâu hơn nữa khi tăng thêm kích thước mạng (**double descent**).

Điểm chung đáng kinh ngạc của cả bốn hiện tượng trong bài là chúng đều bắt nguồn trực tiếp từ hình học địa hình hàm mất mát và động lực học tối ưu mà bạn vừa học!

## Kiến thức cần nhớ: Bốn hiện tượng thực nghiệm định hình lý thuyết học sâu hiện đại

Khi đọc bốn nghiên cứu tình huống trong bài, hãy gắn từng hiện tượng với nguyên lý tối ưu tương ứng:

- **Liên thông mode (Mode Connectivity) và Tính đối xứng:** Do mạng nơ-ron bất biến dưới hoán vị các nơ-ron ẩn, các cực tiểu không nằm tách rời như những hố cô lập mà tạo thành mạng lưới thung lũng liên thông trong tập dưới mức; tuy nhiên *hàng rào mất mát thấp* vẫn có thể kèm *hàng rào entropy/độ cong cao* giữ SGD ở lại từng nhánh.
- **Grokking (Tổng quát hóa muộn sau khi nội suy):** Sau khi mất mát dữ liệu đã bằng $$0$$, trọng số vẫn tiếp tục trượt bên trong đa tạp nghiệm nội suy dưới tác dụng của **weight decay (AdamW)** và thiên kiến ẩn, dần chuyển từ mạch "học vẹt" (chuẩn trọng số lớn) sang mạch "thuật toán tổng quát" (chuẩn trọng số nhỏ).
- **Giảm kép (Double Descent):** Đường cong chữ U cổ điển của đánh đổi thiên lệch–phương sai chỉ mô tả nhánh trái ($$d < n$$). Tại ngưỡng nội suy $$d \approx n$$, ma trận thiết kế gần suy biến làm chuẩn nghiệm bùng nổ (đỉnh sai số test); vượt sang nhánh phải ($$d \gg n$$), thiên kiến ẩn chọn nghiệm chuẩn nhỏ lại kéo sai số test giảm sâu xuống lần thứ hai!
- **Phổ Hessian thực nghiệm của mạng sâu:** Khi đo phổ Hessian của mạng đã huấn luyện, ta luôn thấy một "khối lớn" trị riêng tập trung quanh $$0$$ (hàng triệu phương phẳng) cùng đúng vài trị riêng tách rời lớn (thường bằng số lớp phân loại $$C$$) — xác nhận bức tranh hình học vừa phẳng vừa dị hướng của mạng sâu.

### Giải thích: Tính tay vì sao nội suy thẳng giữa hai cực tiểu hoán vị gặp "ngọn núi" mất mát

Xét mạng nơ-ron 1 lớp ẩn gồm 2 nơ-ron: $$f_\theta(x) = a_1 \max(0, b_1 x) + a_2 \max(0, b_2 x)$$ với 4 tham số $$\theta = (a_1, b_1, a_2, b_2)$$. Giả sử hàm đích là $$y(x) = \max(0, 2x) - \max(0, 3x)$$ (bằng $$-x$$ với $$x > 0$$ và $$0$$ với $$x \le 0$$).

1. **Hai nghiệm tối ưu toàn cục hoàn toàn đối xứng (hoán vị nơ-ron 1 và nơ-ron 2):**
   - Nghiệm A: $$\theta_A = (1,\; 2,\; -1,\; 3) \implies f_{\theta_A}(x) = 1\cdot\max(0, 2x) - 1\cdot\max(0, 3x) = y(x)$$ (mất mát $$= 0$$!).
   - Nghiệm B: $$\theta_B = (-1,\; 3,\; 1,\; 2) \implies f_{\theta_B}(x) = -1\cdot\max(0, 3x) + 1\cdot\max(0, 2x) = y(x)$$ (mất mát $$= 0$$!).
2. **Thử đi theo đoạn thẳng nối $$\theta_A$$ và $$\theta_B$$ tại trung điểm $$\theta_{\text{mid}} = \frac{1}{2}(\theta_A + \theta_B)$$:**
   $$\theta_{\text{mid}} = \left(\frac{1 + (-1)}{2},\; \frac{2 + 3}{2},\; \frac{-1 + 1}{2},\; \frac{3 + 2}{2}\right) = (0,\; 2.5,\; 0,\; 2.5)!$$
   Tại trung điểm này, cả hai trọng số lớp ra đều bằng $$0$$, nên $$f_{\theta_{\text{mid}}}(x) \equiv 0$$ — **sai lệch hoàn toàn so với $$y(x) = -x$$**, tạo thành một ngọn núi mất mát lớn chắn giữa đường thẳng!
3. **Thông điệp của Mode Connectivity:** Hai nghiệm tốt không thể nối bằng *đoạn thẳng* do khác thứ tự hoán vị nơ-ron, nhưng lại có thể nối bằng một **đường gấp khúc 2 đoạn** (hoặc căn chỉnh lại hoán vị trước khi lấy trung bình trọng số) mà mất mát vẫn giữ gần bằng $$0$$ suốt dọc đường — mở đường cho kỹ thuật trộn mô hình (*model soup / weight averaging*) hiện đại!

Các bài 28-01 đến 28-03 đã xây dựng các khái niệm điểm tới hạn, điểm yên ngựa và quá tham số hóa. Bài đọc tùy chọn này điểm qua bốn hiện tượng *thực nghiệm* nổi bật trong học sâu hiện đại gắn trực tiếp với các khái niệm đó.

## 1. Liên thông mode: các cực tiểu không bị cô lập

Garipov, Izmailov, Podoprikhin, Vetrov và Wilson (NeurIPS 2018) cùng Draxler, Veschgini, Salmhofer và Hamprecht (ICML 2018) chỉ ra rằng hai nghiệm độc lập tìm được bởi SGD trên một mạng sâu thường có thể nối với nhau bằng một đường gấp khúc đơn giản (thường chỉ gồm hai đoạn thẳng) mà dọc theo đó hàm mất mát huấn luyện hầu như không tăng. Frankle, Dziugaite, Roy và Carbin (ICML 2020) liên kết tính chất này với hướng nghiên cứu giả thuyết vé số (lottery ticket hypothesis). Một phân tích cập nhật năm 2025 về hiện tượng giam cầm entropy ([arXiv:2512.06297](https://arxiv.org/abs/2512.06297)) làm rõ thêm: đường nối tuy có *giá trị mất mát thấp* nhưng có thể sở hữu *độ cong cao* ở đoạn giữa, khiến SGD có nhiễu vẫn ở lại trong một vùng trũng dù tồn tại đường đi tất định sang vùng trũng khác. Như vậy, tính liên thông là tính chất của *tập dưới mức (sublevel set)*, còn hiện tượng giam cầm là tính chất của *động lực học tối ưu*.

## 2. Grokking: tổng quát hóa xuất hiện rất lâu sau khi nội suy

Power, Burda, Edwards, Babuschkin và Misra (*Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets*, [arXiv:2201.02177](https://arxiv.org/abs/2201.02177), 2022) huấn luyện các mạng transformer nhỏ trên các bài toán số học modulo. Độ chính xác trên tập huấn luyện đạt 100% rất nhanh, nhưng độ chính xác *kiểm định* vẫn ở mức ngẫu nhiên trong hàng bậc độ lớn bước tiếp theo trước khi đột ngột tăng vọt. Góc nhìn từ địa hình hàm mất mát giải thích hiện tượng này: đạt trạng thái nội suy (mất mát huấn luyện $$\approx 0$$) chưa phải là kết thúc quá trình tối ưu. Bộ tối ưu vẫn tiếp tục dịch chuyển *bên trong* tập các nghiệm nội suy, và thiên kiến ẩn (28-03) cùng suy giảm trọng số (AdamW, 26-04) dần dẫn mô hình sang nghiệm có khả năng tổng quát hóa tốt.

## 3. Hiện tượng giảm kép (Double descent)

Belkin, Hsu, Ma và Mandal (*PNAS*, 2019) và Nakkiran, Kaplun, Bansal, Yang, Barak và Sutskever (ICLR 2020; bản thảo 2019, [arXiv:1912.02292](https://arxiv.org/abs/1912.02292)) chứng minh thực nghiệm rằng sai số kiểm tra có thể *tăng đỉnh* tại ngưỡng nội suy rồi lại *giảm xuống* khi kích thước mô hình tiếp tục vượt vào miền quá tham số hóa. Quá tham số hóa (28-03) vì thế không phải là trạng thái bất thường mà là nhánh thứ hai của đường cong này. Các nghiên cứu giai đoạn 2022–2024 tiếp tục ghi nhận cùng quy luật theo số epoch và kích thước tập dữ liệu, thay thế quan niệm đường cong chữ U cổ điển cho các mô hình lớn.

## 4. Cực tiểu phẳng và SAM dưới góc nhìn Hessian

SAM (Foret và cộng sự, ICLR 2021; xem chi tiết ở [26-06]({% multilang_post_url contents/chapter26/2026-09-16-26_06_modern_optimizers %})) là *thuật toán* hướng quá trình học về vùng phẳng. Các phân tích của Bartlett, Long và Bousquet (*JMLR* 24(43), 2023) cùng Shin, Lee, Andriushchenko và Lee ([arXiv:2311.17539](https://arxiv.org/abs/2311.17539)) chuyển quan sát đó thành tính chất *địa hình*: các cực tiểu ổn định của SAM có phổ trị riêng Hessian đồng đều hơn, và khoảng cách tổng quát hóa giữa SAM và SGD *mở rộng* khi mức độ quá tham số hóa tăng lên. Trong các mạng nội suy, không phải mọi cực tiểu địa phương đều tương đương nhau: chúng khác biệt ở độ sắc, và độ sắc được đặc trưng bởi thông tin bậc hai (Hessian hoặc cận PAC-Bayes) chứ không chỉ điều kiện bậc nhất.

Mở [loss_function_landscapes.html](https://nglelinh.github.io/interactive_math/optimization/loss_function_landscapes.html) để quan sát trực quan trên lát cắt 2 chiều sự khác biệt giữa các cực tiểu nằm trong khe hẹp và vùng trũng rộng.

**Bài tập.** (i) Trên một mạng ReLU 2 chiều nhỏ, lấy hai nghiệm tìm được từ SGD với khởi tạo khác nhau và vẽ hàm mất mát dọc đoạn thẳng $$w(t)=(1-t)w_A+t w_B$$ để quan sát hàng rào mất mát ở giữa. (ii) Chèn thêm một điểm uốn $$w_{1/2}= (w_A+w_B)/2 + v$$ và tối ưu theo vector $$v$$ nhỏ để tìm một đường gấp khúc có mức mất mát thấp nối hai nghiệm. (iii) Xem Hình 1 của Power và cộng sự và giải thích ngắn gọn vì sao độ chính xác huấn luyện là tiêu chí dừng không phù hợp trong bối cảnh grokking.

## Nguồn

- T. Garipov et al., NeurIPS 2018; F. Draxler et al., ICML 2018 — liên thông mode.
- J. Frankle et al., ICML 2020 — liên thông và vé số.
- Giam cầm entropy, [arXiv:2512.06297](https://arxiv.org/abs/2512.06297), 2025.
- A. Power et al., [arXiv:2201.02177](https://arxiv.org/abs/2201.02177), 2022 — grokking.
- M. Belkin et al., *PNAS* 2019; P. Nakkiran et al., ICLR 2020 — double descent.
- P. Foret et al., ICLR 2021; P. L. Bartlett et al., *JMLR* 24(43), 2023 — SAM / cực tiểu phẳng.
- S. Shin, D. Lee, M. Andriushchenko, N. Lee, [arXiv:2311.17539](https://arxiv.org/abs/2311.17539) — SAM và quá tham số.
