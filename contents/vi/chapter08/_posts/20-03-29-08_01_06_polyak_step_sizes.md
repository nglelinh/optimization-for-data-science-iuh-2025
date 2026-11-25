---
layout: post
title: '08-01-06 Kích thước bước Polyak'
chapter: '08'
order: 8
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---

Một trong những nỗi đau lớn nhất khi chạy phương pháp subgradient là phải tự "mò" hằng số bước $$t$$ hay lịch giảm dần: chọn hơi lớn thì dao động, chọn hơi nhỏ thì bò như rùa. Năm 1969, nhà toán học Liên Xô Boris Polyak đặt ra một câu hỏi táo bạo: *nếu ta biết trước độ cao đáy thung lũng $$f^*$$, liệu có công thức tự động cho ra bước đi tối ưu nhất ở ngay mỗi vòng lặp không?*

Câu trả lời là công thức ngắn gọn đến mức trông như một phép màu: $$t_k = \frac{f(x^{(k-1)}) - f^*}{\|g^{(k-1)}\|_2^2}$$. Trong nhiều bài toán thực tế, ta thực sự biết chính xác $$f^*$$ — ví dụ tìm điểm chung của các tập lồi ($$f^* = 0$$), giải hệ bất đẳng thức tuyến tính khả thi ($$f^* = 0$$), hay bài toán khớp dữ liệu nội suy (interpolating models) trong học sâu hiện đại nơi loss tối ưu bằng $$0$$. Và ngay cả khi chỉ nhìn vào cách suy ra công thức Polyak, bạn cũng sẽ thấy sự kết hợp hoàn mỹ giữa tối thiểu hóa cận trên khoảng cách và phép chiếu lên siêu phẳng đỡ!

## Kiến thức cần nhớ: Bốn góc nhìn về kích thước bước Polyak

- **Tối thiểu hóa trực tiếp khoảng cách bước sau:** Xuất phát từ bất đẳng thức $$\|x^{(k)} - x^*\|_2^2 \le \|x^{(k-1)} - x^*\|_2^2 - 2 t_k (f^{(k-1)} - f^*) + t_k^2 \|g^{(k-1)}\|_2^2$$, vế phải là một hàm bậc hai lồi theo biến $$t_k$$. Lấy đạo hàm theo $$t_k$$ bằng $$0$$ cho ra ngay nghiệm duy nhất $$t_k = \frac{f^{(k-1)} - f^*}{\|g^{(k-1)}\|_2^2}$$.
- **Diễn giải hình học (Phương pháp Newton 1D / Chiếu lên siêu phẳng):** Siêu phẳng tiếp tuyến đỡ $$y \mapsto f(x^{(k-1)}) + g^{(k-1)T}(y - x^{(k-1)})$$ cắt mặt mức $$f^*$$ tại một siêu phẳng $$H_k$$. Điểm $$x^{(k)}$$ dùng bước Polyak chính xác là **hình chiếu trực giao** của $$x^{(k-1)}$$ lên siêu phẳng $$H_k$$!
- **Tự động thích nghi theo độ dốc và khoảng cách tới đáy:** Khi còn xa đáy ($$f^{(k-1)} - f^*$$ lớn), bước đi tự động lớn để tăng tốc; khi sát đáy ($$f^{(k-1)} - f^* \to 0$$), bước đi tự động co về $$0$$ mà không cần đặt lịch giảm dần bằng tay, đồng thời bất biến với phép nhân hằng số dương vào hàm $$f$$.
- **Mở rộng khi chưa biết chính xác $$f^*$$:** Nếu chỉ có ước lượng $$\hat{f}_k$$ (ví dụ từ nghiệm đối ngẫu hoặc cơ chế cập nhật mục tiêu kiểu Polyak–Nedich), bước Polyak ước lượng vẫn hoạt động hiệu quả và là nền tảng của bộ tối ưu SPS (Stochastic Polyak Step-size) trong học sâu từ năm 2021 trở lại đây.

