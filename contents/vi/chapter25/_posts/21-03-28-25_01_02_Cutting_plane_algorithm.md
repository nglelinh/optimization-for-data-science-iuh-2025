---
layout: post
title: '25-01-02 Thuật toán mặt phẳng cắt'
chapter: '25'
order: 4
owner: YoungJae Choung
categories:
- chapter25
lang: vi
---

Mục này trình bày khái niệm bất đẳng thức hợp lệ và cấu trúc chung của thuật toán mặt phẳng cắt để giải quy hoạch tuyến tính nguyên.

## Bất đẳng thức hợp lệ (Valid Inequality)

Một bất đẳng thức tuyến tính $$\pi^{T}x \le \pi_{0}$$ được gọi là *hợp lệ* đối với tập $$S$$ nếu mọi điểm của $$S$$ đều nằm trong nửa không gian xác định bởi bất đẳng thức đó:

>$$\pi^{T}x \le \pi_{0} \quad \text{với mọi } x \in S$$

Điều kiện hợp lệ đảm bảo việc bổ sung bất đẳng thức sẽ không bao giờ loại bỏ nghiệm nguyên khả thi nào của bài toán gốc.

## Thuật toán mặt phẳng cắt

Xét bài toán quy hoạch nguyên (IP):

> $$
> \begin{align}
>           \min_{x} & \quad {c^{T}x} \\\\
> \text{subject to } & \quad  x \in C \\\\
>                    & \quad  x_j \in \mathbb{Z}, \quad j \in J
> \end{align}
> $$

và đặt $$S := \text{conv} \left \{ x \in C : x_j \in \mathbb{Z}, j \in J \right \}$$.

### Các bước thực hiện

Ký hiệu bài toán nới lỏng lồi là (CP) và bài toán gốc là (IP):

1. Khởi tạo $$C_{0} := C$$ và tính $$x^{(0)} := \arg\min_{x} \left\{c^{T}x : x \in C_{0} \right\}$$.
2. Với $$k = 0, 1, \dots$$: <br>
$$\quad$$ Nếu $$x^{(k)}$$ khả thi cho (IP) thì $$x^{(k)}$$ là nghiệm tối ưu; dừng thuật toán. <br>
$$\quad$$ Ngược lại: <br>
$$\quad\quad$$ Tìm một bất đẳng thức $$(\pi, \pi_{0})$$ hợp lệ đối với $$S$$ sao cho $$\pi^T x^{(k)} > \pi_0$$ (tức cắt bỏ $$x^{(k)}$$). <br>
$$\quad\quad$$ Cập nhật $$C_{k+1} := C_{k} \cap \{ x : \pi^{T}x \le \pi_{0} \}$$. <br>
$$\quad\quad$$ Giải lại bài toán nới lỏng: $$x^{(k+1)} := \arg\min_{x} \left\{c^{T}x : x \in C_{k+1} \right\}$$. <br>
$$\quad$$ Kết thúc nhánh điều kiện. <br>
Kết thúc vòng lặp.

Bất đẳng thức hợp lệ tách được $$x^{(k)}$$ khỏi $$S$$ như trên được gọi là **mặt phẳng cắt (cutting plane)** hoặc **lát cắt (cut)**.

Ở bước 1, thuật toán giải bài toán nới lỏng lồi (CP) ban đầu trên $$C$$. Ở bước 2, nếu nghiệm thu được đã thỏa mãn ràng buộc nguyên thì quá trình kết thúc; ngược lại, ta thêm một mặt phẳng cắt để loại bỏ nghiệm phân số $$x^{(k)}$$, thu hẹp miền khả thi thành $$C_{k+1}$$ và giải lại (CP).

Trong Hình 1, đa giác biểu diễn miền nới lỏng $$C$$ và chấm đen là nghiệm của (CP). Bất đẳng thức hợp lệ cắt bỏ chấm đen này trong khi vẫn giữ nguyên toàn bộ bao lồi $$S$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_02_valid_inequality.png" alt="[Hình 1] Bất đẳng thức hợp lệ">
  <figcaption style="text-align: center;">[Hình 1] Bất đẳng thức hợp lệ [3]</figcaption>
</p>
</figure>

Qua các vòng lặp, tập $$C_k$$ dần được siết chặt về phía bao lồi $$S$$ cho tới khi nghiệm của bài toán nới lỏng rơi vào một điểm nguyên khả thi của (IP).
