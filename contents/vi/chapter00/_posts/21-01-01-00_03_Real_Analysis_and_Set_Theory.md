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
