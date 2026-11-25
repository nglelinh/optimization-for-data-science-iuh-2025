---
layout: post
title: 06-03-06 Can we do better?
chapter: '06'
order: 15
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
---

Gradient Descent đạt tốc độ $$O(1/k)$$ trên hàm lồi $$L$$-trơn và $$O\big((1 - 1/\kappa)^k\big)$$ trên hàm lồi mạnh. Đến đây, một câu hỏi đầy tham vọng tự nhiên vang lên: *nếu ta chỉ được phép dùng đúng thông tin bậc nhất (giá trị hàm và gradient $$\nabla f$$), liệu ta có thể làm nhanh hơn Gradient Descent không? Và giới hạn tốc độ ánh sáng của mọi thuật toán bậc nhất là bao nhiêu?*

Năm 1983, nhà toán học trẻ người Nga Yurii Nesterov đã làm rung chuyển giới tối ưu hóa bằng hai kết quả song sinh: (1) chứng minh **cận dưới bất khả xâm phạm** $$\Omega(1/k^2)$$ cho mọi thuật toán bậc nhất trên hàm lồi $$L$$-trơn, và (2) sáng chế ngay thuật toán **Nesterov Accelerated Gradient (NAG)** chạm đúng cận tối ưu $$O(1/k^2)$$ — chỉ bằng vài phép cộng vector miễn phí!

## Kiến thức cần nhớ: Giới hạn Thông tin Bậc nhất và Bước nhảy Nesterov

Ba trụ cột sau tóm tắt bước ngoặt lịch sử trong lý thuyết độ phức tạp tối ưu hóa:

- **Mô hình Hộp đen Bậc nhất (First-Order Oracle Model):** Thuật toán chỉ được phép truy vấn $$\nabla f(x^{(i)})$$ và tạo điểm mới $$x^{(k)}$$ nằm trong không gian con sinh bởi các gradient đã thấy: $$x^{(k)} \in x^{(0)} + \operatorname{span}\{\nabla f(x^{(0)}), \dots, \nabla f(x^{(k-1)})\}$$.
- **Hàm "Xấu nhất Thế giới" của Nesterov (Worst-Case Quadratic Chain):** Nesterov xây dựng một hàm bậc hai dạng chuỗi khớp nối $$f(x) = \frac{L}{4}\left[\frac{1}{2}(x_1^2 + \sum (x_i - x_{i+1})^2 + x_n^2) - x_1\right]$$ mà sau $$k$$ bước truy vấn gradient, mọi thuật toán bậc nhất chỉ có thể "đánh thức" được tối đa $$k$$ tọa độ đầu tiên! Từ đó ông chứng minh **không một thuật toán bậc nhất nào** thắng được cận dưới $$\Omega(L\|x^{(0)} - x^\star\|^2 / k^2)$$.
- **Khoảng trống giữa GD và Cận tối ưu:**
  - Hàm lồi $$L$$-trơn: GD tốn $$O(1/\epsilon)$$ bước, còn Nesterov tăng tốc chỉ tốn $$O(1/\sqrt{\epsilon})$$ bước!
  - Hàm lồi mạnh ($$\kappa = L/m$$): GD tốn $$O(\kappa \log(1/\epsilon))$$ bước, còn Nesterov chỉ tốn $$O(\sqrt{\kappa} \log(1/\epsilon))$$ bước!

### Giải thích: So sánh sức mạnh của $$O(1/k)$$ vs. $$O(1/k^2)$$ và $$\kappa$$ vs. $$\sqrt{\kappa}$$ bằng con số thật

1. **Trên bài toán lồi trơn cần sai số $$\epsilon = 10^{-4}$$:**
   - Gradient Descent thường ($$O(1/\epsilon)$$): cần cỡ $$10\,000$$ vòng lặp.
   - Tăng tốc Nesterov ($$O(1/\sqrt{\epsilon})$$): chỉ cần cỡ $$\sqrt{10\,000} = 100$$ vòng lặp — **nhanh hơn gấp 100 lần** với chi phí mỗi vòng lặp gần như bằng nhau!
2. **Trên bài toán lồi mạnh điều kiện xấu với $$\kappa = 10\,000$$:**
   - Gradient Descent thường phụ thuộc $$\kappa = 10\,000$$: hệ số co $$1 - 1/10\,000 = 0.9999$$.
   - Tăng tốc Nesterov phụ thuộc $$\sqrt{\kappa} = 100$$: hệ số co $$1 - 1/100 = 0.99$$ — **giảm số vòng lặp đúng 100 lần**!
3. **Bí quyết đằng sau tốc độ đó:** Thay vì chỉ đi từ $$x^{(k)}$$, Nesterov tạo điểm "nhìn trước" $$y^{(k)} = x^{(k)} + \beta_k (x^{(k)} - x^{(k-1)})$$ rồi mới tính gradient tại $$y^{(k)}$$ — trực giác của phương pháp **Momentum** mà ta sẽ khám phá ngay ở các bài sau!

---

Gradient descent đạt tốc độ hội tụ $$O(1/k)$$ (tương ứng cần $$O(1/\epsilon)$$ vòng lặp để đạt sai số $$\epsilon$$) đối với các hàm lồi, khả vi và có gradient liên tục Lipschitz. Câu hỏi đặt ra là liệu có phương pháp bậc nhất nào đạt tốc độ hội tụ nhanh hơn gradient descent hay không.

### Phương pháp Bậc nhất

Một phương pháp bậc nhất tạo ra điểm lặp $$x^{(k)}$$ sao cho $$x^{(k)}$$ nằm trong không gian tuyến tính sinh bởi các gradient đã tính từ điểm khởi tạo $$x^{(0)}$$ đến $$x^{(k-1)}$$:

> $$x^{(k)} \in x^{(0)} + $$ **span**$$\{\nabla f(x^{(0)}),\nabla f(x^{(1)}),...,\nabla f(x^{(k-1)})\}$$

### Định lý Nesterov

Định lý của Nesterov thiết lập một cận dưới cho tốc độ hội tụ tốt nhất có thể của mọi phương pháp bậc nhất.

> **Định lý Nesterov**: Với mọi $$k \le (n-1)/2$$ và mọi điểm xuất phát $$x^{(0)}$$, tồn tại một hàm lồi trơn $$f$$ có gradient $$L$$-Lipschitz sao cho mọi phương pháp bậc nhất đều thỏa mãn (với $$n$$ là số chiều):<br>
\begin{align}
f(x^{(k)}) - f^{\star} \ge \frac{3L \lVert x^{(0)} - x^{\star} \rVert_2^2}{32(k + 1)^2}
\end{align}

Vì cận dưới trong định lý Nesterov có $$k^2$$ ở mẫu số, tốc độ hội tụ tối ưu về mặt lý thuyết của lớp phương pháp bậc nhất là $$O(1/k^2)$$, tương ứng chỉ cần $$O(1/\sqrt{\epsilon})$$ vòng lặp. Các thuật toán tăng tốc đạt được cận này sẽ được trình bày chi tiết hơn ở các phần sau.
