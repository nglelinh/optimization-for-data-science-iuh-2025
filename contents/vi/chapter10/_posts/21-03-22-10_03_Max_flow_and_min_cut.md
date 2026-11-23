---
layout: post
title: 10-03 Luồng cực đại và lát cắt cực tiểu
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

Để minh họa tính đối ngẫu trong quy hoạch tuyến tính, bài học này sẽ phân tích cặp bài toán luồng cực đại (max flow) và lát cắt cực tiểu (min cut).

## Đồ thị có hướng và các điều kiện của luồng

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter10/max_flow.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 1] Đồ thị có hướng[3]</figcaption>
</p>
</figure>

Xét một đồ thị có hướng $$G = (V, E)$$ như Hình 1. Trên mỗi cạnh có hướng $$(i, j) \in E$$ nối từ đỉnh $$i$$ đến đỉnh $$j$$, ta ký hiệu $$f_{ij}$$ là lượng luồng chảy qua cạnh đó và $$c_{ij}$$ là dung lượng (lượng luồng tối đa mà cạnh có thể tải).

Mô hình đồ thị này biểu diễn sự lưu chuyển từ một đỉnh nguồn $$s$$ đến một đỉnh đích $$t$$, thường gặp trong các bài toán thực tế như quy hoạch thoát nước đô thị, truyền tải điện năng hay vận chuyển hàng hóa.

Một luồng hợp lệ phải thỏa mãn ba điều kiện sau:

1. Luồng trên mỗi cạnh không âm: $$f_{ij} \geq 0,\, (i,j)\in E$$.
2. Luồng trên mỗi cạnh không vượt quá dung lượng của cạnh đó: $$f_{ij} \leq c_{ij}, \, (i,j)\in E$$.
3. Bảo toàn luồng tại các đỉnh trung gian: với mọi đỉnh $$k$$ khác nguồn $$s$$ và đích $$t$$, tổng luồng đi vào $$k$$ bằng tổng luồng đi ra khỏi $$k$$: $$\sum_{(i,k)\in E}f_{ik} = \sum_{(k,j)\in E}f_{kj}, \, k\in V\backslash\{s,t\}$$.

## Mối quan hệ giữa bài toán luồng cực đại và lát cắt cực tiểu (1)

Trên đồ thị có hướng đã định nghĩa, ta xét hai bài toán kinh điển là bài toán luồng cực đại và bài toán lát cắt cực tiểu.

Tóm tắt kết quả chính trước khi đi vào chứng minh: bài toán luồng cực đại là một bài toán quy hoạch tuyến tính (LP), còn bài toán lát cắt cực tiểu là một bài toán quy hoạch nguyên (integer program). Khi lập bài toán đối ngẫu của luồng cực đại, ta thu được đúng bài toán nới lỏng tuyến tính (LP relaxation) của lát cắt cực tiểu:

>$$
>\begin{align}
>\text{Giá trị luồng cực đại} &\leq \text{LP đối ngẫu của luồng cực đại}\\
>&= \text{Giá trị tối ưu của lát cắt cực tiểu nới lỏng LP}\\
>&\leq \text{Dung lượng của lát cắt cực tiểu}\\
>\end{align}
>$$

Trong bài này, chúng ta sẽ chứng minh chuỗi bất đẳng thức trên bằng cách lập đối ngẫu và thực hiện quá trình ngược của phép nới lỏng (tức là bổ sung ràng buộc nguyên vào LP để thu được bài toán quy hoạch nguyên). Dù không chứng minh chi tiết tại đây, trên thực tế cả ba giá trị trong chuỗi trên đều bằng nhau. Kết quả đó chính là **định lý luồng cực đại – lát cắt cực tiểu**: giá trị luồng cực đại trong một mạng bằng dung lượng của lát cắt cực tiểu.

Tổng quát hơn, khi giá trị tối ưu của bài toán gốc và bài toán đối ngẫu bằng nhau, ta nói **tính đối ngẫu mạnh (strong duality)** thỏa mãn. Đối với quy hoạch tuyến tính, tính đối ngẫu mạnh luôn đúng ngoại trừ trường hợp cả bài toán gốc lẫn bài toán đối ngẫu đều vô nghiệm (không khả thi); nội dung này sẽ được phân tích kỹ hơn ở Chương 11.

Trước hết, ta phát biểu chính xác hai bài toán, suy ra đối ngẫu của bài toán luồng cực đại, rồi chỉ ra cách thêm ràng buộc nguyên để đưa bài toán đối ngẫu về bài toán lát cắt cực tiểu.

## Bài toán luồng cực đại

