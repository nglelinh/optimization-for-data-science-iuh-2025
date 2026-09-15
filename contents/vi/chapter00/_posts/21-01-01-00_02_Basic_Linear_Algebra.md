---
layout: post
title: 00-02 Đại số tuyến tính cơ bản
chapter: '00'
order: 7
owner: GitHub Copilot
lang: vi
categories:
- chapter00
lesson_type: required
---

Hầu hết mọi vòng lặp tối ưu là một vector, mọi ràng buộc tuyến tính là tích ma trận–vector, và mọi câu chuyện độ cong địa phương là trị riêng của Hessian hoặc ma trận Gram. Trang này định hướng ba bài đại số tuyến tính phía sau.

## Các đối tượng dùng cả học kỳ

- **Vector và tích trong.** Hình học Euclid $$\langle g, d\rangle = g^\top d$$ quyết định $$d$$ có phải hướng giảm ($$g^\top d < 0$$). Các hình học khác (Mahalanobis, mirror map) xuất hiện sau như tiền điều kiện và chuẩn đối ngẫu (Chương 13).
- **Ma trận như ánh xạ tuyến tính.** Đẳng thức $$Ax = b$$ cắt một không gian affine; hạt nhân của $$A$$ là tập bước khả thi. Bình phương tối thiểu (Chương 05) giải $$A^\top A \hat{x} = A^\top y$$ khi $$A$$ đủ hạng cột.
- **Trị riêng và dạng toàn phương.** Nếu $$Q\succeq 0$$ thì $$x\mapsto x^\top Q x$$ lồi; số điều kiện $$\kappa = \lambda_{\max}(Q)/\lambda_{\min}(Q)$$ của một toàn phương lồi mạnh chính là đại lượng làm chậm gradient descent thuần và thúc đẩy tăng tốc (Chương 06, 09, 26).

Ma trận đối xứng $$Q$$ chéo hóa trực giao $$Q = U\Lambda U^\top$$. Thương Rayleigh

$$
\lambda_{\min}(Q) = \min_{\|x\|_2=1} x^\top Q x, \qquad \lambda_{\max}(Q) = \max_{\|x\|_2=1} x^\top Q x
$$

là cách sạch nhất để *nhìn thấy* các hằng số lồi mạnh và trơn.

## Các bài trong khối này

1. Vector và không gian vector
2. Ma trận và biến đổi tuyến tính
3. Trị riêng và vector riêng

Điểm kiểm: giải thích trong một câu vì sao $$\nabla^2 f(x)\succeq 0$$ mọi nơi kéo theo hàm $$f$$ khả vi hai lần là lồi. (Chương 03 sẽ chứng minh; đại số tuyến tính làm cho mệnh đề có nghĩa.)
