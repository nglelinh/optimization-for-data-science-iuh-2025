---
layout: post
title: 04 Cơ bản về tối ưu hóa lồi
chapter: '04'
order: 1
owner: YoungJae Choung
categories:
- chapter04
lang: vi
---

Một kỹ sư lưới điện cần điều phối hàng trăm nhà máy phát điện mỗi 15 phút để vừa đủ công suất tiêu thụ, vừa tối thiểu hóa chi phí nhiên liệu mà không làm quá tải đường dây. Một nhà khoa học dữ liệu khác cần huấn luyện mô hình dự báo rủi ro tín dụng trên hàng triệu hồ sơ mà không bị mắc kẹt ở nghiệm xấu. Điểm chung của hai bài toán tưởng chừng cách xa nhau ấy là gì? Cả hai đều có thể được viết lại dưới **khuôn mẫu bài toán tối ưu hóa lồi** — vùng đất hiếm hoi trong toán học ứng dụng nơi mọi điểm cực tiểu địa phương đều là cực tiểu toàn cục.

Chương 04 đóng vai trò bản lề của toàn khóa học: ta chuyển từ ngôn ngữ hình học của *tập lồi* (Chương 02) và *hàm lồi* (Chương 03) sang ngôn ngữ hành động của **bài toán tối ưu hóa lồi**. Không chỉ dừng ở việc đặt tên cho các thành phần, chương này còn dạy bạn nghệ thuật "nhìn xuyên qua lớp vỏ phi lồi" bằng các phép biến đổi tương đương như đổi biến, loại bỏ ràng buộc đẳng thức, thêm biến phụ hay nới lỏng.

## Bản đồ kiến thức nền: Kiến trúc của một bài toán tối ưu hóa lồi

Để làm chủ Chương 04 mà không bị choáng ngợp bởi hàng loạt định lý và kỹ thuật biến đổi, hãy hình dung chương này đứng trên bốn trụ cột liên kết chặt chẽ:

- **Hình học tập khả thi (Feasible Set Geometry):** Mỗi ràng buộc bất đẳng thức lồi $$g_i(x) \le 0$$ cắt ra một tập mức dưới lồi, còn mỗi ràng buộc đẳng thức affine $$h_j(x) = 0$$ cắt ra một siêu phẳng. Giao của chúng tạo thành tập khả thi lồi — nền sân phẳng không có "hốc lõm" bẫy thuật toán.
- **Giải tích biến phân & Điều kiện tối ưu (Optimality Conditions):** Thay vì chỉ giải $$\nabla f(x) = 0$$ như giải tích cổ điển (vốn chỉ đúng khi không có ràng buộc), tối ưu hóa lồi tổng quát hóa thành bất đẳng thức biến phân $$\nabla f(x^\star)^T (y - x^\star) \ge 0$$ trên tập khả thi, và mở rộng lên bậc hai với ma trận Hessian.
- **Đại số các phép biến đổi tương đương (Equivalent Reformulations):** Một bài toán thực tế hiếm khi xuất hiện sẵn dưới dạng chuẩn. Các phép tối ưu hóa từng phần, đổi biến khả nghịch, loại bỏ ràng buộc đẳng thức tuyến tính và thêm biến phụ giúp ta biến đổi bài toán mà không làm mất nghiệm tối ưu.
- **Nghệ thuật Nới lỏng (Convex Relaxation):** Khi bài toán gốc thực sự phi lồi (ví dụ biến nhị phân $$x_i \in \{0,1\}$$), ta thay tập khả thi bằng bao lồi lớn hơn để thu được cận dưới đáng tin cậy và điểm xuất phát tốt cho nghiệm xấp xỉ.

### Khung giải thích (nên đọc chậm): Nhận diện và giải nhanh một bài toán tối ưu lồi 2 biến

Xét bài toán: tìm $$x = (x_1, x_2) \in \mathbb{R}^2$$ sao cho
$$\min \; f(x_1, x_2) = (x_1 - 3)^2 + (x_2 - 2)^2 \quad \text{thỏa mãn} \quad x_1 + x_2 \le 3,\; x_1 \ge 0,\; x_2 \ge 0.$$

1. **Kiểm tra tính lồi:** Hàm mục tiêu $$f$$ có Hessian $$\nabla^2 f = 2I \succ 0$$ nên lồi chặt. Các ràng buộc $$x_1 + x_2 - 3 \le 0$$, $$-x_1 \le 0$$, $$-x_2 \le 0$$ đều là hàm affine (nên lồi). Vậy đây là bài toán tối ưu hóa lồi.
2. **Thử nghiệm tự do (bỏ ràng buộc):** Giải $$\nabla f(x) = 0$$ cho $$x_{\text{free}} = (3, 2)$$. Thay vào ràng buộc: $$x_1 + x_2 = 5 > 3$$, nên điểm tự do **không khả thi**.
3. **Chiếu hình học lên biên tích cực:** Vì $$(3,2)$$ nằm ngoài tam giác khả thi, nghiệm tối ưu $$x^\star$$ buộc phải nằm trên cạnh $$x_1 + x_2 = 3$$. Thay $$x_2 = 3 - x_1$$ vào $$f$$:
   $$\phi(x_1) = (x_1 - 3)^2 + (1 - x_1)^2 = 2x_1^2 - 8x_1 + 10.$$
4. **Cực tiểu hóa hàm 1 biến:** $$\phi'(x_1) = 4x_1 - 8 = 0 \implies x_1^\star = 2$$, suy ra $$x_2^\star = 1$$. Kiểm tra: $$x_1^\star = 2 \ge 0$$, $$x_2^\star = 1 \ge 0$$, $$x_1^\star + x_2^\star = 3$$. Giá trị tối ưu là $$f^\star = (2-3)^2 + (1-2)^2 = 2$$.
5. **Kiểm tra điều kiện tối ưu bậc nhất:** $$\nabla f(2,1) = (-2, -2)$$. Với mọi điểm khả thi $$y = (y_1, y_2)$$ thỏa $$y_1 + y_2 \le 3$$, ta có
   $$\nabla f(x^\star)^T (y - x^\star) = -2(y_1 - 2) - 2(y_2 - 1) = -2(y_1 + y_2 - 3) \ge 0.$$
   Điều kiện đủ được thỏa mãn tuyệt đối: $$(2,1)$$ là nghiệm tối ưu toàn cục duy nhất!

---

## Cơ bản về Tối ưu hóa Lồi

Chương này giới thiệu các tính chất cơ bản của bài toán tối ưu hóa lồi cùng một số kỹ thuật biến đổi thường dùng để đưa bài toán về dạng thuận lợi hơn cho việc phân tích và giải quyết.

Bài tùy chọn [04-09 Ứng dụng và phát triển gần đây]({% multilang_post_url contents/chapter04/2026-09-16-04_09_Applications_Recent %}) trình bày cách các điều kiện tối ưu trong chương này được ứng dụng để xây dựng lớp tối ưu hóa khả vi trong mạng nơ-ron (cvxpylayers, Theseus) và các hàm mất mát thay thế lồi cho bài toán ra quyết định.
