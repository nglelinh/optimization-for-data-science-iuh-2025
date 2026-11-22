---
layout: post
title: 05-01 Quy Hoạch Tuyến Tính (LP)
chapter: '05'
order: 2
owner: Hooncheol Shin
categories:
- chapter05
lang: vi
lesson_type: required
---

<script src="https://d3js.org/d3.v7.min.js"></script>
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

Quy hoạch tuyến tính (Linear Programming - LP) là một trong những kỹ thuật tối ưu hóa nền tảng và được ứng dụng rộng rãi nhất trong toán học, kinh tế học và kỹ thuật. Ví dụ điển hình là bài toán của một nhà quản lý sản xuất cần tối đa hóa lợi nhuận trong phạm vi nguồn lực hữu hạn — đây chính là dạng bài toán mà LP được xây dựng để giải quyết.

### Khi nào một bài toán là "tuyến tính"?

Một bài toán tối ưu được gọi là tuyến tính khi:
- **Hàm mục tiêu** là một hàm tuyến tính (hoặc affine) theo các biến quyết định.
- Tất cả các **ràng buộc** đều là đẳng thức hoặc bất đẳng thức tuyến tính (affine).
- Không có tích giữa các biến với nhau (chẳng hạn $$x_1 \cdot x_2$$).
- Không có biến nào xuất hiện dưới dạng lũy thừa bậc khác 1, hàm mũ hay căn bậc hai.

### Ví dụ mở đầu: Bài toán của nông dân

Xét một ví dụ trực quan: một nông dân có 100 mẫu đất và muốn trồng ngô và lúa mì để tối đa hóa lợi nhuận:

- **Ngô:** Lợi nhuận $300 mỗi mẫu, cần 2 giờ lao động mỗi mẫu.
- **Lúa mì:** Lợi nhuận $200 mỗi mẫu, cần 1 giờ lao động mỗi mẫu.
- **Quỹ lao động sẵn có:** Tổng cộng 150 giờ.

**Câu hỏi:** Nông dân nên trồng bao nhiêu mẫu ngô và bao nhiêu mẫu lúa mì để đạt lợi nhuận lớn nhất?

<div id="farmer-problem-viz" style="margin: 20px 0;"></div>

<div class="content-box exercise-box">
<strong>Bài tập tương tác:</strong> Sử dụng các thanh trượt bên dưới để thử các phương án phân bổ diện tích trồng ngô và lúa mì khác nhau. Quan sát cách lợi nhuận thay đổi và kiểm tra xem các ràng buộc có được thỏa mãn hay không.

<div style="margin: 10px 0;">
  <label for="corn-acres">Số mẫu ngô: <span id="corn-value">50</span></label><br>
  <input type="range" id="corn-acres" min="0" max="100" value="50" style="width: 300px;">
</div>

<div style="margin: 10px 0;">
  <label for="wheat-acres">Số mẫu lúa mì: <span id="wheat-value">50</span></label><br>
  <input type="range" id="wheat-acres" min="0" max="100" value="50" style="width: 300px;">
</div>

<div id="farmer-results" style="margin-top: 15px; font-family: monospace;">
  <div>Tổng diện tích sử dụng: <span id="land-used">100</span> / 100 mẫu</div>
  <div>Tổng lao động sử dụng: <span id="labor-used">150</span> / 150 giờ</div>
  <div>Tổng lợi nhuận: $<span id="total-profit">25000</span></div>
  <div id="feasibility-status" style="font-weight: bold; color: green;">✓ Nghiệm khả thi</div>
</div>
</div>

Bây giờ hãy phát biểu chặt chẽ hơn. Nếu cả hàm mục tiêu lẫn các hàm ràng buộc đều là hàm affine, bài toán tối ưu được gọi là **bài toán quy hoạch tuyến tính** (LP). Dạng tổng quát của bài toán quy hoạch tuyến tính như sau:

### Bài toán LP tổng quát

>$$ \begin{align}
>    &\text{minimize}_{x} &&{c^T x + d} \\\\
>    &\text{subject to } &&{Gx \preceq h}\\\\
>    & &&{Ax = b},\\\\
>    &\text{where } &&G \in \mathbb{R}^{m \times n} \text{ và } A \in \mathbb{R}^{p \times n}.
>\end{align} $$

* Hằng số $$+d$$ trong hàm mục tiêu không làm thay đổi nghiệm tối ưu và có thể bỏ qua khi giải.
* Bài toán cực đại hóa $$c^T x + d$$ trên cùng tập ràng buộc tương đương với bài toán cực tiểu hóa $$-c^T x - d$$.
* Về mặt hình học, bài toán tìm điểm tối ưu $$x^*$$ của hàm affine $$c^T x + d$$ trên một tập khả thi đa diện.

### Giải thích hình học

Ý nghĩa của quy hoạch tuyến tính thể hiện rõ qua biểu diễn hình học: mỗi ràng buộc bất đẳng thức tuyến tính xác định một nửa không gian, và tập khả thi là giao của tất cả các nửa không gian đó, tạo thành một **tập đa diện** (polyhedron).

