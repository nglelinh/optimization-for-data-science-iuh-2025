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

Một thuật toán từ năm 1956 sống khỏe trong các hội nghị học máy hàng đầu thập niên 2020 (ICML, AISTATS, NeurIPS) không phải vì hoài cổ, mà vì cấu trúc hình học của nhiều bài toán hiện đại trùng khớp hoàn hảo với điểm mạnh nhất của nó: **tập ràng buộc có LMO siêu rẻ nhưng phép chiếu lại quá đắt**.

Từ bài toán dự đoán có cấu trúc trên hàng nghìn nhãn chuỗi, bài toán vận chuyển tối ưu (Optimal Transport) ghép phân phối màu ảnh, cho đến việc giải thích quyết định của mạng nơ-ron sâu bằng các mặt nạ thưa, Frank–Wolfe liên tục xuất hiện như một "vũ khí thầm lặng" giúp giải bài toán quy mô lớn mà vẫn giữ nguyên cấu trúc diễn giải được của nghiệm.

## Bản đồ kiến thức nền: Bốn nhánh ứng dụng hiện đại kết nối với Frank–Wolfe

Để đọc bài tổng quan ứng dụng này thật hiệu quả, hãy nắm trực giác của bốn lĩnh vực mà Frank–Wolfe đang đóng vai trò trung tâm:

- **Dự đoán có cấu trúc (Structured Prediction & BCFW):** Trong mô hình CRF hay SVM có cấu trúc, không gian nhãn $$\mathcal{Y}_i$$ lớn theo hàm mũ, khiến miền đối ngẫu là tích của $$n$$ đơn hình khổng lồ. Frank–Wolfe theo khối tọa độ (BCFW) chỉ cập nhật *một* mẫu $$i$$ mỗi bước, biến LMO thành đúng thuật toán suy luận (như Viterbi) đã có sẵn.
- **Vận chuyển tối ưu (Optimal Transport — OT):** OT tìm kế hoạch chuyển khối lượng từ phân phối nguồn sang phân phối đích với chi phí nhỏ nhất. Trong bài toán OT bán nới lỏng hoặc OT không cân bằng 1 chiều, LMO quy về thao tác tìm cực tiểu từng cột hoặc sắp xếp 1 chiều — rẻ hơn rất nhiều so với giải quy hoạch tuyến tính đầy đủ.
- **Khả năng giải thích mạng nơ-ron (Explainable AI & Rate-Distortion):** Khi giải thích vì sao mạng nơ-ron dự đoán một ảnh là "mèo", ta muốn tìm một mặt nạ đặc trưng nằm trong quả cầu $$\ell_1$$ (ít pixel nhất nhưng giữ nguyên dự đoán). Frank–Wolfe đảm bảo mặt nạ tìm được có tính thưa kiểm soát được trực tiếp qua số vòng lặp.
- **Đánh đổi giữa Frank–Wolfe và Sinkhorn/PGD:** Hiểu rõ khi nào cần kế hoạch vận chuyển *thưa và không chính quy hóa entropy* (ưu thế của Frank–Wolfe) so với kế hoạch *trơn, dễ song song hóa trên GPU* (ưu thế của thuật toán Sinkhorn).

### Khung giải thích (nên đọc chậm): Tính tay một vòng Block-Coordinate Frank–Wolfe (BCFW) trên tích hai đơn hình

Để hình dung cách BCFW hoạt động trong dự đoán có cấu trúc và OT bán nới lỏng, xét miền khả thi là tích của hai đơn hình xác suất $$C = \Delta_2 \times \Delta_2$$, tức biến $$\alpha = (\alpha^{(1)}, \alpha^{(2)})$$ với $$\alpha^{(i)} \in \Delta_2$$. Giả sử ta tối ưu hàm mục tiêu $$f(\alpha^{(1)}, \alpha^{(2)}) = \frac{1}{2}\|\alpha^{(1)} - (1.2, -0.2)\|_2^2 + \frac{1}{2}\|\alpha^{(2)} - (0.1, 0.9)\|_2^2$$, khởi tạo từ $$\alpha_0^{(1)} = (0.5, 0.5)$$ và $$\alpha_0^{(2)} = (0.5, 0.5)$$.

1. **Bước 1 — Chọn ngẫu nhiên khối 1 (giữ nguyên khối 2):**
   Tính gradient riêng theo khối 1: $$\nabla_1 f = (0.5 - 1.2,\; 0.5 - (-0.2)) = (-0.7,\; 0.7)$$.
   Gọi LMO chỉ trên $$\Delta_2$$ của khối 1: $$\arg\min_{s \in \Delta_2} (-0.7 s_1 + 0.7 s_2) = (1, 0)$$.
   Với bước $$\gamma = 0.5$$, cập nhật khối 1:
   $$\alpha_1^{(1)} = 0.5(0.5, 0.5) + 0.5(1, 0) = (0.75,\; 0.25)$$, trong khi $$\alpha_1^{(2)}$$ giữ nguyên $$(0.5, 0.5)$$.
2. **Bước 2 — Chọn khối 2 (giữ nguyên khối 1):**
   Tính gradient riêng theo khối 2: $$\nabla_2 f = (0.5 - 0.1,\; 0.5 - 0.9) = (0.4,\; -0.4)$$.
   Gọi LMO trên $$\Delta_2$$ của khối 2: $$\arg\min_{s \in \Delta_2} (0.4 s_1 - 0.4 s_2) = (0, 1)$$.
   Với bước $$\gamma = 0.5$$, cập nhật khối 2:
   $$\alpha_2^{(2)} = 0.5(0.5, 0.5) + 0.5(0, 1) = (0.25,\; 0.75)$$.
3. **Ý nghĩa thực chiến:** Thay vì phải gọi LMO cho cả $$n$$ khối (tốn $$n$$ lần chạy thuật toán suy luận chỉ để đi 1 bước), BCFW chỉ cần tính gradient và LMO trên **đúng 1 khối** mỗi lần cập nhật — giảm chi phí mỗi vòng đi $$n$$ lần mà vẫn bảo toàn tính khả thi trên toàn bộ tích đơn hình!

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
