---
layout: post
title: 10-03 Max flow and min cut
chapter: '10'
order: 4
owner: Wontak Ryu
categories:
- chapter10
lang: vi
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

As an example of duality in linear programs, we want to examine the max flow min cut problem.

## Directed Graph, Condition of flow


<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter10/max_flow.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig 1] Directed Graph[3]</figcaption>
</p>
</figure>


There is a directed graph $$G = (V, E)$$ as shown above, and let the edge connecting vertex i and vertex j, $$(i,j)\in E$$, i.e., the flow from i to j, be $$f_{ij}$$. Each edge has a capacity, i.e., the maximum flow that can flow through it. Let this be $$c_{ij}$$.

As a simple example, this can be understood as a graph representation of some flow from a source(s) flowing out to a sink(t). It is a graph form that can be applied to various problems such as urban drainage/power transmission planning, material transportation, etc.

Here, the flow satisfies three conditions.

1. $$f_{ij}$$ is always a positive number greater than or equal to 0: $$f_{ij} \geq 0,\, (i,j)\in E$$
2. $$f_{ij}$$ must be less than the maximum flow determined for the edge, i.e., the capacity (limit capacity) $$c_{ij}$$: $$f_{ij}<c_{ij}, \, (i,j)\in E$$
3. For vertex k excluding the source (the point where flow comes out, s) or sink (the point where flow goes out, t), the total amount of flow entering k equals the total amount of flow leaving k: $$\sum_{(i,k)\in E}f_{ik} = \sum_{(k,j)\in E}f_{kj}, \, k\in V\backslash{s,t}$$

## Relationship between Max flow and Min cut problem(1)

For the graph and flow defined above, we will examine two well-known problems, the max flow problem and the min cut problem, and the relationship between them.

To conclude first, the max flow problem is an LP problem, and the min cut problem is an integer program, where the dual of the max flow problem has the same problem form as the LP relaxation of the min cut problem.

>$$
>\begin{align}
>\text{Value of max flow} &\leq \text{dual LP of max flow}\\
>&= \text{Optimal value for LP relaxed min cut}\\
>&\leq \text{Capacity of min cut}\\
>\end{align}
>$$

In this page, we will show the inequality relationship by the reverse process of dual and relaxation (adding constraints to the LP problem to convert it to an integer program). Although not covered here, in reality, all three results are equal.

This is called the max flow min cut theorem, which states that the maximum flow in a network is equal to the minimum capacity of a cut.

More generally, under certain conditions, the optimal values of the primal and dual problems are equal, which is called strong duality.

In LP problems, except for the case where both the primal and dual problems are infeasible, strong duality holds. This will be discussed in Chapter 11.

First, let's look at the two problems, derive the dual from the max flow problem, and show that by adding specific conditions to the dual problem (reverse of relaxation), it transforms into the min cut problem.

## Max flow problem

The max flow problem is to find the maximum flow from s to t in a graph that satisfies the above conditions.

>$$
>\begin{align}
>&\max_{f\in {\mathbb{R}^{|E|}}} &&{\sum_{(s,j)\in E} f_{sj}}\\
>&\text{subject to} &&{f_{ij}\geq 0,\,f_{ij}\leq c_{i,j}\,\, \text{for all }(i, j)\in E}\\
>&&&{\sum_{(i, k)\in E}f_{ik}=\sum_{(k,j)\in E}f_{kj}}\,\, \text{for all }k\in V \backslash \{s,t\}.\\
>\end{align}
>$$

## Min cut problem

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter10/min_cut.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig 2] Graph Cut Example[3]</figcaption>
</p>
</figure>

The min cut problem divides all vertices of the graph into two sets: the shaded region and the unshaded region, as shown in the figure. One set contains the source, and the other contains the sink, while the remaining vertices are arbitrarily assigned to either set (here, the set containing the source is called A, and the set containing the sink is called B). The sum of the capacities of the edges going from set A to set B is defined as the cut.

In other words, a cut is a partition of the graph's vertices such that the source and sink are in different partitions. The min cut problem is to find the minimum value of this cut for a given graph. In the general definition of the min cut problem, since it is defined on a directed graph, it always satisfies source $$x_{s}=1$$, sink $$x_{t}=0$$. This part is omitted in the problem definition below.

>$$
>\begin{align}
>&\min_{b\in {\mathbb{R}^{|E|}},\, x \in {\mathbb{R}^{|V|}} } &&{\sum_{(i,j)\in E} b_{ij}c_{ij}}\\
>&\text{subject to} &&{b_{ij} \geq x_{i}-x_{j}}\\
>&&&{b_{ij},\,x_{i},\,x_{j}\,\in \{ 0,1 \} }\\
>&&&\text{for all }i, j.\\
>\end{align}
>$$

