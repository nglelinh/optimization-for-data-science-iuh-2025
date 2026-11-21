---
layout: post
title: 22-06 Ứng dụng hiện đại của Frank–Wolfe
chapter: '22'
order: 7
owner: Nguyen Le Linh
categories:
- chapter22
lang: vi
lesson_type: optional
---


Frank–Wolfe (gradient có điều kiện) là thuật toán bạn chọn khi tập khả thi $$\mathcal{C}$$ có **oracle cực tiểu tuyến tính** rẻ

$$
s_k \in \arg\min_{s\in\mathcal{C}}\ \langle \nabla f(x_k), s\rangle
$$

và *phép chiếu* lên $$\mathcal{C}$$ đắt hoặc phá thưa. Sự hồi sinh thập niên 2010 (Jaggi; Lacoste-Julien) nay là bộ công cụ thập niên 2020: dự đoán có cấu trúc, vận chuyển tối ưu, và giải thích mạng nơ-ron có ràng buộc. Ghi chú tùy chọn này là bốn nghiên cứu tình huống, không phải chứng minh hội tụ lần hai.

## 1. Dự đoán có cấu trúc: Frank–Wolfe theo khối tọa độ

Một ERM dự đoán có cấu trúc (CRF, SVM cấu trúc) có dạng

$$
\min_{w}\ \frac{\lambda}{2}\|w\|_2^2 + \frac1n\sum_{i=1}^n \max_{y\in\mathcal{Y}_i}\bigl(\langle w, \phi(x_i,y)\rangle - \delta(y_i,y)\bigr).
$$

Đối ngẫu là tối ưu trên tích các simplex xác suất — một tích Descartes mà một bước **block-coordinate Frank–Wolfe (BCFW)** chính là một lần gọi *suy luận tăng cường loss*, tức cùng oracle mà mô hình cấu trúc đã triển khai. Lacoste-Julien, Jaggi, Schmidt và Pletscher (ICML 2013) là tài liệu cổ điển; đó vẫn là lý do FW xuất hiện trong mã dự đoán có cấu trúc năm 2026.

