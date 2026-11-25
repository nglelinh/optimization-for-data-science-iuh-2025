---
layout: post
title: '17 Phương pháp điểm trong gốc-đối ngẫu'
chapter: '17'
order: 1
owner: Minjoo Lee
categories:
- chapter17
lang: vi
---

Nếu bạn từng chạy phương pháp chắn (barrier method) trên một bài toán quy hoạch lớn, có lẽ bạn sẽ thấy một nghịch lý khá khó chịu: để giảm tham số $$1/t$$ thêm một nấc nhỏ, ta phải chạy cả một vòng lặp Newton bên trong chỉ để định tâm thật chính xác vào một điểm tạm thời $$x^\star(t)$$ — một điểm mà ngay bước sau ta lại bỏ đi để chuyển sang giá trị $$t$$ lớn hơn! Phương pháp điểm trong gốc–đối ngẫu (Primal-Dual Interior-Point Method, PD-IPM) ra đời để phá bỏ sự lãng phí đó: thay vì giải trọn vẹn bài toán định tâm ở mỗi $$t$$, nó chỉ đi **đúng một bước Newton** đồng thời trên cả biến gốc và biến đối ngẫu, rồi lập tức hạ tham số nhiễu $$\tau$$ và tiến thẳng về nghiệm tối ưu.

## Bản đồ kiến thức nền: Những trụ cột tạo nên phương pháp điểm trong gốc–đối ngẫu

Để nhìn rõ vì sao một thay đổi tưởng chừng đơn giản ("một bước Newton mỗi vòng lặp") lại biến PD-IPM thành động cơ chủ lực của các bộ giải tối ưu hiện đại, hãy đặt bốn nhánh kiến thức nền cạnh nhau:

- **Lý thuyết đối ngẫu và điều kiện KKT (Duality & KKT Theory):** Điều kiện KKT mô tả nghiệm tối ưu bằng hệ phương trình tính dừng, khả thi gốc–đối ngẫu và bù chặt $$u_i h_i(x) = 0$$. Mọi thuật toán gốc–đối ngẫu đều tìm cách đưa hệ phương trình này về không đồng thời trên cả không gian gốc và đối ngẫu.
- **Đường trung tâm và phép làm trơn đồng luân (Central Path & Homotopy):** Điều kiện bù chặt $$u_i h_i(x) = 0$$ tạo ra các góc gãy khiến phương pháp Newton trực tiếp bị kẹt ở biên. Thay nó bằng $$u_i h_i(x) = -\tau$$ với $$\tau > 0$$ sẽ tạo ra một đường cong trơn đi xuyên qua phần trong miền khả thi dẫn thẳng tới nghiệm tối ưu khi $$\tau \to 0$$.
- **Phương pháp Newton tìm nghiệm hệ phi tuyến (Root-Finding Newton):** Khác với Newton tối ưu hóa không ràng buộc, PD-IPM dùng Newton để giải hệ phi tuyến $$r_\tau(x,u,v) = 0$$. Nhờ vậy, thuật toán không còn đòi hỏi các điểm lặp trung gian phải thỏa mãn chính xác ràng buộc đẳng thức $$Ax = b$$.
- **Đại số tuyến tính số cho hệ KKT (Numerical Linear Algebra):** Ở mỗi vòng lặp, phần tốn kém nhất là giải một hệ tuyến tính có cấu trúc khối (hoặc hệ phương trình chuẩn $$AD^2A^T \Delta v = r$$). Khai thác độ thưa và tính đối xứng giúp giải hàng triệu biến chỉ trong vài chục vòng lặp.

### Khung giải thích (nên đọc chậm): Một bước gốc–đối ngẫu rút ngắn khoảng cách tối ưu nhanh cỡ nào?

Xét bài toán 1 chiều đơn giản $$\min_{x} x$$ với điều kiện $$-x \le 0$$ (tức $$h(x) = -x \le 0$$, nghiệm tối ưu $$x^\star = 0, u^\star = 1$$). Hệ điều kiện KKT bị nhiễu với tham số $$\tau > 0$$ là:

$$r_{\text{dual}} = 1 - u = 0, \qquad r_{\text{cent}} = -ux + \tau = 0.$$

Giả sử ta đang đứng tại điểm trong $$(x^{(0)}, u^{(0)}) = (2, 1)$$ (khoảng cách đối ngẫu hiện tại là $$-h(x^{(0)})u^{(0)} = 2$$) và chọn mục tiêu $$\tau = 0.2$$ (giảm 10 lần):

1. **Tính vector phần dư hiện tại:** $$r_{\text{dual}} = 1 - 1 = 0$$ và $$r_{\text{cent}} = -(1)(2) + 0.2 = -1.8$$.
2. **Tuyến tính hóa hệ quanh $$(2, 1)$$:** Đạo hàm theo $$(\Delta x, \Delta u)$$ cho hệ $$-\Delta u = 0$$ và $$-u\Delta x - x\Delta u = -r_{\text{cent}} = 1.8$$.
3. **Giải bước Newton:** Từ phương trình đầu ta có $$\Delta u = 0$$; thay vào phương trình hai được $$-1 \cdot \Delta x = 1.8 \implies \Delta x = -1.8$$.
4. **Cập nhật kèm hệ số an toàn giữ điểm trong:** Nếu lấy bước đầy đủ $$\theta = 1$$ thì $$x^{(1)} = 0.2 > 0, u^{(1)} = 1 > 0$$ — rơi trúng chính xác điểm đường trung tâm ứng với $$\tau = 0.2$$ chỉ sau **đúng 1 bước**, giảm khoảng cách đối ngẫu từ $$2$$ xuống $$0.2$$! Với bài toán tổng quát có độ cong phi tuyến, ta dùng hệ số an toàn (như $$\theta = 0.9$$ cho $$x^{(1)} = 0.38$$) để vừa tránh chạm biên vừa rút gọn nhanh khoảng cách đối ngẫu.

---

Trong chương này, chúng ta tìm hiểu **phương pháp điểm trong gốc-đối ngẫu (Primal-Dual Interior-Point Method)** — phương pháp cải thiện hiệu năng bằng cách rút gọn bước định tâm (centering) của phương pháp chắn xuống chỉ còn một bước Newton ở mỗi vòng lặp.

**Phương pháp điểm trong gốc-đối ngẫu** nới lỏng yêu cầu phải giữ nghiệm luôn khả thi trong bước định tâm, đồng thời áp dụng phiên bản tìm nghiệm (root-finding) của phương pháp Newton để tuyến tính hóa hệ phương trình phi tuyến. Nhờ đó, thuật toán thường hội tụ nhanh hơn và đạt độ chính xác cao hơn so với phương pháp chắn.

## Tài liệu tham khảo và đọc thêm
* S. Boyd and L. Vandenberghe (2004), “Convex optimization,” Chapter 11
* S. Wright (1997), “Primal-dual interior-point methods,” Chapters 5 and 6
* J. Renegar (2001), “A mathematical view of interior-point methods”
* Y. Nesterov and M. Todd (1998), “Primal-dual interior-point methods for self-scaled cones.” SIAM J. Optim.
