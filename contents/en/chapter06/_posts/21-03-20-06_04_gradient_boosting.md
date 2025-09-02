---
layout: post
title: 06-04 Gradient boosting
chapter: '06'
order: 14
owner: Kyeongmin Woo
categories:
- chapter06
lang: en
---

# Gradient boosting

**Gradient boosting** is a method that uses gradient descent to sequentially create trees while compensating for the errors of previous trees when trying to predict results with an ensemble model composed of multiple trees. **Gradient Boosting** can be used for both regression and classification.

* For detailed information, refer to the [Gradient Boosting from scratch](https://medium.com/mlreview/gradient-boosting-from-scratch-1e317ae4587d) blog


### [Reference] Functional gradient descent algorithm
**Gradient boosting** was introduced as a functional gradient descent algorithm by Llew Mason, Jonathan Baxter, Peter Bartlett and Marcus Frean. The functional gradient descent algorithm optimizes the loss function over function space by repeatedly selecting functions that have the negative direction of the gradient, thus performing gradient descent.

* For detailed information, refer to [Gradient Boosting](https://en.wikipedia.org/wiki/Gradient_boosting)

### [Reference] Boosting vs Bagging
**Boosting** is an ensemble technique that sequentially generates weak learners to predict results. The next stage learner learns from the data that the previous stage learner predicted incorrectly, and the results of sequentially generated learners are combined to create the final result.

**Bagging** is an ensemble technique that generates weak learners independently from each other to predict results. Therefore, each learner runs in parallel and their results are combined to create the final result.

* For detailed information, refer to the [What is the difference between Bagging and Boosting?](https://quantdare.com/what-is-the-difference-between-bagging-and-boosting/) blog
## Gradient Boosting
Let's examine the background of how **Gradient Boosting** came to be developed.

Suppose there is an ensemble model composed of trees that is used for classification. This model will want to predict results that minimize the error with the observed values. Let the observed values be $$y_i$$, $$i=1,\dots,n$$, the input data be $$x_i, i=1,\dots,n$$, and the predicted values be $$u_i$$, $$i=1,\dots,n$$.

As shown in the figure below, each tree belonging to the ensemble receives $$x_i \in R^p$$ as input and outputs results according to the branching conditions in the tree's nodes.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter06/06_04_tree_O9zyAlk.png" alt="tree_O9zyAlk" width="80%" height="80%">
  <figcaption style="text-align: center;">$$\text{[Fig 1] Example of Tree }T_j\text{ [3]}$$</figcaption>
</p>
</figure>

The predicted value $$u_i$$ of the ensemble model can be calculated by weighted summation of each tree's results. (Here, $$T_j(x_i)$$ is the result output by tree $$j$$ when it receives $$x_i$$ as input.)

>
$$ \begin{equation}
u_i = \sum_{j=1}^M \beta_j T_j(x_i)
\end{equation} $$

For the loss function, it can be defined as $$L=(y_i,u_i)=(y_i - u_i)^2$$ in the form of sum of squared errors to minimize the error between observed and predicted values.
>
$$ \begin{equation}
\min_{\beta} \sum_{i=1}^n L\left(y_i, \sum_{j=1}^M \beta_j T_j(x_i)\right)
\end{equation} $$

Generally, when constructing trees in ensemble models, many small trees with fixed depth are created. This is because making trees smaller uses less memory and enables faster prediction, and as the number of trees increases, the performance of the ensemble improves. Generally, the depth of trees is fixed at 5 or less.

Therefore, in this problem, the node conditions defined in each tree are very diverse and the results of very many trees are linearly combined, making the tree space quite large. Thus, it can be said that this is a very difficult problem to optimize.

To solve this problem, the optimization problem must be transformed into an easier one. The original optimization problem is to find $$M$$ weights $$\beta_j$$ that minimize the loss function. Let's think of this problem as a minimization problem $$\min_{u} f(u)$$ of function $$f(u)$$ with respect to predicted values $$u$$. If function $$f(u)$$ is the loss function $$L(y,u)$$, then finding $$u$$ that minimizes the loss function can be said to be an easily redefined problem. (Here, $$n$$ is the number of data points.)

**Gradient boosting** refers to the technique of solving the redefined minimization problem $$\min_{u} f(u)$$ using gradient descent.

## Algorithm
The **Gradient boosting** algorithm performs gradient descent in the following way to find the optimal solution $$u^*$$ of $$\min_u L(y, u)$$.

1. Set the initial value as the result of an arbitrary tree: $$u^{(0)}=T_0$$. Then repeat the following steps 2~4.

2. Calculate the negative gradient for $$u^{(k-1)}$$, which is the most recent predicted value for $$n$$ data points.
>
$$ \begin{equation}
d_i = - \left . \left[ \frac{\partial L(y_i,u_i)}{\partial u_i} \right] \right|_{u_i = u_i^{(k-1)}}, i=1,\dots,n
\end{equation} $$

3. Find the tree $$T_k$$ whose results $$T(x_i)$$ are most similar to the gradients $$d_i$$ for $$n$$ data points.
>
$$ \begin{equation}
\min_{\text{trees } T} \sum_{i=1}^n (d_i-T(x_i))^2
\end{equation} $$

4. Calculate the step size $$a_k$$ and update the predicted values using the $$T_k$$ found above.
>
$$u^{(k)}=u^{(k-1)} + \alpha_k T_k$$

This algorithm finds the gradient $$d$$ with respect to $$u$$ to find the optimal solution $$u^*$$ through gradient descent, finds $$T_k$$ closest to $$d$$, and substitutes $$T_k$$ instead of gradient in the update equation to find the next position.

The final predicted value $$u^*$$ obtained in this way can be seen to be identical to the weighted summation of tree results defined earlier. (That is, if we expand the recursive update equation $$u^{(k)}=u^{(k-1)} + \alpha_k T_k$$ back to $$k=0$$, we get $$u^* = \sum_{k=1}^n \alpha_k T_k$$, which can be made into the form of weighted summation of tree results.)