Bài toán luồng cực đại yêu cầu tìm tổng lượng luồng lớn nhất đi từ nguồn $$s$$ đến đích $$t$$ thỏa mãn ba điều kiện của luồng:

>$$
>\begin{align}
>&\max_{f\in {\mathbb{R}^{|E|}}} &&{\sum_{(s,j)\in E} f_{sj}}\\
>&\text{với điều kiện} &&{f_{ij}\geq 0,\,f_{ij}\leq c_{i,j}\,\, \text{với mọi }(i, j)\in E}\\
>&&&{\sum_{(i, k)\in E}f_{ik}=\sum_{(k,j)\in E}f_{kj}}\,\, \text{với mọi }k\in V \backslash \{s,t\}.\\
>\end{align}
>$$

## Bài toán lát cắt cực tiểu

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter10/min_cut.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 2] Ví dụ Cắt Đồ thị[3]</figcaption>
</p>
</figure>

Bài toán lát cắt cực tiểu phân hoạch tập đỉnh của đồ thị thành hai tập hợp rời nhau (vùng tô đậm và vùng không tô đậm trong Hình 2): tập $$A$$ chứa nguồn $$s$$, tập $$B$$ chứa đích $$t$$, còn các đỉnh khác được xếp vào $$A$$ hoặc $$B$$. Tổng dung lượng của tất cả các cạnh có hướng đi từ $$A$$ sang $$B$$ được gọi là **dung lượng của lát cắt**.

Nói cách khác, một lát cắt là một cách phân hoạch tập đỉnh sao cho nguồn và đích nằm ở hai phía khác nhau, và bài toán lát cắt cực tiểu tìm lát cắt có dung lượng nhỏ nhất. Trong dạng phát biểu dưới đây, ta gán $$x_i = 1$$ nếu $$i \in A$$ và $$x_i = 0$$ nếu $$i \in B$$, với điều kiện cố định $$x_s = 1$$ và $$x_t = 0$$ (được ngầm hiểu trong công thức):

>$$
>\begin{align}
>&\min_{b\in {\mathbb{R}^{|E|}},\, x \in {\mathbb{R}^{|V|}} } &&{\sum_{(i,j)\in E} b_{ij}c_{ij}}\\
>&\text{với điều kiện} &&{b_{ij} \geq x_{i}-x_{j}}\\
>&&&{b_{ij},\,x_{i},\,x_{j}\,\in \{ 0,1 \} }\\
>&&&\text{với mọi }i, j.\\
>\end{align}
>$$

Về mặt trực quan, bài toán luồng cực đại tìm lưu lượng lớn nhất truyền được từ nguồn sang đích, còn bài toán lát cắt cực tiểu tìm "nút thắt cổ chai" có tổng dung lượng nhỏ nhất ngăn cách nguồn với đích, nên hai bài toán này liên hệ chặt chẽ với nhau.

## Bài toán đối ngẫu của luồng cực đại

Bây giờ ta xây dựng bài toán đối ngẫu cho bài toán luồng cực đại.

Đặt các biến đối ngẫu lần lượt là $$a_{ij} \geq 0$$ (cho ràng buộc $$f_{ij} \geq 0$$), $$b_{ij} \geq 0$$ (cho ràng buộc $$f_{ij} \leq c_{ij}$$) và $$x_k \in \mathbb{R}$$ (cho ràng buộc bảo toàn luồng tại đỉnh $$k \in V \setminus \{s, t\}$$). Vì bài toán gốc là bài toán cực đại hóa, bài toán đối ngẫu sẽ đi tìm cận trên nhỏ nhất cho hàm mục tiêu gốc. Ta lập tổ hợp tuyến tính của các ràng buộc như sau:

>$$
>\begin{align}
>\sum_{(i,j)\in E} {\Big(-a_{ij}f_{ij}+b_{ij}(f_{ij}-c_{ij})\Big)} + \sum_{k \in V\backslash \{s,t\}} x_{k}\Big( \sum_{(i,k)\in E} f_{ik} - \sum_{(k,j)\in E } f_{kj} \Big)\leq 0\\
>\text{với bất kỳ }a_{ij}, b_{ij} \geq 0, (i, j)\in E, \text{ và } x_{k}, k\in V \backslash \{s,t\}.
>\end{align}
>$$

Chuyển các số hạng chứa biến $$f$$ sang vế trái và phần hằng số sang vế phải, ta được:

>$$
>\begin{align}
>\sum_{(i,j)\in E}{\Big((b_{ij}-a_{ij})f_{ij}\Big)}+\sum_{k\in V\backslash \{s,t\}}{x_{k}\Big(\sum_{(i,k)\in E}{f_{ik}}-\sum_{(k,j)\in E}{f_{kj}}\Big)} \leq \sum_{(i,j)\in E}b_{ij}c_{ij}.
>\end{align}
>$$

