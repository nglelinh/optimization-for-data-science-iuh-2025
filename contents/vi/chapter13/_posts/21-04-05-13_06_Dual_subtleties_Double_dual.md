---
layout: post
title: 13-06 Tinh tế đối ngẫu & Đối ngẫu kép
chapter: '13'
order: 10
owner: Wontak Ryu
categories:
- chapter13
lang: vi
---

Trong thực hành lập bài toán đối ngẫu, có những "bẫy tinh tế" mà ngay cả người đã thuộc lòng công thức KKT cũng dễ vấp phải. Ví dụ, bạn lấy logarit hoặc nhân đôi hàm mục tiêu của bài toán đối ngẫu để nó trông gọn gàng hơn — nghiệm đối ngẫu $$u^\star$$ vẫn giữ nguyên, nhưng liệu giá trị hàm mục tiêu mới có còn dùng được để tính khoảng cách đối ngẫu không? Câu trả lời là **không**! Chỉ một phép biến đổi đơn điệu tưởng chừng vô hại đã làm mất đi tính chất chặn dưới trực tiếp của hàm đối ngẫu gốc.

Một câu hỏi sâu sắc không kém là: *điều gì xảy ra nếu ta lấy đối ngẫu của chính bài toán đối ngẫu?* Bài học này đi sâu vào những tinh tế đó và chứng minh kết quả đẹp mắt về **đối ngẫu kép (double dual)**: với bài toán lồi đóng có cấu trúc phù hợp, đi qua hai lần phép đối ngẫu sẽ đưa bạn trở về đúng bài toán nguyên thủy ban đầu.

## Bản đồ kiến thức nền: Các quy tắc an toàn khi biến đổi bài toán đối ngẫu

- **Tương đương nghiệm vs. Tương đương giá trị:** Khi biến đổi bài toán đối ngẫu (như đổi dấu thành cực tiểu hóa, lấy logarit, bỏ hằng số), tập nghiệm tối ưu $$u^\star$$ không đổi, nhưng giá trị mục tiêu đã thay đổi — bạn phải hoàn nguyên về $$g(u)$$ gốc trước khi tính duality gap $$f(x) - g(u)$$.
- **Bài toán tương đương nguyên thủy có thể cho đối ngẫu khác nhau:** Thêm ràng buộc dư, biến đổi hàm mục tiêu (ví dụ $$\min \|Ax-b\|_2$$ so với $$\min \frac{1}{2}\|Ax-b\|_2^2$$) hay tách biến không làm thay đổi $$x^\star$$, nhưng có thể biến bài toán đối ngẫu từ chỗ khó giải thành cực kỳ đẹp mắt!
- **Tính đối ngẫu kép (Double Dual):** Lấy đối ngẫu của bài toán đối ngẫu thực chất là lấy liên hợp kép $$f^{**}$$ (bao lồi đóng của $$f$$). Khi bài toán gốc lồi và thỏa tính đóng, đối ngẫu của đối ngẫu trả về đúng bài toán gốc.

### Khung giải thích (nên đọc chậm): Minh họa hai bài toán nguyên thủy tương đương sinh ra hai đối ngẫu khác hẳn nhau

Xét bài toán cực tiểu hóa 1 chiều đơn giản $$\min_{x \in \mathbb{R}} \vert x - 2 \vert$$ (nghiệm hiển nhiên $$x^\star = 2, f^\star = 0$$), và so sánh hai cách viết tương đương:

1. **Cách viết 1 (không tách biến, không ràng buộc):**
   $$\min_x \vert x - 2 \vert.$$
   Không có ràng buộc nên hàm Lagrange là $$L(x) = \vert x - 2 \vert$$, hàm đối ngẫu chỉ là hằng số $$g_1 = 0$$ — không có biến đối ngẫu để khai thác!
2. **Cách viết 2 (thêm biến phụ $$z = x - 2$$):**
   $$\min_{x, z} \vert z \vert \qquad \text{với } z = x - 2.$$
   Hàm Lagrange: $$L(x, z, v) = \vert z \vert + v(x - 2 - z) = vx + (\vert z \vert - vz) - 2v$$.
   Lấy cực tiểu theo $$x$$ buộc $$v = 0$$; lấy cực tiểu theo $$z$$ buộc $$\vert v \vert \le 1$$. Ta thu được đối ngẫu $$\max_{v = 0} (-2v) = 0$$.
