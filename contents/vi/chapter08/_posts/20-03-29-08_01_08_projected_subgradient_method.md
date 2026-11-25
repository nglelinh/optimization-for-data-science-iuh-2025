---
layout: post
title: '08-01-08 Phương pháp Subgradient có Chiếu'
chapter: '08'
order: 10
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---

Trong hầu hết các bài toán thực tế, biến quyết định không được phép tung tăng tự do khắp không gian $$\mathbb{R}^n$$: xác suất phải không âm và có tổng bằng 1 (nằm trên đơn hình xác suất), trọng số danh mục đầu tư không vượt trần rủi ro, hay nhiễu đối kháng phải nằm trong quả cầu $$\ell_\infty$$ bán kính $$\epsilon$$. Nếu chỉ chạy bước subgradient $$y^{(k)} = x^{(k-1)} - t_k g^{(k-1)}$$, điểm mới rất dễ văng ra ngoài miền ràng buộc $$C$$.

**Phương pháp subgradient có chiếu (Projected Subgradient Method)** giải quyết bài toán ấy theo cách trực quan nhất có thể: cứ bước một bước subgradient tự do, rồi kéo ngay điểm vừa bước về điểm gần nhất trong miền hợp lệ $$C$$ bằng phép chiếu Euclid $$P_C(\cdot)$$. Điều đáng kinh ngạc là toàn bộ bộ máy chứng minh hội tụ của phương pháp không ràng buộc — kể cả bất đẳng thức cơ bản và tốc độ $$O(1/\epsilon^2)$$ — vẫn giữ nguyên không sứt mẻ một ly, nhờ một tính chất hình học vàng của tập lồi: phép chiếu luôn làm co (không làm tăng) khoảng cách tới mọi điểm nằm trong $$C$$!

## Kiến thức cần nhớ: Ba trụ cột của phương pháp subgradient có chiếu

- **Tính không giãn (Non-expansiveness) của phép chiếu Euclid lên tập lồi đóng:** Với mọi $$y \in \mathbb{R}^n$$ và mọi điểm $$x^* \in C$$, ta luôn có:
  $$\|P_C(y) - x^*\|_2 \le \|y - x^*\|_2.$$
  Về hình học, góc $$\angle(y - P_C(y), x^* - P_C(y)) \ge 90^\circ$$ (định lý góc tù của phép chiếu lồi). Nhờ bất đẳng thức này, khi ta thay $$y^{(k)} = x^{(k-1)} - t_k g^{(k-1)}$$ bằng $$x^{(k)} = P_C(y^{(k)})$$, khoảng cách bình phương tới $$x^*$$ chỉ có thể *giảm thêm* hoặc giữ nguyên, không bao giờ tăng!
- **Bảo toàn nguyên vẹn tốc độ hội tụ $$O(1/\epsilon^2)$$:** Vì $$\|x^{(k)} - x^*\|_2^2 \le \|x^{(k-1)} - t_k g^{(k-1)} - x^*\|_2^2$$, mọi bước trong chứng minh bất đẳng thức cơ bản đều đi qua trơn tru. Phép chiếu hoàn toàn "miễn phí" về mặt số vòng lặp lý thuyết.
- **Chi phí tính phép chiếu — ranh giới của tính thực tiễn:** Thuật toán chỉ nhanh khi $$P_C(y)$$ có công thức đóng hoặc thuật toán tính nhanh: chiếu lên hộp $$[l, u]$$ là phép cắt ngưỡng (clipping) $$O(n)$$; chiếu lên quả cầu $$\ell_2$$ là co tỷ lệ $$O(n)$$; chiếu lên đơn hình xác suất mất $$O(n \log n)$$ (hoặc $$O(n)$$ kỳ vọng). Nếu $$C$$ là giao phức tạp của nhiều đa diện, phép chiếu bản thân nó đã là một bài toán quy hoạch bậc hai tốn kém.

### Giải thích: Tính tay một bước subgradient có chiếu lên đĩa đơn vị

