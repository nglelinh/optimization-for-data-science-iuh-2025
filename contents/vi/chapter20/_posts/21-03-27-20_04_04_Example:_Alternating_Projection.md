---
layout: post
title: '20-04-04 Ví dụ: Chiếu luân phiên (Alternating Projection)'
chapter: '20'
order: 12
owner: Hooncheol Shin
categories:
- chapter20
lang: vi
---

Tìm một điểm chung nằm trong giao của hai tập lồi $$C \cap D$$ là bài toán kinh điển xuất hiện khắp nơi — từ khôi phục tín hiệu bị cắt xén đến kiểm tra tính khả thi của hệ bất đẳng thức. Cách cổ điển của von Neumann (1933) là **chiếu luân phiên (alternating projection)**: chiếu lên $$C$$, rồi chiếu lên $$D$$, cứ lặp đi lặp lại. Nhưng khi hai tập cắt nhau ở góc nhọn, chiếu luân phiên bị zíc-zắc hàng trăm bước mới tới giao điểm! Bằng cách viết bài toán dưới dạng $$\min I_C(x) + I_D(z) \text{ s.t. } x = z$$ và chạy ADMM dạng có tỉ lệ, ta thu được thuật toán chiếu có "bộ nhớ" $$w$$ — thực chất tương đương với **phương pháp Douglas–Rachford** nổi tiếng, hội tụ nhanh hơn hẳn!

## Kiến thức cần nhớ: Ba ý tưởng tạo nên sức mạnh của ADMM chiếu luân phiên

Để hiểu rõ vì sao chỉ thêm một vector $$w^{(k)}$$ nhỏ bé lại biến phép chiếu luân phiên cổ điển trở nên vượt trội, hãy xem ba điểm sau:

- **Hàm chỉ thị $$I_C(x)$$ và toán tử chiếu Euclid $$P_C$$:** Áp dụng ADMM dạng có tỉ lệ cho $$f = I_C, g = I_D$$ với $$x = z$$ biến bước $$\arg\min_x I_C(x) + \frac{\rho}{2}\|x - v\|_2^2$$ thành đúng phép chiếu Euclid $$P_C(v)$$. Đáng chú ý là tham số $$\rho$$ **tự triệt tiêu hoàn toàn** khỏi thuật toán!
- **Cơ chế "nhắm vượt đích" nhờ biến đối ngẫu $$w$$:** Thay vì chiếu trực tiếp $$z^{(k-1)}$$ lên $$C$$ như von Neumann, ADMM chiếu điểm đã được dịch chuyển $$z^{(k-1)} - w^{(k-1)}$$ lên $$C$$, rồi chiếu $$x^{(k)} + w^{(k-1)}$$ lên $$D$$. Sự dịch chuyển này tự động bẻ góc quỹ đạo zíc-zắc hướng thẳng vào giao điểm $$C \cap D$$!
- **Mở rộng tự nhiên sang giao của $$m$$ tập lồi:** Nếu cần tìm điểm chung của $$m$$ tập lồi $$C_1, \dots, C_m$$, ta chỉ cần áp dụng ADMM đồng thuận (Chương 21) để chiếu song song lên cả $$m$$ tập rồi lấy trung bình cộng!

### Giải thích: Chạy tay so sánh Chiếu luân phiên cổ điển vs. ADMM trên hai đường thẳng cắt nhau

Trong mặt phẳng $$\mathbb{R}^2$$, xét hai tập lồi là hai đường thẳng:
- $$C = \{(x_1, x_2) : x_2 = 0\}$$ (trục hoành; phép chiếu $$P_C(a, b) = (a, 0)$$).
- $$D = \{(x_1, x_2) : x_1 + x_2 = 2\}$$ (phép chiếu $$P_D(a, b) = \left(\frac{a - b + 2}{2}, \; \frac{b - a + 2}{2}\right)$$).

Giao điểm duy nhất là $$C \cap D = \{(2, 0)\}$$. Cùng xuất phát từ $$z^{(0)} = (0, 2)$$ (và $$w^{(0)} = (0, 0)$$ cho ADMM):

