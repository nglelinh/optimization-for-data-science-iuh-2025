---
layout: post
title: 07 Gradient dưới (Subgradient)
chapter: '07'
order: 1
owner: Kyeongmin Woo
categories:
- chapter07
lang: vi
---

Suốt Chương 06, Gradient Descent vận hành trơn tru như một cỗ máy đồng hồ Thụy Sĩ — nhưng nó đòi hỏi một điều kiện tiên quyết khắt khe: **hàm mục tiêu phải khả vi ở mọi nơi**. Vậy điều gì xảy ra ngay khi ta chạm vào những bài toán thực tế hấp dẫn nhất của khoa học dữ liệu như **Lasso** ($$\|w\|_1$$ có góc nhọn tại $$0$$), **SVM** (hàm mất mát bản lề $$\max(0, 1 - y_i w^T x_i)$$ gãy khúc tại $$1$$), hay hàm cực đại $$\max_i f_i(x)$$? Đạo hàm cổ điển biến mất đúng tại điểm tối ưu quan trọng nhất!

Chương 07 mở ra giải pháp thiên tài của giải tích lồi không trơn: **Gradient dưới (Subgradient)** và **Vi phân dưới (Subdifferential)**. Thay vì bất lực trước các điểm gãy khúc, ta nhận ra tại mỗi góc nhọn của hàm lồi không chỉ có một tiếp tuyến duy nhất, mà có cả một **chùm siêu phẳng đỡ phía dưới** — và chỉ cần vector $$0$$ nằm trong chùm đó, ta lập tức có chứng chỉ tối ưu toàn cục!

## Kiến thức cần nhớ: Kiến trúc của Giải tích Lồi Không Trơn (Chương 07)

Toàn bộ 15 bài học trong Chương 07 xây dựng trên bốn trụ cột mạch lạc:

- **Tổng quát hóa Gradient (Subgradient $$g$$):** Mọi vector $$g$$ thỏa bất đẳng thức đỡ toàn cục $$f(y) \ge f(x) + g^T(y - x) \; \forall y$$ đều là một subgradient tại $$x$$. Tại điểm khả vi, $$g = \nabla f(x)$$ là duy nhất; tại điểm gãy khúc, có vô số $$g$$ hợp thành tập lồi đóng $$\partial f(x)$$.
- **Cầu nối Hình học (Hàm chỉ thị & Nón pháp tuyến):** Vi phân dưới của hàm chỉ thị $$I_C(x)$$ (bằng $$0$$ trong tập lồi $$C$$, bằng $$+\infty$$ ngoài $$C$$) chính xác là **nón pháp tuyến** $$N_C(x)$$ — giúp hợp nhất tối ưu *có ràng buộc* và *không ràng buộc* vào chung một công thức duy nhất!
- **Phép tính Vi phân dưới (Subgradient Calculus):** Tương tự quy tắc đạo hàm tổng, nhân hằng số dương, hợp thành affine và hàm cực đại $$\max_i f_i(x)$$ (bao lồi các subgradient của những hàm đang đạt cực đại).
- **Điều kiện tối ưu $$0 \in \partial f(x^\star)$$ & Ứng dụng kinh điển:** Công thức cực gọn $$0 \in \partial f(x^\star)$$ lập tức suy ra điều kiện tối ưu bậc nhất của Chương 04, công thức tối ưu Lasso, phép toán **Ngưỡng mềm (Soft-Thresholding)** và đạo hàm hàm khoảng cách đến tập lồi!

### Giải thích: Khám phá trực giác Subgradient tại điểm gãy khúc của $$f(x) = |x|$$

Xét hàm lồi không khả vi nổi tiếng nhất: $$f(x) = |x|$$ tại điểm gãy khúc $$x = 0$$ (nơi đạo hàm cổ điển không tồn tại).

1. **Kiểm tra điều kiện đỡ toàn cục tại $$x = 0$$:** Ta cần tìm mọi số thực $$g \in \mathbb{R}$$ sao cho
   $$|y| \ge |0| + g(y - 0) \iff |y| \ge g \cdot y \quad \forall y \in \mathbb{R}.$$
2. **Thử giá trị cụ thể:**
   - Chọn $$g = 0.5$$: với $$y = 2$$, $$|2| = 2 \ge 1$$ (đúng); với $$y = -2$$, $$|-2| = 2 \ge -1$$ (đúng!). Vậy $$g = 0.5$$ là một subgradient!
   - Chọn $$g = 0$$: $$|y| \ge 0$$ luôn đúng với mọi $$y$$! Vậy $$0 \in \partial f(0)$$ — chứng nhận ngay $$x^\star = 0$$ là cực tiểu toàn cục!
   - Chọn $$g = 1.5$$: thử $$y = 1$$ cho $$|1| = 1 < 1.5$$ (sai!).
3. **Kết luận:** Tập tất cả các subgradient tại $$x = 0$$ là cả đoạn đóng $$\partial |0| = [-1, 1]$$ — mọi đường thẳng đi qua gốc tọa độ có độ dốc nằm giữa $$-1$$ và $$+1$$ đều nâng đỡ hoàn toàn chữ V phía trên nó!

---

Trong chương này, chúng ta giới thiệu khái niệm gradient dưới (subgradient) và điều kiện tối ưu theo gradient dưới — sự tổng quát hóa của gradient và điều kiện tối ưu bậc một đã trình bày ở các chương trước. Đồng thời, chúng ta cũng sẽ xem xét một số ứng dụng và ví dụ minh họa cho các khái niệm này.

## Ứng dụng hiện đại (2022–2026)

Bài đọc tùy chọn đi kèm liên hệ trực tiếp các khái niệm vi phân dưới trong chương này với những quy trình khoa học máy tính và khoa học dữ liệu gần đây — bao gồm vi phân tự động cho mạng ReLU, đường chính quy hóa Lasso trong `glmnet` / `skglm`, cũng như hồi quy phân vị với hàm mất mát pinball và dự báo conformal — trong khi vẫn giữ nguyên nền tảng lý thuyết. Xem [07-08 Ứng dụng hiện đại của subgradient]({% multilang_post_url contents/chapter07/2026-09-16-07_08_modern_applications %}).
