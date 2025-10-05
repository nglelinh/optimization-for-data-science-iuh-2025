---
layout: post
title: 18-05 Lớp Broyden
chapter: '18'
order: 6
owner: Hooncheol Shin
categories:
- chapter18
lang: vi
---

Lớp Broyden tổng quát hóa BFGS, DFP, và SR1 với công thức sau.

* **Lưu ý:** $$B^+_{\text{BFGS}}$$ và $$B^+_{\text{DFP}}$$ lần lượt là $$B^+$$ được tính bởi BFGS và DFP.

>$$
>B^+ = (1 - \phi)B^+_{\text{BFGS}} + \phi B^+_{\text{DFP}}, \text{ với } \phi \in \mathbb{R}.
>$$

Định nghĩa $$v$$ là $$\frac{y}{y^Ts} - \frac{Bs}{s^TBs}$$, công thức trên trở thành công thức dưới đây.

>$$
>B^+ = B - \frac{Bss^TB}{s^TBs} + \frac{yy^T}{y^Ts} + \phi(s^TBs)vv^T.
>$$

Quan sát:
* Khi $$\phi =0$$, cập nhật trên giống với BFGS.
* Khi $$\phi =1$$, cập nhật trên giống với DFP.
* Khi $$\phi = \frac{y^Ts}{y^Ts - s^TBs}$$, cập nhật trên giống với SR1.

***Tham khảo**: Trường hợp ràng buộc phạm vi của $$\phi$$ vào $$[0, 1]$$ được gọi là lớp Broyden bị hạn chế [14].