---
layout: post
title: 00-02-03 Giá trị riêng và Vector riêng
chapter: '00'
order: 10
owner: GitHub Copilot
lang: vi
categories:
- chapter00
lesson_type: required
---

Bài học này trình bày khái niệm giá trị riêng và vector riêng — công cụ quan trọng để phân tích hành vi của các phép biến đổi tuyến tính và hàm toàn phương trong tối ưu hóa.

---

## Định nghĩa và ý nghĩa trực quan

Khi một ma trận tác động lên một vector, nó thường làm thay đổi cả hướng lẫn độ dài của vector đó. Tuy nhiên, **vector riêng** là những vector khác không đặc biệt mà sau phép biến đổi ma trận, phương của chúng được giữ nguyên và chỉ có độ dài (hoặc chiều) thay đổi theo một hệ số vô hướng.

### Định nghĩa toán học

Với một ma trận vuông $$\mathbf{A}$$ và một vector khác không $$\mathbf{v}$$:

- $$\mathbf{v}$$ là một **vector riêng** của $$\mathbf{A}$$
- $$\lambda$$ là **giá trị riêng** tương ứng

nếu chúng thỏa mãn **phương trình giá trị riêng**:

$$\mathbf{A}\mathbf{v} = \lambda\mathbf{v}$$

### Diễn giải hình học

- **Vector riêng:** các vector khác không giữ nguyên phương dưới phép biến đổi $$\mathbf{A}$$.
- **Giá trị riêng:** hệ số vô hướng co giãn tương ứng với từng vector riêng.

**Ý nghĩa trực quan theo giá trị $$\lambda$$:**
- Nếu $$\lambda > 1$$: vector riêng bị kéo dài.
- Nếu $$0 < \lambda < 1$$: vector riêng bị co ngắn lại.
- Nếu $$\lambda < 0$$: vector riêng bị co giãn và đảo ngược chiều.
- Nếu $$\lambda = 0$$: vector riêng bị ánh xạ về vector không.

---

## Cách tìm giá trị riêng và vector riêng

### Bước 1: Tìm giá trị riêng

Biến đổi phương trình giá trị riêng:
$$\mathbf{A}\mathbf{v} = \lambda\mathbf{v}$$
$$\mathbf{A}\mathbf{v} - \lambda\mathbf{v} = \mathbf{0}$$
$$(\mathbf{A} - \lambda\mathbf{I})\mathbf{v} = \mathbf{0}$$

Để hệ có nghiệm không tầm thường ($$\mathbf{v} \neq \mathbf{0}$$), ma trận $$(\mathbf{A} - \lambda\mathbf{I})$$ phải suy biến, nghĩa là:

$$\det(\mathbf{A} - \lambda\mathbf{I}) = 0$$

Phương trình này được gọi là **phương trình đặc trưng**.

### Bước 2: Tìm vector riêng

Với mỗi giá trị riêng $$\lambda_i$$ tìm được, ta giải hệ phương trình tuyến tính thuần nhất:
$$(\mathbf{A} - \lambda_i\mathbf{I})\mathbf{v} = \mathbf{0}$$

Tập nghiệm của hệ này (kèm theo vector không) tạo thành **không gian riêng** ứng với $$\lambda_i$$.

---

## Ví dụ chi tiết

Tìm các giá trị riêng và vector riêng của ma trận $$\mathbf{A} = \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix}$$.

### Bước 1: Tìm giá trị riêng

$$\mathbf{A} - \lambda\mathbf{I} = \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix} - \lambda\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 3-\lambda & 1 \\ 0 & 2-\lambda \end{pmatrix}$$

$$\det(\mathbf{A} - \lambda\mathbf{I}) = (3-\lambda)(2-\lambda) - (1)(0) = (3-\lambda)(2-\lambda) = 0$$

Ta thu được hai giá trị riêng $$\lambda_1 = 3$$ và $$\lambda_2 = 2$$.

