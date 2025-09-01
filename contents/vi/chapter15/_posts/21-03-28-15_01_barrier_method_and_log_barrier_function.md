---
layout: post
title: 15-01 Barrier method and log barrier function
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

In the previous chapter, we explored how to solve an **equality constrained smooth problem** using Newton's method. In this chapter, we will look at methods for solving **inequality and equality constrained smooth problems**.

The basic idea is to transform the problem into an equality constrained smooth problem and solve it using Newton's method. This approach is called the **interior method**, and in this chapter, we will focus on one type of interior method: the **barrier method**.
