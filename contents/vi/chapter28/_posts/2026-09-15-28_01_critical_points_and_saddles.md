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


Cho $$F:\mathbb{R}^d\to\mathbb{R}$$ khả vi hai lần liên tục. Điểm $$w$$ là **tới hạn** nếu $$\nabla F(w)=0$$. Hessian $$H=\nabla^2 F(w)$$ phân loại điểm tới hạn *khi không suy biến* (không trị riêng 0):

- **Cực tiểu địa phương chặt:** $$H\succ 0$$ (mọi trị riêng dương).
- **Cực đại địa phương chặt:** $$H\prec 0$$.
- **Yên ngựa chặt:** $$H$$ không xác định — ít nhất một trị riêng dương và một âm.

Nếu một số trị riêng triệt tiêu, kiểm định không kết luận (nghĩ $$w\mapsto w^3$$ hoặc cao nguyên). Loss sâu đầy hướng gần suy biến.

**Phương pháp bậc nhất không nhìn thấy $$H$$**, nhưng câu chuyện Taylor địa phương vẫn giải thích hành vi: theo hướng độ cong âm $$u$$, $$F(w+t u)\approx F(w)+\tfrac12 t^2 u^\top H u$$ *giảm* với $$t\neq 0$$ nhỏ. Yên ngựa không phải bẫy với thuật toán có thể đi theo hướng đó; nó là bẫy với thuật toán chỉ nhìn $$\|\nabla F\|$$ nhỏ rồi dừng.

Ở chiều cao, nếu trị riêng của một Hessian “điển hình” tại điểm tới hạn ứng xử như ma trận đối xứng ngẫu nhiên, xác suất *mọi* trị riêng dương nhỏ hàm mũ. Định lý dân gian cần nhớ: **hầu hết điểm tới hạn của hàm generic chiều cao là yên ngựa, không phải cực tiểu**. Loss học sâu không phải Gaussian generic — nhưng trực giác đó giải thích vì sao “kẹt cực tiểu địa phương” thường là chẩn đoán sai sau epoch 2.

**Bài tập.** Với $$F(x,y)=x^2-y^2$$ (paraboloid hyperbolic) viết $$\nabla F$$ và $$H$$. Xuất phát từ $$(0,10^{-3})$$, lấy hai bước gradient. Xuất phát từ $$(0,0)$$, giải thích vì sao GD số học chính xác không bao giờ rời.
