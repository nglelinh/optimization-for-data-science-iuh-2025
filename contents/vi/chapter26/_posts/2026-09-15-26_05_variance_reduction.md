---
layout: post
title: 26-05 Giảm phương sai (khảo sát)
chapter: '26'
order: 6
owner: Nguyen Le Linh
categories:
- chapter26
lang: vi
lesson_type: required
---


Trần $$O(1/\sqrt{T})$$ của SGD trên tổng hữu hạn lồi không phải định mệnh lý thuyết thông tin. Nếu mỗi $$f_i$$ trơn, các phương pháp **giảm phương sai** tái sử dụng gradient cũ để ước lượng đúng tại một ảnh chụp, và nhiễu tắt khi $$w$$ tiến tới cực tiểu.

**SVRG** (Johnson & Zhang, 2013) giữ ảnh chụp $$\tilde w$$ và gradient đầy đủ $$\mu=\nabla F(\tilde w)$$, rồi bước

$$
g_k = \nabla f_{I_k}(w_k) - \nabla f_{I_k}(\tilde w) + \mu.
$$

Tại $$w_k=\tilde w$$ ta có $$g_k=\nabla F(\tilde w)$$ chính xác. Định kỳ làm mới ảnh chụp (một lượt đầy đủ). **SAGA** (Defazio, Bach, Lacoste-Julien, 2014) lưu bảng gradient gần nhất của mỗi $$f_i$$ và cập nhật một hàng mỗi bước — tốn bộ nhớ hơn, không vòng trong tường minh.

Với bài toán *tổng hữu hạn lồi mạnh*, các phương pháp này có thể hội tụ tuyến tính theo số bước gia lượng, điều SGD thuần không làm được. Với **mạng sâu**, lưu bảng gradient thường vô vọng, và người thắng thực nghiệm vẫn là Adam(W) batch lớn cộng lịch. Học SVRG để đọc được ghi chú Opt-for-ML (MIT, BU EC525) và để nhận ra khi một ERM *lồi* (hồi quy logistic, SVM tuyến tính) *không* nên huấn luyện bằng Adam theo thói quen.

**Tóm một trang**

| Phương pháp | Bộ nhớ thêm | Nhà thường trú |
|-------------|-------------|----------------|
| SGD / mini-batch | không | học sâu |
| SVRG | một snapshot + gradient đầy đủ | tổng hữu hạn lồi |
| SAGA | một gradient mỗi mẫu | ERM lồi vừa |
| AdamW | hai EMA | DL mặc định |

**Bài tập.** Trên ridge-logistic lồi mạnh với $$n=5000$$, so thời gian tường của SVRG và SGD để đạt chuẩn gradient huấn luyện $$10^{-4}$$. Rồi thử cùng ngân sách trên mạng một tầng ẩn — chi phí snapshot của SVRG sẽ kém duyên hơn.
