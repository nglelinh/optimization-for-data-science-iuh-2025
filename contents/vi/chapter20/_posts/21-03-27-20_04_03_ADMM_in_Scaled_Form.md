---
layout: post
title: '20-04-03 ADMM dạng có tỉ lệ (Scaled Form)'
chapter: '20'
order: 11
owner: Hooncheol Shin
categories:
- chapter20
lang: vi
---

Nếu nhìn vào công thức ADMM ban đầu ở bài 20-04-01, bạn sẽ thấy hai số hạng hơi rườm rà luôn đi kèm nhau: số hạng tuyến tính $$u^T(Ax + Bz - c)$$ và số hạng bình phương $$\frac{\rho}{2}\|Ax + Bz - c\|_2^2$$. Chỉ bằng một phép đổi biến siêu gọn $$w = u / \rho$$ và kỹ thuật **tạo bình phương đầy đủ (completing the square)** của đại số phổ thông, hai số hạng đó gộp lại thành **duy nhất một bình phương** $$\frac{\rho}{2}\|Ax + Bz - c + w\|_2^2$$! Dạng có tỉ lệ (scaled form) này ngắn hơn, ít sai dấu hơn khi viết code và làm lộ rõ ngay mối liên hệ giữa ADMM với toán tử proximal.

## Kiến thức cần nhớ: Ba lợi ích cốt lõi của ADMM dạng có tỉ lệ

Trước khi đọc phép chứng minh tương đương trong bài, hãy nắm rõ vì sao hầu hết bài báo và thư viện phần mềm đều dùng dạng có tỉ lệ:

- **Định nghĩa biến đối ngẫu có tỉ lệ $$w = u / \rho$$:** Đưa hệ số $$\rho$$ ra ngoài ngoặc biến $$u^T r + \frac{\rho}{2}\|r\|_2^2$$ thành $$\frac{\rho}{2}\|r + w\|_2^2 - \frac{\rho}{2}\|w\|_2^2$$. Vì $$-\frac{\rho}{2}\|w\|_2^2$$ là hằng số không phụ thuộc vào $$x$$ hay $$z$$, ta bỏ luôn nó khỏi phép $$\arg\min$$!
- **Diễn giải trực quan của $$w^{(k)}$$ — tổng tích lũy phần dư (Running Sum of Residuals):** Phương trình cập nhật trở thành $$w^{(k)} = w^{(k-1)} + (Ax^{(k)} + Bz^{(k)} - c) = w^{(0)} + \sum_{j=1}^k r^{(j)}$$. Nói cách khác, $$w^{(k)}$$ chính là **bộ tích phân sai số** (giống thành phần I trong bộ điều khiển PID), liên tục tích lũy độ lệch ràng buộc để kéo hệ thống về đúng $$r = 0$$!
- **Biến bước cập nhật thành toán tử proximal ngay lập tức:** Khi ràng buộc là $$x = z$$, bước $$x^{(k)} = \arg\min_x f(x) + \frac{\rho}{2}\|x - (z^{(k-1)} - w^{(k-1)})\|_2^2$$ chính là $$\operatorname{prox}_{f, 1/\rho}(z^{(k-1)} - w^{(k-1)})$$ — hoàn toàn không cần khai triển tích vô hướng!

### Giải thích: Kiểm chứng bằng số phép gộp bình phương và theo dõi biến tích lũy $$w^{(k)}$$

Giả sử tại một vòng lặp ADMM, ta có tham số phạt $$\rho = 2$$, biến đối ngẫu ban đầu $$u = 4$$ (suy ra biến có tỉ lệ $$w = u / \rho = 4 / 2 = 2$$), và ta đang xét một giá trị phần dư $$r = Ax + Bz - c = 1$$:

1. **Tính theo dạng ban đầu (unscaled):**
   $$u^T r + \frac{\rho}{2}\|r\|_2^2 = (4)(1) + \frac{2}{2}(1)^2 = 4 + 1 = 5.$$
