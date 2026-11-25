---
layout: post
title: 00-02-01 Vector và Không gian Vector
chapter: '00'
order: 8
owner: GitHub Copilot
lang: vi
categories:
- chapter00
lesson_type: required
---

Trong tối ưu hóa, một "phương án" — dù là danh mục đầu tư 50 cổ phiếu, lịch vận hành 24 giờ của nhà máy điện, hay bộ trọng số của một mô hình dự báo — đều được mã hóa thành một điểm duy nhất: một **vector** $$x \in \mathbb{R}^n$$. Khi hiểu không gian vector, cơ sở, tích vô hướng và các chuẩn khác nhau, bạn sẽ nhìn thấy ngay vì sao hình cầu đơn vị của chuẩn $$\ell_1$$ có các góc nhọn tạo nghiệm thưa còn chuẩn $$\ell_2$$ lại trơn tròn.

Bài học này đặt lại nền móng vững chắc cho mọi thao tác vector sẽ xuất hiện xuyên suốt các chương về tập lồi và đối ngẫu.

## Bản đồ kiến thức nền: Hình học của không gian $$\mathbb{R}^n$$

- **Tổ hợp tuyến tính, độc lập tuyến tính và cơ sở:** Cho biết tập các hướng cơ bản nhỏ nhất có thể sinh ra toàn bộ không gian tìm kiếm; tránh dư thừa biến hoặc ràng buộc phụ thuộc tuyến tính.
- **Tích vô hướng và bất đẳng thức Cauchy–Schwarz:** Định nghĩa góc, tính trực giao và phép chiếu: $$|u^T v| \le \|u\|_2 \|v\|_2$$. Đây cũng là nguồn gốc trực tiếp của biểu diễn siêu phẳng $$a^T x = b$$ trong Chương 02.
- **Các chuẩn vector ($$\ell_1, \ell_2, \ell_\infty$$):** Là những "thước đo độ dài" khác nhau trên cùng một không gian. Mỗi chuẩn sinh ra một dạng phạt điều chuẩn (regularization) riêng biệt trong học máy và tối ưu hóa.
- **Không gian con (Subspace):** Tập các vector đóng dưới phép cộng và nhân vô hướng (luôn đi qua gốc tọa độ), là nguyên mẫu để định nghĩa tập affine $$x_0 + V$$ ở chương sau.

### Khung giải thích (nên đọc chậm): So sánh ba chuẩn và kiểm chứng Cauchy–Schwarz trên $$v = (3, -4)^T$$

Cho hai vector trong $$\mathbb{R}^2$$: $$v = (3, -4)^T$$ và $$w = (1, 2)^T$$.

1. **Tính ba chuẩn phổ biến của $$v$$:**
   - Chuẩn $$\ell_1$$ (khoảng cách Manhattan): $$\|v\|_1 = |3| + |-4| = 7$$.
   - Chuẩn $$\ell_2$$ (khoảng cách Euclid): $$\|v\|_2 = \sqrt{3^2 + (-4)^2} = \sqrt{25} = 5$$.
   - Chuẩn $$\ell_\infty$$ (thành phần cực đại): $$\|v\|_\infty = \max(|3|, |-4|) = 4$$.
   Quan sát trật tự luôn đúng trên $$\mathbb{R}^n$$: $$\|v\|_\infty \le \|v\|_2 \le \|v\|_1$$ ($$4 \le 5 \le 7$$).
2. **Kiểm chứng bất đẳng thức Cauchy–Schwarz:**
   - Tích vô hướng: $$v^T w = 3(1) + (-4)(2) = -5 \implies |v^T w| = 5$$.
   - Tích hai chuẩn Euclid: $$\|v\|_2 \|w\|_2 = 5 \cdot \sqrt{1^2 + 2^2} = 5\sqrt{5} \approx 11.18$$.
   Ta thấy $$5 \le 11.18$$, và góc $$\theta$$ giữa hai vector thỏa $$\cos\theta = \frac{-5}{5\sqrt{5}} = -\frac{1}{\sqrt{5}} \approx -0.447$$ (góc tù $$\approx 116.6^\circ$$ — nếu $$v$$ là gradient thì $$w$$ là một hướng giảm!).

---

Bài học này giới thiệu về vector, không gian vector và các khái niệm cơ bản tạo nền tảng cho đại số tuyến tính trong tối ưu hóa.

---

## Vector và không gian vector ($$\mathbb{R}^n$$)

### Vector là gì?

- **Vector:** Có thể hình dung vector như một mũi tên trong không gian, biểu diễn cả hướng và độ lớn (độ dài). Về mặt đại số, vector là một bộ có thứ tự gồm các số thực, tương tự như tọa độ của một điểm. Chẳng hạn, một vector trong không gian hai chiều có thể là $$\mathbf{v} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$$, tương ứng với 3 đơn vị theo trục $$x$$ và 4 đơn vị theo trục $$y$$.