### Bước 2: Tìm vector riêng

**Với $$\lambda_1 = 3$$:**
$$(\mathbf{A} - 3\mathbf{I})\mathbf{v} = \begin{pmatrix} 0 & 1 \\ 0 & -1 \end{pmatrix}\begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$

Suy ra $$v_2 = 0$$ và $$v_1$$ có thể nhận mọi giá trị khác không. Ta chọn $$\mathbf{v}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$$ (hoặc mọi bội khác không của nó).

**Với $$\lambda_2 = 2$$:**
$$(\mathbf{A} - 2\mathbf{I})\mathbf{v} = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}\begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$

Suy ra $$v_1 + v_2 = 0$$, tức $$v_2 = -v_1$$. Ta chọn $$\mathbf{v}_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$$ (hoặc mọi bội khác không của nó).

### Kiểm chứng

Kiểm tra trực tiếp lại kết quả:
- $$\mathbf{A}\mathbf{v}_1 = \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix}\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 3 \\ 0 \end{pmatrix} = 3\begin{pmatrix} 1 \\ 0 \end{pmatrix} = 3\mathbf{v}_1$$ ✓
- $$\mathbf{A}\mathbf{v}_2 = \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix}\begin{pmatrix} 1 \\ -1 \end{pmatrix} = \begin{pmatrix} 2 \\ -2 \end{pmatrix} = 2\begin{pmatrix} 1 \\ -1 \end{pmatrix} = 2\mathbf{v}_2$$ ✓

---

## Các tính chất và định lý quan trọng

### Tính chất cơ bản

1. **Tổng các giá trị riêng bằng vết của ma trận:**
   $$\sum_{i=1}^n \lambda_i = \text{tr}(\mathbf{A}) = \sum_{i=1}^n a_{ii}$$

2. **Tích các giá trị riêng bằng định thức của ma trận:**
   $$\prod_{i=1}^n \lambda_i = \det(\mathbf{A})$$

3. **Các vector riêng ứng với các giá trị riêng đôi một khác nhau thì độc lập tuyến tính.**

4. **Nếu $$\mathbf{A}$$ là ma trận đối xứng thực**, mọi giá trị riêng của nó đều là số thực và các vector riêng ứng với giá trị riêng khác nhau trực giao với nhau.

### Bội của giá trị riêng

- **Bội đại số (algebraic multiplicity):** số lần $$\lambda$$ xuất hiện như một nghiệm của đa thức đặc trưng.
- **Bội hình học (geometric multiplicity):** số chiều của không gian riêng tương ứng (số vector riêng độc lập tuyến tính tối đa ứng với $$\lambda$$).

Với mọi giá trị riêng, luôn có: bội hình học ≤ bội đại số.

---

## Phân tích trị riêng (Eigendecomposition)

### Ma trận đối xứng

Ma trận đối xứng thực $$\mathbf{A} = \mathbf{A}^T$$ có những tính chất đặc biệt quan trọng:

1. **Mọi giá trị riêng đều là số thực.**
2. **Các vector riêng ứng với các giá trị riêng khác nhau trực giao với nhau.**
3. **Luôn chéo hóa được bằng ma trận trực giao.**

Cụ thể, mọi ma trận đối xứng thực đều có phân tích phổ:

$$\mathbf{A} = \mathbf{Q}\mathbf{\Lambda}\mathbf{Q}^T$$

trong đó:
- $$\mathbf{Q}$$ là ma trận trực giao ($$\mathbf{Q}^T\mathbf{Q} = \mathbf{I}$$) có các cột là các vector riêng đơn vị trực chuẩn.
- $$\mathbf{\Lambda}$$ là ma trận đường chéo chứa các giá trị riêng tương ứng.

### Các phép toán dựa trên phân tích trị riêng