Intuitively, the max flow problem is to find the maximum flow from the source, and the min cut problem is to find the minimum total capacity that can be sent from the source set to the sink set, so it is clear that these two problems are closely related.

## Dual of Max flow problem
Let's derive the dual for the max flow optimization problem.

First, define the dual variables for the constraints in order as $$a_{ij}, b_{ij}, x_{k}$$. In the dual of the max problem, the upper bound will be minimized, so the organized form should be in the form of primal objective $$\leq$$ something. Therefore, organize the equation to find the upper bound of $$f_{ij}$$ for the constraints.
This can be organized as follows.

>$$
>\begin{align}
>\sum_{(i,j)\in E} {\Big(-a_{ij}f_{ij}+b_{ij}(f_{ij}-c_{ij})\Big)} + \sum_{k \in V\backslash \{s,t\}} x_{k}\Big( \sum_{(i,k)\in E} f_{ik} - \sum_{(k,j)\in E } f_{kj} \Big)\leq 0\\
>\text{for any }a_{ij}, b_{ij} \geq 0, (i, j)\in E, \text{ and } x_{k}, k\in V \backslash \{s,t\}.
>\end{align}
>$$

Organize the $$f$$ terms related to the primal LP objective function on the left, and the rest on the right.

Next, since we want the upper bound of the primal LP, find the equation such that the terms multiplied by $$f$$ on the left match the primal LP objective function.

The condition that satisfies this equation becomes the constraint in the dual LP.

That is, organize the equation so that the $$f_{ij}$$ term is 1 only in $$\sum_{(s,j)\in E}f_{sj}$$ and 0 elsewhere.

This process is detailed as follows.

>$$
>\begin{align}
>\sum_{(i,j)\in E}{\Big((b_{ij}-a_{ij})f_{ij}\Big)}+\sum_{k\in V\backslash \{s,t\}}{x_{k}\Big(\sum_{(i,k)\in E}{f_{ik}}-\sum_{(k,j)\in E}{f_{kj}}\Big)} \leq \sum_{(i,j)\in E}b_{ij}c_{ij}.
>\end{align}
>$$

Here, our goal is to make the result of the left side when $$i=s$$ be $$\sum_{(s,j)\in E}f_{sj}$$ and 0 for other cases.

The k in the x term of the second sigma does not include the source and sink, and can be divided into three cases: when $$i=s, j\neq t$$, when $$i\neq s, j=t$$, and when $$i\neq s,j\neq t$$.

### Case 1. $$i = s, j \neq t.$$

For the term multiplied by $$x_{k}$$, it is eliminated by the third condition of flow except for the case of $$k=j$$.
Therefore, the sigma for the x term of the second term can be organized as follows.

>$$
>\begin{align}
>&=\sum_{(s,j)\in E}{\Big((b_{sj}-a_{sj})f_{sj}\Big)}+x_{j}\sum_{(s,j)\in E}{f_{sj}}+\sum_{k\in V\backslash \\{s,t,j\\}}{x_{k}\Big(\underbrace{\sum_{(s,k)\in E}{f_{sk}}-\sum_{(k,j)\in E}{f_{kj}}}_{=0}\Big)} \\\\
>&=\sum_{(s,j)\in E}{\Big(b_{sj}-a_{sj}+x_{j}\Big)f_{sj}}, \ j \in V \backslash \{s,t\},\\\\
>\end{align}
>$$

### Case 2. $$i \neq s, j = t.$$
For the term multiplied by $$x_{k}$$, it is eliminated by the third condition of flow except for the case of $$k=i$$.
Therefore, the sigma for the x term of the second term can be organized as follows.

>$$
>\begin{align}
>&=\sum_{(i,t)\in E}{\Big((b_{it}-a_{it})f_{it}\Big)}-x_{i}\sum_{(i,t)\in E}{f_{it}}+\sum_{k\in V\backslash \{s,t,i\}}{x_{k}\Big(\underbrace{\sum_{(i,k)\in E}{f_{ik}}-\sum_{(k,t)\in E}{f_{kt}}}_{=0}\Big)} \\\\
>&=\sum_{(i,t)\in E}{\Big(b_{it}-a_{it}-x_{i}\Big)f_{it}}, \ i \in V\backslash \{s,t\},\\\\
>\end{align}
>$$

### Case 3. $$i \neq s, j \neq t.$$
For the term multiplied by $$x_{k}$$, it is eliminated by the third condition of flow except for the cases of $$k=i$$ and $$k=j$$.
Therefore, the sigma for the x term of the second term can be organized as follows.

