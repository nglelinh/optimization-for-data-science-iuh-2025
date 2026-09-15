---
layout: post
title: 26-02 Momentum và tăng tốc Nesterov
chapter: '26'
order: 3
owner: Nguyen Le Linh
categories:
- chapter26
lang: vi
lesson_type: required
---


Gradient descent trên toàn phương điều kiện xấu đi zíc-zac: bước an toàn với trị riêng sắc thì quá nhỏ theo phương phẳng. **Momentum** giữ một vận tốc tích các thành phần gradient nhất quán và triệt các thành phần dao động.

**Heavy ball Polyak** (1964) dùng hệ thức trông như không ma sát

$$
\begin{align}
v_{k+1} &= \beta v_k + \nabla F(w_k), \\
w_{k+1} &= w_k - \eta v_{k+1},
\end{align}
$$

với $$\beta\in[0,1)$$ (`SGD(momentum=…)` của PyTorch thuộc họ này, tùy gradient được nhân trước hay sau khi trộn).

**Tăng tốc Nesterov** tính gradient tại điểm *nhìn trước*:

$$
\begin{align}
v_{k+1} &= \beta v_k + \nabla F(w_k - \eta \beta v_k), \\
w_{k+1} &= w_k - \eta v_{k+1}.
\end{align}
$$

Trên bài toán lồi trơn, phương pháp Nesterov đạt tốc độ bậc nhất tối ưu $$O(1/T^2)$$ cho giá trị hàm (xem FISTA ở Chương 09). Trên mạng sâu bức tranh là thực nghiệm: $$\beta$$ lớn ($$0.9$$, đôi khi $$0.99$$) là bộ lọc thông thấp nhận biết độ cong, không phải định lý để trích dẫn cho ResNet.

Hình ảnh lớp học tốt nhất vẫn là Goh, *[Why Momentum Really Works](http://distill.pub/2017/momentum)* (Distill, 2017). Ghép với thí nghiệm tư duy thung lũng toàn phương: không momentum bạn nảy tường; có momentum bạn tích tốc theo hành lang.

<div class="content-box insight-box">
<strong>Lý thuyết ≠ thực hành.</strong> Chứng minh Nesterov cần $$\beta_k$$ lên lịch cẩn thận và $$F$$ lồi trơn. “Nesterov” trong học sâu thường là look-ahead $$\beta$$ hằng trên mất mát không lồi. Dùng chứng minh để hiểu <em>vì sao</em> nhìn trước làm giảm dao động, không phải để đoán accuracy CIFAR.
</div>

**Bài tập.** Cài heavy-ball và Nesterov trên $$F(w)=\tfrac12 w^\top \operatorname{diag}(1,100)\,w$$. Vẽ hai quỹ đạo từ cùng điểm xuất phát. $$\beta$$ nào bắt đầu hết zíc-zac nhìn thấy?