### Giải thích: Tính tay bước Polyak trên hàm gấp khúc 1D và 2D

**Ví dụ 1 (1D — chạm đáy trong đúng 1 bước):** Xét $$f(x) = \max(2x - 2, -x + 1)$$, có đáy $$f^* = 0$$ tại $$x^* = 1$$.
1. Bắt đầu tại $$x^{(0)} = 4$$: $$f(4) = \max(6, -3) = 6$$, nhánh hoạt động là $$2x - 2$$ nên $$g^{(0)} = 2$$.
2. Áp dụng công thức Polyak:
   $$t_1 = \frac{f(4) - f^*}{|g^{(0)}|^2} = \frac{6 - 0}{2^2} = 1.5.$$
3. Cập nhật: $$x^{(1)} = 4 - 1.5 \times 2 = 1.0 = x^*$$! Vì nhánh hoạt động là hàm tuyến tính, siêu phẳng đỡ trùng đúng với đồ thị nhánh và cắt mức $$0$$ ngay tại nghiệm.

**Ví dụ 2 (2D — thu hẹp khoảng cách chắc chắn):** Xét $$f(x_1, x_2) = |x_1| + 2|x_2|$$ ($$f^* = 0$$, $$x^* = (0, 0)$$) từ $$x^{(0)} = (2, 1)$$.
1. Tính giá trị và subgradient: $$f(2, 1) = 2 + 2(1) = 4$$; $$g^{(0)} = (1, 2)$$ nên $$\|g^{(0)}\|_2^2 = 1^2 + 2^2 = 5$$.
2. Bước Polyak: $$t_1 = \frac{4 - 0}{5} = 0.8$$.
3. Điểm mới: $$x^{(1)} = (2, 1) - 0.8(1, 2) = (1.2, -0.6)$$.
4. Kiểm chứng cả hai đại lượng:
   - Giá trị hàm giảm: $$f(1.2, -0.6) = 1.2 + 2(0.6) = 2.4 < 4$$.
   - Bình phương khoảng cách tới $$x^*$$ giảm đúng lượng dự báo $$\frac{(f^{(0)} - f^*)^2}{\|g^{(0)}\|_2^2} = \frac{16}{5} = 3.2$$:
     $$\|x^{(0)}\|_2^2 = 5 \longrightarrow \|x^{(1)}\|_2^2 = 1.44 + 0.36 = 1.80 = 5 - 3.2!$$

**Kích thước bước Polyak** là quy tắc chọn kích thước bước khi đã biết trước giá trị tối ưu $$f^*$$. Công thức kích thước bước Polyak được định nghĩa như sau:

## Định nghĩa kích thước bước Polyak
>
$$ \begin{align}
t_k = \frac{f^{(k-1)}-f^*}{ \Vert g^{(k-1)} \Vert_2^{2}}, \quad k = 1,2,3...
\end{align} $$

## Cách suy ra kích thước bước Polyak
Ta xuất phát từ bất đẳng thức trung gian trong phần [bất đẳng thức cơ bản]({% multilang_post_url contents/chapter08/20-03-29-08_01_02_basic_inequality %}):

>
$$ \begin{align}
 \Vert x^{(k)}-x^* \Vert_2^{2}  \quad \le \quad  \Vert x^{(k-1)}-x^* \Vert_2^{2}-2t_k (f(x^{(k-1)})-f^*)+t_k^{2} \Vert g^{(k-1)} \Vert_2^{2} \\
\end{align} $$