<div class="content-box insight-box">
<strong>Tính chất quan trọng:</strong> Nếu một bài toán quy hoạch tuyến tính có nghiệm tối ưu (và tập khả thi không chứa đường thẳng), thì luôn tồn tại ít nhất một nghiệm tối ưu nằm tại một <strong>đỉnh</strong> của miền khả thi. Đây chính là cơ sở để phương pháp Simplex tìm nghiệm bằng cách di chuyển từ đỉnh này sang đỉnh kề.
</div>

<div id="geometric-lp-viz" style="margin: 20px 0; text-align: center;"></div>

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter05/05_01_geometric_interpretation_of_LP.png" alt="[Fig1] Giải thích hình học của LP [1]" width="70%">
  <figcaption style="text-align: center;">[Hình 1] Minh họa hình học của bài toán LP [1]</figcaption>
</p>
</figure>

## LP ở dạng chuẩn

Nhiều thuật toán giải LP (chẳng hạn phương pháp Simplex) được thiết kế để làm việc trên một cấu trúc đầu vào thống nhất gọi là **dạng chuẩn**. Việc đưa bài toán về dạng chuẩn cho phép áp dụng các thuật toán này một cách nhất quán.

### Bài toán LP dạng chuẩn
>$$ \begin{align}
>    &\text{minimize}_{x} &&{c^T x + d} \\\\
>    &\text{subject to } &&{A x = b} \\\\
>    & &&{x \succeq 0}.
>\end{align} $$

**Đặc trưng của dạng chuẩn:**
- **Hàm mục tiêu:** luôn ở dạng cực tiểu hóa (bài toán cực đại hóa được đổi dấu hàm mục tiêu).
- **Ràng buộc:** chỉ gồm các ràng buộc đẳng thức (bất đẳng thức được chuyển đổi bằng biến phụ).
- **Biến quyết định:** mọi biến đều không âm ($$x \succeq 0$$).

<div class="content-box insight-box">
<strong>Vì sao cần dạng chuẩn?</strong> 
<ul>
<li><strong>Thuận tiện cho thuật toán:</strong> Phương pháp Simplex vận hành trực tiếp trên dạng chuẩn.</li>
<li><strong>Phân tích lý thuyết:</strong> Dễ thiết lập và chứng minh các điều kiện tối ưu cũng như đối ngẫu.</li>
<li><strong>Cài đặt phần mềm:</strong> Đa số bộ giải LP yêu cầu dữ liệu đầu vào theo định dạng chuẩn hóa.</li>
</ul>
</div>

Mọi bài toán LP tổng quát đều có thể đưa về dạng chuẩn qua bốn bước sau:

### Chuyển đổi LP tổng quát về dạng chuẩn
**Bước 1.** Thêm vectơ biến phụ (slack variable) $$s \succeq 0$$ để chuyển ràng buộc bất đẳng thức thành ràng buộc đẳng thức:
> $$ \begin{align}
>     &\text{minimize}_{x, s} &&{c^T x + d} \\\\
>     &\text{subject to } &&{Gx + s = h} \\\\
>     & &&{Ax = b},\\\\
>     & &&{s \succeq 0}.
> \end{align} $$

**Bước 2.** Tách mỗi biến tự do $$x$$ thành hiệu của hai biến không âm:
$$ x = x^{+} - x^{-} $$, trong đó $$ x^{+}, \; x^{-} \succeq 0 $$.

> $$ \begin{align}
>     &\text{minimize}_{x^{+}, x^{-}, s} &&{c^Tx^{+} - c^Tx^{-} + d} \\\\
>     &\text{subject to } &&{Gx^{+} - Gx^{-} + s = h} \\\\
>     & &&{Ax^{+} - Ax^{-} = b},\\\\
>     & &&{s \succeq 0}\\\\
>     & &&{x^{+} \succeq 0}, \; {x^{-} \succeq 0}.
> \end{align} $$

**Bước 3.** Định nghĩa các vectơ và ma trận khối $$ 	ilde{x} $$, $$ 	ilde{c} $$, $$ 	ilde{b} $$ và $$ 	ilde{A} $$:

> $$\tilde{x} =
> \begin{bmatrix}
> x^{+} \\\\
> x^{-} \\\\
> s
> \end{bmatrix}, 
> \tilde{c} =
> \begin{bmatrix}
> c \\\\
> -c \\\\
> 0
> \end{bmatrix},
> \tilde{b} =
> \begin{bmatrix}
> h \\\\
> b
> \end{bmatrix}
> $$, 
> $$
> \tilde{A} =
> \begin{bmatrix}
> G & -G & I\\\\
> A & -A & O
> \end{bmatrix}
> $$

**Bước 4.** Thay $$ 	ilde{x} $$, $$ 	ilde{c} $$, $$ 	ilde{b} $$ và $$ 	ilde{A} $$ vào bài toán ở Bước 2 để thu được dạng chuẩn:

