---
layout: post
title: '06-01-05 Tại sao Kích thước Bước lại Quan trọng?'
chapter: '06'
order: 6
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

Trong gradient descent, chọn đúng kích thước bước $$t$$ rất quan trọng. Nhưng tại sao? Câu trả lời nằm ở việc hiểu gradient descent thực sự đang làm gì: **nó đang đưa ra một giả định đơn giản về độ cong của hàm số**.

## Ý tưởng Cốt lõi

Khi chúng ta thực hiện gradient descent:
>$$x^{(k+1)} = x^{(k)} - t \nabla f(x^{(k)})$$

Thực ra chúng ta đang giải bài toán này:
>$$x^{(k+1)} = \arg\min_y \left\{ \nabla f(x^{(k)})^T (y - x^{(k)}) + \frac{1}{2t} \|y - x^{(k)}\|^2 \right\}$$

**Điều này có nghĩa là gì?**
- Số hạng đầu: "Đi theo hướng dốc nhất"
- Số hạng thứ hai: "Nhưng đừng đi quá xa khỏi vị trí hiện tại"
- Tham số $$t$$ điều khiển sự cân bằng này

## Kích thước Bước = Tin tưởng vào Độ phẳng

Hãy nghĩ về kích thước bước theo cách này:
>$$t = \frac{1}{\text{bạn nghĩ hàm số cong đến mức nào}}$$

- **$$t$$ lớn**: "Tôi nghĩ hàm số khá phẳng ở đây" → thực hiện bước lớn
- **$$t$$ nhỏ**: "Tôi nghĩ hàm số rất cong ở đây" → thực hiện bước nhỏ, cẩn thận

## Ví dụ Đơn giản

Xét hai hàm:
1. **Hàm phẳng**: $$f(x_1, x_2) = \frac{1}{2}(x_1^2 + x_2^2)$$ 
2. **Hàm dốc**: $$f(x_1, x_2) = \frac{1}{2}(100x_1^2 + x_2^2)$$

Với hàm phẳng, bạn có thể dùng $$t = 1$$ (bước lớn).
Với hàm dốc, bạn cần $$t = 0.01$$ (bước nhỏ) để tránh vượt quá mục tiêu.

## Tại sao Điều này Hoạt động

Hãy xem tại sao điều này cho chúng ta công thức gradient descent.

Chúng ta muốn tối thiểu hóa:
>$$\nabla f(x)^T (y - x) + \frac{1}{2t} \|y - x\|^2$$

Lấy đạo hàm theo $$y$$ và đặt bằng không:
>$$\nabla f(x) + \frac{1}{t}(y - x) = 0$$

Giải theo $$y$$:
>$$y = x - t \nabla f(x)$$

Đó chính xác là cập nhật gradient descent! Số hạng $$\frac{1}{2t}$$ hoạt động như một "lò xo" kéo bạn về phía $$x$$, ngăn bạn thực hiện những bước quá lớn.

## Khi nào Hoạt động Tốt?

**Trường hợp tốt:**
- Hàm có độ "dốc" gần như nhau theo mọi hướng
- Hàm hình bát như $$f(x_1, x_2) = x_1^2 + x_2^2$$

**Trường hợp xấu:**  
- Hàm rất dốc theo một hướng nhưng phẳng theo hướng khác
- Hàm hình "thung lũng" như $$f(x_1, x_2) = 100x_1^2 + x_2^2$$

## Cách Chọn Kích thước Bước

**Quy tắc thực tế**: Bắt đầu với $$t = 0.1$$ và điều chỉnh:
- Nếu gradient descent dao động mạnh → làm $$t$$ nhỏ hơn
- Nếu gradient descent hội tụ rất chậm → làm $$t$$ lớn hơn
- Nếu bạn hiểu rõ hàm số → dùng $$t \approx \frac{2}{\text{hướng dốc nhất + hướng phẳng nhất}}$$

## Trực quan Hình ảnh

Hãy tưởng tượng bạn đang đi xuống một ngọn đồi trong bóng tối với đèn pin:

- **Kích thước bước lớn**: "Tôi nghĩ con đường phía trước mượt mà" → thực hiện bước dài (rủi ro: có thể bước vào hố)
- **Kích thước bước nhỏ**: "Tôi nghĩ con đường phía trước gồ ghề" → thực hiện bước nhỏ (an toàn nhưng chậm)

Gradient descent làm điều tương tự về mặt toán học!

## Bức tranh Tổng thể

**Gradient descent thực sự làm gì:**
1. Nhìn vào độ dốc (gradient) 
2. Giả định hàm số có dạng "bát" xung quanh bạn
3. Thực hiện một bước về phía đáy của cái bát tưởng tượng đó
4. Lặp lại

**Tại sao kích thước bước quan trọng:**
- Quá lớn → bạn vượt quá mục tiêu và nảy qua nảy lại
- Quá nhỏ → bạn mất mãi mới đến đích  
- Vừa phải → hội tụ mượt mà, nhanh chóng

## Điểm Mấu chốt

Kích thước bước không phải ma thuật - nó là **phỏng đoán của bạn về độ cong của hàm số**:
- $$t = 0.01$$ có nghĩa là "Tôi nghĩ hàm này rất cong"
- $$t = 1.0$$ có nghĩa là "Tôi nghĩ hàm này khá phẳng"

Phỏng đoán càng chính xác, gradient descent hội tụ càng nhanh!