Khi ma trận chéo hóa được ($$\mathbf{A} = \mathbf{P}\mathbf{D}\mathbf{P}^{-1}$$), nhiều phép toán ma trận phức tạp trở nên đơn giản:

**1. Lũy thừa ma trận:**

$$\mathbf{A}^k = \mathbf{P}\mathbf{D}^k\mathbf{P}^{-1}$$

Điều này đặc biệt hữu ích khi $$k$$ lớn, vì lũy thừa của ma trận đường chéo chỉ cần lũy thừa từng phần tử trên đường chéo:

$$\mathbf{D}^k = \begin{pmatrix} \lambda_1^k & 0 & \cdots & 0 \\ 0 & \lambda_2^k & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & \lambda_n^k \end{pmatrix}$$

**2. Ma trận nghịch đảo:**

Nếu tất cả các giá trị riêng đều khác 0:

$$\mathbf{A}^{-1} = \mathbf{P}\mathbf{D}^{-1}\mathbf{P}^{-1}$$

với $$\mathbf{D}^{-1}$$ là ma trận đường chéo có các phần tử $$1/\lambda_i$$.

**3. Hàm mũ ma trận:**

$$e^{\mathbf{A}} = \mathbf{P}e^{\mathbf{D}}\mathbf{P}^{-1}$$

với $$e^{\mathbf{D}} = \text{diag}(e^{\lambda_1}, e^{\lambda_2}, \ldots, e^{\lambda_n})$$.

**4. Định thức và vết (trace):**

- $$\det(\mathbf{A}) = \prod_i \lambda_i$$ (tích các giá trị riêng).
- $$\text{tr}(\mathbf{A}) = \sum_i \lambda_i$$ (tổng các giá trị riêng).

---

## Định lý đĩa Gershgorin

Định lý đĩa Gershgorin (Gershgorin Circle Theorem) cung cấp cách ước lượng nhanh miền chứa các giá trị riêng của ma trận mà không cần giải phương trình đặc trưng.

### Phát biểu định lý

Cho ma trận $$\mathbf{A} = [a_{ij}]_{n \times n}$$. Với mỗi hàng $$i$$, xác định:
- **Tâm:** $$a_{ii}$$ (phần tử trên đường chéo thứ $$i$$)
- **Bán kính:** $$r_i = \sum_{j \neq i} |a_{ij}|$$ (tổng giá trị tuyệt đối các phần tử ngoài đường chéo ở hàng $$i$$)

<div class="textbook-theorem" markdown="1">
**Định lý:** Mọi giá trị riêng của $$\mathbf{A}$$ đều nằm trong hợp của các đĩa Gershgorin:

$$D_i = \{z \in \mathbb{C} : |z - a_{ii}| \leq r_i\}$$
</div>

### Ví dụ

Xét ma trận đối xứng: $$\mathbf{A} = \begin{pmatrix} 4 & 0.3 & 0.2 \\ 0.3 & 5 & 0.1 \\ 0.2 & 0.1 & 3 \end{pmatrix}$$

Do $$\mathbf{A}$$ đối xứng nên mọi giá trị riêng đều là số thực. Các khoảng ứng với đĩa Gershgorin trên trục thực là:
- $$D_1$$: tâm $$4$$, bán kính $$0.5$$, cho khoảng $$3.5 \leq \lambda \leq 4.5$$
- $$D_2$$: tâm $$5$$, bán kính $$0.4$$, cho khoảng $$4.6 \leq \lambda \leq 5.4$$
- $$D_3$$: tâm $$3$$, bán kính $$0.3$$, cho khoảng $$2.7 \leq \lambda \leq 3.3$$

**Kết luận:** Mọi giá trị riêng của $$\mathbf{A}$$ đều nằm trong đoạn $$[2.7, 5.4]$$.

### Ứng dụng thực tế