> $$ \begin{align}
>     &\text{minimize}_{\tilde{x}} &&{\tilde{c}^T \tilde{x} + d} \\\\
>     &\text{subject to} &&{\tilde{A} \tilde{x} = \tilde{b}} \\\\
>     & &&{\tilde{x} \succeq 0}.
> \end{align} $$

### Ví dụ: Bài toán khẩu phần ăn (Diet Problem)

Bài toán khẩu phần ăn là một ứng dụng kinh điển của quy hoạch tuyến tính, lần đầu được nghiên cứu trong Thế chiến thứ hai nhằm tìm thực đơn có chi phí thấp nhất mà vẫn đáp ứng đầy đủ nhu cầu dinh dưỡng tối thiểu.

**Phát biểu bài toán:** Tìm tổ hợp thực phẩm rẻ nhất thỏa mãn tất cả các định mức dinh dưỡng:

> $$ \begin{align}
>     &\text{minimize}_{x} &&{c^T x} \\\\
>     &\text{subject to } &&{Dx \succeq d} \\\\
>     & &&{x \succeq 0}.
> \end{align} $$

**Biến và tham số:**
* $$ c_j $$: giá tiền trên mỗi đơn vị thực phẩm $$j$$ ($/đơn vị).
* $$ d_i $$: mức tiêu thụ tối thiểu khuyến nghị cho chất dinh dưỡng $$i$$ (đơn vị/ngày).
* $$ D_{ij} $$: hàm lượng chất dinh dưỡng $$i$$ trong một đơn vị thực phẩm $$j$$.
* $$ x_j $$: lượng thực phẩm $$j$$ trong khẩu phần ăn (đơn vị/ngày).

<div class="content-box exercise-box">
<strong>Bộ tối ưu hóa khẩu phần ăn tương tác:</strong> Giải bài toán khẩu phần ăn đơn giản với 3 loại thực phẩm và 2 nhóm dinh dưỡng:

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px; margin: 15px 0;">
  <div style="text-align: center;">
    <strong>Bánh mì</strong><br>
    Chi phí: $2/ổ<br>
    Protein: 4g/ổ<br>
    Calories: 200/ổ
  </div>
  <div style="text-align: center;">
    <strong>Sữa</strong><br>
    Chi phí: $3/lít<br>
    Protein: 8g/lít<br>
    Calories: 150/lít
  </div>
  <div style="text-align: center;">
    <strong>Thịt</strong><br>
    Chi phí: $8/kg<br>
    Protein: 20g/kg<br>
    Calories: 300/kg
  </div>
</div>

<div style="margin: 15px 0;">
  <strong>Yêu cầu dinh dưỡng:</strong>
  <div>Protein tối thiểu: <input type="number" id="min-protein" value="20" min="10" max="50" style="width: 60px;"> gram/ngày</div>
  <div>Calories tối thiểu: <input type="number" id="min-calories" value="800" min="500" max="1500" style="width: 80px;"> calories/ngày</div>
</div>

<button id="solve-diet" style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">Giải bài toán khẩu phần ăn</button>

<div id="diet-results" style="margin-top: 15px; font-family: monospace; background-color: #f9f9f9; padding: 10px; border-radius: 4px;">
  <div>Nhấp "Giải bài toán khẩu phần ăn" để xem nghiệm tối ưu.</div>
</div>
</div>

<div class="content-box insight-box">
<strong>Ứng dụng thực tế:</strong>
<ul>
<li><strong>Hậu cần quân sự:</strong> Xây dựng khẩu phần bảo đảm dinh dưỡng với chi phí hợp lý.</li>
<li><strong>Dinh dưỡng bệnh viện:</strong> Lập thực đơn đáp ứng yêu cầu điều trị của từng nhóm bệnh nhân.</li>
<li><strong>Phối trộn thức ăn chăn nuôi:</strong> Đáp ứng định mức dinh dưỡng vật nuôi với chi phí tối thiểu.</li>
<li><strong>Bữa ăn học đường:</strong> Thiết kế thực đơn cân bằng trong giới hạn ngân sách.</li>
</ul>
</div>

## Thuật toán Simplex

**Thuật toán Simplex** (phương pháp đơn hình), do George Dantzig phát triển năm 1947, là một trong những thuật toán nền tảng của ngành tối ưu hóa, cung cấp phương pháp có hệ thống để giải các bài toán LP.

### Vì sao Simplex hoạt động: Định lý cơ bản

<div class="content-box insight-box">
<strong>Định lý cơ bản của Quy hoạch tuyến tính:</strong> Nếu một bài toán quy hoạch tuyến tính có nghiệm tối ưu (và miền khả thi không chứa đường thẳng), thì luôn tồn tại một nghiệm tối ưu nằm tại một đỉnh (điểm cực biên) của miền khả thi.
</div>

Nhờ định lý này, thay vì phải tìm kiếm trên toàn bộ miền khả thi chứa vô số điểm, thuật toán chỉ cần khảo sát một tập hữu hạn các đỉnh.

### Chiến lược hoạt động của Simplex

Thuật toán Simplex vận hành theo quy trình bốn bước:

