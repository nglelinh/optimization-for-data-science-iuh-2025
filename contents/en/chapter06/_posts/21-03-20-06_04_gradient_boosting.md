---
layout: post
title: 06-04 Gradient boosting
chapter: '06'
order: 16
owner: Kyeongmin Woo
categories:
- chapter06
lang: en
---

Up to now, gradient descent has updated a finite vector of numbers $$x \in \mathbb{R}^n$$. Now make a dazzling conceptual leap due to Jerome Friedman (2001): what if the object you are optimizing is not a vector of weights, but an entire *prediction function* $$F(x)$$? Take gradient descent in function space—fitting each new decision tree to the negative gradient of the loss—and you have **Gradient Boosting** (XGBoost, LightGBM, CatBoost), the reigning champion of tabular machine learning.

## Key ideas: Gradient Descent in Function Space

1. **Functional Gradient Descent**: Given data $$\{(x_i, y_i)\}_{i=1}^N$$ and differentiable loss $$\mathcal{L}(F) = \sum_{i=1}^N L(y_i, F(x_i))$$, treat the vector of predictions $$\mathbf{f} = (F(x_1), \dots, F(x_N))^T \in \mathbb{R}^N$$ as the optimization variable. The negative functional gradient at sample $$i$$ is the *pseudo-residual*
   $$r_{im} = -\left[\frac{\partial L(y_i, F(x_i))}{\partial F(x_i)}\right]_{F = F_{m-1}}.$$
2. **Projecting onto Weak Learners (Trees)**: An arbitrary vector $$r_m \in \mathbb{R}^N$$ cannot predict on unseen test points. Gradient boosting projects $$r_m$$ onto the space of shallow regression trees by fitting a tree $$h_m(x)$$ to the targets $$\{(x_i, r_{im})\}$$, then updating $$F_m(x) = F_{m-1}(x) + \eta h_m(x)$$.
3. **Special Case — Squared Error = Residual Fitting**: For $$L(y, \hat{y}) = \frac{1}{2}(y - \hat{y})^2$$, the negative gradient is simply $$r_i = y_i - F_{m-1}(x_i)$$, the ordinary residual! Changing $$L$$ to logistic loss or Huber loss immediately yields classification or robust regression with the exact same algorithm.
4. **Boosting vs. Bagging (Bias vs. Variance)**: Random Forests (Bagging) average *independent* deep trees in parallel to cut variance; Gradient Boosting adds *sequential* shallow trees along negative gradients to systematically eliminate bias (while learning rate $$\eta \ll 1$$ prevents overfitting).

### Worked example: One Boosting Round for Squared-Error Regression

Given four data points with targets $$y = (10, 12, 20, 22)$$ at features $$x = (1, 2, 5, 6)$$, run Round 0 and Round 1 of Gradient Boosting with squared loss $$L(y, \hat{y}) = \frac{1}{2}(y - \hat{y})^2$$, learning rate $$\eta = 0.5$$, and decision stumps (depth-1 trees).

1. **Initialize $$F_0(x)$$ with the constant minimizing total squared loss**:
   $$F_0(x) = \bar{y} = \frac{10 + 12 + 20 + 22}{4} = 16.$$
   Initial squared loss: $$\frac{1}{2}\bigl((-6)^2 + (-4)^2 + 4^2 + 6^2\bigr) = \frac{1}{2}(36 + 16 + 16 + 36) = 52.$$
2. **Compute pseudo-residuals (negative gradients) $$r_{i1} = y_i - F_0(x_i)$$**:
   $$r_1 = (-6,\; -4,\; +4,\; +6).$$
3. **Fit a depth-1 regression stump $$h_1(x)$$ to $$r_1$$**:
   - Split at $$x \le 3.5$$: left leaf averages $$\{-6, -4\} \to -5$$; right leaf averages $$\{+4, +6\} \to +5$$.
   - Thus $$h_1(x) = -5$$ if $$x \le 3.5$$, else $$+5$$.
4. **Update the ensemble with shrinkage $$\eta = 0.5$$**:
   $$F_1(x) = F_0(x) + 0.5 h_1(x) = \begin{cases} 16 - 2.5 = 13.5 & \text{if } x \le 3.5, \\ 16 + 2.5 = 18.5 & \text{if } x > 3.5. \end{cases}$$
   New residuals: $$(-3.5, -1.5, +1.5, +3.5)$$; new loss: $$\frac{1}{2}(12.25 + 2.25 + 2.25 + 12.25) = 14.5$$ — cutting the loss by **72%** in one stump!

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