3. **Thử bẫy biến đổi hàm đối ngẫu trên bài toán có ràng buộc:**
   Xét $$\min_{x \ge 1} x^2$$ ($$f^\star = 1$$). Đối ngẫu gốc là $$\max_{u \ge 0} g(u)$$ với $$g(u) = u - \frac{u^2}{4}$$ (đạt cực đại $$g(2) = 1$$).
   - Nếu ai đó "viết gọn" bài toán đối ngẫu bằng cách nhân 4 lên thành $$\max_{u \ge 0} \tilde{g}(u) = 4u - u^2$$: nghiệm tối ưu vẫn là $$u^\star = 2$$, nhưng tại $$u = 1$$ ta có $$\tilde{g}(1) = 3 > f^\star = 1$$! Nếu dùng $$\tilde{g}(1)$$ để tính duality gap sẽ ra số âm vô nghĩa, trong khi dùng $$g(1) = 0.75 \le 1$$ mới cho chặn dưới đúng.

---

## Một số lưu ý tinh tế về đối ngẫu

* Trong thực hành, ta thường biến đổi bài toán đối ngẫu sang một bài toán tối ưu tương đương gọn hơn và vẫn gọi đó là bài toán đối ngẫu. Khi tính đối ngẫu mạnh được thỏa mãn, nghiệm của bài toán đối ngẫu đã biến đổi vẫn có thể dùng để phân tích đặc trưng hoặc khôi phục nghiệm nguyên thủy.

#### Lưu ý
Giá trị mục tiêu tối ưu của bài toán đối ngẫu sau khi biến đổi (chẳng hạn bỏ hằng số hay đổi dấu) không nhất thiết bằng giá trị tối ưu của bài toán nguyên thủy.

* Một kỹ thuật phổ biến để xây dựng bài toán đối ngẫu cho bài toán không ràng buộc là đưa thêm các biến phụ và ràng buộc đẳng thức vào bài toán nguyên thủy. Cách biến đổi này không duy nhất; các cách đặt biến phụ khác nhau có thể dẫn tới những bài toán đối ngẫu khác nhau.

## Đối ngẫu kép

Xét bài toán cực tiểu hóa tổng quát với các ràng buộc tuyến tính:

> $$ \min_x f(x) \text{ với điều kiện } Ax \le b, \; Cx = d$$

Hàm Lagrangian tương ứng là:

> $$L(x,u,v) = f(x) + (A^Tu + C^Tv)^Tx - b^Tu - d^Tv$$

Từ đó, bài toán đối ngẫu có dạng:

> $$ \max_{u,v} -f^*(-A^Tu - C^Tv) - b^Tu - d^Tv \text{ với điều kiện } u \ge 0 $$

#### Nhắc lại tính chất

Nếu $$f$$ là hàm đóng và lồi, ta đã biết hàm liên hợp kép bằng chính hàm gốc ($$f^{**} = f$$), nên bài toán đối ngẫu của bài toán đối ngẫu chính là bài toán nguyên thủy.

Thực tế, tính chất này còn mở rộng vượt ra ngoài trường hợp ràng buộc tuyến tính. Xét bài toán tổng quát:

> $$ 
>\begin{align}
> & \min_x && f(x) \\
>&\text{ với điều kiện } && h_i(x) \le 0, \; i = 1,\dots,m \\
> &&&l_j(x) = 0, \; j = 1,\dots,r
>\end{align}$$

Nếu $$f$$ và các hàm $$h_1, \dots, h_m$$ đều đóng và lồi, còn $$l_1, \dots, l_r$$ là các hàm affine, thì đối ngẫu của đối ngẫu vẫn là bài toán nguyên thủy. Kết quả này được xây dựng từ góc nhìn lý thuyết hàm hai biến (xem thêm Chương 29 và Chương 30 trong sách của Rockafellar).