1. **Chiếu luân phiên cổ điển (von Neumann):**
   - Vòng 1: $$x^{(1)} = P_C(0, 2) = (0, 0)$$; $$z^{(1)} = P_D(0, 0) = (1, 1)$$.
   - Vòng 2: $$x^{(2)} = P_C(1, 1) = (1, 0)$$; $$z^{(2)} = P_D(1, 0) = (1.5, 0.5)$$.
   (Mỗi vòng khoảng cách tới $$(2, 0)$$ chỉ giảm đúng một nửa — cần vô hạn bước mới chạm $$(2, 0)$$!)
2. **ADMM chiếu luân phiên (dạng có tỉ lệ):**
   - **Vòng 1:**
     - $$x^{(1)} = P_C(z^{(0)} - w^{(0)}) = P_C(0, 2) = (0, 0)$$.
     - $$z^{(1)} = P_D(x^{(1)} + w^{(0)}) = P_D(0, 0) = (1, 1)$$.
     - $$w^{(1)} = w^{(0)} + x^{(1)} - z^{(1)} = (0, 0) + (0, 0) - (1, 1) = (-1, -1)$$.
   - **Vòng 2:**
     - Điểm đích đã được dịch chuyển: $$z^{(1)} - w^{(1)} = (1, 1) - (-1, -1) = (2, 2)$$!
     - $$x^{(2)} = P_C(2, 2) = \mathbf{(2, 0)}$$ — **chạm trúng chính xác giao điểm $$(2, 0)$$ ngay ở vòng lặp thứ 2!**

---

# Ví dụ: Chiếu luân phiên

Xét bài toán tìm một điểm thuộc giao của hai tập lồi $$C, D \subseteq \mathbb{R}^n$$:
>\begin{equation}
\min_x I_C(x) + I_D(x)    
\end{equation}

trong đó $$I_C(x)$$ và $$I_D(x)$$ lần lượt là hàm chỉ thị của hai tập $$C$$ và $$D$$.

Để đưa bài toán về dạng ADMM, ta tách biến như sau:
> $$
> \begin{equation}
> \min_{x,z} I_C(x) + I_D(z) \quad \text{subject to} \quad x - z = 0   
> \end{equation}
> $$

## Thuật toán ADMM cho bài toán chiếu luân phiên

Mỗi vòng lặp ADMM (ở dạng có tỉ lệ) gồm hai phép chiếu liên tiếp và một bước cập nhật biến đối ngẫu:
> $$
> \begin{alignat}{1}
> x^{(k)} & = P_C \left( z^{(k-1)} - w^{(k-1)} \right) \\
> z^{(k)} & = P_D \left( x^{(k)} + w^{(k-1)} \right) \\
> w^{(k)} & = w^{(k-1)} + x^{(k)} - z^{(k)}
> \end{alignat}
> $$

trong đó $$P_C$$ và $$P_D$$ lần lượt là toán tử chiếu Euclid lên tập $$C$$ và tập $$D$$.

## Suy diễn

Bước cập nhật $$x^{(k)}$$ thu được từ định nghĩa phép chiếu:

> $$
> \begin{alignat}{1}
> x^{(k)} & = \arg\min_x I_C(x) + \frac{\rho}{2} \lVert x - z^{(k-1)} + w^{(k-1)} \rVert_2^2 \\
> & = P_C \left( z^{(k-1)} - w^{(k-1)} \right)
> \end{alignat}
> $$

Tương tự, bước cập nhật $$z^{(k)}$$ là:

> $$
> \begin{alignat}{1}
> z^{(k)} & = \arg\min_z I_D(z) + \frac{\rho}{2} \lVert x^{(k)} - z + w^{(k-1)} \rVert_2^2 \\
> & = P_D \left( x^{(k)} + w^{(k-1)} \right)
> \end{alignat}
> $$

## So sánh với phương pháp cổ điển

Thuật toán trên có cấu trúc gần giống phương pháp chiếu luân phiên cổ điển (chỉ thêm biến tích lũy độ lệch $$w^{(k)}$$), nhưng trong thực tế thường hội tụ nhanh và ổn định hơn.