1. **Kiểm tra nhanh tính xác định dương:** Với ma trận đối xứng, nếu mọi đĩa Gershgorin đều nằm hoàn toàn bên phải trục ảo (tức $$a_{ii} - r_i > 0$$ với mọi $$i$$), ma trận chắc chắn xác định dương.
2. **Ước lượng số điều kiện (condition number):** Giúp đánh giá nhanh độ ổn định số học của ma trận.
3. **Thiết kế ma trận:** Đảm bảo các tính chất phổ mong muốn bằng cách kiểm soát độ lớn phần tử đường chéo so với phần tử ngoài đường chéo.

---

## Phép chéo hóa ma trận

Một ma trận vuông $$\mathbf{A}$$ được gọi là **chéo hóa được** nếu tồn tại ma trận khả nghịch $$\mathbf{P}$$ và ma trận đường chéo $$\mathbf{D}$$ sao cho:

$$\mathbf{A} = \mathbf{P}\mathbf{D}\mathbf{P}^{-1}$$

trong đó:
- $$\mathbf{D}$$ là ma trận đường chéo chứa các giá trị riêng của $$\mathbf{A}$$.
- $$\mathbf{P}$$ là ma trận có các cột là các vector riêng tương ứng.

### Lợi ích của phép chéo hóa

1. **Tính lũy thừa ma trận nhanh chóng:** $$\mathbf{A}^k = \mathbf{P}\mathbf{D}^k\mathbf{P}^{-1}$$.
2. **Hiểu rõ cấu trúc phép biến đổi:** Các giá trị riêng mô tả trực tiếp mức độ co giãn của phép biến đổi dọc theo từng phương vector riêng.

---

## Ứng dụng: Hành vi của phép nhân ma trận lặp

Một ứng dụng quan trọng của giá trị riêng là phân tích hành vi dài hạn khi nhân lặp lại một ma trận với vector: $$\mathbf{A}\mathbf{x}, \mathbf{A}^2\mathbf{x}, \mathbf{A}^3\mathbf{x}, \ldots$$

### Vector riêng và hành vi dài hạn

Giả sử ma trận $$\mathbf{A}$$ chéo hóa được dưới dạng:

$$\mathbf{A} = \mathbf{P}\mathbf{D}\mathbf{P}^{-1}$$

Khi đó:

$$\mathbf{A}^k = \mathbf{P}\mathbf{D}^k\mathbf{P}^{-1} = \mathbf{P}\begin{pmatrix} \lambda_1^k & 0 & \cdots \\ 0 & \lambda_2^k & \cdots \\ \vdots & \vdots & \ddots \end{pmatrix}\mathbf{P}^{-1}$$

**Nhận xét quan trọng:**

1. **Nếu $$|\lambda_{\max}| > 1$$:** độ lớn của vector tăng theo hàm mũ (bùng nổ — explode).
2. **Nếu $$|\lambda_{\max}| < 1$$:** vector tiến dần về $$\mathbf{0}$$ (triệt tiêu — vanish).
3. **Nếu $$|\lambda_{\max}| = 1$$:** vector giữ độ lớn ổn định hoặc dao động (tùy bội và phần ảo của giá trị riêng).

### Ví dụ: Ma trận ngẫu nhiên

Xét ma trận ngẫu nhiên cỡ $$5 \times 5$$ có các phần tử độc lập tuân theo phân phối chuẩn tắc (trung bình bằng 0, phương sai bằng 1).

Khi nhân lặp lại ma trận này với một vector ngẫu nhiên, ta thấy:
- Độ dài vector tăng theo cấp số nhân.
- Tốc độ tăng được chi phối bởi giá trị riêng có mô-đun lớn nhất $$\lambda_{\max}$$.

**Định luật đường tròn (Circular Law):** Với ma trận ngẫu nhiên lớn cỡ $$n \times n$$ có các phần tử độc lập, trung bình bằng 0, phương sai bằng 1, giá trị riêng có mô-đun lớn nhất xấp xỉ $$\sqrt{n}$$.

### Chuẩn hóa ma trận

