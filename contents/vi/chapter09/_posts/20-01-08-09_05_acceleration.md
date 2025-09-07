---
layout: post
title: '09-05 Tăng tốc'
chapter: '09'
order: 6
owner: Kyeongmin Woo
categories:
- chapter09
lang: vi
---

# Tăng tốc

Các kỹ thuật tăng tốc được sử dụng để tăng tốc sự hội tụ của các thuật toán tối ưu. Trong bối cảnh của các phương pháp gradient gần kề, tăng tốc có thể cải thiện đáng kể tốc độ tìm ra giải pháp.

## Tăng tốc của Nesterov
Tăng tốc của Nesterov là một kỹ thuật phổ biến giới thiệu động lượng vào các bước cập nhật, cho phép thuật toán di chuyển nhanh hơn về phía điểm tối ưu.

## FISTA
FISTA (Thuật toán Ngưỡng-Co lặp Nhanh) là một phương pháp gradient gần kề tăng tốc đạt được tốc độ hội tụ $$O(1/k^2)$$.

## Cân nhắc thực tế
Mặc dù tăng tốc có thể cải thiện hội tụ, nó cũng có thể gây ra mất ổn định hoặc dao động trong một số trường hợp. Quan trọng là giám sát hành vi của thuật toán và điều chỉnh các tham số khi cần thiết.