>$$
>\begin{align}
>&=\sum_{(i,j)\in E}{\Big((b_{ij}-a_{ij})f_{ij}\Big)}+x_{j}\sum_{(i,j)\in E}{f_{ij}}-x_{i}\sum_{(i,j)\in E}{f_{ij}}+\sum_{k\in V\backslash \{s,t,i,j\}}{x_{k}\Big(\underbrace{\sum_{(i,k)\in E}{f_{ik}}-\sum_{(k,j)\in E}{f_{kj}}}_{=0}\Big)} \\\\
>&=\sum_{(i,j)\in E}{\Big(b_{ij}-a_{ij}+x_{j}-x_{i}\Big)f_{ij}}, \ i, j \in V \backslash \{s,t\}. \\\\
>\end{align}
>$$

The objective function of the primal LP matches with the case 1 of the above, where the term is 1 in $$b_{sj}-a_{sj}+x_{j}$$, and for the other cases, it makes the multiplied term 0, completing the form of left side being the objective function and the right side being the upper bound.

>$$
>\begin{align}
>&b_{sj}-a_{sj}+x_{j} = 1\\\\
>&b_{it}-a_{it}-x_{i} = 0\\\\
>&b_{ij}-a_{ij}+x_{j}-x_{i} = 0\\\\
>&\text{Result in,} \\\\
>&\sum_{(s,j)\in E}{f_{sj}} \leq \sum_{(i,j)\in E}{b_{ij}c_{ij}}.
>\end{align}
>$$

Therefore, the dual problem is to find the minimum value of the upper bound (objective function of dual LP) for the dual variables $$a, b, x$$, and this minimum value becomes the best upper bound. A dummy variable $$a$$ is eliminated while maintaining the conditions. Additionally, by adding the condition that flow occurs from source to sink in the directed graph, the equation becomes:

>$$
>\begin{align}
>&\min_{b\in {\mathbb{R}^{|E|}},\, x\in{\mathbb{R}^{|V|}}}  &&{\sum_{(i,j)\in E} b_{ij}c_{ij}} \\\\
>&\text{subject to} &&{b_{ij}+x_{j}-x_{i}\geq 0 \,\, \text{for all } (i,j)\in E}\\\\
>&&&{b\geq 0, x_{s}=1,x_{t}=0}.\\\\
>\end{align}
>$$

## Dual LP to Integer program
Now, we want to show that this dual LP is the same as the LP relaxation of the min cut problem.
Therefore, we will go through the process of converting it to an integer program by adding conditions to the above dual LP problem.
The variable $$x$$ is not defined for vertices other than s and t.
Therefore, to narrow the scope of the problem, let's add a condition that the remaining vertices except s and t belong to either group s or t.
In other words, let's assume that all vertices belong to either group 0 or 1. This is equivalent to determining the vertex partition for the min cut.

>$$
>\begin{align}
>x_{i} \in \{0,1 \} \ \ \text{ for all }i\in V.
>\end{align}
>$$

Let's define the group that belongs to 1 as set A, and the group that belongs to 0 as set B. Also, let's define that the source (s) belongs to A, and the sink (t) belongs to B.

With the above definitions, $$b_{ij}$$ acts as an on/off switch, being 1 for edges going from set A to set B, and 0 otherwise.

This can be organized as follows.

>$$
>\begin{align}
>&\text{Let } A= \{ i:x_{i}=1 \} ,\, B= \{ i:x_{i}=0 \} \\\\
>&\text{note that  } s \in A, \,t \in B, \text{ and  }b_{ij}\geq x_{i}-x_{j} \,\,\,\, \text{for }\,(i,j) \in E, \,\, b\geq 0,\\\\
>\end{align}
>$$
>$$
>\begin{align}
>\text{Simply say, } \qquad \begin{cases} b_{ij}=1 \qquad \text{if } i\in A, j\in B\\\\
>0 \qquad\qquad \text{otherwise}.\end{cases}
>\end{align}
>$$

The above result is the same as the formulation of the min cut problem.

## Relationship between Max flow and Min cut problem(2)
That is, the dual problem of the max flow problem is the result of removing the condition that the vertices except s and t in the min cut problem are included in 0 or 1 (relaxation). The optimal value of max flow $$\leq$$ dual LP (upper bound), and this relaxation expands the domain scope of the optimization variable, so the optimal value LP relaxed min cut $$\leq$$ capacity of min cut. Summarizing these three results, we get the following result.

>$$
>\begin{align}
>\text{Value of max flow} &\leq \text{Dual LP of max flow}\\\\
>&= \text{Optimal value for LP relaxed min cut}\\\\
>&\leq \text{Capacity of min cut}\\\\
>\end{align}
>$$

For the equality of these three results, refer to the max-flow min-cut theorem[11], and for a representative algorithm for solving the max flow min cut problem, refer to the Ford-Fulkerson algorithm[12].
