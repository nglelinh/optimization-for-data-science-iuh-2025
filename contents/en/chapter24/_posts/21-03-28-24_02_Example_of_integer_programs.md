---
layout: post
title: 24-02 Examples of integer programs
chapter: '24'
order: 3
owner: YoungJae Choung
categories:
- chapter24
lang: en
---

In this section, let's examine various examples corresponding to Integer programming and learn how they are utilized.

## Knapsack problem
The Knapsack problem is a traditional combinatorial optimization problem where the volume that can be put into the knapsack is limited, constraining the total magnitude of items that can fit inside the knapsack. When this constraint exists, the problem aims to select items with maximum value. This problem can be expressed using binary variables $$x$$, where $$x_{j}$$ takes a value of 0 or 1 depending on whether the $$j$$-th item is selected or not.

> $$
> \begin{align}
> &\max_{x} && c^\intercal x \\\\
> &\text{subject to } && a^\intercal x \leq b \\\\
> &&&x_{j} \in {0, 1}, j = 1, \dotsc , n
> \end{align}
> $$

$$c_{j}, a_{j}$$ represent the value and magnitude (volume) of the $$j$$-th item, respectively.

## Assignment problem
Let's assume there are $$n$$ people and $$n$$ tasks. Each person can be assigned to exactly one task. Here, $$c_{ij}$$ represents the cost required for person $$i$$ to perform task $$j$$. The Assignment problem aims to assign $$n$$ people to $$n$$ tasks with the minimum cost. To optimize these conditions, the mathematical formulation is as follows:

> $$
> \begin{align}
> &\min_{x} &&\sum_{i = 1}^{n} \sum_{j = 1}^{n} c_{ij} x_{ij} \\\\
> &\text{subject to } &&\sum_{i = 1}^{n} x_{ij} = 1, j = 1 \dotsc n \\\\
> &&&\sum_{j = 1}^{n} x_{ij} = 1, i = 1 \dotsc n \\\\
> &&&x_{ij} \in \lbrace 0, 1\rbrace \quad i = 1 \dotsc n, \quad j = 1 \dotsc n
> \end{align}
> $$


## Facility location problem
The Facility location problem aims to minimize transportation costs from specific facilities to customers.<br>

Let's assume there are depots $$N = \lbrace 1, \dotsc, n \rbrace$$ and customers $$M = \lbrace 1, \dotsc, m \rbrace$$.<br>
The fixed cost $$f_{j}$$ is associated with using depot $$j$$.
The transportation cost $$c_{ij}$$ is the cost incurred when goods delivered to customer $$i$$ are transported from depot $$j$$.<br>

The decisions to be made here are which depots should be operational and which customers should receive deliveries from each depot, with the goal of minimizing both fixed costs and transportation costs by deriving and solving the mathematical formulation.

> $$
> \begin{align}
> &\min_{x, y} && \sum_{i = 1}^{n} f_{j} y_{j} + \sum_{i = 1}^{m} \sum_{j = 1}^{n} c_{ij} x_{ij} \\
> &\text{subject to } && \sum_{j = 1}^{n} x_{ij} = 1,  \quad i = 1 \dotsc m \\
> &&& x_{ij} \leq y_{j},  \quad i = 1 \dotsc m,  \quad j = 1 \dotsc n \\
> &&& x_{ij} \in \lbrace 0, 1\rbrace \quad i = 1 \dotsc m, \quad j = 1 \dotsc n \\
> &&& y_{j} \in \lbrace 0, 1\rbrace \quad j = 1 \dotsc n \\
> \end{align}
> $$

The first constraint means that each customer can receive goods from one depot. The second constraint states that depot $$j$$ must be operational for customer $$i$$ to receive goods from there. Since both $$x_{ij}$$ and $$y_{j}$$ are binary, we can consider $$mn$$ constraints. This can also be expressed in a "marginalized" form as the following constraint:

> $$ \sum_{i = 1}^{n} x_{ij} \leq m y_{j}, \quad j = 1 \dotsc n $$

Reflecting this, it can be replaced with the following mathematical formulation:

> $$
> \begin{align}
> &\min_{x, y} &&\sum_{i = 1}^{n} f_{j} y_{j} + \sum_{i = 1}^{m} \sum_{j = 1}^{n} c_{ij} x_{ij} \\
> &\text{subject to } &&\sum_{j = 1}^{n} x_{ij} = 1,  \quad i = 1 \dotsc n \\
> &&& \sum_{i = 1}^{n} x_{ij} \leq m y_{j}, \quad j = 1 \dotsc n \\
> &&& x_{ij} \in \lbrace 0, 1\rbrace \quad i = 1 \dotsc n, \quad j = 1 \dotsc n \\
> &&& y_{j} \in \lbrace 0, 1\rbrace \quad j = 1 \dotsc n \\
> \end{align}
> $$