Cùng ý tưởng khối tọa độ chuyển sang **vận chuyển tối ưu**. Fukunaga và Kasai, [arXiv:2205.13766](https://arxiv.org/abs/2205.13766) (2022; bản hội nghị ICASSP 2022), áp BCFW — kể cả away-step và pairwise step — cho bài toán OT *bán nới* mà ràng buộc biên chặt lẽ ra buộc một LP đầy đủ. Oracle tuyến tính trên mỗi khối là argmin dạng đóng trên simplex; kế hoạch ghép thưa. Ứng dụng chạy của họ là **chuyển màu** giữa ảnh: kế hoạch vận chuyển đúng là đối tượng thưa, ràng buộc simplex mà FW được thiết kế để giữ.

## 2. Vận chuyển không cân và 1-D

Séjourné, Feydy, Vialard, Trouvé và Peyré (AISTATS 2022, [PMLR v151](https://proceedings.mlr.press/v151/sejourne22a.html)) đặt Frank–Wolfe lên *đối ngẫu* của OT không cân 1-D. Bài toán con tuyến tính hóa là OT 1-D *cân*, giải được thời gian tuyến tính sau một lần sắp. Đó là hợp đồng FW trong một câu: thay chương trình phi tuyến khó bằng một oracle tuyến tính bạn đã biết cách giải. Họ cũng tính barycenter 1-D bằng cùng tuyến tính hóa. Khi mục tiêu là nghiệm UOT *không regularize*, FW có thể thắng Sinkhorn; khi bạn muốn ghép trơn, thân thiện GPU, Sinkhorn vẫn thắng. Sinh viên phải nói được *vì sao*, không chỉ *cái nào*.

## 3. Giải thích mạng nơ-ron có ràng buộc

Macdonald, Besançon và Pokutta (ICML 2022, [PMLR v162](https://proceedings.mlr.press/v162/macdonald22a.html)) viết lại **giải thích méo-tốc độ (RDE)** thành bài toán ràng buộc và giải bằng Frank–Wolfe tất định cũng như ngẫu nhiên. Độ thưa của bản đồ liên quan trở thành ràng buộc quả cầu $$\ell_1$$ (hoặc simplex); biến thể *sắp thứ tự đặc trưng* tối ưu trên **đa diện Birkhoff** (bao lồi của ma trận hoán vị), mà oracle tuyến tính là bài toán gán. Trên chuẩn phân loại ảnh, biến thể đa tốc độ và sắp thứ tự thắng RDE gốc. Đây là dự đoán có cấu trúc trá hình: “cấu trúc” là một đa diện mã hóa lời giải thích đọc được, và FW không bao giờ hiện thực hóa phép chiếu lên đa diện đó.

## 4. Khảo sát 2024 để để trên bàn

Bomze, Rinaldi và Zeffiro, **“Frank–Wolfe and friends: a journey into projection-free first-order optimization methods”**, *Ann. Oper. Res.* 343:607–638, 2024, [doi:10.1007/s10479-024-06251-7](https://doi.org/10.1007/s10479-024-06251-7), đi qua gán giao thông, tối ưu submodular, hoàn thiện ma trận, tấn công đối kháng, huấn luyện SVM, và tìm clique cực đại, rồi giải thích các biến thể thập niên 2020 (away-step, pairwise, sliding, ngẫu nhiên). Dùng khi bạn cần *thực đơn*, không khi bạn cần chứng minh.

## Khi nào FW vẫn thắng gradient chiếu năm 2026

Dùng Frank–Wolfe khi (i) $$\mathcal{C}$$ là đa diện, phổ diện, hoặc đa diện dòng chảy mà LMO là một lần sắp, một bài gán, hoặc một trị riêng, và (ii) bạn *muốn* vòng lặp ở lại tổ hợp lồi thưa của các nguyên tử. Dùng phương pháp chiếu khi phép chiếu là clip rẻ (hộp, simplex Michelot) và bạn cần tốc độ tuyến tính mà FW thuần không cho nếu không có away-step.

**Bài tập.** Đồ chơi chuyển màu: hai histogram 1-D $$a,b\in\Delta^{k}$$ và chi phí $$C_{ij}=(i-j)^2$$. Chạy (i) 40 bước FW trên đa diện vận chuyển (LMO = bài toán vận chuyển, có thể giải bằng `scipy.optimize.linprog` với $$k=12$$ nhỏ) và (ii) gradient chiếu trên cùng đa diện. So sánh số phần tử khác không trong kế hoạch và chi phí OT. FW phải thưa hơn; PGD phải giảm chi phí nhanh hơn vài bước đầu nếu bạn chiếu đúng.

## Nguồn

- M. Jaggi, ICML 2013 — khe đối ngẫu FW và tốc độ bất biến affine.
- S. Lacoste-Julien, M. Jaggi, M. Schmidt, P. Pletscher, ICML 2013 — BCFW cho SVM cấu trúc.
- T. Fukunaga and H. Kasai, [arXiv:2205.13766](https://arxiv.org/abs/2205.13766), 2022 / ICASSP 2022 — BCFW cho OT bán nới, chuyển màu.
- T. Séjourné et al., AISTATS 2022, [PMLR v151](https://proceedings.mlr.press/v151/sejourne22a.html) — FW cho OT không cân 1-D.
- J. Macdonald et al., ICML 2022, [PMLR v162](https://proceedings.mlr.press/v162/macdonald22a.html) — FW cho giải thích méo-tốc độ.
- I. M. Bomze, F. Rinaldi, D. Zeffiro, *Ann. Oper. Res.*, 2024, [doi:10.1007/s10479-024-06251-7](https://doi.org/10.1007/s10479-024-06251-7) — “Frank–Wolfe and friends.”