1. **Khởi tạo** tại một đỉnh (nghiệm khả thi cơ sở) bất kỳ của miền khả thi.
2. **Kiểm tra** xem đỉnh hiện tại đã tối ưu hay chưa.
3. **Di chuyển** dọc theo một cạnh sang đỉnh kề giúp cải thiện giá trị hàm mục tiêu.
4. **Lặp lại** cho đến khi không còn hướng cải thiện nào (đạt nghiệm tối ưu).

### Các bước của thuật toán Simplex

Xét bài toán LP ở dạng chuẩn:

> $$ \begin{align}
>     &\text{minimize}_{x} &&{c^T x} \\\\
>     &\text{subject to } &&{A x = b} \\\\
>     & &&{x \succeq 0}.
> \end{align} $$

**Bước 1: Thiết lập ban đầu**
- Đưa bài toán LP về dạng chuẩn (nếu chưa ở dạng chuẩn).
- Tìm một nghiệm khả thi cơ sở ban đầu (một đỉnh xuất phát).
- Lập bảng đơn hình (simplex tableau).

**Bước 2: Kiểm tra điều kiện tối ưu**
- Kiểm tra xem nghiệm cơ sở hiện tại đã tối ưu chưa.
- Nếu mọi chi phí rút gọn đều không âm, dừng thuật toán và trả về nghiệm tối ưu.

**Bước 3: Chọn biến vào cơ sở**
- Chọn biến ngoài cơ sở có chi phí rút gọn âm nhất.
- Biến này xác định cạnh (hướng) di chuyển tiếp theo.

**Bước 4: Chọn biến ra khỏi cơ sở**
- Áp dụng phép kiểm định tỉ số nhỏ nhất (minimum ratio test) để duy trì tính khả thi ($$x \succeq 0$$).
- Phép kiểm định này xác định độ dài bước di chuyển tới đỉnh kề.

**Bước 5: Phép xoay (Pivot)**
- Cập nhật bảng đơn hình bằng phép khử Gauss.
- Chuyển sang đỉnh mới tương ứng với cơ sở mới.

**Bước 6: Lặp lại**
- Quay về Bước 2 cho đến khi đạt điều kiện dừng.

### Minh họa tương tác thuật toán Simplex

Theo dõi từng bước di chuyển qua các đỉnh trên một bài toán hai chiều đơn giản:

<div class="content-box exercise-box">
<strong>Bộ giải Simplex tương tác:</strong> Quan sát thuật toán di chuyển qua từng đỉnh của miền khả thi.

**Bài toán:**
$$\begin{align}
\text{maximize } & 3x_1 + 2x_2 \\
\text{subject to } & x_1 + x_2 \leq 4 \\
& 2x_1 + x_2 \leq 6 \\
& x_1, x_2 \geq 0
\end{align}$$

<div id="simplex-interactive" style="margin: 20px 0;"></div>

<div style="margin: 15px 0;">
  <button id="simplex-step" style="background-color: #2196F3; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; margin-right: 10px;">Bước tiếp theo</button>
  <button id="simplex-reset" style="background-color: #f44336; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">Đặt lại</button>
</div>

<div id="simplex-status" style="margin-top: 15px; font-family: monospace; background-color: #f9f9f9; padding: 15px; border-radius: 4px;">
  <div><strong>Bước 0:</strong> Bắt đầu tại gốc tọa độ (0, 0)</div>
  <div>Giá trị hàm mục tiêu hiện tại: 0</div>
  <div>Nhấp "Bước tiếp theo" để bắt đầu thuật toán Simplex.</div>
</div>

<div id="simplex-tableau" style="margin-top: 15px; font-family: monospace; background-color: #f0f8ff; padding: 15px; border-radius: 4px;">
  <strong>Bảng Simplex hiện tại:</strong>
  <div id="tableau-content" style="margin-top: 10px;">
    Nhấp "Bước tiếp theo" để xem bảng đơn hình.
  </div>
</div>
</div>

### Hiệu năng thực tế của Simplex

Mặc dù có độ phức tạp trường hợp xấu nhất là hàm mũ, thuật toán Simplex vẫn đạt hiệu quả cao trên các bài toán thực tế:

<div class="content-box insight-box">
<strong>Đặc điểm hiệu năng của Simplex:</strong>
<ul>
<li><strong>Trường hợp trung bình:</strong> Thường chỉ cần duyệt số đỉnh gấp khoảng 2–3 lần số ràng buộc.</li>
<li><strong>Bài toán thực tiễn:</strong> Hành vi tính toán thực tế thường tương đương thời gian đa thức.</li>
<li><strong>Khởi tạo nóng (warm start):</strong> Dễ tận dụng lại cơ sở tối ưu cũ khi tham số bài toán thay đổi nhẹ.</li>
<li><strong>Xử lý suy biến:</strong> Các cài đặt hiện đại có cơ chế chống lặp vòng hiệu quả cho các đỉnh suy biến.</li>
</ul>
</div>

### Các biến thể của Simplex và hướng phát triển hiện đại

