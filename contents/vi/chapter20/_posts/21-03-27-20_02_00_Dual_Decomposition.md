---
layout: post
title: '20-02 Phân rã đối ngẫu (Dual Decomposition)'
chapter: '20'
order: 4
owner: Hooncheol Shin
categories:
- chapter20
lang: vi
---

Hãy tưởng tượng một tập đoàn quản lý 100 nhà máy khác nhau, mỗi nhà máy có hàm chi phí sản xuất riêng $$f_i(x_i)$$, nhưng cả 100 nhà máy lại dùng chung một nguồn điện hoặc một hạn mức phát thải chung $$\sum_{i=1}^{100} A_i x_i = b$$. Nếu gom toàn bộ biến của 100 nhà máy vào một máy tính duy nhất thì bài toán quá khổng lồ, còn nếu để từng nhà máy tự tối ưu riêng thì lại vi phạm nguồn lực chung. **Phân rã đối ngẫu (Dual Decomposition)** mang đến một lời giải vừa toán học vừa đậm chất kinh tế học: đặt một "người điều phối" chỉ phát đi duy nhất một **bảng giá** (biến đối ngẫu $$u$$), để 100 nhà máy tự tính toán hoàn toàn song song!

## Kiến thức cần nhớ: Ba trụ cột của tư duy phân rã đối ngẫu

Phần 20-02 mở rộng phương pháp tăng đối ngẫu thành một kiến trúc tối ưu hóa phân tán hoàn chỉnh dựa trên ba nguyên lý:

- **Tính tách được của hàm Lagrange (Lagrangian Separability):** Khi hàm mục tiêu có dạng tổng $$\sum_{i=1}^B f_i(x_i)$$ và ràng buộc tuyến tính tách theo khối $$\sum_{i=1}^B A_i x_i = b$$ (hoặc $$\le b$$), hàm Lagrange tách thành tổng $$B$$ hàm độc lập $$\sum_{i=1}^B (f_i(x_i) + u^T A_i x_i) - u^T b$$.
- **Chu trình Broadcast – Solve – Gather:** Ở mỗi vòng lặp, máy chủ trung tâm phát giá $$u^{(k-1)}$$ tới các nút (broadcast); mỗi nút tự giải bài toán con $$x_i^{(k)}$$ độc lập song song (solve); máy chủ thu gom phần dư tổng $$\sum_i A_i x_i^{(k)} - b$$ để điều chỉnh giá $$u^{(k)}$$ (gather).
- **Quy luật cung–cầu tự nhiên:** Với ràng buộc bất đẳng thức (hạn mức tài nguyên $$\le b$$), nếu tổng mức dùng vượt hạn mức thì giá $$u$$ tăng lên để kìm hãm tiêu thụ; nếu dư thừa tài nguyên thì giá giảm xuống (nhưng không âm nhờ phép chiếu $$(\cdot)_+$$).

### Giải thích: Cơ chế "bảng giá điện" điều phối 2 nhà máy độc lập

Giả sử 2 nhà máy cần cùng nhau sản xuất tổng cộng $$10$$ đơn vị sản phẩm ($$x_1 + x_2 = 10$$) với chi phí riêng $$f_1(x_1) = x_1^2$$ và $$f_2(x_2) = 4x_2^2$$:

1. **Khi chưa có giá điều phối ($$u = 0$$):** Cả hai nhà máy đều chọn $$x_1 = 0, x_2 = 0$$ để chi phí bằng $$0$$ — tổng sản lượng là $$0 < 10$$ (thiếu $$10$$ đơn vị!).
2. **Người điều phối phát giá thưởng $$p = -u = 8$$ (tức $$u = -8$$) cho mỗi đơn vị sản xuất:**
   - Nhà máy 1 tự tối ưu $$\min_{x_1} (x_1^2 - 8x_1) \implies x_1 = 4$$.
   - Nhà máy 2 tự tối ưu $$\min_{x_2} (4x_2^2 - 8x_2) \implies x_2 = 1$$.
   - Tổng sản lượng $$4 + 1 = 5 < 10$$ (vẫn thiếu $$5$$ đơn vị, nên người điều phối phải nâng giá thưởng lên gấp đôi!).
3. **Người điều phối nâng giá thưởng lên $$p = -u = 16$$ (tức $$u = -16$$):**
   - Nhà máy 1 chọn $$x_1 = 8$$; Nhà máy 2 chọn $$x_2 = 2$$.
   - Tổng sản lượng $$8 + 2 = 10$$ — **khớp chính xác chỉ tiêu chung** mà hai nhà máy chưa từng phải tiết lộ hàm chi phí riêng của mình cho nhau!

---

Trong phần này, chúng ta tìm hiểu các kỹ thuật phân rã bài toán tối ưu thành nhiều bài toán con độc lập thông qua hàm đối ngẫu.
