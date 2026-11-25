---
layout: post
title: '15-03 Tính chất và diễn giải'
chapter: "15"
order: 7
owner: "Minjoo Lee"
categories:
- chapter16
lang: vi
---

Một câu hỏi cực kỳ quan trọng của người học khi lần đầu gặp bài toán chắn là: *làm sao tôi biết nghiệm $$x^*(t)$$ của bài toán xấp xỉ $$t f(x) + \phi(x)$$ thực sự gần nghiệm thật $$x^*$$ của bài toán gốc đến mức nào? Lỡ với $$t = 1000$$ mà sai số vẫn còn lớn thì sao?*

Mục 15-03 trả lời câu hỏi ấy bằng một kết nối đẹp đến nghẹt thở giữa Chương 15 và lý thuyết đối ngẫu KKT: bằng cách đối chiếu điều kiện dừng của bài toán chắn với điều kiện KKT của bài toán gốc, ta phát hiện ra rằng **mỗi điểm đường trung tâm $$x^*(t)$$ tự động tặng miễn phí một cặp nhân tử đối ngẫu khả thi $$(u^*(t), v^*(t))$$**, từ đó rút ra cận sai số tuyệt đối $$f(x^*(t)) - f(x^*) \le m/t$$!

## Bản đồ kiến thức nền: Hai phát hiện cốt lõi của mục Tính chất và Diễn giải

- **Điều kiện KKT nhiễu (Perturbed KKT):** Phương trình dừng của bài toán chắn khớp hoàn toàn với 3 trong 4 điều kiện KKT của bài toán gốc (khả thi nguyên thủy, khả thi đối ngẫu, điều kiện dừng Lagrangian), và chỉ làm "mềm" duy nhất điều kiện bù yếu từ $$-u_i h_i(x) = 0$$ thành $$-u_i h_i(x) = \frac{1}{t}$$!
- **Tự động sinh điểm khả thi đối ngẫu:** Công thức $$u_i^*(t) = -\frac{1}{t h_i(x^*(t))} > 0$$ biến mọi điểm trên đường trung tâm thành một chứng chỉ đối ngẫu hợp lệ cho bài toán gốc mà không cần giải thêm bài toán đối ngẫu nào.
- **Khoảng cách dưới tối ưu đóng $$m/t$$:** Nhờ cặp điểm khả thi nguyên thủy – đối ngẫu đó, khoảng cách đối ngẫu tính ra **chính xác bằng $$m/t$$**, mang lại thước đo dừng đơn giản và chắc chắn tuyệt đối.

### Khung giải thích (nên đọc chậm): Khôi phục nhân tử đối ngẫu từ điểm đường trung tâm trên ví dụ số

Quay lại bài toán $$\min_x x$$ với ràng buộc $$h_1(x) = -x \le 0$$ và $$h_2(x) = x - 4 \le 0$$ ở bài trước ($$m = 2$$, $$f^* = 0$$). Tại $$t = 1$$, ta đã tính được điểm đường trung tâm $$x^*(1) = 3 - \sqrt{5} \approx 0.7639$$.

1. **Tính cặp nhân tử đối ngẫu theo công thức $$u_i^*(t) = -\frac{1}{t h_i(x^*(t))}$$:**
   - $$u_1^*(1) = \frac{1}{1 \cdot x^*(1)} = \frac{1}{0.7639} \approx 1.3090 > 0$$.
   - $$u_2^*(1) = \frac{1}{1 \cdot (4 - x^*(1))} = \frac{1}{3.2361} \approx 0.3090 > 0$$.
2. **Kiểm tra điều kiện dừng của bài toán gốc:**
   $$\nabla f(x^*) + u_1^* \nabla h_1 + u_2^* \nabla h_2 = 1 + 1.3090(-1) + 0.3090(+1) = 1 - 1.3090 + 0.3090 = 0!$$
   Điều kiện dừng của hàm Lagrange gốc thỏa mãn chính xác!
3. **Tính hàm đối ngẫu $$g(u^*(1))$$ và kiểm tra khoảng cách đối ngẫu:**
   $$g(u^*(1)) = L(x^*(1), u^*(1)) = x^*(1) + u_1^*(1)(-x^*(1)) + u_2^*(1)(x^*(1) - 4) = 0.7639 - 1 - 1 = -1.2361.$$
   Khoảng cách đối ngẫu:
   $$f(x^*(1)) - g(u^*(1)) = 0.7639 - (-1.2361) = 2.0000 = \frac{m}{t} = \frac{2}{1}!$$
   Và sai số thật $$f(x^*(1)) - f^* = 0.7639 \le 2.0$$!

---

Trong mục này, ta đối chiếu các điều kiện KKT của bài toán chắn với điều kiện KKT của bài toán ban đầu để thấy rõ mối liên hệ giữa chúng, đồng thời dẫn xuất cận cho khoảng cách dưới tối ưu (suboptimality gap) giữa hai nghiệm.
