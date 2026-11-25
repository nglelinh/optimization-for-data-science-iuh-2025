---
layout: post
title: 03-04 Hàm giả lồi
chapter: '03'
order: 8
owner: Minjoo Lee
categories:
- chapter03
lang: vi
---

Trong kinh tế học, kỹ thuật và học máy, rất nhiều hàm mục tiêu hoàn toàn tự nhiên — như tỷ lệ chi phí trên lợi ích $$\frac{c^T x + d}{e^T x + f}$$, độ dài đoạn tín hiệu, hay hàm $$\sqrt{|x|}$$ — lại **không phải hàm lồi**. Liệu ta phải bó tay xếp chúng vào nhóm không lồi khó giải? Không hề! Nếu tất cả các **tập mức dưới** của hàm vẫn là tập lồi, ta gọi đó là **hàm giả lồi (quasiconvex)** — và bài toán cực tiểu hóa chúng vẫn giải được chính xác bằng một chuỗi ngắn các bài toán khả thi lồi (phương pháp chia đôi)!

Phần 03-04 mở rộng tầm nhìn của bạn vượt ra ngoài ranh giới hàm lồi cổ điển sang thế giới hàm giả lồi đầy thực dụng.

## Bản đồ kiến thức nền: Ba đặc trưng quan trọng của Hàm giả lồi

- **Định nghĩa qua tập mức dưới:** $$f$$ là giả lồi khi $$\operatorname{dom} f$$ lồi và mọi tập mức dưới $$S_\alpha = \{x : f(x) \le \alpha\}$$ đều là tập lồi. Mọi hàm lồi đều là giả lồi, nhưng chiều ngược lại rộng hơn rất nhiều.
- **Trực giác một biến (Đơn điệu hoặc một đáy):** Trên $$\mathbb{R}$$, hàm liên tục là giả lồi khi và chỉ khi nó đơn điệu tăng, đơn điệu giảm, hoặc giảm đến một điểm rồi tăng (unimodal) — không có nhiều thung lũng lồi lõm!
- **Thuật toán chia đôi (Bisection):** Vì kiểm tra $$\exists x : f(x) \le t$$ chính là kiểm tra một tập lồi $$S_t$$ có khác rỗng hay không, ta có thể chặt đôi khoảng chứa $$p^*$$ sau mỗi bước để tìm cực tiểu toàn cục với độ chính xác $$\epsilon$$ chỉ sau $$\lceil \log_2((u-l)/\epsilon)\rceil$$ bước!

### Khung giải thích (nên đọc chậm): Hàm $$f(x) = \sqrt{|x|}$$ — Không lồi nhưng Giả lồi tuyệt đối

Xét hàm $$f(x) = \sqrt{|x|}$$ trên $$\mathbb{R}$$:

1. **Chứng minh $$f$$ là hàm giả lồi:** Với mọi mức $$\alpha \in \mathbb{R}$$:
   - Nếu $$\alpha < 0$$: $$S_\alpha = \emptyset$$ (tập lồi).
   - Nếu $$\alpha \ge 0$$: $$S_\alpha = \{x \in \mathbb{R} : \sqrt{|x|} \le \alpha\} = \{x : |x| \le \alpha^2\} = [-\alpha^2,\ \alpha^2]$$.
   Vì mọi đoạn đóng $$[-\alpha^2, \alpha^2]$$ đều là tập lồi, $$f$$ chắc chắn là **hàm giả lồi**!
2. **Chứng minh $$f$$ KHÔNG phải hàm lồi:** Chọn $$x = 0,\ y = 4,\ \theta = 0.5$$ (trung điểm $$2$$):
   - $$f(2) = \sqrt{2} \approx 1.414$$.
   - $$0.5 f(0) + 0.5 f(4) = 0.5(0) + 0.5(2) = 1$$.
   Vì $$1.414 > 1$$, đồ thị nhô lên **phía trên** dây cung (vi phạm tính lồi), nhưng vẫn chỉ có đúng một đáy duy nhất tại $$x^* = 0$$!

---

Phần này giới thiệu khái niệm hàm giả lồi (quasiconvex function), cùng các ví dụ tiêu biểu và tính chất cơ bản của chúng.