Để vế trái trùng khớp với hàm mục tiêu của LP gốc là $$\sum_{(s,j)\in E} f_{sj}$$, hệ số của $$f_{ij}$$ ở vế trái phải bằng $$1$$ khi $$i = s$$ và bằng $$0$$ với mọi cạnh khác. Các điều kiện hệ số này chính là ràng buộc của bài toán đối ngẫu.

Vì chỉ số $$k$$ trong tổng thứ hai không bao gồm $$s$$ và $$t$$, ta xét hệ số của $$f_{ij}$$ theo ba trường hợp:

### Trường hợp 1. $$i = s, j \neq t.$$

Trong tổng theo $$x_k$$, mọi số hạng với $$k \neq j$$ đều triệt tiêu (do điều kiện bảo toàn luồng), chỉ còn lại phần tử ứng với $$k = j$$:

>$$
>\begin{align}
>&=\sum_{(s,j)\in E}{\Big((b_{sj}-a_{sj})f_{sj}\Big)}+x_{j}\sum_{(s,j)\in E}{f_{sj}}+\sum_{k\in V\backslash \{s,t,j\}}{x_{k}\Big(\underbrace{\sum_{(s,k)\in E}{f_{sk}}-\sum_{(k,j)\in E}{f_{kj}}}_{=0}\Big)} \\\\
>&=\sum_{(s,j)\in E}{\Big(b_{sj}-a_{sj}+x_{j}\Big)f_{sj}}, \ j \in V \backslash \{s,t\},\\\\
>\end{align}
>$$

### Trường hợp 2. $$i \neq s, j = t.$$

Tương tự, trong tổng theo $$x_k$$ chỉ còn lại phần tử ứng với $$k = i$$ (với dấu trừ):

>$$
>\begin{align}
>&=\sum_{(i,t)\in E}{\Big((b_{it}-a_{it})f_{it}\Big)}-x_{i}\sum_{(i,t)\in E}{f_{it}}+\sum_{k\in V\backslash \{s,t,i\}}{x_{k}\Big(\underbrace{\sum_{(i,k)\in E}{f_{ik}}-\sum_{(k,t)\in E}{f_{kt}}}_{=0}\Big)} \\\\
>&=\sum_{(i,t)\in E}{\Big(b_{it}-a_{it}-x_{i}\Big)f_{it}}, \ i \in V\backslash \{s,t\},\\\\
>\end{align}
>$$

### Trường hợp 3. $$i \neq s, j \neq t.$$

Trong trường hợp này, tổng theo $$x_k$$ giữ lại cả hai phần tử ứng với $$k = j$$ và $$k = i$$:

>$$
>\begin{align}
>&=\sum_{(i,j)\in E}{\Big((b_{ij}-a_{ij})f_{ij}\Big)}+x_{j}\sum_{(i,j)\in E}{f_{ij}}-x_{i}\sum_{(i,j)\in E}{f_{ij}}+\sum_{k\in V\backslash \{s,t,i,j\}}{x_{k}\Big(\underbrace{\sum_{(i,k)\in E}{f_{ik}}-\sum_{(k,j)\in E}{f_{kj}}}_{=0}\Big)} \\\\
>&=\sum_{(i,j)\in E}{\Big(b_{ij}-a_{ij}+x_{j}-x_{i}\Big)f_{ij}}, \ i, j \in V \backslash \{s,t\}. \\\\
>\end{align}
>$$

Đặt hệ số ở Trường hợp 1 bằng $$1$$ và ở hai trường hợp còn lại bằng $$0$$, ta thu được cận trên cho hàm mục tiêu gốc:

>$$
>\begin{align}
>&b_{sj}-a_{sj}+x_{j} = 1\\\\
>&b_{it}-a_{it}-x_{i} = 0\\\\
>&b_{ij}-a_{ij}+x_{j}-x_{i} = 0\\\\
>&\text{Do đó,} \\\\
>&\sum_{(s,j)\in E}{f_{sj}} \leq \sum_{(i,j)\in E}{b_{ij}c_{ij}}.
>\end{align}
>$$

Bài toán đối ngẫu nhằm cực tiểu hóa cận trên $$\sum_{(i,j)\in E} b_{ij} c_{ij}$$. Vì $$a_{ij} \geq 0$$ chỉ đóng vai trò biến bù (slack variable), ta có thể khử $$a_{ij}$$ để viết lại các đẳng thức thành bất đẳng thức. Đồng thời, khi đặt thêm quy ước $$x_s = 1$$ và $$x_t = 0$$, cả ba điều kiện trên gộp thành một dạng thống nhất:

