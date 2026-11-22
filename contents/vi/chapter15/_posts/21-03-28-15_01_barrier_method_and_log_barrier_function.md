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

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

Ở chương trước, chúng ta đã tìm hiểu cách giải **bài toán tối ưu trơn có ràng buộc đẳng thức** bằng phương pháp Newton. Trong chương này, ta mở rộng sang **bài toán tối ưu trơn có cả ràng buộc bất đẳng thức lẫn ràng buộc đẳng thức**.

Ý tưởng cốt lõi là đưa bài toán về một chuỗi các bài toán trơn chỉ còn ràng buộc đẳng thức rồi giải bằng phương pháp Newton. Hướng tiếp cận này thuộc nhóm **phương pháp điểm trong (interior-point methods)**, mà đại diện tiêu biểu được xét trong chương này là **phương pháp chắn (barrier method)**.
