---
layout: post
title: '15-01 Phương pháp chắn và hàm chắn logarit'
chapter: '15'
order: 2
owner: Minjoo Lee
categories:
- chapter15
lang: vi
---

Mục 15-01 mở màn cho Chương 15 bằng câu hỏi bản lề: *làm sao tái sử dụng toàn bộ cỗ máy Newton có ràng buộc đẳng thức siêu mạnh ở Chương 14 cho bài toán có thêm hàng trăm ràng buộc bất đẳng thức $$h_i(x) \le 0$$?*

Câu trả lời là một kỹ thuật cầu nối cực kỳ thanh lịch: nhét toàn bộ các ràng buộc bất đẳng thức vào hàm mục tiêu dưới dạng **hàm chỉ thị**, rồi làm trơn hàm chỉ thị "góc cạnh" đó bằng **hàm chắn logarit** $$\phi(x) = -\sum_{i=1}^m \log(-h_i(x))$$. Từ đây, ta vừa giữ nguyên tính lồi, vừa có đạo hàm cấp 1 và cấp 2 đẹp mắt để đưa thẳng vào phương pháp Newton.

## Bản đồ kiến thức nền: Ba bước chuyển hóa từ bài toán bất đẳng thức sang bài toán Newton

- **Bước 1 — Nhúng bất đẳng thức vào mục tiêu bằng hàm chỉ thị:** Viết lại $$\min f(x)$$ thỏa $$h_i(x) \le 0, Ax = b$$ thành $$\min f(x) + \sum_{i=1}^m I_-(h_i(x))$$ thỏa $$Ax = b$$, trong đó $$I_-(u) = 0$$ nếu $$u \le 0$$ và $$+\infty$$ nếu $$u > 0$$.
- **Bước 2 — Làm trơn bằng hàm chắn logarit:** Thay $$I_-(u)$$ (không khả vi) bằng $$-\frac{1}{t}\log(-u)$$ (khả vi vô hạn lần trên $$u < 0$$ và là hàm tự hài hòa!).
- **Bước 3 — Giải chuỗi bài toán định tâm:** Với mỗi $$t > 0$$ cố định, bài toán $$\min_x t f(x) + \phi(x)$$ thỏa $$Ax = b$$ chỉ còn ràng buộc đẳng thức, giải cực nhanh bằng phương pháp Newton của mục 14-08.

### Khung giải thích (nên đọc chậm): So sánh trực tiếp giá trị hàm chỉ thị và hàm chắn logarit tại nhiều mức $$t$$

Xét một ràng buộc bất đẳng thức $$u \le 0$$ (với $$u = h(x)$$) và hàm xấp xỉ $$B_t(u) = -\frac{1}{t}\log(-u)$$ trên miền $$u < 0$$. Hãy tính giá trị tại 3 vị trí: sâu trong miền ($$u = -1$$), gần biên ($$u = -0.1$$), và sát biên ($$u = -0.001$$):

| Vị trí $$u$$ | Hàm chỉ thị $$I_-(u)$$ | $$t = 1$$: $$-\log(-u)$$ | $$t = 10$$: $$-\frac{1}{10}\log(-u)$$ | $$t = 100$$: $$-\frac{1}{100}\log(-u)$$ |
| :--- | :---: | :---: | :---: | :---: |
| $$u = -1$$ | $$0$$ | $$0.000$$ | $$0.000$$ | $$0.000$$ |
| $$u = -0.1$$ | $$0$$ | $$2.303$$ | $$0.230$$ | $$0.023$$ |
| $$u = -0.001$$ | $$0$$ | $$6.908$$ | $$0.691$$ | $$0.069$$ |
| $$u \to 0^-$$ | $$0$$ (rồi nhảy lên $$+\infty$$) | $$+\infty$$ | $$+\infty$$ | $$+\infty$$ |

Nhìn bảng số trên, ta thấy rõ hai điều: tại mọi $$u < 0$$ cố định, khi $$t$$ tăng từ $$1 \to 100$$ thì $$B_t(u) \to 0 = I_-(u)$$; nhưng hễ $$u \to 0^-$$, $$B_t(u)$$ vẫn luôn vọt lên $$+\infty$$ để ngăn thuật toán vượt qua biên!

---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

Ở chương trước, chúng ta đã tìm hiểu cách giải **bài toán tối ưu trơn có ràng buộc đẳng thức** bằng phương pháp Newton. Trong chương này, ta mở rộng sang **bài toán tối ưu trơn có cả ràng buộc bất đẳng thức lẫn ràng buộc đẳng thức**.

Ý tưởng cốt lõi là đưa bài toán về một chuỗi các bài toán trơn chỉ còn ràng buộc đẳng thức rồi giải bằng phương pháp Newton. Hướng tiếp cận này thuộc nhóm **phương pháp điểm trong (interior-point methods)**, mà đại diện tiêu biểu được xét trong chương này là **phương pháp chắn (barrier method)**.
