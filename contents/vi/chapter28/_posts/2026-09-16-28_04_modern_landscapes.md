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
