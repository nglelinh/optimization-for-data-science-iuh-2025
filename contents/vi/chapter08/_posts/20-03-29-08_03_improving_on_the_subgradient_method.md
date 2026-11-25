---
layout: post
title: '08-03 Cải tiến Phương pháp Subgradient'
chapter: '08'
order: 16
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---

Kết thúc hành trình Chương 08, ta mang theo một cảm giác vừa phấn khởi vừa tiếc nuối. Phấn khởi vì phương pháp subgradient giải được mọi bài toán lồi không trơn chỉ với một dòng cập nhật duy nhất; nhưng tiếc nuối vì rào cản tốc độ $$O(1/\epsilon^2)$$ quá chậm — muốn thêm một chữ số chính xác phải trả giá bằng 100 lần số vòng lặp!

Câu hỏi lớn mở ra cánh cửa sang Chương 09 là: *có phải ta đang lãng phí thông tin không?* Hãy nhìn lại bài toán Lasso $$\frac{1}{2}\|y - X\beta\|_2^2 + \lambda\|\beta\|_1$$ hay hồi quy logistic có điều chuẩn $$\ell_1$$. Chúng đâu có "xấu xí không trơn ở khắp mọi nơi"! Thực ra chúng là tổng của một hàm **rất đẹp, trơn mượt** $$g(x)$$ cộng với một hàm **không trơn nhưng cực kỳ đơn giản** $$h(x)$$. Phương pháp subgradient đối xử với cả hai như nhau — vứt bỏ hoàn toàn tính trơn của $$g(x)$$! Nếu biết tách riêng hai phần ấy ra, ta có thể kéo tốc độ hội tụ từ $$O(1/\epsilon^2)$$ nhảy vọt lên $$O(1/\epsilon)$$, và thậm chí $$O(1/\sqrt{\epsilon})$$ khi tăng tốc!

## Bản đồ kiến thức nền: Ba con đường vượt qua rào cản $$O(1/\epsilon^2)$$

- **Khai thác cấu trúc phân tách (Composite Structure $$f = g + h$$):** Thay vì dùng hộp đen subgradient cho toàn bộ $$f$$, ta dùng gradient $$\nabla g(x)$$ trên phần trơn và xử lý chính xác phần không trơn $$h(x)$$ bằng toán tử gần kề (proximal operator). Đây chính là nền tảng của **Proximal Gradient Descent (Chương 09)**, khôi phục tốc độ $$O(1/\epsilon)$$ và $$O(1/\sqrt{\epsilon})$$ (FISTA).
- **Làm trơn hóa có kiểm soát (Nesterov Smoothing):** Với một số hàm không trơn dạng $$\max_u (\langle Ax, u\rangle - \phi(u))$$, ta có thể cộng thêm số hạng điều chuẩn mạnh nhỏ $$\mu$$ để tạo xấp xỉ trơn $$f_\mu$$ có gradient Lipschitz $$O(1/\mu)$$, rồi chạy gradient tăng tốc để đạt tốc độ $$O(1/\epsilon)$$ thay vì $$O(1/\epsilon^2)$$.
- **Khai thác cấu trúc hình học phi Euclid (Mirror Descent & Bundle Methods):** Thay chuẩn Euclid bằng phân kỳ Bregman (ví dụ entropy âm trên đơn hình xác suất) giúp giảm mạnh hằng số chiều $$n$$ từ $$O(\sqrt{n})$$ xuống $$O(\sqrt{\ln n})$$; còn phương pháp bó (bundle methods) lưu lại nhiều siêu phẳng đỡ quá khứ để xấp xỉ hàm lồi tốt hơn nhiều so với chỉ giữ 1 subgradient hiện tại.

### Khung giải thích (nên đọc chậm): Một phép thử tính tay cho thấy vì sao "tách cấu trúc" thắng áp đảo subgradient

Xét bài toán tối ưu tổng hợp 1D:
$$\min_{x \in \mathbb{R}} \; f(x) = \underbrace{\frac{1}{2}(x - 3)^2}_{g(x)\text{ trơn, }L=1} + \underbrace{|x|}_{h(x)\text{ không trơn}}.$$
Nghiệm tối ưu chính xác là $$x^* = 2$$ (vì $$g'(2) + h'(2) = (2 - 3) + 1 = 0$$), với $$f^* = 0.5 + 2 = 2.5$$. Xuất phát từ $$x^{(0)} = 0$$ ($$f(0) = 4.5$$).

1. **Nếu chạy phương pháp subgradient (coi cả $$f$$ là hộp đen không trơn) với bước $$t = 0.5$$:**
   - Bước 1: tại $$x^{(0)} = 0$$, $$g^{(0)} = -3 + 0 = -3 \implies x^{(1)} = 0 - 0.5(-3) = 1.5$$ ($$f(1.5) = 1.125 + 1.5 = 2.625$$).
   - Bước 2: tại $$x^{(1)} = 1.5$$, $$g^{(1)} = -1.5 + 1 = -0.5 \implies x^{(2)} = 1.5 - 0.5(-0.5) = 1.75$$ ($$f(1.75) = 2.53125$$).
   - Bước 3: $$x^{(3)} = 1.875$$... Càng gần $$x^*=2$$, phải chạy nhiều bước (và nếu $$x^* = 0$$, subgradient sẽ dao động qua lại mãi quanh $$0$$ mà không bao giờ đặt chính xác $$x = 0$$!).
2. **Nếu tách cấu trúc (Proximal Gradient, Chương 09) với bước $$t = 1/L = 1$$:**
   - Bước gradient trên phần trơn $$g$$: $$z = x^{(0)} - 1 \cdot g'(0) = 0 - (-3) = 3$$.
   - Áp dụng toán tử co ngưỡng mềm (prox của $$|x|$$ với ngưỡng $$t = 1$$):
     $$x^{(1)} = \operatorname{sign}(3)\max(|3| - 1, 0) = 2.0 = x^*!$$
   Chạm đúng nghiệm tối ưu trong **đúng 1 bước duy nhất**! Đó chính là sức mạnh của việc tôn trọng cấu trúc toán học thay vì coi hàm là hộp đen.

Phương pháp subgradient có ưu điểm là áp dụng được cho các hàm lồi không khả vi, nên có phạm vi sử dụng rộng hơn gradient descent. Tuy nhiên, tốc độ hội tụ $$O(1/\epsilon^{2})$$ của nó chậm hơn nhiều so với tốc độ $$O(1/\epsilon)$$ của gradient descent.

Liệu có thể kết hợp ưu điểm của cả hai phương pháp không? Trong chương tiếp theo, chúng ta sẽ tìm hiểu **phương pháp gradient gần kề (proximal gradient descent)**, giúp giữ được tốc độ hội tụ tốt trên lớp bài toán tổng hợp có thành phần không khả vi.