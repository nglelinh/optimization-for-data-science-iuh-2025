---
layout: post
title: 18-08 Ứng dụng hiện đại của phương pháp quasi-Newton (2022–2026)
chapter: '18'
order: 10
owner: Nguyen Le Linh
categories:
- chapter18
lang: vi
lesson_type: optional
---

Phương pháp quasi-Newton thay $$\nabla^2 f(x)$$ bằng một ma trận $$B$$ thỏa phương trình cát tuyến $$B^{+}s = y$$ và (với BFGS/L-BFGS) giữ xác định dương dưới điều kiện độ cong $$y^\top s > 0$$. Các ứng dụng 2022–2026 vẫn *trông như chương này* không phải các bộ tiền huấn luyện LLM ước lượng Hessian đường chéo (những cái đó thuộc Newton / Sophia ở Chương 14). Chúng là các mã giữ một lịch sử ngắn các cặp $$(s,y)$$ — L-BFGS trong học máy khoa học và trong mô hình bảng cổ điển — và các tiền điều kiện có cấu trúc (Shampoo / SOAP) là họ hàng Kronecker của BFGS.

## PINN: Adam để tới gần, L-BFGS để kết

Mạng nơ-ron thông tin vật lý cực tiểu hóa phần dư chứa toán tử vi phân. Những toán tử đó làm mất mát điều kiện xấu: dải trị riêng Hessian bám phổ của PDE rời rạc, không phải phổ của entropy chéo. Rathore, Lei, Frangella, Lu và Udell (ICML 2024) so Adam, L-BFGS, và **Adam+L-BFGS**, cho thấy tổ hợp thắng từng phương pháp riêng, và giới thiệu NysNewton-CG như một tinh chỉnh bậc hai thêm. Đóng góp lý thuyết của bài là mối liên hệ giữa toán tử vi phân điều kiện xấu và Hessian PINN điều kiện xấu — đúng vì sao phương pháp cát tuyến, vốn tích độ cong dọc quỹ đạo, thắng phương pháp thích nghi đường chéo không bao giờ thấy khớp phần dư ngoài đường chéo.

