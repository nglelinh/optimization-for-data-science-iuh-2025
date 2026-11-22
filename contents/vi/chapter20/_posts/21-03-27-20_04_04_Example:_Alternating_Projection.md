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