2. **Tính theo dạng có tỉ lệ (scaled) kèm hằng số bù $$-\frac{\rho}{2}\|w\|_2^2$$:**
   $$\frac{\rho}{2}\|r + w\|_2^2 - \frac{\rho}{2}\|w\|_2^2 = \frac{2}{2}(1 + 2)^2 - \frac{2}{2}(2)^2 = 9 - 4 = 5.$$
   Hai biểu thức bằng nhau từng đơn vị một — và vì $$-4$$ không đổi khi ta thay đổi $$x$$ hay $$z$$, việc cực tiểu hóa $$(r + 2)^2$$ cho đúng nghiệm hệt như cực tiểu hóa $$4r + r^2$$!
3. **Thấy ngay vai trò "tích lũy sai số" của $$w$$:** Nếu ở 3 vòng lặp đầu phần dư lần lượt là $$r^{(1)} = +0.6, \; r^{(2)} = +0.3, \; r^{(3)} = +0.1$$ (khởi tạo $$w^{(0)} = 0$$), thì:
   $$w^{(1)} = 0.6, \qquad w^{(2)} = 0.9, \qquad w^{(3)} = 1.0.$$
   Ngay cả khi $$r^{(3)}$$ nhỏ dần về $$0$$, giá trị $$w^{(3)} = 1.0$$ vẫn lưu giữ toàn bộ "áp lực" cần thiết để giữ điểm tối ưu đứng vững tại ràng buộc $$r = 0$$!

---

# ADMM dạng có tỉ lệ

ADMM có thể được viết gọn hơn dưới dạng có tỉ lệ (scaled form) bằng cách đổi biến đối ngẫu $$w = u/\rho$$. Khi đó, các bước lặp của ADMM trở thành:
> $$
> \begin{alignat}{1}
> x^{(k)} & = \arg\min_x f(x) + \frac{\rho}{2} \lVert Ax + Bz^{(k-1)} - c + w^{(k-1)} \rVert_2^2  \\
> z^{(k)} & = \arg\min_z g(z) + \frac{\rho}{2} \lVert Ax^{(k)} + Bz - c + w^{(k-1)} \rVert_2^2  \\
> w^{(k)} & = w^{(k-1)} + Ax^{(k)} + Bz^{(k)} - c 
> \end{alignat}
> $$

## Chứng minh tương đương với dạng ban đầu

Khai triển số hạng bình phương ở bước cập nhật $$x^{(k)}$$:

> $$
> \begin{align}
> x^{(k)} & = \arg\min_x f(x) + \frac{\rho}{2} \lVert Ax + Bz^{(k-1)} - c + w^{(k-1)} \rVert_2^2  \\
> & = \arg\min_x f(x)  + \frac{\rho}{2} \lVert Ax + Bz^{(k-1)} - c \rVert_2^2  + \rho w^{(k-1)T} (Ax + Bz^{(k-1)} - c)  + \frac{\rho}{2}\lVert w^{(k-1)} \rVert_2^2 \\
> & = \arg\min_x f(x)  + \frac{\rho}{2} \lVert Ax + Bz^{(k-1)} - c \rVert_2^2  + u^{(k-1)T} (Ax + Bz^{(k-1)} - c) \\
> \end{align}
> $$

trong đó ta thay $$u^{(k-1)} = \rho w^{(k-1)}$$ và lược bỏ hằng số $$\frac{\rho}{2}\lVert w^{(k-1)} \rVert_2^2$$ không phụ thuộc vào $$x$$. Biến đổi cho bước cập nhật $$z^{(k)}$$ hoàn toàn tương tự.

## Ý nghĩa của biến đối ngẫu có tỉ lệ

Từ quy tắc cập nhật ở trên, $$w^{(k)}$$ chính là tổng tích lũy các phần dư gốc từ đầu cho đến vòng lặp thứ $$k$$:

> $$
> \begin{equation}
> w^{(k)} = w^{(0)} + \sum_{i=1}^k (Ax^{(i)} + Bz^{(i)} - c) 
> \end{equation}
> $$

Dạng có tỉ lệ gọn gàng hơn và thường thuận tiện hơn cả trong phân tích lý thuyết lẫn cài đặt thuật toán.