## K-means and K-medoids clustering
Clustering is the process of dividing data into similar groups. The K-means algorithm aims to find K clusters by finding $$K$$ center values (centroids) that minimize the average distance between data points within clusters. The goal is to find a partition $$S_{1} \cup \dotsc \cup S_{K} = \lbrace 1, \dotsc, n \rbrace$$ for the given data. In this case, the following formula is minimized:

$$ \sum_{i = 1}^{K} \sum_{j \in S_{i}} \| x^{(j)} - \mu^{(i)} \|^{2} $$

where $$ \mu^{(i)} :  = \frac{1}{| S_{i} |} \sum_{j \in S_{i}} x^{(i)} $$,
$$ \mu^{(i)} $$ represents the centroid of cluster $$i$$.

A method that is more robust to outliers than computing centroids by averaging (K-means) is K-medoids clustering, which sets the center value as the data point closest to the cluster center instead of computing the center values of K clusters using arithmetic mean.
That is, K-medoids clustering is a method that considers each data point ($$y^{(i)}$$) as a center point and designates the data point that yields the minimum value when computed as the centroid.

>$$\sum_{i = 1}^{K} \sum_{j \in S_{i}} \| x^{(j)} - y^{(i)} \|^{2} $$
>$$\text{where } y^{(i)} \in \lbrace x^{(j)} : j \in S_{i} \rbrace $$

<br>
This problem can be transformed and represented as an integer program.
First, we define $$ d_{ij} = \| x^{(i)} - x^{(j)} \|^2 $$ and define the following two binary variables:

$$\begin{align}
&w_{i} =\begin{cases}1 && \text{if choose } x^{(i)} \text{ as a centroid} \\\\
0 && \text{otherwise.} \end{cases}\\\\
&z_{ji} =\begin{cases}1 && \text{if } x^{(j)} \text{ in the cluster with centroid } x^{(i)} \\\\
0 && \text{otherwise.} \end{cases}
\end{align}$$

<br>

The K-medoids problem can be defined as an optimization problem as follows:

> $$
> \begin{align}
> &\min_{w, z} && \sum_{i = 1}^{n} \sum_{j = 1}^{n} d_{ij} z_{ji} \\\\
> &\text{subject to } && z_{ji} \leq w_{i} \\\\
> &&& \sum_{i = 1}^{n} w_{i} = k \\\\
> &&& w_{ij} \in 0, 1 \quad i = 1 \dotsc n \\\\
> &&& z_{ji} \in 0, 1 \quad j, i = 1 \dotsc n
> \end{align}
> $$

The first constraint means that after the centroid is first determined, we will determine whether $x_{j}$ belongs to $x_{i}$ or not.

## Best subset selection
When the conditions $$X = [x^{1} \quad \dotsc \quad x^{p}] \in \mathbb{R}^{n×p}, \quad y \in \mathbb{R}^{n}$$ are given, the Best subset selection problem is as follows:

> $$
> \begin{align}
> &\min_{\beta} &&\frac{1}{2} \| y - X\beta \|^{2} \\\\
> &\text{subject to } &&\| \beta \| \leq k\\\\
> \end{align}$$
> $$\begin{align}
> \text{where}  \| \beta \|_{0}  :  = \text{ the number of nonzero entries of } \beta.
> \end{align}
> $$

Since $$ \| \beta \|_{0} $$ is a non-convex constraint, the problem can be solved more easily by transforming it using Integer programming.

> $$
> \begin{align}
> &\min_{\beta, z} && \frac{1}{2} \| y - X\beta \|^{2} \\\\
> &\text{subject to } && | \beta_{i} | \leq Mz_{i} \quad i = 1 \dotsc n \\\\
> &&&z_{ji} \in \lbrace 0, 1 \rbrace \quad i = 1 \dotsc n \\\\
> &&&\sum_{i = 1}^{p} z_{i} \leq k
> \end{align}
> $$

## Least median of squares regression
When the conditions $$X = [x^{1} \quad \dotsc \quad x^{p}] \in \mathbb{R}^{n×p}, \quad y \in \mathbb{R}^{n}$$, and $$\beta \in \mathbb{R}^{p}$$ are given, if we define $$r : = y - X\beta$$, the Least median of squares regression problem is as follows:

> $$\beta_{LMS} : = \arg\min_{\beta} (median | r_{i} | ).$$
