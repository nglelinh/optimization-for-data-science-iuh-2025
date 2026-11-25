---
layout: post
title: 25 Quy Hoạch Số Nguyên Hỗn Hợp (Phần II)
chapter: '25'
order: 1
owner: YoungJae Choung
categories:
- chapter25
lang: vi
---

Nếu Chương 24 trao cho bạn thanh kiếm **Nhánh và Cận (Branch and Bound)** để chia nhỏ bài toán quy hoạch nguyên, thì Chương 25 trao thêm chiếc khiên và mũi khoan sắc bén nhất của vận trù học hiện đại: **Mặt phẳng cắt (Cutting Planes)** cùng sự hợp nhất huyền thoại **Nhánh và Cắt (Branch and Cut)**.

Trong thực tế, Nhánh và Cận thuần túy thường bị "nổ cây" khi cận dưới từ nới lỏng LP quá lỏng lẻo. Thay vì vội vàng phân nhánh ngay, Chương 25 chỉ ra cách *gọt bớt* những phần thừa chứa nghiệm phân số ra khỏi đa diện LP bằng các bất đẳng thức hợp lệ, rồi áp dụng trực tiếp vũ khí MIP này vào hai bài toán thống kê lừng danh vốn từng bị xem là bất khả thi: **chọn tập con tốt nhất (Best Subset Selection)** và **hồi quy bình phương trung vị nhỏ nhất (Least Median of Squares)**.

## Bản đồ kiến thức nền: Bốn trụ cột của Quy hoạch số nguyên hỗn hợp (Phần II)

Chương 25 kết nối hình học đa diện cổ điển với thống kê hiện đại qua bốn trụ cột sau:

- **Lồi hóa và Bao lồi nguyên (Convexification):** Mọi quy hoạch tuyến tính nguyên về nguyên tắc đều tương đương với một quy hoạch tuyến tính trên *bao lồi* của các điểm nguyên khả thi — vấn đề duy nhất là bao lồi này có thể có số mặt lớn theo hàm mũ.
- **Lát cắt Gomory và Bài toán tách (Cutting Planes & Separation):** Thay vì liệt kê hết mọi mặt của bao lồi, ta chỉ sinh ra đúng một siêu phẳng *cắt đứt nghiệm phân số hiện tại* mà không chạm vào bất kỳ điểm nguyên khả thi nào.
- **Nhánh và Cắt (Branch and Cut):** Kết hợp tinh hoa của hai thế giới — dùng mặt phẳng cắt để siết chặt cận dưới ngay tại nút gốc và các nút trung gian, rồi mới phân nhánh khi cần thiết — giúp tốc độ giải tăng hàng triệu lần trong ba thập kỷ qua.
- **MIP cho Thống kê hiện đại (Best Subset & LQS):** Nhờ khởi động nóng bằng thuật toán bậc nhất rời rạc và MIP hiện đại, các bài toán thống kê phi lồi từng bị thay thế bằng xấp xỉ Lasso nay có thể được giải *chính xác* kèm chứng nhận tối ưu ở quy mô hàng trăm đến hàng nghìn biến.

### Khung giải thích (nên đọc chậm): Một lát cắt duy nhất mạnh bằng cả một nhánh cây

Hãy quay lại bài toán cực tiểu hóa $$\min -3x_1 - 2x_2$$ thỏa mãn $$2x_1 + 2x_2 \le 5$$ với $$x_1, x_2 \in \mathbb{Z}_+$$ để thấy phép màu của mặt phẳng cắt.

1. **Trước khi thêm lát cắt:**
   Miền nới lỏng LP là tam giác $$2x_1 + 2x_2 \le 5,\; x_1, x_2 \ge 0$$. Nghiệm LP nằm tại đỉnh phân số $$(2.5,\; 0)$$ với giá trị $$-7.5$$.
2. **Suy ra một lát cắt hợp lệ cực đơn giản:**
   Chia hai vế của $$2x_1 + 2x_2 \le 5$$ cho $$2$$, ta được $$x_1 + x_2 \le 2.5$$.
   Nhưng vì $$x_1, x_2$$ đều là số nguyên, tổng $$x_1 + x_2$$ **bắt buộc phải là số nguyên**, nên nó không thể vượt quá $$\lfloor 2.5 \rfloor = 2$$!
   Vậy bất đẳng thức $$x_1 + x_2 \le 2$$ là một **mặt phẳng cắt hợp lệ**.
3. **Sau khi thêm đúng 1 lát cắt $$x_1 + x_2 \le 2$$:**
   - Kiểm tra nghiệm phân số cũ $$(2.5, 0)$$: $$2.5 + 0 = 2.5 > 2$$ — **bị cắt bỏ ngay lập tức!**
   - Kiểm tra mọi điểm nguyên khả thi cũ $$(0,0), (1,0), (2,0), (0,1), (1,1), (0,2)$$: tất cả đều có $$x_1 + x_2 \le 2$$ — **được bảo toàn 100%!**
   - Giải lại LP mới: nghiệm nhảy thẳng về đỉnh nguyên $$(2, 0)$$ với giá trị $$-6$$. Bài toán được giải xong ngay lập tức mà **không cần rẽ nhánh dù chỉ một lần**!

Chương này trình bày thuật toán mặt phẳng cắt (cutting plane) — một trong những công cụ cốt lõi của quy hoạch nguyên (IP) — cùng thuật toán nhánh và cắt (branch and cut), là sự kết hợp được triển khai phổ biến nhất trong các bộ giải thực tế.

Tiếp theo, chương minh họa hai ví dụ mở rộng của quy hoạch nguyên hỗn hợp trong thống kê: chọn tập con tốt nhất (best subset selection) và hồi quy bình phương trung vị nhỏ nhất / hồi quy phân vị nhỏ nhất (least median of squares / least quantile regression).

## Tài liệu tham khảo

* Belotti, Kirches, Leyffer, Linderoth, Luedke, and Mahajan (2012), "Mixed-integer nonlinear optimization"
* Bertsimas and Mazumder (2016), "Best subset selection via a modern optimization lens"
* Bertsimas, King, and Mazumder (2014), "Least quantile regression via modern optimization"
* Conforti, Cornuejols, and Zambelli (2014), "Integer programming"
* Wolsey (1998), "Integer programming"

## Ứng dụng giai đoạn 2022–2026 (tùy chọn)

Bài toán chọn tập con tốt nhất bằng MIP vẫn là ví dụ tiêu biểu trong thống kê; cùng kỹ thuật mã hóa big-$$M$$ cho hàm kích hoạt ReLU hiện còn được dùng để chọn đặc trưng cho mạng nơ-ron đã huấn luyện, *chứng nhận* độ bền vững đối kháng và xây dựng cây phân loại tối ưu. Bên cạnh đó, các nghiên cứu năm 2024 về học quy tắc chọn mặt phẳng cắt kiểu Gomory biến chính quy trình ở mục 25-01 thành bài toán học máy. Đọc thêm tại bài tùy chọn: [25-03 Ứng dụng hiện đại của MIP trong khoa học dữ liệu]({% multilang_post_url contents/chapter25/2026-09-16-25_03_modern_applications %}).
