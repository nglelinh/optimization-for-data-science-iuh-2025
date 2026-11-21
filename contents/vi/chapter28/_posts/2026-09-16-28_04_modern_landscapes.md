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


Các bài 28-01 đến 28-03 đã định nghĩa điểm tới hạn, yên ngựa, và quá tham số. Ghi chú tùy chọn này là bốn hiện tượng *thực nghiệm* mà những định nghĩa đó nhằm mở khóa. Nó không chứng minh lại rằng yên ngựa chiều cao chiếm ưu thế, và không suy diễn lại bất đẳng thức PL.

## 1. Liên thông mode: cực tiểu không phải đảo

Garipov, Izmailov, Podoprikhin, Vetrov và Wilson (NeurIPS 2018) cùng Draxler, Veschgini, Salmhofer và Hamprecht (ICML 2018) cho thấy hai nghiệm SGD của một mạng sâu có thể nối bằng một đường *đa giác* loss thấp — thường hai đoạn thẳng — trên đó loss huấn luyện gần như không đổi. Frankle, Dziugaite, Roy và Carbin (ICML 2020) gắn cùng bức tranh với văn liệu vé số. Tinh chỉnh 2025 (giam cầm entropy, [arXiv:2512.06297](https://arxiv.org/abs/2512.06297)) là câu đấm ở mức sinh viên: đường có thể *loss thấp* mà vẫn *độ cong cao* ở giữa, nên SGD nhiễu ở lại một lưu vực dù tồn tại đường tất định sang lưu vực khác. Liên thông là phát biểu về *tập dưới mức*; giam cầm là phát biểu về *động lực học*. Chương 28 cần cả hai.

## 2. Grokking: tổng quát hóa lâu sau nội suy

Power, Burda, Edwards, Babuschkin và Misra, *Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets*, [arXiv:2201.02177](https://arxiv.org/abs/2201.02177), 2022, huấn luyện transformer nhỏ trên số học modulo. Độ chính xác huấn luyện chạm 100% nhanh; độ chính xác *kiểm chứng* ở mức ngẫu nhiên thêm nhiều bậc độ lớn bước, rồi nhảy. Diễn giải phong cảnh thuộc chương này: nội suy (loss huấn luyện $$\approx 0$$) không phải hết huấn luyện. Bộ tối ưu vẫn chuyển động *bên trong* tập nội suy, và thiên kiến ẩn của Chương 28-03 cuối cùng chọn một điểm tổng quát hóa. Weight decay (AdamW, 26-04) thực nghiệm cần cho grokking trên các bài này — lời nhắc khác rằng bộ tối ưu là một phần thiên kiến quy nạp.

## 3. Double descent, nay là sự thật phong cảnh

Belkin, Hsu, Ma và Mandal, *PNAS* 2019, và Nakkiran, Kaplun, Bansal, Yang, Barak và Sutskever, ICLR 2020 (bản thảo 2019, [arXiv:1912.02292](https://arxiv.org/abs/1912.02292)), cho thấy lỗi kiểm tra có thể *tăng* tại ngưỡng nội suy rồi *giảm* lại khi mô hình lớn thêm. Quá tham số (28-03) không phải bệnh lý; đó là nửa sau của đường cong đó. Các bài theo 2022–2024 (double descent theo epoch, theo dữ liệu) là cùng hình học với trục khác. Khi sinh viên nói “thêm tham số thì quá khớp,” hình cần vẽ là double descent, không phải đường U thống kê thập niên 1990.

## 4. Cực tiểu phẳng và SAM, nhìn từ Hessian

Foret et al., ICLR 2021 (SAM; chi tiết ở [26-06]({% multilang_post_url contents/chapter26/2026-09-16-26_06_modern_optimizers %})) là *thuật toán* thích vùng phẳng. Bartlett, Long và Bousquet, *JMLR* 24(43), 2023, cùng Shin, Lee, Andriushchenko và Lee, [arXiv:2311.17539](https://arxiv.org/abs/2311.17539), biến nó thành phát biểu *phong cảnh*: cực tiểu SAM ổn định tuyến tính có phổ Hessian đều hơn, và khe tổng quát hóa giữa SAM và SGD *nới* khi mạng càng quá tham số. Bạn không cần hiện thực SAM để dùng mục này. Bạn cần thôi nói “cực tiểu địa phương là cực tiểu địa phương.” Trong mạng sâu nội suy, các cực tiểu khác nhau bởi độ sắc, và độ sắc là câu chuyện Hessian (hoặc PAC-Bayes), không phải bậc nhất.

Mở [loss_function_landscapes.html](https://nglelinh.github.io/interactive_math/optimization/loss_function_landscapes.html) và nhìn một lát 2-D: cùng loss thấp có thể nằm trong khe hoặc bát. Hoạt họa đó là toàn bộ 28-04.

**Bài tập.** (i) Trên mạng ReLU ngẫu nhiên 2-D, lấy hai nghiệm SGD và vẽ loss dọc đường thẳng $$w(t)=(1-t)w_A+t w_B$$. Bạn thường thấy rào (đường thẳng là nối *sai*). (ii) Chèn một khúc $$w_{1/2}= (w_A+w_B)/2 + v$$ và cực tiểu hóa rào theo $$v$$ nhỏ — tìm liên thông mode kiểu nghèo. (iii) Đọc Hình 1 của Power et al. và viết ba câu vì sao độ chính xác huấn luyện là quy tắc dừng sai cho đồ thị đó.

## Nguồn

- T. Garipov et al., NeurIPS 2018; F. Draxler et al., ICML 2018 — liên thông mode.
- J. Frankle et al., ICML 2020 — liên thông và vé số.
- Giam cầm entropy, [arXiv:2512.06297](https://arxiv.org/abs/2512.06297), 2025.
- A. Power et al., [arXiv:2201.02177](https://arxiv.org/abs/2201.02177), 2022 — grokking.
- M. Belkin et al., *PNAS* 2019; P. Nakkiran et al., ICLR 2020 — double descent.
- P. Foret et al., ICLR 2021; P. L. Bartlett et al., *JMLR* 24(43), 2023 — SAM / cực tiểu phẳng.
- S. Shin, D. Lee, M. Andriushchenko, N. Lee, [arXiv:2311.17539](https://arxiv.org/abs/2311.17539) — SAM và quá tham số.
