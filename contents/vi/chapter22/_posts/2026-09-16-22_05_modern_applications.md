---
layout: post
title: 22-05 Ứng dụng hiện đại của Frank–Wolfe
chapter: '22'
order: 6
owner: Nguyen Le Linh
categories:
- chapter22
lang: vi
lesson_type: optional
redirect_from:
  - /contents/vi/chapter22/22_06_modern_applications/
---


Frank–Wolfe (gradient có điều kiện) là lựa chọn phù hợp khi tập khả thi $$\mathcal{C}$$ có **bộ giải cực tiểu tuyến tính (linear minimization oracle — LMO)** rẻ:

$$
s_k \in \arg\min_{s\in\mathcal{C}}\ \langle \nabla f(x_k), s\rangle
$$

trong khi *phép chiếu* lên $$\mathcal{C}$$ tốn kém hoặc phá vỡ tính thưa của nghiệm. Làn sóng nghiên cứu thập niên 2010 (Jaggi; Lacoste-Julien) đã hình thành nên bộ công cụ ứng dụng rộng rãi trong thập niên 2020: dự đoán có cấu trúc, vận chuyển tối ưu và giải thích mạng nơ-ron có ràng buộc. Bài đọc tùy chọn này trình bày bốn trường hợp tiêu biểu, không lặp lại phần chứng minh hội tụ.

## 1. Dự đoán có cấu trúc: Frank–Wolfe theo khối tọa độ

Bài toán cực tiểu hóa rủi ro thực nghiệm (ERM) trong dự đoán có cấu trúc (CRF, SVM có cấu trúc) có dạng:

$$
\min_{w}\ \frac{\lambda}{2}\|w\|_2^2 + \frac1n\sum_{i=1}^n \max_{y\in\mathcal{Y}_i}\bigl(\langle w, \phi(x_i,y)\rangle - \delta(y_i,y)\bigr).
$$

Bài toán đối ngẫu là tối ưu trên tích Descartes của các đơn hình (simplex) xác suất. Nhờ cấu trúc tích này, mỗi bước **Frank–Wolfe theo khối tọa độ (BCFW)** tương ứng đúng với một lần gọi *suy luận tăng cường hàm mất mát (loss-augmented inference)* — chính là bộ giải vốn đã có sẵn trong mô hình cấu trúc. Công trình của Lacoste-Julien, Jaggi, Schmidt và Pletscher (ICML 2013) đặt nền móng cho hướng này, và đó vẫn là lý do Frank–Wolfe được duy trì trong các thư viện dự đoán có cấu trúc hiện nay.

