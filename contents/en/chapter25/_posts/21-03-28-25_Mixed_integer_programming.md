---
layout: post
title: 25 Mixed Integer Programming (part II)
chapter: '25'
order: 1
owner: YoungJae Choung
categories:
- chapter25
lang: en
---

This chapter examines the cutting plane algorithm, which can be considered the most core algorithm in Integer Programming (IP), and the branch and cut algorithm, which is its practical implementation. 

We will also examine examples of Integer Programming such as best subset selection and Least mean squares.

## Reference
* Belotti, Kirches, Leyer, Linderoth, Luedke, and Mahajan (2012), "Mixed-integer nonlinear optimization"
* Bertsimas and Mazumder (2016), "Best subset selection via a modern optimization lens"
* Bertsimas, King, and Mazumder (2014), "Least quantile regression via modern optimization"
* Conforti, Cornuejols, and Zambelli (2014), "Integer programming"
* Wolsey (1998), "Integer programming"

## 2026 applications (optional)

Best-subset MIP is still the statistical poster child; the same big-$$M$$ / ReLU encoding now selects pixels for a trained net, *certifies* robustness, and grows optimal classification trees. Learning to pick Gomory-style cuts (2024) turns 25-01 into training data. Optional lesson: [25-03 Modern applications of MIP in data science]({% multilang_post_url contents/chapter25/2026-09-16-25_03_modern_applications %}).