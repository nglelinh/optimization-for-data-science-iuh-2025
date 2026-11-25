---
layout: post
title: 24 Quy Hoạch Số Nguyên Hỗn Hợp (Phần I)
chapter: '24'
order: 1
owner: YoungJae Choung
categories:
- chapter24
lang: vi
---

Suốt 23 chương trước, ta sống trong thế giới êm đềm của tối ưu lồi liên tục — nơi mọi biến đều có thể nhận giá trị $$0.37$$ hay $$2.418$$, và một bước đạo hàm dẫn thẳng tới cực tiểu toàn cục. Nhưng thế giới thực hiếm khi liên tục như vậy: bạn không thể điều $$0.4$$ chiếc máy bay cất cánh, không thể xây $$0.7$$ cái nhà kho, và cũng không thể chọn $$0.6$$ một đặc trưng trong mô hình thống kê.

Ngay khoảnh khắc ta thêm ràng buộc tưởng chừng bé nhỏ $$x_j \in \mathbb{Z}$$ (hoặc $$x_j \in \{0, 1\}$$), toàn bộ địa hình tối ưu vỡ vụn thành các điểm rời rạc, biến bài toán thành **quy hoạch số nguyên hỗn hợp (Mixed Integer Programming — MIP)** — một trong những công cụ mô hình hóa mạnh mẽ nhất nhưng cũng thách thức nhất của vận trù học và khoa học dữ liệu.

## Bản đồ kiến thức nền: Bốn trụ cột của Quy hoạch số nguyên hỗn hợp (Phần I)

Chương 24 mở cánh cửa bước vào thế giới tối ưu rời rạc thông qua bốn trụ cột liên hoàn:

- **Ngôn ngữ mô hình hóa bằng biến nhị phân (Binary Modeling):** Biến $$x_j \in \{0, 1\}$$ đóng vai trò như công tắc logic "có/không", cho phép mã hóa quyết định đầu tư, ràng buộc chọn tối đa $$k$$ phần tử, định tuyến, và các điều kiện logic "nếu–thì" thành hệ bất đẳng thức tuyến tính.
- **Độ khó NP-khó và Nghịch lý làm tròn (Why Rounding Fails):** Việc giải bài toán nới lỏng liên tục (bỏ ràng buộc nguyên) rồi làm tròn nghiệm có thể cho ra điểm *không khả thi* hoặc *kém tối ưu rất xa* — đó là lý do ta cần các thuật toán tìm kiếm có chứng nhận.
- **Phép nới lỏng và Cận đối ngẫu (Relaxations & Dual Bounds):** Mở rộng miền khả thi về một tập lồi (nới lỏng LP/lồi hoặc nới lỏng Lagrange) cung cấp cận dưới chặt, đóng vai trò chiếc la bàn đo khoảng cách tới nghiệm nguyên tối ưu.
- **Chia để trị bằng Nhánh và Cận (Branch and Bound):** Phân hoạch bài toán gốc thành cây các bài toán con nhỏ hơn và mạnh tay *cắt tỉa* (prune) những nhánh có cận dưới tệ hơn nghiệm nguyên tốt nhất đã biết — nền tảng của mọi bộ giải MIP chính xác.

### Khung giải thích (nên đọc chậm): Vì sao không thể "giải LP rồi làm tròn"?

Xét bài toán quy hoạch nguyên 2 biến cực kỳ đơn giản:

$$
\max_{x_1, x_2}\ 3x_1 + 2x_2 \qquad \text{thỏa mãn } x_1 + x_2 \le 2.5,\quad 2x_1 + x_2 \le 4,\quad x_1, x_2 \in \mathbb{Z}_+.
$$

1. **Giải bài toán nới lỏng tuyến tính (LP relaxation, bỏ yêu cầu nguyên):**
   Giao điểm của hai đường thẳng biên $$x_1 + x_2 = 2.5$$ và $$2x_1 + x_2 = 4$$ là $$(x_1, x_2) = (1.5,\; 1)$$.
   Kiểm tra các đỉnh của miền LP: tại $$(0, 2.5)$$ giá trị bằng $$5$$; tại $$(2, 0)$$ giá trị bằng $$6$$; tại $$(1.5, 1)$$ giá trị bằng $$3(1.5) + 2(1) = 6.5$$ (cực đại LP!).
2. **Thử làm tròn nghiệm LP $$(1.5,\; 1)$$ sang số nguyên gần nhất:**
   - *Làm tròn lên* thành $$(2, 1)$$: kiểm tra ràng buộc $$2(2) + 1 = 5 > 4$$ — **vi phạm ràng buộc, không khả thi!**
   - *Làm tròn xuống* thành $$(1, 1)$$: khả thi ($$1+1=2 \le 2.5$$ và $$2+1=3 \le 4$$), cho giá trị $$3(1) + 2(1) = 5$$.
3. **So với nghiệm nguyên tối ưu thực sự:**
   Điểm nguyên $$(2, 0)$$ thỏa mãn cả hai ràng buộc ($$2 + 0 = 2 \le 2.5$$ và $$4 + 0 = 4 \le 4$$) và đạt giá trị $$3(2) + 2(0) = 6 > 5$$!
4. **Bài học rút ra:** Làm tròn lên thì mất tính khả thi, làm tròn xuống thì bỏ lỡ nghiệm tối ưu $$(2, 0)$$ nằm ở hướng hoàn toàn khác. Chính khoảng trống này giải thích vì sao ta cần cả Chương 24 (Nhánh và cận) lẫn Chương 25 (Mặt phẳng cắt).

Chương này giới thiệu định nghĩa, tính chất và các ví dụ kinh điển của quy hoạch số nguyên hỗn hợp (Mixed Integer Programming — MIP), đồng thời trình bày cách tiếp cận tìm nghiệm tối ưu gián tiếp thông qua các bài toán nới lỏng (relaxation) và thuật toán nhánh và cận.

## Ứng dụng giai đoạn 2022–2026 (tùy chọn)

Các mô hình phân công, bài toán cái túi (knapsack) và đặt cơ sở không chỉ là ví dụ kinh điển trong giáo trình: xếp lịch phi hành đoàn (bộ chuẩn MIPLIB `air05`), định tuyến giao hàng chặng cuối (last-mile) kết hợp dự báo nhu cầu, và lựa chọn vị trí kho hàng hay cụm GPU biên đều trực tiếp kế thừa khung mô hình ở mục 24-02. Bên cạnh đó, từ sau NeurIPS 2019, một hướng nghiên cứu mới — học quy tắc rẽ nhánh ngay bên trong thuật toán nhánh và cận — đã phát triển mạnh quanh các mô hình này. Bạn có thể đọc tiếp tại [24-06 Ứng dụng hiện đại của mô hình nguyên hỗn hợp]({% multilang_post_url contents/chapter24/2026-09-16-24_06_modern_applications %}); các chủ đề chọn đặc trưng, kiểm chứng mạng nơ-ron và cây quyết định tối ưu sẽ được trình bày ở Chương 25.
