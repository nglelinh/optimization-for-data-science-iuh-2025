---
layout: post
title: "09-03 Example: matrix completion"
chapter: "09"
order: 4
owner: "Kyeongmin Woo"
---

# Example: matrix completion

In various applications, measured data is often represented as a matrix. In these cases, most entries in the matrix may be empty, with only a few entries containing observed data, leading to a sparse matrix. The challenge of filling in the missing entries in such a matrix is referred to as the **Matrix completion** problem.

For instance, this issue can occur in recommendation systems when suggesting products or services to customers who have not yet made a purchase.

## Matrix Completion Problem
The **Matrix completion** problem can be articulated as follows:

Let the matrix $$Y \in \mathbb{R}^{m\times n}$$ represent the observed data, and let $$Y_{ij}, (i,j) \in \Omega$$ denote the entries that contain observed data. The matrix $$B$$ is the estimated matrix used to predict the missing entries.

> $$\min_B \frac{1}{2} \sum_{(i,j)\in\Omega} (Y_{ij} −B_{ij})^2 + \lambda\lVert B \rVert_{tr}$$

The first term in the objective function aims to minimize the error between matrix $$B$$ and the observed data, while the second term encourages matrix $$B$$ to be low-rank. (It is assumed that matrix B resides on a low-dimensional manifold.) Consequently, matrix $$B$$ fills in the missing entries with the lowest-dimensional values that align with the observed data.

#### [Reference] Trace Norm
The trace norm of a matrix is defined as the sum of its singular values.

> $$\lVert B \rVert_{tr} = \text{trace}(\sqrt{B^* B}) = \sum_{i=1}^r \sigma_i(B), \quad r = rank(B)$$

Here, $$B^* B$$ is positive semi-definite, and the singular values are ordered as $$\sigma_1(X) \ge ... \ge \sigma_r(X) \ge 0$$.

#### [Reference] **L1** Norm Regularizer vs. Trace Norm Regularizer
This problem can be interpreted as matrix soft-thresholding, where the vector in the original soft-thresholding is substituted with a matrix. In the regularizer term, the **L1** norm regularizer for vectors ($$\lVert \cdot \rVert_{1}$$) is replaced by the trace norm regularizer ($$\lVert \cdot \rVert_{tr}$$) for matrices, and indeed, the functions of the two regularizers are analogous.

The **L1** norm regularizer induces sparsity in the vector, while the trace norm regularizer similarly induces sparsity in the singular value vector of the matrix. When the matrix is diagonal, the diagonal elements can be viewed as the singular value vector, and the trace norm regularizer minimizes the sum of the singular values, promoting sparsity in the singular value vector.

In this context, the trace norm $$\lVert B \rVert_{tr}$$ serves as an approximation for $$\text{Rank}(B)$$.

## Proximal gradient descent
When this problem is framed using a projection operator, proximal gradient descent can be effectively utilized.
#### Projection Operator
Let's define the projection operator $$P_\Omega$$ for the observed values as follows:

> $$[ P_\Omega(B) ] _{ij} =
> \begin{cases}
B_{ij}, & (i,j) ∈ \Omega \\\
0, & (i,j) \notin \Omega
> \end{cases}$$

#### Objective Function
Utilizing the projection operator, the objective function is defined as:

>$$f(B) = \underbrace{ \frac{1}{2} \lVert P_\Omega(Y) − P_\Omega(B) \rVert_F^2 }_{g(B)} + \underbrace{ \lambda \lVert B \rVert_{tr} }_{h(B)}$$

Now, the function $$f(B)$$ consists of a differentiable part $$g(B)$$ and a non-differentiable part $$h(B)$$.

#### Proximal Mapping
To apply proximal gradient descent, we need to compute the gradient of the function $$g(B)$$ and define the proximal mapping.

* Gradient of $$g(B)$$: $$\nabla g(B) = −(P_\Omega(Y )−P_\Omega(B))$$
* Proximal mapping: 

> $$ \begin{align}
\text{prox}_t (B) = \underset{Z}{\text{argmin}} \frac{1}{2t} \Vert B−Z \Vert_F^2 + \lambda \Vert Z \Vert_{tr}
\end{align} $$