**Phương pháp Simplex cải tiến (Revised Simplex):**
- Ổn định số tốt hơn so với cập nhật toàn bộ bảng.
- Khai thác tốt tính thưa của ma trận ràng buộc.
- Là nền tảng của hầu hết các bộ giải LP thương mại.

**Phương pháp Simplex đối ngẫu (Dual Simplex):**
- Bắt đầu từ nghiệm khả thi đối ngẫu và duy trì tính khả thi đối ngẫu trong suốt quá trình xoay.
- Rất thuận tiện cho phân tích độ nhạy và khi bổ sung ràng buộc mới (như trong nhánh cận của quy hoạch nguyên).

**Phương pháp điểm trong (Interior-Point Methods):**
- Có đảm bảo lý thuyết về độ phức tạp thời gian đa thức.
- Thường tỏ ra lợi thế trên các bài toán kích thước rất lớn.
- Bổ trợ cho Simplex thay vì thay thế hoàn toàn.

### Ứng dụng thực tế

Thuật toán Simplex và quy hoạch tuyến tính được ứng dụng rộng rãi trong nhiều lĩnh vực:

<div class="content-box insight-box">
<strong>Các lĩnh vực ứng dụng tiêu biểu:</strong>
<ul>
<li><strong>Hàng không:</strong> Lập lịch phi hành đoàn, tối ưu hóa đường bay và phân bổ đội tàu bay.</li>
<li><strong>Sản xuất:</strong> Lập kế hoạch sản xuất và tối ưu hóa chuỗi cung ứng.</li>
<li><strong>Tài chính:</strong> Phân bổ tài sản và quản trị rủi ro.</li>
<li><strong>Viễn thông:</strong> Tối ưu hóa luồng mạng và phân bổ băng thông.</li>
<li><strong>Năng lượng:</strong> Điều độ lưới điện và phân bổ nguồn phát.</li>
</ul>
</div>

