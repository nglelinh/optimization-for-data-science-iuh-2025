---
layout: post
title: 28-03 Quá tham số
chapter: '28'
order: 4
owner: Nguyen Le Linh
categories:
- chapter28
lang: vi
lesson_type: required
---


Mô hình **quá tham số** khi số tham số $$d$$ vượt rõ số ràng buộc hiệu dụng từ dữ liệu (cổ điển $$d \gg n$$ để nội suy $$n$$ nhãn vô hướng). Khi đó phương trình $$F(w)=0$$ (hoặc “train loss $$\approx 0$$”) có thể có một **tập nghiệm khổng lồ**. Huấn luyện không còn là “tìm cực tiểu duy nhất”; mà là “thuật toán chọn bộ nội suy nào?”

Đó là góc nhìn thiên kiến ẩn: gradient descent trên bình phương tối thiểu thiếu xác định hội tụ về bộ nội suy **chuẩn nhỏ nhất** trong bao của đặc trưng; trên phân loại tuyến tính tách được, nó cực đại hóa lề trong giới hạn (Soudry et al., và một văn liệu nối tiếp lớn). Mạng sâu không tuyến tính, nhưng khẩu hiệu vẫn: **bộ tối ưu là một phần của thiên kiến quy nạp**.

Quá tham số cũng đổi *hình* của $$F$$. Trong nhiều giới hạn đặc trưng ngẫu nhiên và mạng rộng, loss trở nên lành *địa phương*: một khi đủ gần, mọi điểm tới hạn mà SGD tìm thấy đều nội suy, và yên ngựa kém quan trọng hơn việc bạn đáp **điểm nội suy nào**. Đó là vì sao “không lồi ⇒ cực tiểu địa phương vô dụng” là khẩu hiệu sai cho học sâu hiện đại, dù hàm vẫn không lồi.

**Điều kiện Polyak–Łojasiewicz (PL)** (con trỏ, không phải cả bài). Nếu

$$
\tfrac12 \|\nabla F(w)\|_2^2 \ge \mu \bigl(F(w)-F^\star\bigr)
$$

với $$\mu>0$$ nào đó, thì gradient descent có tốc độ tuyến tính *không cần lồi*. Một số bình phương tối thiểu quá tham số và một số chế độ mạng rộng thỏa PL địa phương. Karimi, Nutini, Schmidt ([arXiv:1608.04636](https://arxiv.org/abs/1608.04636)) là ghi chú để đọc khi muốn tái sử dụng chứng minh Chương 06 trên ERM không lồi.

**Bài tập.** Khớp $$n=20$$ điểm vô hướng bằng đa thức bậc $$50$$ theo (i) nghiệm chuẩn-min của numpy và (ii) GD từ hai khởi tạo ngẫu nhiên. So lỗi kiểm trên một hàm gốc trơn. Cùng train loss, khác bộ nội suy.
