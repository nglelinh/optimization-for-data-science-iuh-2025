layout: post
title: 15-04 Barrier method v.0 and v.1
chapter: "15"
order: 10
owner: "Minjoo Lee"
## Barrier method v.0
**Barrier method v.0** chooses $$t = m/\epsilon$$ for $$\epsilon > 0$$ and solves the following barrier problem to obtain $$f(x^*(t)) - f(x^*) \le \epsilon $$.
>
$$\begin{align}
 &\min_{x} \ && tf(x) + \phi(x) \\
 &\text{subject to } \ && Ax = b \\
\end{align}$$

Here, $$m$$ is the number of constraints and $$t$$ is a multiple of $$1/\epsilon$$, so as $$\epsilon$$ gets smaller, $$t$$ becomes very large, and eventually the end of the central path is reached, making the problem equivalent to the original problem. Therefore, this can be very slow and difficult to solve.

Thus, a better approach is to follow the central path to find the solution, which leads to the definition of **barrier method v.1**.

## Barrier method v.1
**Barrier method v.1** is a method that gradually increases the value of $$t$$ and solves the following barrier problem multiple times.
>
$$\begin{align}
 &\min_{x} \ && tf(x) + \phi(x) \\
 &\text{subject to } \ && Ax = b \\
\end{align}$$

#### Algorithm
The algorithm can be described as follows.

1. Choose $$t^{(0)} > 0$$ and set $$k := 0$$.
2. At $$t = t^{(0)}$$, solve the barrier problem to obtain $$x^{(0)} = x^*(t)$$.
3. While $$m/t > \epsilon$$ <br>
  3-1. Choose $$t^{(k+1)} > t^{(k)}$$. <br>
  3-2. Initialize Newton's method with $$x^{(k)}$$. (warm start)<br>
        At $$t = t^{(k+1)}$$, solve the barrier problem to obtain $$x^{(k+1)} = x^*(t)$$.<br>
  end while<br>

#### Comments
* **Common update method**: $$t^{(k+1)} = \mu t^{(k)}$$, ($$\mu > 1$$)
* **Warm start** :  단계 3-2에서는 이전 단계의 solution을 다음 단계의 초기값으로 사용하는데 이를 warm start라고 한다.
* **Centering step** :  알고리즘에서 barrier problem을 푸는 단계인 2와 3-2를 centering step ( or outer iteration)이라고 한다.

#### Considerations
$$\mu$$와 $$t^{(0)}$$의 선택에 있어서, 다음의 trade off를 고려해야 한다.
###### $$\mu$$의 선택
* $$\mu$$가 너무 작다면, outer iteration이 많아진다. (이 경우 warm start가 도움이 된다.)<br>
* $$\mu$$가 너무 크다면, 모든 centering step에서 newton method가 수렴할 때까지 iteration을 많이 해야 한다. 

###### 알고리즘 초기값 선택
* $$t^{(0)}$$가 너무 작다면, outer iteration이 많아진다.<br>
* $$t^{(0)}$$가 너무 크다면, v.0과 같은 문제가 된다. 따라서, 첫번째 centering step에서 newton method가 $$x^{(0)}$$을 구하기 위해 iteration을 많이 해야 한다. 

다행히도 실제 barrier method의 성능은 $$\mu$$와 $$t^{(0)}$$의 선택에 매우 robust한 편이다. 그리고, 이들 parameter의 적절한 범위는 문제의 크기에 따라 달라진다.

## Example of small LP
다음 그릠에는 n=50 dimensions, m=100 inequality constraints 조건의 LP 문제를 barrier method로 실행했을 때 성능을 보여주고 있다. $$\mu = 2$$인 경우 outer iteration이 커지고 $$\mu=150$$인 경우에 centering step이 $$\mu=50$$일 때보다 상대적으로 증가했음을 확인할 수 있다.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter15/15_barrier_method_03.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig 1] Example of small LP [3]</figcaption>
</p>
</figure>