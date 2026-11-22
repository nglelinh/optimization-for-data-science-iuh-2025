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

Trong hầu hết các thuật toán tối ưu hóa, mỗi bước lặp đều thao tác trên vector, mỗi ràng buộc tuyến tính là một tích ma trận–vector, và độ cong cục bộ được mô tả qua các giá trị riêng của ma trận Hessian hoặc ma trận Gram. Trang này giới thiệu tổng quan cho ba bài đại số tuyến tính tiếp theo.

## Các đối tượng sử dụng xuyên suốt khóa học

- **Vector và tích trong.** Hình học Euclid $$\langle g, d\rangle = g^\top d$$ quyết định $$d$$ có phải hướng giảm hay không ($$g^\top d < 0$$). Các hình học khác (Mahalanobis, ánh xạ gương) sẽ xuất hiện ở phần sau dưới dạng tiền điều kiện và chuẩn đối ngẫu (Chương 13).
- **Ma trận như ánh xạ tuyến tính.** Ràng buộc đẳng thức $$Ax = b$$ xác định một không gian affine; hạt nhân (kernel) của $$A$$ là không gian các hướng bước khả thi. Bài toán bình phương tối thiểu (Chương 05) giải hệ $$A^\top A \hat{x} = A^\top y$$ khi $$A$$ đủ hạng cột.
- **Giá trị riêng và dạng toàn phương.** Nếu $$Q\succeq 0$$ thì hàm $$x\mapsto x^\top Q x$$ là hàm lồi; số điều kiện $$\kappa = \lambda_{\max}(Q)/\lambda_{\min}(Q)$$ của một hàm toàn phương lồi mạnh chính là yếu tố làm chậm gradient descent thuần và là động lực cho các phương pháp tăng tốc (Chương 06, 09, 26).

Mọi ma trận đối xứng $$Q$$ đều chéo hóa trực giao được dưới dạng $$Q = U\Lambda U^\top$$. Thương Rayleigh

$$
\lambda_{\min}(Q) = \min_{\|x\|_2=1} x^\top Q x, \qquad \lambda_{\max}(Q) = \max_{\|x\|_2=1} x^\top Q x
$$

là cách trực quan nhất để xác định các hằng số lồi mạnh và độ trơn.

## Các bài trong phần này

1. Vector và không gian vector
2. Ma trận và phép biến đổi tuyến tính
3. Giá trị riêng và vector riêng

Tự kiểm tra: hãy giải thích trong một câu vì sao điều kiện $$\nabla^2 f(x)\succeq 0$$ tại mọi điểm kéo theo hàm $$f$$ khả vi hai lần là hàm lồi. (Chương 03 sẽ chứng minh đầy đủ; đại số tuyến tính giúp ta hiểu rõ ý nghĩa của mệnh đề này.)
