---
layout: post
title: 12 Điều Kiện KKT
chapter: '12'
order: 1
owner: Wontak Ryu
categories:
- chapter12
lang: vi
---

Năm 1939, chàng sinh viên cao học 22 tuổi William Karush tại Đại học Chicago viết một luận văn thạc sĩ giải quyết trọn vẹn bài toán tìm điều kiện cực trị cho tối ưu có ràng buộc bất đẳng thức — rồi luận văn ấy nằm yên lặng trên kệ thư viện suốt hơn một thập kỷ. Mãi đến năm 1951, Harold Kuhn và Albert Tucker độc lập tái khám phá và công bố rộng rãi hệ điều kiện này, mở ra kỷ nguyên mới cho toàn bộ ngành tối ưu phi tuyến hiện đại. Ngày nay, thế giới gọi chúng bằng tên chung đầy trân trọng: **Điều kiện Karush–Kuhn–Tucker (KKT)**.

Nếu quy tắc $$\nabla f(x^*) = 0$$ là chiếc la bàn vàng của giải tích không ràng buộc, thì hệ 4 điều kiện KKT chính là **luật cơ bản của giải tích có ràng buộc**. Chương 12 sẽ biến công cụ lý thuyết này thành vũ khí giải toán thực chiến: từ hệ phương trình khối cho quy hoạch bậc hai, thuật toán "đổ nước" (water-filling) trong lý thuyết thông tin Shannon, phân tích vector hỗ trợ của SVM, cho đến tính duy nhất của nghiệm Lasso!

## Bản đồ kiến thức nền: Bốn trụ cột tạo nên hệ điều kiện KKT

- **Điều kiện dừng (Stationarity):** $$0 \in \partial f(x^*) + \sum u_i^* \partial h_i(x^*) + \sum v_j^* \partial l_j(x^*)$$ (hoặc $$\nabla f + \sum u_i^* \nabla h_i + \sum v_j^* \nabla l_j = 0$$ khi khả vi). Trực giác hình học: lực kéo hướng giảm $$-\nabla f(x^*)$$ phải bị cân bằng hoàn toàn bởi tổ hợp các pháp tuyến hướng ra ngoài của các bức tường ràng buộc đang chạm!
- **Điều kiện bù (Complementary Slackness):** $$u_i^* h_i(x^*) = 0$$ với mọi $$i = 1, \dots, m$$. Ràng buộc nào chưa chạm tường ($$h_i(x^*) < 0$$) thì không hề tạo lực đẩy ($$u_i^* = 0$$); chỉ ràng buộc đang chạm chặt ($$h_i(x^*) = 0$$) mới được phép có lực phản hồi $$u_i^* > 0$$.
- **Tính khả thi nguyên thủy & đối ngẫu (Primal & Dual Feasibility):** $$h_i(x^*) \le 0, \; l_j(x^*) = 0$$ và $$u_i^* \ge 0$$. Dấu $$u_i^* \ge 0$$ đảm bảo bức tường ràng buộc chỉ "đẩy ngược vào trong miền hợp lệ" chứ không bao giờ hút điểm lặp ra ngoài.
- **Cầu nối hai chiều với đối ngẫu mạnh (Chương 11):** KKT tương đương chính xác với việc khoảng cách đối ngẫu bằng $$0$$ ($$f(x^*) = g(u^*, v^*)$$) khi bài toán lồi — là điều kiện **đủ** cho mọi bài toán lồi, và là điều kiện **cần** khi có đối ngẫu mạnh (ví dụ thỏa điều kiện Slater).

### Khung giải thích (nên đọc chậm): Kiểm chứng cả 4 điều kiện KKT bằng tay trên bài toán 1 biến

Xét bài toán lồi cực giản dị:
$$\min_{x \in \mathbb{R}} \; f(x) = (x - 3)^2 \quad \text{s.t.} \quad h(x) = x - 2 \le 0 \; (\text{tức } x \le 2).$$
Đáy tự do nằm tại $$x = 3$$ (ngoài bức tường $$x \le 2$$), nên trực giác bảo ngay nghiệm tối ưu phải tựa sát bức tường tại $$x^* = 2$$. Hãy kiểm chứng hệ KKT:

1. **Tính khả thi nguyên thủy:** $$h(x^*) = 2 - 2 = 0 \le 0$$ (thỏa!).
2. **Điều kiện dừng ($$f'(x) + u h'(x) = 0$$):**
   $$2(x - 3) + u(1) = 0 \implies \text{tại } x^* = 2:\; 2(2 - 3) + u^* = 0 \implies u^* = 2.$$
3. **Tính khả thi đối ngẫu:** $$u^* = 2 \ge 0$$ (thỏa!).
4. **Điều kiện bù:** $$u^* h(x^*) = 2 \times (2 - 2) = 0$$ (thỏa!).
*Thử phản chứng:* nếu ta đặt ràng buộc ngược lại là $$x \le 5$$ (tường ở xa đáy $$x = 3$$), thì tại $$x^* = 3$$ ta có $$h(3) = -2 < 0$$ (lỏng), điều kiện bù ép $$u^* = 0$$, và điều kiện dừng $$2(3 - 3) + 0 = 0$$ thỏa mãn hoàn hảo!

Khi bài toán nguyên thủy là bài toán lồi, các điều kiện Karush–Kuhn–Tucker (KKT) là **điều kiện đủ** để các điểm nguyên thủy và đối ngẫu đạt tối ưu với khoảng cách đối ngẫu bằng không. Bên cạnh đó, nếu hàm mục tiêu và các hàm ràng buộc của bài toán nguyên thủy khả vi và bài toán thỏa mãn tính đối ngẫu mạnh, thì mọi cặp nghiệm tối ưu nguyên thủy và đối ngẫu đều phải thỏa mãn các điều kiện KKT.

Các điều kiện KKT giữ vai trò quan trọng trong tối ưu hóa. Nhờ chúng, nhiều bài toán có cấu trúc đặc biệt có thể được giải bằng phương pháp giải tích, đồng thời nhiều thuật toán tối ưu hóa lồi cũng có thể được xem là các phương pháp đi tìm nghiệm của hệ điều kiện KKT [1]. Trong chương này, chúng ta sẽ tìm hiểu định nghĩa, tính chất của các điều kiện KKT và phân tích một số ví dụ minh họa.

*Ghi chú lịch sử:* Các điều kiện KKT ban đầu được Harold W. Kuhn và Albert W. Tucker công bố vào năm 1951 và khi đó được gọi là điều kiện KT (Kuhn–Tucker). Về sau, giới nghiên cứu phát hiện ra rằng các điều kiện cần tương tự đã được William Karush trình bày trong luận văn thạc sĩ năm 1939; từ đó tên của Karush được bổ sung và hệ điều kiện này mang tên KKT (Karush–Kuhn–Tucker) [3].

## Ứng dụng hiện đại (2022–2026)

Bài đọc tùy chọn đi kèm trình bày cách hệ KKT xuất hiện trong cvxpylayers và Theseus, các vector hỗ trợ của SVM, giá biên theo vị trí (LMP) trong thị trường điện và các ràng buộc công bằng đang chặt. Xem [12-07 Ứng dụng hiện đại của điều kiện KKT]({% multilang_post_url contents/chapter12/2026-09-16-12_07_modern_applications %}).
