---
layout: post
title: 28-01 Điểm tới hạn và yên ngựa
chapter: '28'
order: 2
owner: Nguyen Le Linh
categories:
- chapter28
lang: vi
lesson_type: required
---


Cho hàm $$F:\mathbb{R}^d\to\mathbb{R}$$ khả vi hai lần liên tục. Điểm $$w$$ là **điểm tới hạn (critical point)** nếu $$\nabla F(w)=0$$. Khi ma trận Hessian $$H=\nabla^2 F(w)$$ không suy biến (không có trị riêng bằng 0), ta phân loại $$w$$ như sau:

* **Cực tiểu địa phương chặt:** $$H\succ 0$$ (mọi trị riêng đều dương).
* **Cực đại địa phương chặt:** $$H\prec 0$$ (mọi trị riêng đều âm).
* **Điểm yên ngựa chặt (strict saddle):** $$H$$ không xác định dấu — có ít nhất một trị riêng dương và một trị riêng âm.

Nếu tồn tại trị riêng bằng 0, kiểm định bậc hai chưa đủ để kết luận (ví dụ hàm $$w\mapsto w^3$$ hoặc các vùng cao nguyên phẳng). Hàm mất mát của mạng nơ-ron sâu thường chứa rất nhiều phương gần suy biến.

Mặc dù **các phương pháp bậc nhất không tính trực tiếp $$H$$**, khai triển Taylor bậc hai cục bộ vẫn cho thấy hành vi tại điểm yên ngựa: dọc theo một phương $$u$$ có độ cong âm ($$u^\top H u < 0$$), giá trị $$F(w+t u)\approx F(w)+\tfrac12 t^2 u^\top H u$$ *giảm* với $$t\neq 0$$ đủ nhỏ. Do đó, điểm yên ngựa chặt không phải là cái bẫy đối với thuật toán có thể dịch chuyển theo phương độ cong âm, mà chỉ gây dừng sớm cho các thuật toán chỉ kiểm tra điều kiện $$\|\nabla F\| \approx 0$$.

Trong không gian nhiều chiều, nếu dấu các trị riêng của ma trận Hessian tại một điểm tới hạn bất kỳ ứng xử tương tự ma trận đối xứng ngẫu nhiên, xác suất để *tất cả* $$d$$ trị riêng đều dương giảm theo hàm mũ của $$d$$. Nhận xét định tính quan trọng cần nhớ là: **với các hàm tổng quát nhiều chiều, đa số điểm tới hạn là điểm yên ngựa chứ không phải cực tiểu địa phương**. Dù hàm mất mát học sâu không hoàn toàn giống hàm ngẫu nhiên Gaussian, trực giác này giải thích vì sao tình trạng chậm tiến triển khi huấn luyện thường liên quan đến điểm yên ngựa và vùng phẳng hơn là bị mắc kẹt ở một cực tiểu địa phương xấu.

**Bài tập.** Xét hàm yên ngựa $$F(x,y)=x^2-y^2$$: hãy viết $$\nabla F$$ và ma trận Hessian $$H$$. Thực hiện hai bước gradient descent xuất phát từ $$(0, 10^{-3})$$, sau đó giải thích vì sao nếu xuất phát chính xác từ $$(0, 0)$$ thì gradient descent lý tưởng sẽ không bao giờ rời khỏi điểm đó.
