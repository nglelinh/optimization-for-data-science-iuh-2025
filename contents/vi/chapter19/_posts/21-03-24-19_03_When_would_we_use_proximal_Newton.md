---
layout: post
title: '19-03 Khi nào nên dùng Newton proximal?'
chapter: '19'
order: 7
owner: Hooncheol Shin
categories:
- chapter19
lang: vi
---

Trong tối ưu hóa, không có thuật toán nào là "chén thánh" thắng ở mọi bài toán. Proximal Newton hội tụ siêu nhanh về số vòng lặp ngoài ($$O(\log\log(1/\epsilon))$$ so với $$O(1/\epsilon)$$ của proximal gradient), nhưng cái giá phải trả lại vô cùng đắt đỏ: **mỗi một vòng lặp ngoài của nó lại phải giải cả một bài toán tối ưu bậc hai có phạt bên trong!** Vậy ranh giới nào phân định lúc nào nên dùng Proximal Newton và lúc nào nên trung thành với Proximal Gradient?

## Bản đồ kiến thức nền: Bốn tiêu chí quyết định chọn Proximal Newton hay Proximal Gradient

Để đưa ra quyết định kiến trúc bộ giải chính xác trong thực tế, hãy cân đo bốn yếu tố sau:

- **Chi phí đánh giá hàm $$g$$ và gradient $$\nabla g$$:** Nếu tính $$\nabla g(x)$$ rất đắt (ví dụ duyệt qua tập dữ liệu hàng triệu mẫu trong hồi quy logistic, hoặc tính nghịch đảo ma trận log-det $$O(p^3)$$ trong graphical lasso), thì việc giảm số vòng lặp ngoài từ 2.000 xuống còn 10 vòng của Proximal Newton sẽ tiết kiệm thời gian khổng lồ.
- **Độ thưa của nghiệm và tập hoạt động (Active Set):** Khi $$h(x) = \lambda\|x\|_1$$ tạo ra nghiệm rất thưa (hầu hết tọa độ bằng $$0$$), bộ giải hạ tọa độ bên trong chỉ cần chạy trên tập nhỏ các biến khác $$0$$ — biến bài toán con bậc hai tưởng chừng đắt đỏ trở nên cực rẻ!
- **Yêu cầu độ chính xác cuối cùng $$\epsilon$$:** Nếu chỉ cần sai số thô $$10^{-2}$$ (như nhiều bài toán học sâu), bậc nhất là đủ nhanh; nhưng nếu cần sai số chính xác $$10^{-8}\text{–}10^{-12}$$ (thống kê, điều khiển, tài chính), hội tụ bậc hai của Newton proximal bỏ xa hoàn toàn.
- **Số điều kiện của Hessian $$\nabla^2 g$$:** Khi các đặc trưng tương quan mạnh làm số điều kiện $$\kappa = L/m$$ rất lớn, PGD bị dao động hình răng cưa suốt hàng nghìn bước, còn Proximal Newton triệt tiêu hoàn toàn độ lệch trục.

### Khung giải thích (nên đọc chậm): Tính nhanh bài toán chi phí thực tế giữa PGD và Proximal Newton

Giả sử bạn giải một bài toán hồi quy logistic có phạt $$\ell_1$$ với $$n = 50{,}000$$ mẫu và $$p = 500$$ đặc trưng (nhưng chỉ có khoảng $$s = 25$$ đặc trưng thực sự khác $$0$$ ở nghiệm):

1. **Chi phí mỗi vòng lặp của Proximal Gradient (PGD):**
   - Đánh giá $$\nabla g(x)$$ cần nhân ma trận $$X^T(p - y)$$ tốn cỡ $$2np = 5 \times 10^7$$ phép toán; bước ngưỡng mềm chỉ tốn $$500$$ phép toán (không đáng kể).
   - Giả sử bài toán có số điều kiện xấu khiến PGD cần **400 vòng lặp** để đạt $$\epsilon = 10^{-6}$$: tổng chi phí $$\approx 400 \times 5 \times 10^7 = 2.0 \times 10^{10}$$ phép toán.
2. **Chi phí mỗi vòng lặp của Proximal Newton (kiểu `glmnet`):**
   - Đánh giá $$\nabla g(x)$$ và ma trận trọng số đường chéo $$W$$ tốn cỡ $$5 \times 10^7$$ phép toán.
   - Bài toán con bậc hai được giải bằng hạ tọa độ trên tập hoạt động $$s = 25$$ biến (chỉ lập ma trận Hessian con $$25 \times 25$$), tốn cỡ $$3 \times 10^6$$ phép toán (chỉ bằng **6%** chi phí tính gradient!).
   - Proximal Newton chỉ cần **8 vòng lặp ngoài** để đạt $$\epsilon = 10^{-6}$$: tổng chi phí $$\approx 8 \times 5.3 \times 10^7 = 4.24 \times 10^8$$ phép toán — **nhanh gấp gần 47 lần so với PGD!**

---

Khi nào phương pháp Newton proximal là lựa chọn phù hợp?

Để trả lời câu hỏi này, ta so sánh phương pháp Newton proximal với proximal gradient descent trên bài toán tổng hợp:

**Bài toán:** $$\min_x g(x) + h(x)$$

## So sánh Proximal gradient descent và Newton proximal

| **Proximal gradient descent** |**Newton proximal** | 
| -------- | -------- |
| Ở mỗi bước cực tiểu hóa $$\frac{1}{2} \parallel b - x \parallel_2^2 + h(x)$$ | Ở mỗi bước cực tiểu hóa $$b^T x + x^T A x + h(x)$$ | 
| Toán tử prox thường có nghiệm dạng đóng | Toán tử prox thường không có nghiệm dạng đóng |
| Chi phí mỗi vòng lặp thấp | Chi phí mỗi vòng lặp rất cao (cao hơn cả phương pháp Newton) | 
| Tốc độ hội tụ tương tự gradient descent: <br> $$O(1/\epsilon)$$ | Tốc độ hội tụ tương tự phương pháp Newton: <br> $$O(\log \log (1/\epsilon))$$ | 

Dù có dạng công thức tương đồng, hai phương pháp vận hành rất khác nhau về đánh đổi chi phí.

Vì vậy, phương pháp Newton proximal đặc biệt đáng dùng khi ta có một bộ giải bên trong đủ nhanh cho bài toán prox có tỉ lệ (dạng toàn phương $$+\ h$$), nhờ đó tận dụng ưu thế chỉ cần rất ít vòng lặp ngoài. Khi $$h$$ là hàm tách biến (separable), bộ giải bên trong phổ biến nhất là phương pháp hạ theo tọa độ (coordinate descent).