#### Matrix SVD & Soft-thresholding
The proximal mapping corresponds to matrix soft-thresholding at level $$\lambda$$: $$\text{prox}_t(B) = S_{\lambda t}(B)$$.

Typically, matrix $$B$$ is large, so Singular Vector Decomposition (SVD) is employed to minimize the computational load. If we perform SVD such that $$B = U \Sigma V^T$$, then $$S_\lambda(B)$$ can be defined as:

> $$ S_\lambda(B) = U \Sigma_\lambda V^T$$

Here, $$\Sigma_\lambda$$ is a diagonal matrix defined as follows:

> $$(\Sigma_\lambda)_{ii} = \max \{ \Sigma_{ii} −\lambda,0 \}$$
 

#### [Reference] $$(\Sigma_\lambda)_{ii} = \max \{ \Sigma_{ii} −\lambda,0 \}$$  inducement
How is this expression derived? Assuming $$\text{prox}_t(B) = Z$$, we have:
(Differentiating the right-hand side of $$\text{prox}_t(B)$$ with respect to Z yields the following result.)

> $$0 ∈ Z − B + \lambda t \cdot \partial \lVert Z \rVert_{tr}$$

Rearranging this expression gives:

>$$\begin{align}
Z & = B - \lambda t \cdot \partial \lVert Z \rVert_{tr} \\
 & = U \Sigma V^T - \lambda t \cdot (UV^T + W) \\
 & = U (\Sigma - \lambda t) V^T - \lambda t  W \\
 & = U (\Sigma - \lambda ) V^T  \\
\end{align}$$

The final expression can be obtained when the Lipschitz constant is $$L=1$$ and $$W$$ is 0.

Thus, we have $$\text{prox}_t(B) = S_\lambda(B) = Z$$, leading to the derivation of the following expression:

> $$(\Sigma_\lambda)_{ii} = \max \{ \Sigma_{ii} −\lambda,0 \}$$

#### [Reference] Derivative of Trace Norm
If $$Z = U \Sigma V^T$$, the derivative of the trace norm is given by: 
> $$\partial \lVert Z \rVert_{tr} = \{UV^T + W : \lVert W \rVert_{op} ≤ 1, U^TW = 0, WV = 0 \}$$

Here, $$\lVert W \rVert_{op}$$ represents the operator norm, with the largest singular value being less than 1. Additionally, $$W$$ is orthogonal to both $$U^T$$ and $$V$$.

* For proof, refer to [Derivative of the nuclear norm with respect to its argument](https://math.stackexchange.com/questions/701062/derivative-of-the-nuclear-norm-with-respect-to-its-argument)

#### Proximal gradient update
Now, let's define the proximal gradient update equation.

> $$B^+ = S_{\lambda t} ( B + t( P_\Omega(Y) − P_\Omega(B) ) )$$

When $$L = 1$$, $$\nabla g(B)$$ is Lipschitz continuous, allowing us to choose a fixed step size of $$t = 1$$.

Consequently, the update equation simplifies to:

> $$B^+ = S_\lambda (P_\Omega(Y) + P_\Omega^\bot (B) )$$

Here, $$P_\Omega^\bot$$ represents the projection onto the unobserved values, satisfying the equation $$P_\Omega(B) + P_\Omega^\bot (B) = B$$.

In this equation, $$P_\Omega(Y)$$ denotes the observed part, while $$P_\Omega^\bot (B)$$ represents the missing part. The $$S_\lambda$$ function is straightforward to compute, as it only requires performing SVD and calculating $$(\Sigma_\lambda)_{ii} = \max \{ \Sigma_{ii} −\lambda,0 \}$$.

## Soft-Impute Algorithm
This algorithm is known as **Soft-Impute** and provides a simple yet effective solution for matrix completion. When dealing with large matrices, the computational cost of SVD can be high. However, due to the sparsity of $$P_\Omega(Y)$$ and the low rank of $$P_\Omega^\bot (B)$$ in this algorithm, SVD can be performed efficiently.

* For more detailed information, please refer to the paper: Mazumder et al. (2011), "Spectral regularization algorithms for learning
large incomplete matrices"