Công thức huấn luyện mà các bài thực sự chuyển đi cũ hơn 2024 và vẫn chuẩn năm 2026: chạy Adam tới khi phần dư vào một bát toàn phương, rồi chuyển sang L-BFGS với tìm kiếm dòng Wolfe. Urbán, Stefanou, Pons et al. (2024, [arXiv:2405.04230](https://arxiv.org/abs/2405.04230)) nêu cùng cách tách và đo lượng độ chính xác mà BFGS / L-BFGS thêm sau phần mở Adam. Đây là Chương 18 trong sổ lab: đệ quy hai vòng của 18-07, không phải bộ tối ưu mới.

## BFGS tự co trên PINN, PIKAN và DeepONet

Kiyani, Shukla, Urbán, Darbon và Karniadakis (2025, [arXiv:2501.16371](https://arxiv.org/abs/2501.16371)) xem lại lớp Broyden bạn học ở 18-05. **BFGS tự co** và **Broyden tự co** co giãn xấp xỉ Hessian bằng cặp độ cong mới nhất, một bảo vệ cổ điển (Oren–Luenberger) chống biến thiên bước hoang của phần dư PDE. Trên Burgers, Allen–Cahn, Kuramoto–Sivashinsky và Ginzburg–Landau, và trên mạng Kolmogorov–Arnold thông tin vật lý, họ báo cải thiện phần dư hàng bậc độ lớn *không* cần trọng số mất mát thích nghi mà các bài PINN thường cần. Cùng cập nhật giúp huấn luyện DeepONet.

Đọc đây như một thí nghiệm lớp Broyden sống: $$\phi=0$$ là BFGS, $$\phi=1$$ là DFP, và một thành viên tự co là $$\phi$$ phụ thuộc dữ liệu cộng một hệ số vô hướng. Điều kiện độ cong $$y^\top s>0$$ được buộc bởi tìm kiếm dòng; khi thất bại, cặp bị bỏ — cùng phép bỏ mà mọi cài L-BFGS vẫn dùng.

## L-BFGS-B như mặc định lặng lẽ trong ML bảng

`LogisticRegression(solver="lbfgs")` của scikit-learn và họ GLM (`solver="lbfgs"`, mặc định cạnh `newton-cholesky`) gọi **L-BFGS-B** của SciPy: BFGS bộ nhớ hạn chế với ràng buộc hộp. Với $$n$$ hàng chục nghìn và $$d$$ hàng trăm tới vài nghìn, đây vẫn là thuật toán đúng — rẻ hơn lập Hessian, chính xác hơn SGD trên GLM lồi, và khởi động ấm được dọc đường regularize. Hugging Face Trainer lộ `optim="lbfgs"` cho tinh chỉnh hiếm đủ nhỏ; sự kiện văn hóa quan trọng là ngược câu chuyện Sophia: *khi mô hình vừa một phác Hessian CPU gồm vài chục vector, quasi-Newton thắng Adam*.

Một kiểm năm dòng:

```python
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(solver="lbfgs", max_iter=200, C=1.0)
clf.fit(X, y)
print(clf.n_iter_)
```

So với `solver="newton-cholesky"` (Chương 14) trên thiết kế cao và với `solver="saga"` trên thiết kế rộng. Bạn đang chọn giữa Newton, L-BFGS, và phương pháp bậc nhất giảm phương sai chỉ bằng các chiều $$n,d$$ và kiểu ràng buộc.

## SOAP: cơ sở riêng của Shampoo như quasi-Newton có cấu trúc

Vyas, Morwani, Zhao, Kwun, Shapira, Brandfonbrener, Janson và Kakade (ICLR 2025) giới thiệu **SOAP** (*ShampoO with Adam in the Preconditioner's eigenbasis*). Shampoo (Gupta, Koren, Singer, 2018; các bản phục hưng quy mô lớn 2023–2024) giữ các ma trận mô-men hai phân rã Kronecker và là lai quasi-Newton / gradient tự nhiên có cấu trúc. SOAP chứng minh Shampoo với nghịch đảo căn là Adafactor chạy trong cơ sở riêng của Shampoo, rồi *thay* Adafactor bằng AdamW trong cơ sở chuyển chậm đó. Trên mô hình ngôn ngữ 360 triệu và 660 triệu, ở chế độ lô lớn, SOAP cắt số vòng hơn 40% và thời gian tường hơn 35% so với AdamW, và khoảng 20% so với Shampoo.

Đây không phải L-BFGS — không có cặp $$(s,y)$$ — nhưng cùng luận đề thiết kế với DFP/BFGS: *ước lượng độ cong xác định dương, đảo rẻ, làm mới trên lịch chậm hơn gradient.* Siêu tham số thêm là tần suất phân rã riêng, tương tự bộ nhớ $$m$$ của L-BFGS. Đặt SOAP cạnh K-FAC (Chương 14) trong seminar; đặt L-BFGS cạnh PINN trong lab.

## Nguồn

- P. Rathore, W. Lei, Z. Frangella, L. Lu, M. Udell, “Challenges in Training PINNs: A Loss Landscape Perspective,” ICML 2024, PMLR 235.
- W. Urbán et al., “Unveiling the optimization process of Physics Informed Neural Networks,” 2024. [arXiv:2405.04230](https://arxiv.org/abs/2405.04230)
- E. Kiyani, K. Shukla, J. F. Urbán, J. Darbon, G. E. Karniadakis, “Optimizing the Optimizer for Physics-Informed Neural Networks and Kolmogorov-Arnold Networks,” 2025. [arXiv:2501.16371](https://arxiv.org/abs/2501.16371)
- N. Vyas et al., “SOAP: Improving and Stabilizing Shampoo using Adam,” ICLR 2025. [arXiv:2409.11321](https://arxiv.org/abs/2409.11321)
- SciPy `L-BFGS-B`; scikit-learn `LogisticRegression(solver="lbfgs")`.
