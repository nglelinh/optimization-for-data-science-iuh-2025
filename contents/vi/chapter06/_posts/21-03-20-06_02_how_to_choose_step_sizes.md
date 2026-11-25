---
layout: post
title: 06-02 Cách chọn kích thước bước
chapter: '06'
order: 5
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
lesson_type: required
---

Biết hướng đi $$-\nabla f(x)$$ mới chỉ là một nửa câu chuyện của Gradient Descent; nửa quyết định thành bại còn lại là câu hỏi: **đi theo hướng đó bao xa?** Một tay đua công thức 1 không thể giữ cùng một tốc độ trên đường thẳng và khúc cua gắt; tương tự, một thuật toán tối ưu giỏi phải biết lúc nào nên sải bước dài và lúc nào phải hãm phanh lại.

Mục 06-02 đặt ba chiến lược chọn kích thước bước lên cùng một bàn cân so sánh: **bước cố định (Fixed Step Size)** đơn giản nhưng mạo hiểm nếu không biết $$L$$, **Tìm kiếm đường lùi (Backtracking Line Search)** linh hoạt và cực kỳ phổ biến trong thực chiến, và **Tìm kiếm đường chính xác (Exact Line Search)** lý tưởng về mặt lý thuyết nhưng đắt đỏ ở bài toán tổng quát.

## Bản đồ kiến thức nền: Ba triết lý chọn kích thước bước trong Gradient Descent

Để chọn đúng chiến lược cho từng bài toán thực tế, hãy nhìn rõ sự đánh đổi giữa ba phương pháp:

- **Bước cố định (Fixed Step Size):** Đặt $$t_k = t$$ cho mọi bước. Chi phí chọn bước bằng $$0$$, nhưng đòi hỏi biết trước hằng số trơn $$L$$ (để chọn $$t \le 1/L$$). Nếu đoán sai $$t > 2/L$$, thuật toán phân kỳ ngay lập tức.
- **Tìm kiếm đường lùi (Backtracking / Armijo Line Search):** Bắt đầu thử bước lớn $$t = 1$$ (hoặc $$t_0$$), rồi nhân thu nhỏ dần $$t \leftarrow \beta t$$ cho đến khi thỏa điều kiện giảm đủ $$f(x - t\nabla f(x)) \le f(x) - \alpha t \|\nabla f(x)\|_2^2$$. Không cần biết $$L$$ trước, tự động thích ứng với độ cong địa phương!
- **Tìm kiếm đường chính xác (Exact Line Search):** Giải bài toán tối ưu 1 chiều $$t_k = \arg\min_{s > 0} f(x_k - s\nabla f(x_k))$$ tại mỗi bước. Chỉ dùng hiệu quả khi có công thức đóng (như hàm bậc hai $$f(x) = \frac{1}{2}x^T Q x + b^T x$$); trên hàm phi tuyến tổng quát, chi phí giải bài toán 1D thường tốn kém hơn lợi ích mang lại.

### Khung giải thích (nên đọc chậm): So sánh 3 chiến lược bước trên cùng một điểm xuất phát

Xét hàm $$f(x) = \frac{1}{2} x^2$$ tại $$x_0 = 4$$, nơi $$f(4) = 8$$ và $$f'(4) = 4$$ (nghiệm đúng là $$x^\star = 0$$):

1. **Bước cố định $$t = 0.25$$:**
   $$x_1 = 4 - 0.25(4) = 3, \qquad f(x_1) = 4.5$$ (giảm $$3.5$$ đơn vị).
2. **Tìm kiếm đường lùi với $$t_0 = 2,\; \alpha = 0.5,\; \beta = 0.5$$:**
   - Thử $$t = 2$$: $$x_{\text{try}} = 4 - 8 = -4$$, $$f(-4) = 8$$. Kiểm tra Armijo: $$8 \le 8 - 0.5(2)(16) = -8$$? **Sai!** Thu nhỏ $$t \leftarrow 1$$.
   - Thử $$t = 1$$: $$x_{\text{try}} = 4 - 4 = 0$$, $$f(0) = 0$$. Kiểm tra Armijo: $$0 \le 8 - 0.5(1)(16) = 0$$? **Đúng!** Chấp nhận $$t_0 = 1 \implies x_1 = 0$$ (đạt đích ngay!).
3. **Tìm kiếm đường chính xác:**
   Giải $$\min_{s > 0} \frac{1}{2}(4 - 4s)^2$$ cho đạo hàm $$-4(4 - 4s) = 0 \implies s^\star = 1 \implies x_1 = 0$$.
   Nhận xét: Backtracking tự động "cứu" thuật toán khỏi bước phân kỳ $$t_0 = 2$$ chỉ sau 1 lần co bước mà không hề cần biết trước $$L = 1$$!

---

Khi thực hiện gradient descent, **kích thước bước** quyết định mức độ cập nhật của biến $$x$$ ở mỗi lần lặp, qua đó ảnh hưởng trực tiếp đến tốc độ và khả năng hội tụ về nghiệm tối ưu. Mục này giới thiệu ba phương pháp chính để lựa chọn kích thước bước:

- Kích thước bước cố định (fixed step size)
- Tìm kiếm đường lùi (backtracking line search)
- Tìm kiếm đường chính xác (exact line search)