<script>
/**
 * Interactive Linear Programming Visualizations
 * Implements farmer problem, geometric interpretation, diet optimizer, and norm comparisons
 */

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    
    // ==================== FARMER PROBLEM INTERACTIVE ====================
    
    function initializeFarmerProblem() {
        const cornSlider = document.getElementById('corn-acres');
        const wheatSlider = document.getElementById('wheat-acres');
        
        if (!cornSlider || !wheatSlider) return;
        
        function updateFarmerResults() {
            const corn = parseFloat(cornSlider.value);
            const wheat = parseFloat(wheatSlider.value);
            
            // Update display values
            document.getElementById('corn-value').textContent = corn;
            document.getElementById('wheat-value').textContent = wheat;
            
            // Calculate metrics
            const landUsed = corn + wheat;
            const laborUsed = corn * 2 + wheat * 1; // 2 hours per corn acre, 1 hour per wheat acre
            const profit = corn * 300 + wheat * 200; // $300 per corn acre, $200 per wheat acre
            
            // Update results
            document.getElementById('land-used').textContent = landUsed;
            document.getElementById('labor-used').textContent = laborUsed;
            document.getElementById('total-profit').textContent = profit;
            
            // Check feasibility
            const feasibilityStatus = document.getElementById('feasibility-status');
            if (landUsed <= 100 && laborUsed <= 150) {
                feasibilityStatus.textContent = '✓ Feasible solution';
                feasibilityStatus.style.color = 'green';
            } else {
                feasibilityStatus.textContent = '✗ Infeasible solution';
                feasibilityStatus.style.color = 'red';
            }
        }
        
        cornSlider.addEventListener('input', updateFarmerResults);
        wheatSlider.addEventListener('input', updateFarmerResults);
        
        // Initialize
        updateFarmerResults();
    }
    
    // ==================== DIET PROBLEM SOLVER ====================
    
    function initializeDietSolver() {
        const solveButton = document.getElementById('solve-diet');
        if (!solveButton) return;
        
        solveButton.addEventListener('click', function() {
            const minProtein = parseFloat(document.getElementById('min-protein').value);
            const minCalories = parseFloat(document.getElementById('min-calories').value);
            
            // Simple heuristic solver (in practice, would use simplex method)
            // Food data: [cost, protein, calories]
            const bread = [2, 4, 200];
            const milk = [3, 8, 150];
            const meat = [8, 20, 300];
            
            // Try different combinations and find minimum cost feasible solution
            let bestCost = Infinity;
            let bestSolution = null;
            
            for (let b = 0; b <= 20; b += 0.5) {
                for (let m = 0; m <= 10; m += 0.5) {
                    for (let mt = 0; mt <= 5; mt += 0.5) {
                        const protein = b * bread[1] + m * milk[1] + mt * meat[1];
                        const calories = b * bread[2] + m * milk[2] + mt * meat[2];
                        const cost = b * bread[0] + m * milk[0] + mt * meat[0];
                        
                        if (protein >= minProtein && calories >= minCalories && cost < bestCost) {
                            bestCost = cost;
                            bestSolution = [b, m, mt];
                        }
                    }
                }
            }
            
            const resultsDiv = document.getElementById('diet-results');
            if (bestSolution) {
                const [bread_amt, milk_amt, meat_amt] = bestSolution;
                const totalProtein = bread_amt * bread[1] + milk_amt * milk[1] + meat_amt * meat[1];
                const totalCalories = bread_amt * bread[2] + milk_amt * milk[2] + meat_amt * meat[2];
                
                resultsDiv.innerHTML = `
                    <div><strong>Optimal Diet Solution:</strong></div>
                    <div>Bread: ${bread_amt.toFixed(1)} loaves</div>
                    <div>Milk: ${milk_amt.toFixed(1)} liters</div>
                    <div>Meat: ${meat_amt.toFixed(1)} kg</div>
                    <div>---</div>
                    <div>Total cost: $${bestCost.toFixed(2)}</div>
                    <div>Total protein: ${totalProtein.toFixed(1)}g (required: ${minProtein}g)</div>
                    <div>Total calories: ${totalCalories.toFixed(0)} (required: ${minCalories})</div>
                `;
            } else {
                resultsDiv.innerHTML = '<div style="color: red;">No feasible solution found!</div>';
            }
        });
    }
    
    // ==================== SIMPLEX ALGORITHM VISUALIZATION ====================
    
    function initializeSimplexVisualization() {
        const stepButton = document.getElementById('simplex-step');
        const resetButton = document.getElementById('simplex-reset');
        const statusDiv = document.getElementById('simplex-status');
        const tableauDiv = document.getElementById('tableau-content');
        const interactiveDiv = document.getElementById('simplex-interactive');
        
        if (!stepButton || !resetButton || !statusDiv || !tableauDiv || !interactiveDiv) return;
        
        // Simplex algorithm state
        let currentStep = 0;
        let currentVertex = [0, 0]; // Starting at origin
        let isOptimal = false;
        
        // Problem: maximize 3x1 + 2x2 subject to x1 + x2 <= 4, 2x1 + x2 <= 6, x1,x2 >= 0
        // In standard form: minimize -3x1 - 2x2 subject to x1 + x2 + s1 = 4, 2x1 + x2 + s2 = 6
        
        const vertices = [
            [0, 0, 4, 6], // (x1, x2, s1, s2) - origin
            [0, 4, 0, 2], // (0, 4, 0, 2) - intersection with x1 + x2 = 4
            [2, 2, 0, 0], // (2, 2, 0, 0) - intersection of both constraints
            [3, 0, 1, 0]  // (3, 0, 1, 0) - intersection with 2x1 + x2 = 6
        ];
        
        const objectiveValues = [0, 8, 10, 9]; // 3x1 + 2x2 at each vertex
        const simplexPath = [0, 3, 2]; // Path: origin -> (3,0) -> (2,2) optimal
        
        function createVisualization() {
            const width = 400;
            const height = 300;
            const margin = {top: 20, right: 20, bottom: 40, left: 40};
            
            // Clear previous content
            interactiveDiv.innerHTML = '';
            
            const svg = d3.select('#simplex-interactive')
                .append('svg')
                .attr('width', width)
                .attr('height', height);
            
            // Scales
            const xScale = d3.scaleLinear()
                .domain([0, 4])
                .range([margin.left, width - margin.right]);
            
            const yScale = d3.scaleLinear()
                .domain([0, 6])
                .range([height - margin.bottom, margin.top]);
            
            // Draw feasible region
            const feasibleRegion = [
                [0, 0], [0, 4], [2, 2], [3, 0], [0, 0]
            ];
            
            svg.append('path')
                .datum(feasibleRegion)
                .attr('fill', 'lightblue')
                .attr('fill-opacity', 0.3)
                .attr('stroke', 'blue')
                .attr('stroke-width', 2)
                .attr('d', d3.line()
                    .x(d => xScale(d[0]))
                    .y(d => yScale(d[1]))
                );
            
            // Draw constraint lines
            // x1 + x2 = 4
            svg.append('line')
                .attr('x1', xScale(0))
                .attr('y1', yScale(4))
                .attr('x2', xScale(4))
                .attr('y2', yScale(0))
                .attr('stroke', 'red')
                .attr('stroke-width', 2)
                .attr('stroke-dasharray', '5,5');
            
            // 2x1 + x2 = 6
            svg.append('line')
                .attr('x1', xScale(0))
                .attr('y1', yScale(6))
                .attr('x2', xScale(3))
                .attr('y2', yScale(0))
                .attr('stroke', 'green')
                .attr('stroke-width', 2)
                .attr('stroke-dasharray', '5,5');
            
            // Draw vertices
            const vertexPoints = [[0,0], [0,4], [2,2], [3,0]];
            svg.selectAll('.vertex')
                .data(vertexPoints)
                .enter()
                .append('circle')
                .attr('class', 'vertex')
                .attr('cx', d => xScale(d[0]))
                .attr('cy', d => yScale(d[1]))
                .attr('r', 6)
                .attr('fill', 'orange')
                .attr('stroke', 'black')
                .attr('stroke-width', 2);
            
            // Current position indicator
            svg.append('circle')
                .attr('id', 'current-position')
                .attr('cx', xScale(currentVertex[0]))
                .attr('cy', yScale(currentVertex[1]))
                .attr('r', 8)
                .attr('fill', 'red')
                .attr('stroke', 'darkred')
                .attr('stroke-width', 3);
            
            // Axes
            svg.append('g')
                .attr('transform', `translate(0,${height - margin.bottom})`)
                .call(d3.axisBottom(xScale));
            
            svg.append('g')
                .attr('transform', `translate(${margin.left},0)`)
                .call(d3.axisLeft(yScale));
            
            // Axis labels
            svg.append('text')
                .attr('x', width / 2)
                .attr('y', height - 5)
                .attr('text-anchor', 'middle')
                .text('x₁');
            
            svg.append('text')
                .attr('transform', 'rotate(-90)')
                .attr('x', -height / 2)
                .attr('y', 15)
                .attr('text-anchor', 'middle')
                .text('x₂');
            
            // Legend
            const legend = svg.append('g')
                .attr('transform', `translate(${width - 150}, 30)`);
            
            legend.append('text')
                .attr('x', 0)
                .attr('y', 0)
                .text('Constraints:')
                .attr('font-weight', 'bold');
            
            legend.append('line')
                .attr('x1', 0)
                .attr('y1', 15)
                .attr('x2', 20)
                .attr('y2', 15)
                .attr('stroke', 'red')
                .attr('stroke-width', 2)
                .attr('stroke-dasharray', '5,5');
            
            legend.append('text')
                .attr('x', 25)
                .attr('y', 19)
                .text('x₁ + x₂ ≤ 4')
                .attr('font-size', '12px');
            
            legend.append('line')
                .attr('x1', 0)
                .attr('y1', 30)
                .attr('x2', 20)
                .attr('y2', 30)
                .attr('stroke', 'green')
                .attr('stroke-width', 2)
                .attr('stroke-dasharray', '5,5');
            
            legend.append('text')
                .attr('x', 25)
                .attr('y', 34)
                .text('2x₁ + x₂ ≤ 6')
                .attr('font-size', '12px');
        }
        
        function updateTableau(step) {
            let tableauHTML = '';
            
            switch(step) {
                case 0:
                    tableauHTML = `
                        <table style="border-collapse: collapse; margin: 10px 0;">
                            <tr style="background-color: #e0e0e0;">
                                <th style="border: 1px solid #ccc; padding: 8px;">Basic</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">x₁</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">x₂</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">s₁</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">s₂</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">RHS</th>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ccc; padding: 8px;">s₁</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">4</td>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ccc; padding: 8px;">s₂</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">2</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">6</td>
                            </tr>
                            <tr style="background-color: #fff2cc;">
                                <td style="border: 1px solid #ccc; padding: 8px;">z</td>
                                <td style="border: 1px solid #ccc; padding: 8px; color: red;"><strong>-3</strong></td>
                                <td style="border: 1px solid #ccc; padding: 8px; color: red;">-2</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                            </tr>
                        </table>
                        <div style="margin-top: 10px;">
                            <strong>Analysis:</strong> Most negative coefficient is -3 (x₁ column). x₁ enters the basis.
                        </div>
                    `;
                    break;
                case 1:
                    tableauHTML = `
                        <table style="border-collapse: collapse; margin: 10px 0;">
                            <tr style="background-color: #e0e0e0;">
                                <th style="border: 1px solid #ccc; padding: 8px;">Basic</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">x₁</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">x₂</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">s₁</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">s₂</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">RHS</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">Ratio</th>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ccc; padding: 8px;">s₁</td>
                                <td style="border: 1px solid #ccc; padding: 8px; background-color: #ffcccc;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">4</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">4/1 = 4</td>
                            </tr>
                            <tr style="background-color: #ccffcc;">
                                <td style="border: 1px solid #ccc; padding: 8px;">s₂</td>
                                <td style="border: 1px solid #ccc; padding: 8px; background-color: #ffcccc;"><strong>2</strong></td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">6</td>
                                <td style="border: 1px solid #ccc; padding: 8px;"><strong>6/2 = 3</strong></td>
                            </tr>
                            <tr style="background-color: #fff2cc;">
                                <td style="border: 1px solid #ccc; padding: 8px;">z</td>
                                <td style="border: 1px solid #ccc; padding: 8px; background-color: #ffcccc;">-3</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">-2</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">-</td>
                            </tr>
                        </table>
                        <div style="margin-top: 10px;">
                            <strong>Minimum ratio test:</strong> min{4/1, 6/2} = min{4, 3} = 3. s₂ leaves the basis.
                        </div>
                    `;
                    break;
                case 2:
                    tableauHTML = `
                        <table style="border-collapse: collapse; margin: 10px 0;">
                            <tr style="background-color: #e0e0e0;">
                                <th style="border: 1px solid #ccc; padding: 8px;">Basic</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">x₁</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">x₂</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">s₁</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">s₂</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">RHS</th>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ccc; padding: 8px;">s₁</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px; color: red;"><strong>0.5</strong></td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">-0.5</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ccc; padding: 8px;">x₁</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0.5</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0.5</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">3</td>
                            </tr>
                            <tr style="background-color: #fff2cc;">
                                <td style="border: 1px solid #ccc; padding: 8px;">z</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px; color: red;"><strong>-0.5</strong></td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1.5</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">9</td>
                            </tr>
                        </table>
                        <div style="margin-top: 10px;">
                            <strong>Current solution:</strong> x₁ = 3, x₂ = 0, objective = 9<br>
                            <strong>Analysis:</strong> x₂ has negative coefficient (-0.5), so x₂ enters the basis.
                        </div>
                    `;
                    break;
                case 3:
                    tableauHTML = `
                        <table style="border-collapse: collapse; margin: 10px 0;">
                            <tr style="background-color: #e0e0e0;">
                                <th style="border: 1px solid #ccc; padding: 8px;">Basic</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">x₁</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">x₂</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">s₁</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">s₂</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">RHS</th>
                            </tr>
                            <tr style="background-color: #ccffcc;">
                                <td style="border: 1px solid #ccc; padding: 8px;">x₂</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">2</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">-1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">2</td>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ccc; padding: 8px;">x₁</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">-1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">2</td>
                            </tr>
                            <tr style="background-color: #ccffcc;">
                                <td style="border: 1px solid #ccc; padding: 8px;">z</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">10</td>
                            </tr>
                        </table>
                        <div style="margin-top: 10px;">
                            <strong>OPTIMAL SOLUTION FOUND!</strong><br>
                            x₁ = 2, x₂ = 2, Maximum objective value = 10<br>
                            All coefficients in the objective row are non-negative.
                        </div>
                    `;
                    break;
            }
            
            tableauDiv.innerHTML = tableauHTML;
        }
        
        function updateStatus(step) {
            let statusHTML = '';
            
            switch(step) {
                case 0:
                    statusHTML = `
                        <div><strong>Step 0:</strong> Initial basic feasible solution</div>
                        <div>Current vertex: (0, 0)</div>
                        <div>Current objective value: 0</div>
                        <div>Basic variables: s₁ = 4, s₂ = 6</div>
                    `;
                    currentVertex = [0, 0];
                    break;
                case 1:
                    statusHTML = `
                        <div><strong>Step 1:</strong> Choose entering variable</div>
                        <div>Most negative coefficient: -3 (x₁ column)</div>
                        <div>x₁ enters the basis</div>
                        <div>Performing minimum ratio test...</div>
                    `;
                    break;
                case 2:
                    statusHTML = `
                        <div><strong>Step 2:</strong> First iteration complete</div>
                        <div>Current vertex: (3, 0)</div>
                        <div>Current objective value: 9</div>
                        <div>Basic variables: x₁ = 3, s₁ = 1</div>
                    `;
                    currentVertex = [3, 0];
                    break;
                case 3:
                    statusHTML = `
                        <div><strong>Step 3:</strong> OPTIMAL SOLUTION FOUND!</div>
                        <div>Current vertex: (2, 2)</div>
                        <div>Maximum objective value: 10</div>
                        <div>Basic variables: x₁ = 2, x₂ = 2</div>
                    `;
                    currentVertex = [2, 2];
                    isOptimal = true;
                    break;
            }
            
            statusDiv.innerHTML = statusHTML;
            
            // Update visualization
            const currentPos = d3.select('#current-position');
            if (currentPos.node()) {
                const xScale = d3.scaleLinear().domain([0, 4]).range([40, 360]);
                const yScale = d3.scaleLinear().domain([0, 6]).range([260, 40]);
                
                currentPos
                    .transition()
                    .duration(500)
                    .attr('cx', xScale(currentVertex[0]))
                    .attr('cy', yScale(currentVertex[1]));
            }
        }
        
        function nextStep() {
            if (currentStep < 3) {
                currentStep++;
                updateStatus(currentStep);
                updateTableau(currentStep);
                
                if (currentStep === 3) {
                    stepButton.textContent = 'Algorithm Complete!';
                    stepButton.disabled = true;
                    stepButton.style.backgroundColor = '#4CAF50';
                }
            }
        }
        
        function reset() {
            currentStep = 0;
            currentVertex = [0, 0];
            isOptimal = false;
            
            stepButton.textContent = 'Next Step';
            stepButton.disabled = false;
            stepButton.style.backgroundColor = '#2196F3';
            
            updateStatus(0);
            updateTableau(0);
            createVisualization();
        }
        
        // Event listeners
        stepButton.addEventListener('click', nextStep);
        resetButton.addEventListener('click', reset);
        
        // Initialize
        createVisualization();
        updateStatus(0);
        updateTableau(0);
    }
    
    // Initialize all interactive elements
    initializeFarmerProblem();
    initializeDietSolver();
    initializeSimplexVisualization();
    
    // Trigger MathJax re-rendering if needed
    if (window.MathJax) {
        MathJax.typesetPromise();
    }
});
</script>
