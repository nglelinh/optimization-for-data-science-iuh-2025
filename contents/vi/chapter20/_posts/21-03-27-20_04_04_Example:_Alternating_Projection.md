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

Xét bài toán tìm một điểm trong giao của các tập lồi $$C, D \in \mathbb{R}^n$$:
>\begin{equation}
\min_x I_C(x) + I_D(x)    
\end{equation}

trong đó $$I_C(x)$$ và $$I_D(x)$$ lần lượt là các hàm chỉ thị của các tập $$C$$ và $$D$$.

Để viết lại bài toán này dưới dạng ADMM, ta biểu diễn như sau:
> $$
> \begin{equation}
> \min_{x,z} I_C(x) + I_D(z) \quad \text{subject to} \quad x - z = 0   
> \end{equation}
> $$

## Thuật toán ADMM cho chiếu luân phiên

Mỗi chu kỳ ADMM gồm hai phép chiếu:
> $$
> \begin{alignat}{1}
> x^{(k)} & = P_C \left( z^{(k-1)} - w^{(k-1)} \right) \\
> z^{(k)} & = P_D \left( x^{(k)} + w^{(k-1)} \right) \\
> w^{(k)} & = w^{(k-1)} + x^{(k)} - z^{(k)}
> \end{alignat}
> $$

trong đó $$P_C$$ và $$P_D$$ lần lượt là các toán tử chiếu lên tập $$C$$ và $$D$$.

## Suy diễn

Cập nhật cho $$x^{(k)}$$ được suy ra như sau:

> $$
> \begin{alignat}{1}
> x^{(k)} & = \arg\min_x I_C(x) + \frac{\rho}{2} \lVert x - z^{(k-1)} + w^{(k-1)} \rVert_2^2 \\
> & = P_C \left( z^{(k-1)} - w^{(k-1)} \right)
> \end{alignat}
> $$

Tương tự, cập nhật cho $$z^{(k)}$$ được suy ra như sau:

> $$
> \begin{alignat}{1}
> z^{(k)} & = \arg\min_z I_D(z) + \frac{\rho}{2} \lVert x^{(k)} - z + w^{(k-1)} \rVert_2^2 \\
> & = P_D \left( x^{(k)} + w^{(k-1)} \right)
> \end{alignat}
> $$

## So sánh với phương pháp cổ điển

Phương pháp này tương tự phương pháp chiếu luân phiên cổ điển nhưng trong thực tế thường hiệu quả và vững chắc hơn.