Lấy đạo hàm vế phải theo $$t_k$$ và cho bằng 0 để cực tiểu hóa cận trên của khoảng cách $$\Vert x^{(k)}-x^* \Vert_2^2$$, ta thu được kích thước bước Polyak:
>
$$ \begin{align}
& \frac{\partial}{\partial t_k}  \Vert x^{(k-1)}-x^* \Vert_2^{2}-2t_k (f(x^{(k-1)})-f^*)+t_k^{2} \Vert g^{(k-1)} \Vert_2^{2} = 0 \\
 \Longleftrightarrow & -2(f(x^{(k-1)})-f^*)+2t_k \Vert g^{(k-1)} \Vert_2^{2} = 0 \\
 \Longleftrightarrow & f(x^{(k-1)})-f^* = t_k \Vert g^{(k-1)} \Vert_2^{2} \\
 \Longleftrightarrow & t_k = \frac{f(x^{(k-1)})-f^*}{ \Vert g^{(k-1)} \Vert_2^{2}} \quad \text{(kích thước bước Polyak tại bước k)}
\end{align} $$

## Tốc độ hội tụ của kích thước bước Polyak

Thay kích thước bước Polyak $$t_i$$ vào bất đẳng thức tổng quát từ phần [bất đẳng thức cơ bản]({% multilang_post_url contents/chapter08/20-03-29-08_01_02_basic_inequality %}):
>
$$ \begin{align}
& 2\sum_{i=1}^{k}t_i(f(x^{(i)})-f^*) \le R^2 + \sum_{i=1}^kt_i^2 \Vert g^{(i)} \Vert_2^2 \\
 \Longleftrightarrow \quad & 2\sum_{i=1}^{k}\frac{(f(x^{(i)})-f^*)^2}{ \Vert g^{(i)} \Vert_2^2} \le R^2 + \sum_{i=1}^k\frac{(f(x^{(i)})-f^*)^2}{ \Vert g^{(i)} \Vert_2^2} \\
 \Longleftrightarrow \quad & \sum_{i=1}^{k}\frac{(f(x^{(i)})-f^*)^2}{ \Vert g^{(i)} \Vert_2^2} \le R^2 \\
\end{align} $$

Với giả thiết Lipschitz $$ \Vert g^{(i)} \Vert_2 \le G$$, bất đẳng thức trên dẫn đến:
>
$$ \begin{align}
& \sum_{i=1}^{k}(f(x^{(i)})-f^*)^2 \le R^2G^2 \\
 \Longleftrightarrow \quad & k ⋅ (f(x^{(i)})-f^*)^2 \le R^2G^2 \\
 \Longleftrightarrow \quad & \sqrt{k} ⋅ (f(x^{(i)})-f^*) \le RG \\
 \Longleftrightarrow \quad & (f(x^{(i)})-f^*) \le \frac{RG}{\sqrt{k}} \\
\end{align} $$

(Trong các dòng suy ra cuối, $$f(x^{(i)})$$ được hiểu là giá trị tốt nhất qua $$k$$ bước lặp, tức $$f^{(k)}_{best}$$.)

Đặt $$\frac{RG}{\sqrt{k}}=\epsilon$$, ta thu được $$k=\big(\frac{RG}{\epsilon}\big)^2$$. Như vậy, số bước lặp cần thiết để đạt sai số $$\epsilon$$ có bậc $$\big(\frac{RG}{\epsilon}\big)^2$$, tức tốc độ hội tụ là $$O(1/\epsilon^{2})$$ — cùng bậc với các quy tắc chọn bước khác của phương pháp subgradient.

### Bước Polyak: chọn độ dài bước từ f* (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/polyak-step_vi.mp4"></video>
</div>

Bước cố định dừng lại ở một lân cận quanh nghiệm tối ưu, bước giảm dần tiến rất chậm, còn bước Polyak $$\alpha_k=\dfrac{f(x_k)-f^*}{\|g_k\|_2^2}$$ hướng thẳng về điểm cực tiểu nhưng đòi hỏi phải biết trước $$f^*$$.

### Tự tay thử: ba quy tắc kích thước bước

<div class="opx-explainer" data-opx="sgm" data-lang="vi"></div>
