---
layout: post
title: 06-03 Phân tích hội tụ
chapter: '06'
order: 9
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
---

Một thuật toán nhìn trên đồ thị có vẻ đang giảm dần giá trị hàm mất mát, nhưng làm sao ta biết chắc nó sẽ thực sự chạm tới $$f^\star$$ chứ không dừng lơ lửng giữa chừng? Và quan trọng hơn: muốn giảm sai số từ $$10^{-2}$$ xuống $$10^{-6}$$, ta cần thêm bao nhiêu vòng lặp — gấp 10 lần, gấp 10.000 lần, hay chỉ gấp 3 lần?

Mục 06-03 mở ra **Phân tích hội tụ (Convergence Analysis)** — phần toán học sâu sắc nhất của Chương 06. Bạn sẽ chứng kiến sự khác biệt một trời một vực giữa hai thế giới: hàm **lồi trơn** (hội tụ dưới tuyến tính $$O(1/k)$$ — cần $$O(1/\epsilon)$$ bước) và hàm **lồi mạnh & trơn** (hội tụ tuyến tính $$O(c^k)$$ — chỉ cần $$O(\log(1/\epsilon))$$ bước), đồng thời hiểu giới hạn tự nhiên của mọi thuật toán bậc nhất qua Định lý Nesterov!

## Kiến thức cần nhớ: Bốn tầng phân tích tốc độ hội tụ

Toàn bộ phần 06-03 được xây dựng theo một chuỗi suy luận bốn tầng cực kỳ chặt chẽ:

- **Tầng 1 — Vũ khí nền tảng (Cận trên bậc hai / $$L$$-smoothness):** Giả thiết $$\|\nabla f(x) - \nabla f(y)\|_2 \le L\|x - y\|_2$$ cho phép kẹp hàm $$f$$ dưới một parabol bậc hai, sinh ra **Bổ đề Giảm (Descent Lemma)**: mỗi bước GD với $$t \le 1/L$$ giảm ít nhất $$\frac{t}{2}\|\nabla f(x)\|_2^2$$.
- **Tầng 2 — Hội tụ của hàm lồi trơn ($$O(1/k)$$):** Kết hợp Bổ đề Giảm với bất đẳng thức lồi bậc nhất và kỹ thuật tổng lồng nhau (telescoping sum) chứng minh $$f(x^{(k)}) - f^\star \le \frac{\|x^{(0)} - x^\star\|_2^2}{2tk}$$ cho cả bước cố định lẫn Backtracking!
- **Tầng 3 — Bứt tốc nhờ Lồi mạnh ($$O(c^k)$$):** Khi hàm có thêm cận dưới bậc hai với độ cong $$m > 0$$, sai số giảm theo cấp số nhân với hệ số co $$c = 1 - m/L = 1 - 1/\kappa$$ — tức là đạt thêm 1 chữ số chính xác chỉ tốn thêm một số hằng bước lặp!
- **Tầng 4 — Giới hạn lý thuyết & Tăng tốc Nesterov:** Nesterov chứng minh mọi thuật toán bậc nhất trên hàm lồi $$L$$-trơn đều không thể nhanh hơn $$\Omega(1/k^2)$$ — và Gradient Descent thường ($$O(1/k)$$) chưa chạm ngưỡng đó, mở đường cho phương pháp tăng tốc Nesterov!

### Giải thích: So sánh trực quan số vòng lặp giữa $$O(1/\epsilon)$$ và $$O(\log(1/\epsilon))$$

Giả sử bài toán có hằng số trơn $$L = 10$$, khoảng cách ban đầu $$\|x^{(0)} - x^\star\|_2 = 1$$, và ta cần đạt độ chính xác $$\epsilon$$ (tức $$f(x^{(k)}) - f^\star \le \epsilon$$):

1. **Trường hợp 1 — Chỉ lồi & $$L$$-trơn (tốc độ $$O(1/k)$$, cận $$k \approx \frac{L \|x^{(0)} - x^\star\|_2^2}{2\epsilon} = \frac{5}{\epsilon}$$):**
   - Muốn $$\epsilon = 10^{-2}$$: cần khoảng $$500$$ vòng lặp.
   - Muốn $$\epsilon = 10^{-4}$$: cần khoảng $$50\,000$$ vòng lặp (tăng **100 lần**!).
   - Muốn $$\epsilon = 10^{-6}$$: cần khoảng $$5\,000\,000$$ vòng lặp!
2. **Trường hợp 2 — Lồi mạnh với $$m = 1$$ ($$\kappa = L/m = 10$$, cận $$k \approx \kappa \ln\frac{f(x^{(0)}) - f^\star}{\epsilon}$$):**
   - Với $$f(x^{(0)}) - f^\star = 5$$ và $$\epsilon = 10^{-2}$$: $$k \approx 10 \ln(500) \approx 62$$ vòng lặp.
   - Muốn $$\epsilon = 10^{-4}$$: $$k \approx 10 \ln(50\,000) \approx 108$$ vòng lặp (chỉ tăng thêm 46 bước!).
   - Muốn $$\epsilon = 10^{-6}$$: $$k \approx 10 \ln(5\,000\,000) \approx 154$$ vòng lặp!
   **Kết luận sâu sắc:** Tính lồi mạnh (chẳng hạn nhờ cộng thêm điều chuẩn Ridge $$\frac{\lambda}{2}\|x\|_2^2$$) biến bài toán tốn 5 triệu vòng lặp thành bài toán giải xong trong 154 bước!

---

Trong phần này, chúng ta sẽ phân tích tốc độ hội tụ của thuật toán Gradient Descent. Cụ thể, ta sẽ xem xét các cận sai số trong trường hợp dùng kích thước bước cố định, trường hợp dùng tìm kiếm đường lùi (backtracking line search), và trường hợp hàm mục tiêu thỏa mãn điều kiện lồi mạnh.