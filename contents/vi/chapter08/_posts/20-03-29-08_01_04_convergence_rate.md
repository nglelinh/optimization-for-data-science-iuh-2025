---
layout: post
title: '08-01-04 Tốc độ hội tụ'
chapter: '08'
order: 6
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---

Có một thực tế phũ phàng mà bất kỳ kỹ sư tối ưu nào cũng sớm chạm mặt: một thuật toán *có hội tụ* chưa chắc đã *dùng được*. Nếu để giảm sai số đi 10 lần mà số vòng lặp tăng lên 100 lần, thời gian tính toán sẽ nhanh chóng vượt quá tuổi thọ dự án. Bài học này đặt con số chính xác lên chiếc đồng hồ đó: phương pháp subgradient đạt tốc độ hội tụ $$O(1/\epsilon^2)$$ — chậm hơn một bậc toàn diện so với $$O(1/\epsilon)$$ của gradient descent trên hàm trơn.

Điều đặc biệt là tốc độ $$O(1/\epsilon^2)$$ không phải do ta chứng minh kém hay chọn bước chưa khéo. Trong lý thuyết độ phức tạp thông tin của Nemirovski và Yudin, tồn tại các hàm lồi không trơn (trong không gian chiều đủ lớn) mà *không một thuật toán bậc nhất hộp đen nào* chỉ hỏi giá trị hàm và subgradient có thể vượt qua cận dưới $$\Omega(1/\epsilon^2)$$. Nói cách khác, $$O(1/\epsilon^2)$$ vừa là giới hạn, vừa là thành tích tối ưu của lớp bài toán hoàn toàn không trơn.

## Kiến thức cần nhớ: Ba trụ cột của phân tích tốc độ hội tụ

- **Tối ưu hóa cận trên theo kích thước bước (Step-size Balancing):** Xuất phát từ cận $$f_{\text{best}}^{(k)} - f^* \le \frac{R^2}{2kt} + \frac{G^2 t}{2}$$, ta xem đây là hàm của $$t > 0$$. Dùng bất đẳng thức AM–GM (hoặc lấy đạo hàm theo $$t$$ bằng $$0$$), hai số hạng bằng nhau khi $$t^* = \frac{R}{G\sqrt{k}}$$, cho ra cận nhỏ nhất $$\frac{RG}{\sqrt{k}}$$.
- **Chuyển đổi giữa tốc độ theo số bước $$k$$ và độ phức tạp theo sai số $$\epsilon$$:** Đặt $$\frac{RG}{\sqrt{k}} \le \epsilon$$ rồi giải tìm $$k$$, ta thu được $$k \ge \frac{R^2 G^2}{\epsilon^2} = O(1/\epsilon^2)$$. Như vậy tốc độ $$O(1/\sqrt{k})$$ theo số bước tương đương chính xác với độ phức tạp $$O(1/\epsilon^2)$$ theo độ chính xác mong muốn.
- **Định lý cận dưới thông tin (Oracle Complexity Lower Bound):** Trên lớp hàm lồi $$G$$-Lipschitz trong $$\mathbb{R}^n$$ (với $$n$$ lớn), mọi phương pháp bậc nhất chỉ dùng tổ hợp tuyến tính các subgradient quá khứ đều có sai số ít nhất $$\Omega(RG/\sqrt{k})$$. Do đó, muốn phá vỡ rào cản $$O(1/\epsilon^2)$$, ta bắt buộc phải khai thác thêm cấu trúc (tính trơn, tính tách được, hoặc phép toán gần kề).

### Giải thích: Tính ngân sách vòng lặp cụ thể cho $$O(1/\epsilon^2)$$ so với $$O(1/\epsilon)$$

Giả sử bài toán có $$R = 10$$ và $$G = 2$$, nên tích $$RG = 20$$.

1. **Tìm bước cố định tối ưu cho ngân sách $$k$$ bước:**
   Đặt $$\phi(t) = \frac{100}{2kt} + \frac{4t}{2} = \frac{50}{kt} + 2t$$.
   Đạo hàm $$\phi'(t) = -\frac{50}{kt^2} + 2 = 0 \implies t^* = \frac{5}{\sqrt{k}} = \frac{R}{G\sqrt{k}}$$.
   Thay vào $$\phi(t^*)$$: $$\phi(t^*) = \frac{50}{k(5/\sqrt{k})} + 2\frac{5}{\sqrt{k}} = \frac{10}{\sqrt{k}} + \frac{10}{\sqrt{k}} = \frac{20}{\sqrt{k}}$$.
