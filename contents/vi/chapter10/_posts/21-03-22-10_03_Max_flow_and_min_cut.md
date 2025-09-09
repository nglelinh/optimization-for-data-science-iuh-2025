---
layout: post
title: 10-03 Luồng cực đại và cắt cực tiểu
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

Như một ví dụ về tính đối ngẫu trong chương trình tuyến tính, chúng ta muốn xem xét bài toán luồng cực đại cắt cực tiểu.

## Đồ thị có hướng, Điều kiện của luồng


<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter10/max_flow.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 1] Đồ thị có hướng[3]</figcaption>
</p>
</figure>


Có một đồ thị có hướng $$G = (V, E)$$ như được hiển thị ở trên, và đặt cạnh nối đỉnh i và đỉnh j, $$(i,j)\in E$$, tức là luồng từ i đến j, là $$f_{ij}$$. Mỗi cạnh có một công suất, tức là luồng tối đa có thể chảy qua nó. Đặt đây là $$c_{ij}$$.

Như một ví dụ đơn giản, điều này có thể được hiểu như một biểu diễn đồ thị của một luồng nào đó từ một nguồn(s) chảy ra đến một đích(t). Đây là một dạng đồ thị có thể được áp dụng cho nhiều bài toán khác nhau như quy hoạch thoát nước đô thị/truyền tải điện, vận chuyển vật liệu, v.v.

Ở đây, luồng thỏa mãn ba điều kiện.

1. $$f_{ij}$$ luôn là một số dương lớn hơn hoặc bằng 0: $$f_{ij} \geq 0,\, (i,j)\in E$$
2. $$f_{ij}$$ phải nhỏ hơn luồng tối đa được xác định cho cạnh, tức là công suất (giới hạn công suất) $$c_{ij}$$: $$f_{ij}<c_{ij}, \, (i,j)\in E$$
3. Đối với đỉnh k không bao gồm nguồn (điểm mà luồng ra, s) hoặc đích (điểm mà luồng vào, t), tổng lượng luồng vào k bằng tổng lượng luồng ra khỏi k: $$\sum_{(i,k)\in E}f_{ik} = \sum_{(k,j)\in E}f_{kj}, \, k\in V\backslash{s,t}$$

## Mối quan hệ giữa bài toán Luồng cực đại và Cắt cực tiểu(1)

Đối với đồ thị và luồng được định nghĩa ở trên, chúng ta sẽ xem xét hai bài toán nổi tiếng, bài toán luồng cực đại và bài toán cắt cực tiểu, và mối quan hệ giữa chúng.

Để kết luận trước, bài toán luồng cực đại là một bài toán LP, và bài toán cắt cực tiểu là một chương trình nguyên, trong đó đối ngẫu của bài toán luồng cực đại có cùng dạng bài toán như việc nới lỏng LP của bài toán cắt cực tiểu.

>$$
>\begin{align}
>\text{Giá trị luồng cực đại} &\leq \text{LP đối ngẫu của luồng cực đại}\\
>&= \text{Giá trị tối ưu cho cắt cực tiểu nới lỏng LP}\\
>&\leq \text{Công suất của cắt cực tiểu}\\
>\end{align}
>$$

Trong trang này, chúng ta sẽ chỉ ra mối quan hệ bất đẳng thức bằng quá trình ngược của đối ngẫu và nới lỏng (thêm ràng buộc vào bài toán LP để chuyển đổi nó thành chương trình nguyên). Mặc dù không được đề cập ở đây, trên thực tế, cả ba kết quả đều bằng nhau.

Điều này được gọi là định lý luồng cực đại cắt cực tiểu, nói rằng luồng tối đa trong một mạng bằng công suất tối thiểu của một cắt.

Tổng quát hơn, dưới một số điều kiện nhất định, các giá trị tối ưu của các bài toán nguyên thủy và đối ngẫu bằng nhau, điều này được gọi là tính đối ngẫu mạnh.

Trong các bài toán LP, ngoại trừ trường hợp mà cả bài toán nguyên thủy và đối ngẫu đều không khả thi, tính đối ngẫu mạnh được giữ. Điều này sẽ được thảo luận trong Chương 11.

Đầu tiên, hãy xem xét hai bài toán, suy ra đối ngẫu từ bài toán luồng cực đại, và chỉ ra rằng bằng cách thêm các điều kiện cụ thể vào bài toán đối ngẫu (ngược lại của nới lỏng), nó biến đổi thành bài toán cắt cực tiểu.

## Bài toán luồng cực đại

Bài toán luồng cực đại là tìm luồng tối đa từ s đến t trong một đồ thị thỏa mãn các điều kiện trên.