Xét bài toán có ràng buộc trong $$\mathbb{R}^2$$:
$$\min_{x \in C} \; f(x) = |x_1 - 2| + |x_2 - 2|, \quad C = \{x \in \mathbb{R}^2 : \|x\|_2 \le 1\}.$$
Đích tự do $$(2, 2)$$ nằm ngoài đĩa đơn vị, nên nghiệm có ràng buộc phải nằm trên biên của $$C$$. Bắt đầu từ $$x^{(0)} = (0, 0) \in C$$ với bước $$t_1 = 1$$.

1. **Tính subgradient tại $$x^{(0)} = (0, 0)$$:**
   Vì $$x_1 = 0 < 2$$ và $$x_2 = 0 < 2$$, cả hai nhánh trị tuyệt đối đều trơn tại $$(0, 0)$$ với $$g^{(0)} = (-1, -1)$$.
   Giá trị ban đầu: $$f(0, 0) = 2 + 2 = 4$$.
2. **Bước subgradient tự do (chưa chiếu):**
   $$y^{(1)} = x^{(0)} - t_1 g^{(0)} = (0, 0) - 1(-1, -1) = (1, 1).$$
   Kiểm tra tính khả thi: $$\|y^{(1)}\|_2 = \sqrt{1^2 + 1^2} = \sqrt{2} \approx 1.414 > 1$$ — điểm $$y^{(1)}$$ đã văng ra ngoài đĩa $$C$$!
3. **Chiếu trực giao lên đĩa đơn vị $$C$$:**
   $$x^{(1)} = P_C(1, 1) = \frac{(1, 1)}{\|(1, 1)\|_2} = \left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right) \approx (0.707, 0.707).$$
4. **Kiểm chứng tính không giãn và chất lượng nghiệm:**
   - Giá trị hàm giảm mạnh: $$f(x^{(1)}) = 2\left(2 - \frac{1}{\sqrt{2}}\right) = 4 - \sqrt{2} \approx 2.586 < 4$$.
   - Thực tế, theo bất đẳng thức Cauchy–Schwarz $$x_1 + x_2 \le \sqrt{2}\|x\|_2 \le \sqrt{2}$$, nên $$4 - \sqrt{2}$$ chính là giá trị tối ưu toàn cục $$f^*$$ và $$x^{(1)}$$ chạm đúng nghiệm tối ưu ngay trong bước chiếu đầu tiên!

Ý tưởng phép chiếu ở ví dụ trước dẫn đến **phương pháp subgradient có chiếu (projected subgradient method)**, dùng để giải các bài toán tối ưu lồi có ràng buộc.

Ký hiệu miền ràng buộc là tập lồi đóng $$C$$, bài toán tối ưu có dạng:

>
$$ \begin{align}
\min_x \text{ }f(x) \quad \text{với điều kiện } x \in C
\end{align} $$

Phương pháp subgradient có chiếu thực hiện tương tự phương pháp subgradient tiêu chuẩn, nhưng sau mỗi bước cập nhật, điểm mới được chiếu trở lại tập ràng buộc $$C$$:

>
$$ \begin{align}
x^{(k)} = P_c(x^{(k-1)} - t_k \cdot g^{(k-1)}), \quad k = 1,2,3,...
\end{align} $$

Nếu phép chiếu $$P_C$$ thực hiện được chính xác, phương pháp này có cùng các tính chất hội tụ và tốc độ hội tụ như phương pháp subgradient không ràng buộc.

Tuy nhiên, cần lưu ý rằng ngay cả khi $$C$$ là một tập lồi có mô tả đơn giản, nếu phép chiếu $$P_C$$ khó tính toán thì thuật toán tổng thể vẫn tốn kém. Một số tập $$C$$ có phép chiếu tương đối dễ tính gồm:

- Tập ảnh affine: {$$Ax + b : x \in \mathbb{R}^{n}$$}
- Tập nghiệm của hệ phương trình tuyến tính: {$$x: Ax=b$$}
- Góc phần tư không âm (nonnegative orthant): $$\mathbb{R}_+^{n} = $$ {$$x: x\ge 0$$}
- Một số quả cầu chuẩn: {$$x: \lVert x \rVert _p \le 1 $$} với $$p=1,2,\infty$$
- Một số đa diện đơn giản và hình nón đơn giản