2. **Đếm số vòng lặp theo từng mức sai số $$\epsilon$$:**
   - Muốn $$\epsilon = 0.1$$: cần $$\frac{20}{\sqrt{k}} \le 0.1 \implies \sqrt{k} \ge 200 \implies k \ge 40{,}000$$ bước (với $$t^* = 5/200 = 0.025$$).
   - Muốn chính xác gấp 10 lần, $$\epsilon = 0.01$$: cần $$\sqrt{k} \ge 2{,}000 \implies k \ge 4{,}000{,}000$$ bước — **tăng gấp 100 lần**!
3. **So sánh với gradient descent trên hàm trơn ($$L = 2$$):**
   Với gradient descent, cận sai số là $$\frac{LR^2}{2k} = \frac{100}{k}$$.
   - Để đạt $$\epsilon = 0.1$$: chỉ cần $$k = 1{,}000$$ bước (nhanh hơn 40 lần).
   - Để đạt $$\epsilon = 0.01$$: chỉ cần $$k = 10{,}000$$ bước (nhanh hơn **400 lần**!).
   Con số chênh lệch 400 lần này giải thích trọn vẹn vì sao trong thực tế, mỗi khi tách được phần trơn ra khỏi phần không trơn (như Lasso hay hồi quy logistic có chuẩn $$\ell_1$$), ta sẽ rất hào hứng chuyển sang phương pháp gradient gần kề ở Chương 09.

Tốc độ hội tụ mô tả số bước lặp cần thiết để đạt một điểm cận tối ưu với sai số $$\epsilon$$ theo độ lớn của $$\epsilon$$, biểu diễn qua [ký hiệu Big-O](https://en.wikipedia.org/wiki/Big_O_notation). Chẳng hạn, nếu $$\epsilon = 10^{-2}$$ và tốc độ hội tụ là $$O(1/\epsilon)$$, thuật toán cần khoảng $$1/10^{-2}=10^2$$ bước lặp.

Ta sử dụng [08-01-02 Bất đẳng thức cơ bản]({% multilang_post_url contents/chapter08/20-03-29-08_01_02_basic_inequality %}) để suy ra tốc độ hội tụ của phương pháp subgradient với kích thước bước cố định.

>$$Nhắc lại:$$
>\begin{align}
> f^{k}_{best} - f^{*} \quad \le \quad \frac{R^{2}}{2kt} + \frac{G^{2}t}{2}
\end{align}

Giả sử ta chọn $$t$$ và $$k$$ sao cho $$\frac{R^{2}}{2kt} \le \frac{\epsilon}{2}$$ và $$\frac{G^{2}t}{2} \le \frac{\epsilon}{2}$$ (trong đó $$\epsilon$$ là sai số cận tối ưu, $$G$$ là hằng số Lipschitz, và $$R$$ là khoảng cách từ điểm khởi tạo đến điểm tối ưu). Khi đó $$ \frac{R^{2}}{2kt} + \frac{G^{2}t}{2} \le \epsilon$$. Từ $$\frac{G^{2}t}{2} \le \frac{\epsilon}{2}$$ suy ra $$t \le \frac{\epsilon}{G^{2}}$$; kết hợp với $$\frac{R^{2}}{2kt} \le \frac{\epsilon}{2}$$ ta có $$k \ge \frac{R^2G^2}{\epsilon^2}$$. Như vậy, để bảo đảm $$f^{k}_{best} - f^{*} \le \epsilon$$, số bước lặp cần thiết có bậc $$\frac{R^2G^2}{\epsilon^2}$$.

Do đó, tốc độ hội tụ của phương pháp subgradient là $$O(1/\epsilon^2)$$, đòi hỏi nhiều bước lặp hơn đáng kể so với tốc độ $$O(1/\epsilon)$$ của gradient descent trên hàm trơn.