>$$
>\begin{align}
>&\min_{b\in {\mathbb{R}^{|E|}},\, x\in{\mathbb{R}^{|V|}}}  &&{\sum_{(i,j)\in E} b_{ij}c_{ij}} \\\\
>&\text{với điều kiện} &&{b_{ij}+x_{j}-x_{i}\geq 0 \,\, \text{với mọi } (i,j)\in E}\\\\
>&&&{b\geq 0, x_{s}=1,x_{t}=0}.\\\\
>\end{align}
>$$

## Từ LP đối ngẫu đến bài toán quy hoạch nguyên

Bây giờ ta chỉ ra rằng LP đối ngẫu trên chính là bản nới lỏng tuyến tính của bài toán lát cắt cực tiểu. Để chuyển bài toán LP đối ngẫu này về bài toán quy hoạch nguyên, ta bổ sung điều kiện nhị phân cho các biến $$x_i$$ (tức là ép mọi đỉnh ngoài $$s$$ và $$t$$ chỉ được nhận giá trị $$0$$ hoặc $$1$$, tương ứng với việc phân hoạch tập đỉnh thành hai nhóm):

>$$
>\begin{align}
>x_{i} \in \{0,1 \} \ \ \text{ với mọi }i\in V.
>\end{align}
>$$

Đặt $$A = \{i : x_i = 1\}$$ (chứa nguồn $$s$$) và $$B = \{i : x_i = 0\}$$ (chứa đích $$t$$). Khi đó, với mục tiêu cực tiểu hóa $$\sum_{(i,j)\in E} b_{ij} c_{ij}$$ cùng các ràng buộc $$b_{ij} \geq x_i - x_j$$ và $$b_{ij} \geq 0$$, biến $$b_{ij}$$ nhận giá trị $$1$$ nếu cạnh $$(i, j)$$ đi từ $$A$$ sang $$B$$ và bằng $$0$$ trong mọi trường hợp còn lại:

>$$
>\begin{align}
>&\text{Đặt } A= \{ i:x_{i}=1 \} ,\, B= \{ i:x_{i}=0 \} \\\\
>&\text{khi đó } s \in A, \,t \in B, \text{ và }b_{ij}\geq x_{i}-x_{j} \,\,\,\, \text{với }\,(i,j) \in E, \,\, b\geq 0,\\\\
>\end{align}
>$$
>$$
>\begin{align}
>\text{Nói gọn, } \qquad \begin{cases} b_{ij}=1 \qquad \text{nếu } i\in A, j\in B\\\\
>0 \qquad\qquad \text{trường hợp còn lại}.\end{cases}
>\end{align}
>$$

Đây chính xác là bài toán lát cắt cực tiểu đã phát biểu ở trên.

## Mối quan hệ giữa bài toán luồng cực đại và lát cắt cực tiểu (2)

Như vậy, LP đối ngẫu của bài toán luồng cực đại thu được từ bài toán lát cắt cực tiểu bằng cách bỏ ràng buộc nhị phân $$x_i \in \{0, 1\}$$ (phép nới lỏng LP). Theo tính đối ngẫu yếu, giá trị luồng cực đại không vượt quá giá trị tối ưu của LP đối ngẫu. Mặt khác, vì phép nới lỏng mở rộng tập khả thi, giá trị tối ưu của bài toán lát cắt cực tiểu nới lỏng không vượt quá dung lượng lát cắt cực tiểu. Tóm lại, ta có:

>$$
>\begin{align}
>\text{Giá trị luồng cực đại} &\leq \text{LP đối ngẫu của luồng cực đại}\\\\
>&= \text{Giá trị tối ưu của lát cắt cực tiểu nới lỏng LP}\\\\
>&\leq \text{Dung lượng của lát cắt cực tiểu}\\\\
>\end{align}
>$$

Để xem chứng minh dấu bằng xảy ra cho cả chuỗi trên, bạn đọc có thể tham khảo định lý luồng cực đại – lát cắt cực tiểu [11]; về thuật toán tiêu biểu để giải bài toán này, xem thuật toán Ford–Fulkerson [12].

### Luồng cực đại và lát cắt cực tiểu trong khoảng 3 phút

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/max-flow-min-cut_vi.mp4"></video>
</div>

Một mạng 6 đỉnh: đường tăng luồng, đồ thị dư với cạnh ngược, lát cắt cực tiểu bằng giá trị luồng, và liên hệ với đối ngẫu LP.
