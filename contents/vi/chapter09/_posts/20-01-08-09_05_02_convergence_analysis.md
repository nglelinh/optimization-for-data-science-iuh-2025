---
layout: post
title: '09-05-02 Phân tích hội tụ'
chapter: '09'
order: 8
owner: Kyeongmin Woo
categories:
- chapter09
lang: vi
---

Trong giải tích thuật toán, bước nhảy từ $$O(1/k)$$ sang $$O(1/k^2)$$ không chỉ là thêm một số mũ nhỏ ở mẫu số — đó là ranh giới giữa việc chờ 10 giây và chờ 3 giờ đồng hồ! Bài học này phát biểu định lý hội tụ chính xác cho phương pháp gradient gần kề tăng tốc: dưới đúng các giả thiết quen thuộc của bài 09-02 ($$g$$ lồi với $$\nabla g$$ liên tục $$L$$-Lipschitz, $$h$$ lồi có prox tính được), sai số giảm theo $$\frac{2\|x^{(0)} - x^*\|_2^2}{t(k+1)^2}$$ với bước cố định $$t \le 1/L$$ (và giữ nguyên bậc $$O(1/k^2)$$ với tìm kiếm đường thẳng lùi).

Điểm đáng chiêm ngưỡng nhất về mặt lý thuyết là con số $$O(1/k^2)$$ này **khớp chặt với cận dưới thông tin của Nemirovski–Yudin** cho toàn bộ lớp hàm lồi trơn $$L$$-Lipschitz! Nghĩa là không tồn tại bất kỳ thuật toán bậc nhất nào (chỉ dùng giá trị hàm, $$\nabla g$$ và $$\operatorname{prox}_h$$) có thể đạt tốc độ tốt hơn $$\Omega(1/k^2)$$ trong trường hợp xấu nhất trên không gian chiều cao.

## Bản đồ kiến thức nền: Ba trụ cột của phân tích hội tụ tăng tốc $$O(1/k^2)$$

- **Hàm thế năng Lyapunov (Estimate Sequence):** Khác với ISTA chỉ cần theo dõi $$f(x^{(k)}) - f^*$$ giảm đơn điệu, bản tăng tốc có thể làm $$f$$ tạm tăng ở một vài bước. Chứng minh vì thế theo dõi một *hàm năng lượng tổng hợp* kết hợp cả sai số hàm $$(k+1)^2(f(x^{(k)}) - f^*)$$ lẫn bình phương khoảng cách của điểm phụ tới $$x^*$$ — và chứng minh tổng năng lượng này không tăng theo $$k$$!
- **So sánh hằng số đầu và hệ số tiệm cận:**
  - ISTA (không tăng tốc): $$f(x^{(k)}) - f^* \le \frac{L\|x^{(0)} - x^*\|_2^2}{2k}$$.
  - Tăng tốc (FISTA / APG): $$f(x^{(k)}) - f^* \le \frac{2L\|x^{(0)} - x^*\|_2^2}{(k+1)^2}$$.
  Ở $$k = 1$$ hai cận gần ngang nhau, nhưng ngay từ $$k \ge 4$$ tử số lớn gấp 4 lần đã bị mẫu số $$(k+1)^2$$ đè bẹp hoàn toàn!
- **Tìm kiếm đường thẳng lùi với bước không tăng:** Khi dùng backtracking cho phương pháp tăng tốc, ta kiểm tra điều kiện chặn trên parabol của $$g$$ tại điểm ngoại suy $$v^{(k)}$$ (thay vì $$x^{(k)}$$), và cần chú ý giữ dãy bước $$t_k$$ không tăng (hoặc điều chỉnh hệ số $$\theta_k$$ theo tỷ lệ $$t_k / t_{k-1}$$) để bảo toàn bất đẳng thức Lyapunov.

### Khung giải thích (nên đọc chậm): Tính trực tiếp cận sai số của ISTA và Tăng tốc theo số vòng lặp $$k$$

Giả sử bài toán có $$L = 2$$ và khoảng cách khởi điểm $$\|x^{(0)} - x^*\|_2 = 5$$ (nên $$L\|x^{(0)} - x^*\|_2^2 = 2 \times 25 = 50$$). Với bước $$t = 1/L = 0.5$$:
- Cận ISTA: $$B_{\text{ISTA}}(k) = \frac{50}{2k} = \frac{25}{k}$$.
- Cận Tăng tốc: $$B_{\text{APG}}(k) = \frac{2 \times 50}{(k+1)^2} = \frac{100}{(k+1)^2}$$.

1. **Tại $$k = 10$$ vòng lặp:**
   - ISTA: $$25 / 10 = 2.50$$.
   - Tăng tốc: $$100 / 11^2 = 100 / 121 \approx 0.826$$ (nhỏ hơn **3 lần**).
2. **Tại $$k = 100$$ vòng lặp:**
   - ISTA: $$25 / 100 = 0.25$$.
   - Tăng tốc: $$100 / 101^2 = 100 / 10{,}201 \approx 0.0098$$ (nhỏ hơn **25.5 lần**!).
3. **Số vòng lặp cần để đảm bảo sai số $$\le 0.01$$:**
   - ISTA cần $$\frac{25}{k} \le 0.01 \implies k \ge 2{,}500$$ vòng lặp.
   - Tăng tốc chỉ cần $$\frac{100}{(k+1)^2} \le 0.01 \implies (k+1)^2 \ge 10{,}000 \implies k \ge 99$$ vòng lặp!
   Chỉ mất **99 vòng thay vì 2,500 vòng** — một phép tính tay đủ nói lên toàn bộ giá trị của định lý hội tụ $$O(1/k^2)$$.

# Phân tích hội tụ

Trong phần này, chúng ta trình bày kết quả hội tụ của phương pháp gradient gần kề tăng tốc.

## Định lý hội tụ
Giả sử $$g$$ là hàm lồi và khả vi, $$h$$ là hàm lồi, và $$\nabla g$$ liên tục Lipschitz với hằng số $$L > 0$$. Khi đó, phương pháp gradient gần kề tăng tốc với kích thước bước cố định $$t \le 1/L$$ thỏa mãn:

> $$f(x^{(k)}) - f^* \le \frac{2L \lVert x^{(0)} - x^* \rVert^2_2}{(k+1)^2}$$

Kết quả này cho thấy tốc độ hội tụ của thuật toán đạt $$O(1/k^2)$$, nhanh hơn đáng kể so với tốc độ $$O(1/k)$$ của phương pháp gradient gần kề tiêu chuẩn.

## Tìm kiếm đường thẳng lùi
Tìm kiếm đường thẳng lùi cũng có thể áp dụng cho phương pháp gradient gần kề tăng tốc tương tự như phương pháp gradient gần kề tiêu chuẩn, cho phép điều chỉnh kích thước bước thích ứng khi không biết trước hằng số Lipschitz $$L$$.

Để xem chứng minh chi tiết và phiên bản có tìm kiếm đường thẳng lùi, tham khảo Beck và Teboulle (2009), "A Fast Iterative Shrinkage-Thresholding Algorithm for Linear Inverse Problems" (FISTA).