Cùng ý tưởng tách theo khối tọa độ được áp dụng sang **vận chuyển tối ưu (optimal transport — OT)**. Fukunaga và Kasai ([arXiv:2205.13766](https://arxiv.org/abs/2205.13766), 2022; bản hội nghị ICASSP 2022) triển khai BCFW — bao gồm cả biến thể away-step và pairwise step — cho bài toán OT *bán nới lỏng (semi-relaxed)*, nơi ràng buộc biên chặt thông thường buộc phải giải một bài toán quy hoạch tuyến tính đầy đủ. Bộ giải tuyến tính trên từng khối có nghiệm dạng đóng trên đơn hình và tạo ra kế hoạch vận chuyển thưa. Ứng dụng minh họa chính của bài báo là **chuyển màu (color transfer)** giữa hai ảnh: kế hoạch vận chuyển có cấu trúc thưa trên đơn hình đúng với thế mạnh bảo toàn tính thưa của Frank–Wolfe.

## 2. Vận chuyển tối ưu không cân bằng một chiều

Séjourné, Feydy, Vialard, Trouvé và Peyré (AISTATS 2022, [PMLR v151](https://proceedings.mlr.press/v151/sejourne22a.html)) áp dụng Frank–Wolfe lên bài toán *đối ngẫu* của vận chuyển tối ưu không cân bằng 1 chiều (1-D unbalanced OT). Bài toán con tuyến tính hóa lúc này là bài toán OT 1 chiều *cân bằng*, có thể giải trong thời gian tuyến tính sau một bước sắp xếp. Đây là minh họa trực diện cho nguyên lý của Frank–Wolfe: thay thế bài toán phi tuyến khó bằng một bộ giải tuyến tính đơn giản và hiệu quả. Nhóm tác giả cũng tính tâm khối (barycenter) 1 chiều bằng cùng phép tuyến tính hóa. Khi cần nghiệm UOT *không chính quy hóa*, Frank–Wolfe có thể vượt trội Sinkhorn; ngược lại, khi cần kế hoạch ghép trơn và tận dụng GPU tốt, Sinkhorn vẫn có ưu thế. Điều quan trọng là hiểu rõ *vì sao* có sự đánh đổi này thay vì chỉ chọn một phương pháp cố định.

## 3. Giải thích mạng nơ-ron có ràng buộc

Macdonald, Besançon và Pokutta (ICML 2022, [PMLR v162](https://proceedings.mlr.press/v162/macdonald22a.html)) phát biểu lại bài toán **giải thích theo độ méo–tốc độ (rate-distortion explanation — RDE)** dưới dạng tối ưu có ràng buộc và giải bằng Frank–Wolfe tất định cũng như ngẫu nhiên. Yêu cầu độ thưa của bản đồ độ liên quan trở thành ràng buộc hình cầu $$\ell_1$$ (hoặc đơn hình); còn biến thể *xếp hạng đặc trưng* tối ưu trên **đa diện Birkhoff** (bao lồi của tập các ma trận hoán vị), nơi bộ giải tuyến tính quy về bài toán gán tuyến tính (linear assignment). Trên các bộ dữ liệu phân loại ảnh tiêu chuẩn, các biến thể đa tốc độ và xếp hạng đạt kết quả tốt hơn RDE gốc. Về bản chất, đây là một dạng dự đoán có cấu trúc: miền đa diện mã hóa dạng lời giải thích dễ đọc, và Frank–Wolfe tránh hoàn toàn phép chiếu tốn kém lên đa diện đó.

## 4. Bài tổng quan năm 2024 đáng tham khảo

Bomze, Rinaldi và Zeffiro, **“Frank–Wolfe and friends: a journey into projection-free first-order optimization methods”**, *Ann. Oper. Res.* 343:607–638, 2024, [doi:10.1007/s10479-024-06251-7](https://doi.org/10.1007/s10479-024-06251-7), hệ thống hóa các ứng dụng từ gán lưu lượng giao thông, tối ưu hàm dưới mô-đun (submodular), hoàn thiện ma trận, tấn công đối kháng, huấn luyện SVM đến tìm tập đầy đủ cực đại (maximum clique), đồng thời trình bày các biến thể hiện đại (away-step, pairwise, sliding, ngẫu nhiên). Đây là tài liệu tra cứu tổng quan hữu ích khi cần chọn biến thể phù hợp cho từng ứng dụng.

## Khi nào nên chọn Frank–Wolfe thay vì gradient có chiếu

Nên dùng Frank–Wolfe khi: (i) tập ràng buộc $$\mathcal{C}$$ là đa diện, phổ diện (spectrahedron) hoặc đa diện luồng mà LMO quy về một phép sắp xếp, bài toán gán hay tìm vector kỳ dị hàng đầu; và (ii) mong muốn các điểm lặp giữ dạng tổ hợp lồi thưa của ít nguyên tử. Ngược lại, nên chọn phương pháp chiếu khi phép chiếu rất rẻ (như cắt ngưỡng trên hình hộp hay chiếu lên đơn hình theo thuật toán Michelot) và cần tốc độ hội tụ tuyến tính mà Frank–Wolfe thuần không đạt được nếu thiếu away-step.

**Bài tập.** Xét bài toán mô phỏng chuyển màu 1 chiều với hai biểu đồ tần suất $$a,b\in\Delta^{k}$$ và ma trận chi phí $$C_{ij}=(i-j)^2$$. Hãy chạy: (i) 40 bước Frank–Wolfe trên đa diện vận chuyển (trong đó LMO là bài toán vận chuyển, có thể giải bằng `scipy.optimize.linprog` với kích thước nhỏ $$k=12$$) và (ii) gradient descent có chiếu trên cùng đa diện. So sánh số phần tử khác không trong kế hoạch vận chuyển và giá trị chi phí OT giữa hai phương pháp: Frank–Wolfe cho nghiệm thưa hơn, còn PGD thường giảm chi phí nhanh hơn ở vài bước đầu nếu phép chiếu được cài đặt chính xác.

## Nguồn

- M. Jaggi, ICML 2013 — khe đối ngẫu FW và tốc độ bất biến affine.
- S. Lacoste-Julien, M. Jaggi, M. Schmidt, P. Pletscher, ICML 2013 — BCFW cho SVM cấu trúc.
- T. Fukunaga and H. Kasai, [arXiv:2205.13766](https://arxiv.org/abs/2205.13766), 2022 / ICASSP 2022 — BCFW cho OT bán nới, chuyển màu.
- T. Séjourné et al., AISTATS 2022, [PMLR v151](https://proceedings.mlr.press/v151/sejourne22a.html) — FW cho OT không cân 1-D.
- J. Macdonald et al., ICML 2022, [PMLR v162](https://proceedings.mlr.press/v162/macdonald22a.html) — FW cho giải thích méo-tốc độ.
- I. M. Bomze, F. Rinaldi, D. Zeffiro, *Ann. Oper. Res.*, 2024, [doi:10.1007/s10479-024-06251-7](https://doi.org/10.1007/s10479-024-06251-7) — “Frank–Wolfe and friends.”