Để kiểm soát sự bùng nổ hoặc triệt tiêu này, ta có thể chuẩn hóa ma trận theo giá trị riêng lớn nhất:

$$\mathbf{A}_{\text{normalized}} = \frac{\mathbf{A}}{\lambda_{\max}}$$

Sau khi chuẩn hóa (khi $$\lambda_{\max} > 0$$):
- Giá trị riêng lớn nhất bằng 1.
- Độ lớn vector không bị bùng nổ hay triệt tiêu theo hàm mũ.
- Dãy lặp duy trì hành vi ổn định.

### Ý nghĩa trong học sâu (Deep Learning)

Hiện tượng nhân lặp ma trận có hệ quả trực tiếp trong mạng nơ-ron sâu:

1. **Gradient triệt tiêu / bùng nổ (Vanishing/Exploding Gradients):**
   - Nếu ma trận trọng số có các giá trị riêng quá lớn → gradient bùng nổ.
   - Nếu các giá trị riêng quá nhỏ → gradient triệt tiêu.

2. **Khởi tạo trọng số (Weight Initialization):**
   - Cần khởi tạo sao cho quy mô phổ (giá trị riêng / giá trị kỳ dị) gần 1.
   - Các phương pháp như khởi tạo Xavier và He được xây dựng dựa trên nguyên lý này.

3. **Chuẩn hóa theo lô (Batch Normalization):**
   - Kiểm soát phân phối của các giá trị kích hoạt giữa các tầng.
   - Hạn chế hiện tượng bùng nổ và triệt tiêu trong quá trình huấn luyện.

4. **Kết nối tắt (Residual Connections — ResNet):**
   - Bổ sung nhánh tắt giúp luồng gradient truyền ngược ổn định hơn.
   - Về mặt toán học, nhánh tắt tương đương việc cộng thêm ma trận đơn vị, giúp giữ các giá trị riêng gần 1 khi trọng số nhánh dư còn nhỏ.

### Phân tích hội tụ của thuật toán lặp

Trong nhiều thuật toán lặp (như gradient descent, phương pháp lũy thừa — power iteration), **tốc độ hội tụ** phụ thuộc vào tỷ số giữa hai giá trị riêng lớn nhất theo mô-đun:

$$\text{Convergence rate} \propto \left|\frac{\lambda_2}{\lambda_1}\right|$$

- Nếu $$|\lambda_2| \ll |\lambda_1|$$: thuật toán hội tụ nhanh.
- Nếu $$|\lambda_2| \approx |\lambda_1|$$: thuật toán hội tụ chậm.

**Thuật toán lặp lũy thừa (Power Iteration):**
1. Khởi tạo với một vector ngẫu nhiên $$\mathbf{v}_0$$.
2. Lặp bước chuẩn hóa: $$\mathbf{v}_{k+1} = \frac{\mathbf{A}\mathbf{v}_k}{\|\mathbf{A}\mathbf{v}_k\|}$$.
3. Dãy vector hội tụ về vector riêng ứng với giá trị riêng có mô-đun lớn nhất $$|\lambda_{\max}|$$.

Đây là nguyên lý nền tảng cho nhiều thuật toán tính giá trị riêng và vector riêng trên ma trận cỡ lớn.

---

## Ứng dụng trong tối ưu hóa

Giá trị riêng và vector riêng giữ vai trò then chốt trong tối ưu hóa ở nhiều khía cạnh:

### 1. Dạng toàn phương và tính xác định dấu

Với hàm toàn phương $$f(\mathbf{x}) = \mathbf{x}^T\mathbf{Q}\mathbf{x}$$ ($$\mathbf{Q}$$ đối xứng):

