---
layout: post
title: '08-02 Phương pháp Subgradient Ngẫu nhiên'
chapter: '08'
order: 11
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---

Hãy hình dung bạn đang huấn luyện một bộ phân loại SVM tuyến tính trên 10 triệu văn bản. Phương pháp subgradient toàn phần (batch) đòi hỏi bạn phải đọc qua toàn bộ 10 triệu văn bản, cộng dồn 10 triệu vector subgradient, chỉ để thực hiện *đúng một bước nhích nhỏ* của vector trọng số! Trong khi đó, chỉ cần bốc ngẫu nhiên một (hoặc một lô nhỏ) văn bản thôi, hướng subgradient của nó tuy ồn ào nhưng trung bình lại chỉ đúng về hướng của cả tập dữ liệu.

Đó chính là bước nhảy tư duy của **phương pháp subgradient ngẫu nhiên (Stochastic Subgradient Method)** — cầu nối trực tiếp từ giải tích lồi không trơn sang trái tim của học máy quy mô lớn. Mục này giới thiệu khung tư tưởng chung trước khi ta đi sâu vào hai biến thể (chọn ngẫu nhiên và chọn tuần hoàn), định lý hội tụ, tốc độ hội tụ và sự đánh đổi thực chiến với phương pháp batch.

## Kiến thức cần nhớ: Ba trụ cột của tối ưu không trơn ngẫu nhiên

- **Bài toán tổng hữu hạn (Finite-sum Optimization):** Hàm mục tiêu có dạng $$f(x) = \sum_{i=1}^m f_i(x)$$ (hoặc trung bình $$\frac{1}{m}\sum_{i=1}^m f_i(x)$$) với $$m$$ rất lớn và từng $$f_i$$ lồi nhưng có thể không trơn (như mất mát hinge hay $$\ell_1$$).
- **Ước lượng không chệch của subgradient:** Nếu chọn chỉ số $$i_k$$ đều ngẫu nhiên từ $$\{1, \dots, m\}$$ và lấy $$g_{i_k} \in \partial f_{i_k}(x)$$, thì $$\mathbb{E}[m \, g_{i_k}] = \sum_{i=1}^m g_i \in \partial f(x)$$. Nhờ tính không chệch này, sai lệch ngẫu nhiên ở từng bước có kỳ vọng bằng $$0$$ và triệt tiêu dần khi cộng dồn.
- **Đánh đổi chi phí mỗi bước lấy nhiễu phương sai:** Chi phí mỗi vòng lặp giảm $$m$$ lần (từ $$O(mp)$$ xuống $$O(p)$$), nhưng bước cập nhật luôn kèm nhiễu phương sai nên yêu cầu bước giảm dần $$t_k \to 0$$ để đạt độ chính xác cao.

### Giải thích: Kiểm chứng ước lượng không chệch trên 4 mẫu mất mát hinge

Xét 4 điểm dữ liệu 1D có tổng mất mát trung bình $$f(w) = \frac{1}{4}\sum_{i=1}^4 \max(0, 1 - y_i x_i w)$$ với $$y_i x_i$$ lần lượt là $$+2, +1, -1, +2$$ tại $$w = 0.6$$.

1. **Tính subgradient từng mẫu tại $$w = 0.6$$:**
   - Mẫu 1 ($$1 - 1.2 = -0.2 < 0$$): $$g_1 = 0$$.
   - Mẫu 2 ($$1 - 0.6 = +0.4 > 0$$): $$g_2 = -1$$.
   - Mẫu 3 ($$1 - (-0.6) = +1.6 > 0$$): $$g_3 = +1$$.
   - Mẫu 4 ($$1 - 1.2 = -0.2 < 0$$): $$g_4 = 0$$.
2. **So sánh subgradient toàn phần (batch) và kỳ vọng subgradient ngẫu nhiên:**
   - Subgradient batch: $$g_{\text{batch}} = \frac{1}{4}(0 - 1 + 1 + 0) = 0$$ (tốn 4 lần tính).
   - Chọn ngẫu nhiên đều $$i \in \{1, 2, 3, 4\}$$: kỳ vọng $$\mathbb{E}[g_i] = \frac{1}{4}(0) + \frac{1}{4}(-1) + \frac{1}{4}(1) + \frac{1}{4}(0) = 0 = g_{\text{batch}}$$ (chỉ tốn 1 lần tính!).
   - Tuy nhiên phương sai $$\operatorname{Var}(g_i) = \frac{1}{4}(0 + 1 + 1 + 0) = 0.5 > 0$$: dù đang đứng ngay tại điểm có $$g_{\text{batch}} = 0$$, bước ngẫu nhiên vẫn có 50% cơ hội đẩy $$w$$ lệch đi $$\pm t_k$$ — đó là lý do ta phải phân tích sâu hơn về hội tụ ngẫu nhiên ở các bài tiếp theo.

Phương pháp subgradient ngẫu nhiên là sự mở rộng của stochastic gradient descent, trong đó gradient được thay thế bằng subgradient để xử lý các hàm mục tiêu không khả vi.