---
layout: post
title: '08-01 Phương pháp Subgradient'
chapter: '08'
order: 2
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---

Nếu bạn đã quen với gradient descent, phản xạ tự nhiên nhất khi gặp bài toán không trơn là: "Thay $$\nabla f$$ bằng một subgradient $$g \in \partial f$$ là ta có ngay *subgradient descent*, đúng không?" Câu trả lời khiến hầu hết người học tối ưu lần đầu đều bất ngờ: **không có từ "descent" ở đây**. Phương pháp này chỉ được gọi là *phương pháp subgradient* (subgradient method), và việc bỏ đi một chữ ấy chứa đựng cả một bài học hình học sâu sắc.

Tại sao hướng âm của một subgradient lại có thể đưa bạn *leo ngược lên dốc* ngay cả khi kích thước bước nhỏ tùy ý? Bởi vì subgradient chỉ là pháp tuyến của một siêu phẳng đỡ nằm dưới mặt cong lồi — nó đảm bảo góc nhọn với vector hướng về nghiệm $$x^*$$, chứ không đảm bảo độ dốc theo hướng $$-g$$ là âm dọc theo mọi cạnh gãy của đồ thị. Vì vậy, muốn thuật toán vận hành tin cậy, ta phải theo dõi kỷ lục tốt nhất $$f_{\text{best}}^{(k)} = \min_{i \le k} f(x^{(i)})$$ thay vì chỉ nhìn vào điểm cuối $$x^{(k)}$$.

## Bản đồ kiến thức nền: Ba trực giác định nghĩa phương pháp subgradient

Để đọc công thức cập nhật $$x^{(k)} = x^{(k-1)} - t_k g^{(k-1)}$$ mà thấy ngay chuyển động hình học phía sau, hãy nắm chắc ba nhánh sau:

- **Siêu phẳng đỡ và nón pháp tuyến:** Bất đẳng thức $$f(y) \ge f(x) + g^T(y-x)$$ nói rằng khi đặt $$y = x^*$$, ta luôn có $$g^T(x - x^*) \ge f(x) - f(x^*) \ge 0$$. Nghĩa là $$-g$$ luôn tạo góc tù (hoặc vuông) với $$x - x^*$$ — tức là nó *luôn* chỉ về nửa không gian chứa nghiệm tối ưu $$x^*$$.
- **Sự khác biệt giữa hướng giảm hàm và hướng giảm khoảng cách:** Với hàm khả vi, $$-\nabla f(x)$$ vừa làm giảm $$f(x)$$ vừa kéo gần $$x^*$$. Với hàm không trơn, $$-g$$ chỉ bảo toàn tính chất thứ hai (giảm khoảng cách $$\|x - x^*\|_2$$ khi bước đủ nhỏ), còn giá trị hàm $$f(x)$$ có thể tăng lên ngay lập tức.
- **Kỷ lục tốt nhất (Best Iterate Tracking):** Vì chuỗi $$f(x^{(0)}), f(x^{(1)}), \dots$$ có thể nhấp nhô lên xuống như răng cưa, đầu ra thực tế của thuật toán là $$x_{\text{best}}^{(k)} = \arg\min_{0 \le i \le k} f(x^{(i)})$$. Toàn bộ các định lý hội tụ của chương này đều phát biểu cho $$f_{\text{best}}^{(k)} - f^*$$.

### Khung giải thích (nên đọc chậm): Ví dụ tính tay chứng minh $$-g$$ làm hàm tăng nhưng vẫn kéo gần $$x^*$$

Xét hàm lồi không trơn hai biến $$f(x_1, x_2) = 3|x_1| + |x_2|$$, có nghiệm tối ưu duy nhất $$x^* = (0, 0)$$ với $$f^* = 0$$.

1. **Chọn điểm xuất phát trên sống gãy:** Lấy $$x^{(0)} = (0, 1)$$, giá trị hàm là $$f(0, 1) = 3(0) + 1 = 1$$, khoảng cách bình phương tới nghiệm là $$\|x^{(0)} - x^*\|_2^2 = 0^2 + 1^2 = 1$$.
2. **Tìm một subgradient hợp lệ:** Tại $$x_1 = 0$$, $$\partial (3|x_1|)\big|_{0} = [-3, 3]$$; tại $$x_2 = 1$$, đạo hàm của $$|x_2|$$ là $$1$$. Vậy $$g^{(0)} = (3, 1)$$ là một subgradient hoàn toàn hợp lệ trong $$\partial f(0, 1)$$.
3. **Đi một bước nhỏ tùy ý $$t \in (0, 1)$$ theo hướng $$-g^{(0)} = (-3, -1)$$:**
   $$x^{(1)} = (0, 1) - t(3, 1) = (-3t, 1 - t).$$
   Tính giá trị hàm mới:
   $$f(x^{(1)}) = 3|-3t| + |1 - t| = 9t + (1 - t) = 1 + 8t > 1 = f(x^{(0)}).$$
   Dù chọn bước nhỏ tới đâu ($$t = 0.01$$ hay $$t = 10^{-6}$$), hàm $$f$$ **vẫn tăng**! Đây là bằng chứng rõ nhất vì sao $$-g^{(0)}$$ không phải hướng giảm.
4. **Kiểm tra khoảng cách bình phương tới nghiệm $$x^* = (0, 0)$$:**
   $$\|x^{(1)} - x^*\|_2^2 = (-3t)^2 + (1 - t)^2 = 1 - 2t + 10t^2.$$
   Với $$t = 0.1$$: $$f(x^{(1)}) = 1.8 > 1$$ (hàm tăng!), nhưng $$\|x^{(1)} - x^*\|_2^2 = 1 - 0.2 + 0.1 = 0.9 < 1$$ (khoảng cách tới nghiệm **giảm thật sự**!). Nhờ sự co lại của khoảng cách này mà phương pháp subgradient vẫn hội tụ.

Giả sử $$f$$ là một hàm lồi xác định trên $${R}^n$$ và có thể không khả vi tại một số điểm.

Phương pháp subgradient được xây dựng bằng cách thay thế gradient trong phương pháp gradient descent bằng một subgradient ($$\nabla f(x^{(k-1)}) \to g(x^{(k-1)})$$):

>$$ x^{(k)} = x^{(k-1)} - t_k \cdot g^{(k-1)}, \quad k = 1, 2, 3, . . . $$

trong đó $$g^{(k-1)} \in \partial f(x^{(k-1)})$$ là một subgradient của $$f$$ tại $$x^{(k-1)}$$.

## Vì sao gọi là "phương pháp subgradient" (chứ không phải "subgradient descent")

Khác với gradient descent, phương pháp subgradient không đảm bảo giá trị hàm mục tiêu luôn giảm sau mỗi bước lặp (do đó thuật toán không được gọi là "subgradient descent"). Vì vậy, trong quá trình chạy thuật toán, cần lưu lại giá trị tốt nhất đạt được tính đến bước hiện tại:

>$$f(x_{best}^{(k)}) = \min_{i=0,...k} f(x^{(i)})$$ 

Ở đây, $$f(x^{(k)}_{best})$$ ký hiệu giá trị nhỏ nhất của hàm $$f$$ thu được sau $$k$$ bước lặp.