- **Xác định dương** ($$f(\mathbf{x}) > 0$$ với mọi $$\mathbf{x} \neq \mathbf{0}$$): mọi giá trị riêng của $$\mathbf{Q}$$ đều dương.
- **Nửa xác định dương** ($$f(\mathbf{x}) \geq 0$$): mọi giá trị riêng đều không âm.
- **Xác định âm** ($$f(\mathbf{x}) < 0$$ với mọi $$\mathbf{x} \neq \mathbf{0}$$): mọi giá trị riêng đều âm.
- **Không xác định dấu** ($$f(\mathbf{x})$$ nhận cả giá trị dương và âm): có cả giá trị riêng dương lẫn giá trị riêng âm.

### 2. Điều kiện tối ưu bậc hai

Với hàm $$f(\mathbf{x})$$ khả vi hai lần tại một điểm tới hạn $$\mathbf{x}^*$$ (nơi $$\nabla f(\mathbf{x}^*) = \mathbf{0}$$):

- **Cực tiểu địa phương:** ma trận Hessian $$\nabla^2 f(\mathbf{x}^*)$$ xác định dương (mọi giá trị riêng đều dương).
- **Cực đại địa phương:** ma trận Hessian xác định âm (mọi giá trị riêng đều âm).
- **Điểm yên ngựa:** ma trận Hessian không xác định dấu (có cả giá trị riêng dương và âm).

### 3. Phân tích thành phần chính (PCA)

PCA tìm các phương mà dữ liệu có phương sai lớn nhất:
- Các vector riêng của ma trận hiệp phương sai xác định các trục thành phần chính.
- Các giá trị riêng tương ứng cho biết phương sai của dữ liệu theo từng trục đó.

### 4. Phân tích hội tụ

Trong các thuật toán tối ưu hóa lặp:
- **Số điều kiện** $$\kappa = \frac{\lambda_{\max}}{\lambda_{\min}}$$ ảnh hưởng trực tiếp đến tốc độ hội tụ.
- Số điều kiện lớn dẫn đến hội tụ chậm (đặc biệt với các phương pháp bậc nhất).

### 5. Phương pháp Newton

Phương pháp Newton sử dụng nghịch đảo của ma trận Hessian:
$$\mathbf{x}_{k+1} = \mathbf{x}_k - [\nabla^2 f(\mathbf{x}_k)]^{-1} \nabla f(\mathbf{x}_k)$$

Phổ giá trị riêng của ma trận Hessian quyết định hành vi cục bộ và tốc độ hội tụ của phương pháp.

---

## Ví dụ: Ứng dụng trong tối ưu hóa

Xét bài toán cực tiểu hóa hàm $$f(x, y) = 2x^2 + 3y^2 + 2xy$$.

Ma trận Hessian của hàm là: $$\mathbf{H} = \begin{pmatrix} 4 & 2 \\ 2 & 6 \end{pmatrix}$$

**Tìm các giá trị riêng:**
$$\det(\mathbf{H} - \lambda\mathbf{I}) = (4-\lambda)(6-\lambda) - 4 = \lambda^2 - 10\lambda + 20 = 0$$

$$\lambda = \frac{10 \pm \sqrt{100-80}}{2} = \frac{10 \pm 2\sqrt{5}}{2} = 5 \pm \sqrt{5}$$

Vì cả hai giá trị riêng đều dương ($$\lambda_1 = 5 + \sqrt{5} > 0$$ và $$\lambda_2 = 5 - \sqrt{5} > 0$$), ma trận Hessian xác định dương, khẳng định gốc tọa độ $$(0, 0)$$ là điểm cực tiểu toàn cục.

Số điều kiện của ma trận Hessian là $$\kappa = \frac{5 + \sqrt{5}}{5 - \sqrt{5}} \approx 4.24$$, cho thấy bài toán có điều kiện số khá tốt đối với các thuật toán tối ưu hóa.

Nắm vững giá trị riêng và vector riêng giúp ta hiểu rõ cấu trúc hình học và giải tích của các bài toán tối ưu hóa, từ đó thiết kế thuật toán và phân tích hội tụ hiệu quả hơn.
