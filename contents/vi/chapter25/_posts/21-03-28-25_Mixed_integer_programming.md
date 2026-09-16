---
layout: post
title: 25 Quy Hoạch Số Nguyên Hỗn Hợp (Phần II)
chapter: '25'
order: 1
owner: YoungJae Choung
categories:
- chapter25
lang: vi
---

This chapter examines the cutting plane algorithm, which can be considered the most core algorithm in Integer Programming (IP), and the branch and cut algorithm, which is its practical implementation. 

We will also examine examples of Integer Programming such as best subset selection and Least mean squares.

## Reference
* Belotti, Kirches, Leyer, Linderoth, Luedke, and Mahajan (2012), "Mixed-integer nonlinear optimization"
* Bertsimas and Mazumder (2016), "Best subset selection via a modern optimization lens"
* Bertsimas, King, and Mazumder (2014), "Least quantile regression via modern optimization"
* Conforti, Cornuejols, and Zambelli (2014), "Integer programming"
* Wolsey (1998), "Integer programming"

## Ứng dụng 2026 (tùy chọn)

MIP tập con tốt nhất vẫn là poster thống kê; cùng mã hóa big-$$M$$ / ReLU nay chọn pixel cho mạng đã huấn luyện, *chứng nhận* bền vững, và mọc cây phân loại tối ưu. Học chọn cắt kiểu Gomory (2024) biến 25-01 thành dữ liệu huấn luyện. Bài tùy chọn: [25-03 Ứng dụng hiện đại của MIP trong khoa học dữ liệu]({% multilang_post_url contents/chapter25/2026-09-16-25_03_modern_applications %}).