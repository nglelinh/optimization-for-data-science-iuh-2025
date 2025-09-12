---
layout: post
title: 17-03 Some history
chapter: '17'
order: 7
owner: Minjoo Lee
categories:
- chapter17
lang: vi
---
Generally, modern state-of-the-art LP Solvers use both Simplex method and interior-point method.

* Dantzig (1940s): Simplex method, the first method to solve the general form of LP, obtaining exact solutions without iteration. It remains one of the best-known and most studied algorithms for LP to this day.

* Klee and Minty (1972): A pathological LP with $$n$$ variables and $$2n$$ constraints. Solving with the Simplex method requires $$2^n$$ iterations.

* Khachiyan (1979): A polynomial-time algorithm for LP based on the ellipsoid method of Nemirovski and Yudin (1976), which is theoretically strong but not so in practice.

* Karmarkar (1984): An interior-point polynomial-time LP method that is quite effective and became a breakthrough research. (US Patent 4,744,026, expired in 2006).

* Renegar (1988): Newton-based interior-point algorithm for LP. It had the theoretically best computational complexity until the latest research by Lee-Sidford emerged.