- **Góc nhìn hình học và đại số:**
  - **Hình học:** vector là đoạn thẳng có hướng với độ lớn xác định.
  - **Đại số:** vector là bộ có thứ tự gồm các số thực.

### Không gian vector

- **Không gian vector ($$\mathbb{R}^n$$):** Là tập hợp tất cả các vector gồm $$n$$ thành phần thực. Ví dụ, $$\mathbb{R}^2$$ là tập hợp mọi vector có 2 thành phần, biểu diễn các điểm hoặc mũi tên trong mặt phẳng hai chiều.

- **Ví dụ:**
  - $$\mathbb{R}^2 = \left\{\begin{pmatrix} x \\ y \end{pmatrix} : x, y \in \mathbb{R}\right\}$$ (mặt phẳng 2D)
  - $$\mathbb{R}^3 = \left\{\begin{pmatrix} x \\ y \\ z \end{pmatrix} : x, y, z \in \mathbb{R}\right\}$$ (không gian 3D)

### Các phép toán trên vector

**Phép cộng vector:**
$$\mathbf{u} + \mathbf{v} = \begin{pmatrix} u_1 \\ u_2 \\ \vdots \\ u_n \end{pmatrix} + \begin{pmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{pmatrix} = \begin{pmatrix} u_1 + v_1 \\ u_2 + v_2 \\ \vdots \\ u_n + v_n \end{pmatrix}$$

**Phép nhân vô hướng:**
$$c\mathbf{v} = c \begin{pmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{pmatrix} = \begin{pmatrix} cv_1 \\ cv_2 \\ \vdots \\ cv_n \end{pmatrix}$$

---

## Độc lập tuyến tính, cơ sở và số chiều

### Độc lập tuyến tính

Một hệ vector $$\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_k\}$$ được gọi là **độc lập tuyến tính** nếu phương trình

$$c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k = \mathbf{0}$$

chỉ có nghiệm tầm thường $$c_1 = c_2 = \cdots = c_k = 0$$.

**Ý nghĩa trực quan:** Một hệ vector độc lập tuyến tính khi không có vector nào trong hệ có thể biểu diễn được bằng cách nhân vô hướng và cộng các vector còn lại. Các vector này độc lập về phương hướng, không bị dư thừa.

**Ví dụ trong $$\mathbb{R}^2$$:**
- $$\mathbf{v}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$$ và $$\mathbf{v}_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$ độc lập tuyến tính.
- $$\mathbf{v}_1 = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$$ và $$\mathbf{v}_2 = \begin{pmatrix} 2 \\ 4 \end{pmatrix}$$ phụ thuộc tuyến tính (vì $$\mathbf{v}_2 = 2\mathbf{v}_1$$).

### Cơ sở

Một **cơ sở** của không gian vector là một hệ vector độc lập tuyến tính tối tiểu có thể tổ hợp (nhân vô hướng và cộng) để tạo thành *mọi* vector trong không gian đó.

**Tính chất của một cơ sở:**
1. Các vector trong cơ sở độc lập tuyến tính.
2. Hệ vector đó sinh ra toàn bộ không gian vector.
3. Mọi vector trong không gian đều biểu diễn được một cách duy nhất dưới dạng tổ hợp tuyến tính của các vector cơ sở.

**Cơ sở chính tắc của $$\mathbb{R}^n$$:**
$$\mathbf{e}_1 = \begin{pmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{pmatrix}, \mathbf{e}_2 = \begin{pmatrix} 0 \\ 1 \\ \vdots \\ 0 \end{pmatrix}, \ldots, \mathbf{e}_n = \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{pmatrix}$$

### Số chiều

**Số chiều** của một không gian vector là số lượng vector có trong bất kỳ cơ sở nào của không gian đó, phản ánh số hướng độc lập cần thiết để mô tả toàn bộ không gian.

- $$\dim(\mathbb{R}^2) = 2$$
- $$\dim(\mathbb{R}^3) = 3$$
- $$\dim(\mathbb{R}^n) = n$$

---

## Chuẩn của vector

**Chuẩn** là một hàm gán "độ dài" hoặc "kích thước" cho mỗi vector, tổng quát hóa khái niệm khoảng cách từ gốc tọa độ.

### Tính chất của chuẩn

Mọi chuẩn $$\|\cdot\|$$ đều phải thỏa mãn ba tiên đề:

1. **Tính xác định không âm:** $$\|\mathbf{x}\| \geq 0$$, và $$\|\mathbf{x}\| = 0$$ khi và chỉ khi $$\mathbf{x} = \mathbf{0}$$.
2. **Tính thuần nhất:** $$\|t\mathbf{x}\| = |t| \|\mathbf{x}\|$$ với mọi số thực $$t$$.
3. **Bất đẳng thức tam giác:** $$\|\mathbf{x} + \mathbf{y}\| \leq \|\mathbf{x}\| + \|\mathbf{y}\|$$.

### Các chuẩn thông dụng

**Chuẩn Euclid (chuẩn $$L_2$$):**
$$\|\mathbf{x}\|_2 = \sqrt{\sum_{i=1}^n x_i^2} = \sqrt{x_1^2 + x_2^2 + \cdots + x_n^2}$$

Đây là khoảng cách hình học quen thuộc trong không gian Euclid.

**Chuẩn Manhattan (chuẩn $$L_1$$):**
$$\|\mathbf{x}\|_1 = \sum_{i=1}^n |x_i| = |x_1| + |x_2| + \cdots + |x_n|$$

Còn được gọi là "chuẩn taxi", tương ứng với quãng đường di chuyển dọc theo lưới ô vuông của các tuyến phố.

**Chuẩn cực đại (chuẩn $$L_\infty$$):**
$$\|\mathbf{x}\|_\infty = \max_{i} |x_i|$$

Bằng giá trị tuyệt đối lớn nhất trong các thành phần của vector.

**Ví dụ:** Với $$\mathbf{x} = \begin{pmatrix} 3 \\ -4 \\ 1 \end{pmatrix}$$:
- $$\|\mathbf{x}\|_2 = \sqrt{3^2 + (-4)^2 + 1^2} = \sqrt{26} \approx 5.1$$
- $$\|\mathbf{x}\|_1 = |3| + |-4| + |1| = 8$$
- $$\|\mathbf{x}\|_\infty = \max\{|3|, |-4|, |1|\} = 4$$

---

## Tích vô hướng (tích chấm)

**Tích vô hướng** (hay tích chấm) là phép toán phổ biến giữa hai vector cùng chiều, cho kết quả là một số vô hướng.

### Định nghĩa

Với hai vector $$\mathbf{x}$$ và $$\mathbf{y}$$ trong $$\mathbb{R}^n$$:

$$\mathbf{x}^T \mathbf{y} = \mathbf{x} \cdot \mathbf{y} = \sum_{i=1}^n x_i y_i = x_1 y_1 + x_2 y_2 + \cdots + x_n y_n$$

### Diễn giải hình học

$$\mathbf{x} \cdot \mathbf{y} = \|\mathbf{x}\| \|\mathbf{y}\| \cos \theta$$

trong đó $$\theta$$ là góc giữa hai vector $$\mathbf{x}$$ và $$\mathbf{y}$$.

### Tính chất

1. **Tính giao hoán:** $$\mathbf{x} \cdot \mathbf{y} = \mathbf{y} \cdot \mathbf{x}$$
2. **Tính phân phối:** $$\mathbf{x} \cdot (\mathbf{y} + \mathbf{z}) = \mathbf{x} \cdot \mathbf{y} + \mathbf{x} \cdot \mathbf{z}$$
3. **Tính thuần nhất:** $$(c\mathbf{x}) \cdot \mathbf{y} = c(\mathbf{x} \cdot \mathbf{y})$$

### Các trường hợp đặc biệt

- **Hai vector trực giao:** $$\mathbf{x} \cdot \mathbf{y} = 0$$ (vuông góc với nhau).
- **Hai vector cùng phương:** $$\mathbf{x} \cdot \mathbf{y} = \pm \|\mathbf{x}\| \|\mathbf{y}\|$$.
- **Tích vô hướng với chính nó:** $$\mathbf{x} \cdot \mathbf{x} = \|\mathbf{x}\|_2^2$$.

### Ví dụ

Với $$\mathbf{x} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$$ và $$\mathbf{y} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$$:

$$\mathbf{x}^T \mathbf{y} = (1)(3) + (2)(4) = 3 + 8 = 11$$

---

## Ứng dụng trong tối ưu hóa

Vector và không gian vector giữ vai trò cốt lõi trong tối ưu hóa ở các khía cạnh sau:

1. **Biến quyết định:** Bài toán tối ưu hóa nhiều biến được biểu diễn gọn gàng dưới dạng tìm một vector biến tối ưu.
2. **Gradient:** Gradient của hàm số là một vector chỉ theo hướng tăng nhanh nhất.
3. **Ràng buộc:** Ràng buộc tuyến tính được biểu diễn trực tiếp bằng tích vô hướng: $$\mathbf{a}^T \mathbf{x} \leq b$$.
4. **Khoảng cách và độ lớn bước lặp:** Các chuẩn khác nhau cho phép đo khoảng cách giữa các nghiệm hoặc kích thước bước dịch chuyển theo những tiêu chí khác nhau.
5. **Tính trực giao:** Nhiều tính chất trong tối ưu hóa gắn với quan hệ vuông góc, chẳng hạn giữa vector gradient và tiếp tuyến của đường mức.
6. **Tổ hợp tuyến tính:** Nhiều vùng khả thi được xây dựng từ tổ hợp tuyến tính của các vector (bao lồi, nón lồi, v.v.).

Khung lý thuyết về không gian vector cung cấp ngôn ngữ toán học chuẩn xác để mô hình hóa và giải các bài toán tối ưu hóa một cách có hệ thống.