>$$
>\begin{align}
>&\max_{f\in {\mathbb{R}^{|E|}}} &&{\sum_{(s,j)\in E} f_{sj}}\\
>&\text{với điều kiện} &&{f_{ij}\geq 0,\,f_{ij}\leq c_{i,j}\,\, \text{với mọi }(i, j)\in E}\\
>&&&{\sum_{(i, k)\in E}f_{ik}=\sum_{(k,j)\in E}f_{kj}}\,\, \text{với mọi }k\in V \backslash \{s,t\}.\\
>\end{align}
>$$

## Bài toán cắt cực tiểu

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter10/min_cut.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 2] Ví dụ Cắt Đồ thị[3]</figcaption>
</p>
</figure>

Bài toán cắt cực tiểu chia tất cả các đỉnh của đồ thị thành hai tập hợp: vùng có bóng và vùng không có bóng, như được hiển thị trong hình. Một tập hợp chứa nguồn, và tập hợp khác chứa đích, trong khi các đỉnh còn lại được gán tùy ý vào một trong hai tập hợp (ở đây, tập hợp chứa nguồn được gọi là A, và tập hợp chứa đích được gọi là B). Tổng các công suất của các cạnh đi từ tập hợp A đến tập hợp B được định nghĩa là cắt.

Nói cách khác, một cắt là một phân hoạch các đỉnh của đồ thị sao cho nguồn và đích ở các phân hoạch khác nhau. Bài toán cắt cực tiểu là tìm giá trị tối thiểu của cắt này cho một đồ thị cho trước. Trong định nghĩa tổng quát của bài toán cắt cực tiểu, vì nó được định nghĩa trên một đồ thị có hướng, nó luôn thỏa mãn nguồn $$x_{s}=1$$, đích $$x_{t}=0$$. Phần này được bỏ qua trong định nghĩa bài toán dưới đây.

>$$
>\begin{align}
>&\min_{b\in {\mathbb{R}^{|E|}},\, x \in {\mathbb{R}^{|V|}} } &&{\sum_{(i,j)\in E} b_{ij}c_{ij}}\\
>&\text{với điều kiện} &&{b_{ij} \geq x_{i}-x_{j}}\\
>&&&{b_{ij},\,x_{i},\,x_{j}\,\in \{ 0,1 \} }\\
>&&&\text{với mọi }i, j.\\
>\end{align}
>$$

Trực quan, bài toán luồng cực đại là tìm luồng tối đa từ nguồn, và bài toán cắt cực tiểu là tìm tổng công suất tối thiểu có thể được gửi từ tập nguồn đến tập đích, vì vậy rõ ràng rằng hai bài toán này có liên quan chặt chẽ.

## Đối ngẫu của bài toán Luồng cực đại
Hãy suy ra đối ngẫu cho bài toán tối ưu luồng cực đại.

Đầu tiên, định nghĩa các biến đối ngẫu cho các ràng buộc theo thứ tự là $$a_{ij}, b_{ij}, x_{k}$$. Trong đối ngẫu của bài toán max, cận trên sẽ được tối thiểu hóa, vì vậy dạng được tổ chức phải ở dạng mục tiêu nguyên thủy $$\leq$$ một cái gì đó. Do đó, tổ chức phương trình để tìm cận trên của $$f_{ij}$$ cho các ràng buộc.
Điều này có thể được tổ chức như sau.

>$$
>\begin{align}
>\sum_{(i,j)\in E} {\Big(-a_{ij}f_{ij}+b_{ij}(f_{ij}-c_{ij})\Big)} + \sum_{k \in V\backslash \{s,t\}} x_{k}\Big( \sum_{(i,k)\in E} f_{ik} - \sum_{(k,j)\in E } f_{kj} \Big)\leq 0\\
>\text{với bất kỳ }a_{ij}, b_{ij} \geq 0, (i, j)\in E, \text{ và } x_{k}, k\in V \backslash \{s,t\}.
>\end{align}
>$$

Tổ chức các số hạng $$f$$ liên quan đến hàm mục tiêu LP nguyên thủy ở bên trái, và phần còn lại ở bên phải.

Tiếp theo, vì chúng ta muốn cận trên của LP nguyên thủy, tìm phương trình sao cho các số hạng được nhân với $$f$$ ở bên trái khớp với hàm mục tiêu LP nguyên thủy.

Điều kiện thỏa mãn phương trình này trở thành ràng buộc trong LP đối ngẫu.

Tức là, tổ chức phương trình sao cho số hạng $$f_{ij}$$ chỉ là 1 trong $$\sum_{(s,j)\in E}f_{sj}$$ và 0 ở nơi khác.

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
