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

Tối ưu lồi là giải tích trên *tập hợp*: miền khả thi, biểu đồ trên (epigraph), nón nhân tử đối ngẫu. Trước khi Chương 02 định nghĩa tập lồi, ta cần từ vựng tập mở/đóng, phần trong, và dãy.

## Vì sao có khối này

- **Tập khả thi** là tập con của $$\mathbb{R}^n$$. Tính đóng quyết định dãy cực tiểu có giới hạn *trong* tập hay không; bị chặn cộng đóng (Heine–Borel trong chiều hữu hạn) cho sự tồn tại cực tiểu của hàm liên tục.
- **Tập mở và phần trong** xuất hiện trong điều kiện chính quy ràng buộc (Slater: một điểm ở phần trong tương đối của các bất đẳng thức) khiến KKT trở thành điều kiện cần ở Chương 12.
- **Dãy và giới hạn** là cách ta phát biểu “$$x^{(k)}\to x^\star$$” cho gradient descent.

Tập $$C\subseteq\mathbb{R}^n$$ **đóng** nếu chứa mọi điểm tụ, **mở** nếu là lân cận của mỗi điểm của nó, và **compact** (trong $$\mathbb{R}^n$$) khi và chỉ khi đóng và bị chặn. **Biểu đồ trên**

$$
\operatorname{epi} f = \bigl\{(x,t): f(x)\le t\bigr\}
$$

là một tập trong $$\mathbb{R}^{n+1}$$; $$f$$ nửa liên tục dưới đúng khi $$\operatorname{epi} f$$ đóng. Một câu đó là xương sống giải tích của “hàm mất mát này có đạt infimum không?”

## Các bài trong khối này

1. Nền tảng lý thuyết tập hợp (hợp, giao, phần bù, tích — đại số của ràng buộc)
2. Tô-pô trong giải tích thực (tập mở/đóng, phần trong, dãy)

Sau hai bài này bạn cần nói được ngay $$\{x: \|x\|_2 \le 1\}$$ có compact không, và $$\{x: \|x\|_2 < 1\}$$ có thể chứa cực tiểu của hàm đang giảm về biên hay không.
