---
layout: post
title: '20-04-03 ADMM dạng có tỉ lệ (Scaled Form)'
chapter: '20'
order: 11
owner: Hooncheol Shin
categories:
- chapter20
lang: vi
---

# ADMM dạng có tỉ lệ

ADMM có thể được biểu diễn dưới dạng có tỉ lệ bằng cách thay biến đối ngẫu $$u$$ bằng $$w = u/\rho$$. Khi đó các bước ADMM có thể được viết như sau:
> $$
> \begin{alignat}{1}
> x^{(k)} & = \arg\min_x f(x) + \frac{\rho}{2} \lVert Ax + Bz^{(k-1)} - c + w^{(k-1)} \rVert_2^2  \\
> z^{(k)} & = \arg\min_z g(z) + \frac{\rho}{2} \lVert Ax^{(k)} + Bz - c + w^{(k-1)} \rVert_2^2  \\
> w^{(k)} & = w^{(k-1)} + Ax^{(k)} + Bz^{(k)} - c 
> \end{alignat}
> $$

## Tương đương với dạng ban đầu

Ta có thể chứng minh các phương trình trên tương đương với dạng ban đầu qua quá trình sau:

> $$
> \begin{align}
> x^{(k)} & = \arg\min_x f(x) + \frac{\rho}{2} \lVert Ax + Bz^{(k-1)} - c + w^{(k-1)} \rVert_2^2  \\
> & = \arg\min_x f(x)  + \frac{\rho}{2} \lVert Ax + Bz^{(k-1)} - c \rVert_2^2  + \rho w^{(k-1)T} (Ax + Bz^{(k-1)} - c)  + \frac{\rho}{2}\lVert w^{(k-1)} \rVert_2^2 \\
> & = \arg\min_x f(x)  + \frac{\rho}{2} \lVert Ax + Bz^{(k-1)} - c \rVert_2^2  + u^{(k-1)T} (Ax + Bz^{(k-1)} - c) \\
> \end{align}
> $$

trong đó ta đã dùng $$u^{(k-1)} = \rho w^{(k-1)}$$ và bỏ đi số hạng hằng.

## Diễn giải biến có tỉ lệ

Ở đây, $$w^{(k)}$$ có thể được xem là tổng các phần dư cho đến vòng lặp $$k$$:

> $$
> \begin{equation}
> w^{(k)} = w^{(0)} + \sum_{i=1}^k (Ax^{(i)} + Bz^{(i)} - c) 
> \end{equation}
> $$

Dạng có tỉ lệ này thường thuận tiện hơn cho việc cài đặt và phân tích.
