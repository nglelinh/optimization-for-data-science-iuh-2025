---
layout: post
title: '06-01-05 Tại sao Kích thước Bước lại Quan trọng?'
chapter: '06'
order: 3
owner: AI Assistant
categories:
- chapter06
lang: vi
lesson_type: supplementary
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

Trong gradient descent, việc chọn kích thước bước $$t$$ phù hợp có ý nghĩa rất quan trọng. Lý do nằm ở bản chất hình học của thuật toán: **gradient descent ngầm đặt một giả định đơn giản về độ cong của hàm mục tiêu**.

## Ý tưởng Cốt lõi

Khi thực hiện cập nhật gradient descent:
>$$x^{(k+1)} = x^{(k)} - t \nabla f(x^{(k)})$$

thực chất ta đang giải bài toán tối ưu cục bộ sau:
>$$x^{(k+1)} = \arg\min_y \left\{ \nabla f(x^{(k)})^T (y - x^{(k)}) + \frac{1}{2t} \|y - x^{(k)}\|^2 \right\}$$

**Ý nghĩa của từng thành phần:**
- Số hạng thứ nhất thúc đẩy di chuyển theo hướng giảm dốc nhất.
- Số hạng thứ hai phạt các bước nhảy quá xa khỏi vị trí hiện tại $$x^{(k)}$$.
- Tham số $$t$$ điều chỉnh sự cân bằng giữa hai xu hướng này.

## Kích thước Bước và Ước lượng Độ cong

Có thể hình dung kích thước bước theo mối quan hệ nghịch đảo với độ cong ước lượng của hàm số:
>$$t = \frac{1}{\text{độ cong ước lượng của hàm số}}$$

- **$$t$$ lớn**: Tương ứng với giả định hàm số tương đối phẳng tại vùng lân cận, cho phép thực hiện bước dài.
- **$$t$$ nhỏ**: Tương ứng với giả định hàm số cong mạnh tại vùng lân cận, buộc thuật toán thực hiện các bước ngắn và thận trọng hơn.

## Ví dụ Minh họa

Xét hai hàm bậc hai:
1. **Hàm phẳng (đẳng hướng)**: $$f(x_1, x_2) = \frac{1}{2}(x_1^2 + x_2^2)$$
2. **Hàm dốc (dị hướng)**: $$f(x_1, x_2) = \frac{1}{2}(100x_1^2 + x_2^2)$$

Với hàm thứ nhất, ta có thể chọn $$t = 1$$ (bước lớn). Với hàm thứ hai, ta cần chọn $$t = 0.01$$ (bước nhỏ) để tránh vượt quá điểm cực tiểu theo phương $$x_1$$.

## Suy ra Quy tắc Cập nhật

Để cực tiểu hóa biểu thức bậc hai:
>$$\nabla f(x)^T (y - x) + \frac{1}{2t} \|y - x\|^2$$

ta lấy đạo hàm theo $$y$$ và đặt bằng 0:
>$$\nabla f(x) + \frac{1}{t}(y - x) = 0$$

Giải phương trình theo $$y$$ thu được:
>$$y = x - t \nabla f(x)$$

Đây chính là công thức cập nhật của gradient descent. Hệ số $$\frac{1}{2t}$$ hoạt động như một lực đàn hồi kéo $$y$$ về gần $$x$$, hạn chế các bước nhảy quá lớn.

## Khi nào Gradient Descent Hoạt động Hiệu quả?

**Trường hợp thuận lợi:**
- Hàm số có độ cong tương đương nhau theo mọi hướng.
- Ví dụ: hàm có dạng hình bát tròn như $$f(x_1, x_2) = x_1^2 + x_2^2$$.

**Trường hợp kém thuận lợi:**
- Hàm số rất dốc theo một hướng nhưng lại rất phẳng theo hướng khác.
- Ví dụ: hàm có dạng thung lũng hẹp như $$f(x_1, x_2) = 100x_1^2 + x_2^2$$.

## Nguyên tắc Chọn Kích thước Bước

**Quy tắc thực hành**: Có thể bắt đầu thử từ $$t = 0.1$$ và điều chỉnh theo hành vi hội tụ:
- Nếu quá trình lặp dao động mạnh: giảm $$t$$.
- Nếu quá trình lặp hội tụ quá chậm: tăng $$t$$.
- Nếu biết rõ độ cong lớn nhất và nhỏ nhất của hàm số: chọn $$t \approx \frac{2}{\text{độ cong lớn nhất} + \text{độ cong nhỏ nhất}}$$.

## Trực quan Hình học

Hãy hình dung việc đi xuống một sườn đồi trong bóng tối với ánh đèn pin hạn chế:

- **Kích thước bước lớn**: Khi giả định địa hình phía trước bằng phẳng, ta bước dài hơn (nhưng có rủi ro bước hụt nếu địa hình thay đổi đột ngột).
- **Kích thước bước nhỏ**: Khi giả định địa hình gồ ghề, ta bước ngắn hơn (an toàn nhưng tốn nhiều thời gian).

Gradient descent vận hành theo cơ chế tương tự về mặt toán học.

## Tóm tắt Quy trình

**Cơ chế của gradient descent:**
1. Tính độ dốc cục bộ (gradient).
2. Xấp xỉ hàm số quanh điểm hiện tại bằng một mặt bậc hai dạng hình bát.
3. Di chuyển tới đáy của mặt bậc hai xấp xỉ đó.
4. Lặp lại cho đến khi hội tụ.

**Tác động của kích thước bước:**
- Quá lớn: vượt quá điểm cực tiểu và dao động hoặc phân kỳ.
- Quá nhỏ: tiến độ hội tụ rất chậm.
- Phù hợp: hội tụ nhanh và ổn định.

## Điểm Mấu chốt

Kích thước bước phản ánh **ước lượng của ta về độ cong cục bộ của hàm mục tiêu**:
- $$t = 0.01$$ tương ứng với hàm có độ cong rất lớn.
- $$t = 1.0$$ tương ứng với hàm tương đối phẳng.

Ước lượng độ cong càng sát với thực tế, gradient descent hội tụ càng nhanh.