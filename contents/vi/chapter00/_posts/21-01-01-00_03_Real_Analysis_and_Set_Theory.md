---
layout: post
title: 00-03 Giải tích thực và Lý thuyết tập hợp
chapter: '00'
order: 11
owner: GitHub Copilot
lang: vi
categories:
- chapter00
lesson_type: required
---

Trước khi viết một dòng code để tìm giá trị nhỏ nhất của hàm $$f(x)$$ trên tập $$S$$, nhà toán học tối ưu luôn hỏi một câu tưởng chừng đơn giản nhưng vô cùng hiểm hóc: *liệu giá trị nhỏ nhất ấy có thực sự tồn tại không?* Một bài toán thiết kế thiếu cẩn thận có thể có cận dưới $$\inf$$ bằng $$0$$ nhưng không bao giờ chạm tới $$0$$ — khiến mọi thuật toán chạy vô tận mà không hội tụ về một điểm hợp lệ nào.

Phần 00-03 trang bị ngôn ngữ tập hợp và tôpô thực để bạn phân biệt rạch ròi giữa $$\inf$$ và $$\min$$, giữa biên và phần trong, làm bệ phóng trực tiếp cho Chương 02 về tập lồi.

## Bản đồ kiến thức nền: Vì sao tối ưu hóa cần tập hợp và tôpô?

- **Ngôn ngữ tập hợp và miền khả thi:** Mọi hệ ràng buộc $$g_i(x) \le 0, h_j(x) = 0$$ thực chất định nghĩa miền khả thi $$D$$ dưới dạng **giao** của nhiều tập con trong $$\mathbb{R}^n$$.
- **Tập mở, tập đóng và biên (Open, Closed, Boundary):** Xác định khi nào ta có thể nhích biến theo mọi hướng mà vẫn ở trong miền khả thi (điểm trong), và khi nào ràng buộc bị "chạm ngưỡng" (điểm biên).
- **Tính compact và Định lý Weierstrass:** Trong $$\mathbb{R}^n$$, tập compact đồng nghĩa với **đóng và bị chặn** (định lý Heine–Borel). Mọi hàm liên tục trên tập compact khác rỗng luôn đạt giá trị nhỏ nhất và lớn nhất toàn cục.
- **Cận dưới đúng ($$\inf$$) so với Cực tiểu ($$\min$$):** Giúp phân biệt trường hợp giá trị tối ưu hữu hạn nhưng không đạt được tại bất kỳ điểm khả thi nào.

### Khung giải thích (nên đọc chậm): Một ranh giới đóng hay mở quyết định sự tồn tại của nghiệm

So sánh hai bài toán tối ưu cực kỳ đơn giản trên trục số thực:

1. **Bài toán A (miền không đóng):** $$\min_{x \in (0, 1]} f(x) = x$$.
   - Với mọi $$x \in (0, 1]$$, ta có $$f(x) > 0$$. Nếu bạn thử $$x = 0.01$$, luôn có $$x = 0.001$$ nhỏ hơn; thử $$10^{-9}$$, luôn có $$10^{-10}$$ nhỏ hơn.
   - Vậy $$\inf_{x \in (0, 1]} f(x) = 0$$, nhưng **không tồn tại** $$x^* \in (0, 1]$$ đạt $$f(x^*) = 0$$ vì $$0 \notin (0, 1]$$!
2. **Bài toán B (đóng lại thành tập compact):** $$\min_{x \in [0, 1]} f(x) = x$$.
   - Miền $$[0, 1]$$ vừa đóng vừa bị chặn (compact), hàm $$f(x) = x$$ liên tục.
   - Theo định lý Weierstrass, cực tiểu toàn cục chắc chắn tồn tại và đạt tại đúng điểm biên $$x^* = 0$$ với $$\min f = 0$$.
3. **Thông điệp thực hành:** Đó là lý do trong dạng chuẩn của bài toán tối ưu hóa, ta luôn viết ràng buộc bất đẳng thức lỏng $$g_i(x) \le 0$$ (tạo tập đóng) thay vì bất đẳng thức chặt $$g_i(x) < 0$$ (tạo tập mở dễ mất nghiệm).

---

Tối ưu hóa lồi là giải tích trên *tập hợp*: miền khả thi, biểu đồ trên (epigraph) và nón nhân tử đối ngẫu. Trước khi Chương 02 định nghĩa tập lồi, ta cần nắm vững ngôn ngữ về tập mở, tập đóng, phần trong và dãy hội tụ.

## Vai trò của phần này

- **Tập khả thi** là một tập con của $$\mathbb{R}^n$$. Tính đóng quyết định liệu giới hạn của một dãy điểm giảm dần có nằm *trong* tập khả thi hay không; tính đóng kết hợp với tính bị chặn (định lý Heine–Borel trong không gian hữu hạn chiều) đảm bảo hàm liên tục đạt giá trị nhỏ nhất.
- **Tập mở và phần trong** xuất hiện trong điều kiện chính quy ràng buộc (điều kiện Slater: tồn tại điểm nằm trong phần trong tương đối của tập ràng buộc bất đẳng thức), giúp điều kiện KKT trở thành điều kiện cần ở Chương 12.
- **Dãy và giới hạn** là công cụ để phát biểu chặt chẽ sự hội tụ “$$x^{(k)}\to x^\star$$” của các thuật toán như gradient descent.

Một tập $$C\subseteq\mathbb{R}^n$$ được gọi là **đóng** nếu nó chứa mọi điểm giới hạn của mình, **mở** nếu là lân cận của mỗi điểm thuộc nó, và **compact** (trong $$\mathbb{R}^n$$) khi và chỉ khi nó vừa đóng vừa bị chặn. **Biểu đồ trên** (epigraph)

$$
\operatorname{epi} f = \bigl\{(x,t): f(x)\le t\bigr\}
$$

là một tập con trong $$\mathbb{R}^{n+1}$$; hàm $$f$$ nửa liên tục dưới khi và chỉ khi $$\operatorname{epi} f$$ là tập đóng. Nhận định ngắn gọn này chính là nền tảng giải tích để trả lời câu hỏi: liệu một hàm mất mát có đạt được cận dưới đúng (infimum) hay không.

## Các bài trong phần này

1. Cơ sở lý thuyết tập hợp (hợp, giao, phần bù, tích — phép toán trên các tập ràng buộc)
2. Tôpô trong giải tích thực (tập mở/đóng, phần trong, tính compact, dãy hội tụ)

Sau hai bài này, bạn cần trả lời được ngay: tập $$\{x: \|x\|_2 \le 1\}$$ có compact không, và tập $$\{x: \|x\|_2 < 1\}$$ có thể chứa cực tiểu của một hàm đang giảm dần về phía biên hay không.
