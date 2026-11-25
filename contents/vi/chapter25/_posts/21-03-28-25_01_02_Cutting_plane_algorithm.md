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

Ở bài trước, ta biết rằng bao lồi nguyên $$S$$ có thể có hàng tỷ mặt biên nên không thể viết hết ra giấy. Vậy làm sao để vẫn tận dụng được bao lồi $$S$$? **Thuật toán mặt phẳng cắt** giải quyết nghịch lý này bằng chiến lược "lười thông minh": bắt đầu từ đa diện đơn giản $$C_0 = C$$, giải bài toán nới lỏng, rồi **chỉ đi tìm một bất đẳng thức hợp lệ duy nhất** vi phạm đúng điểm phân số vừa xuất hiện.

Cốt lõi của mỗi vòng lặp nằm ở **bài toán tách (separation problem)**: cho một điểm $$x^{(k)} \notin S$$, hãy tìm một siêu phẳng $$\pi^T x \le \pi_0$$ đúng với mọi điểm trong $$S$$ nhưng thỏa mãn $$\pi^T x^{(k)} > \pi_0$$. Định lý nổi tiếng Grötschel–Lovász–Schrijver thậm chí chỉ ra rằng tối ưu hóa và tách điểm có độ khó tương đương nhau về mặt thời gian đa thức!

## Bản đồ kiến thức nền: Ba trụ cột của vòng lặp Mặt phẳng cắt

Để nắm chắc cách thuật toán mặt phẳng cắt vận hành từ đầu tới cuối, hãy chú ý ba trụ cột sau:

- **Tính hợp lệ (Validity) vs. Tính tách biệt (Separation):** Một bất đẳng thức mới phải thỏa mãn đồng thời hai vế: *hợp lệ* (không được cắt mất bất kỳ nghiệm nguyên khả thi nào) và *tách được* (phải cắt bỏ được nghiệm phân số $$x^{(k)}$$ hiện tại để vòng lặp thực sự tiến bộ).
- **Tính đơn điệu của dãy đa diện và cận dưới:** Sau mỗi vòng lặp, ta có $$S \subseteq C_{k+1} \subseteq C_k$$, do đó dãy giá trị nới lỏng $$z_{\text{LP}}^{(0)} \le z_{\text{LP}}^{(1)} \le \dots \le z^\star$$ tăng dần về nghiệm nguyên tối ưu. Khi nghiệm nới lỏng $$x^{(k)}$$ đầu tiên rơi trúng vào tập nguyên, thuật toán dừng ngay với chứng nhận tối ưu tuyệt đối.
- **Tái tối ưu bằng Đơn hình Đối ngẫu (Dual Simplex Warm Start):** Khi thêm một ràng buộc mới cắt bỏ điểm tối ưu LP cũ $$x^{(k)}$$, điểm cũ mất tính khả thi gốc nhưng *vẫn giữ tính khả thi đối ngẫu*. Nhờ vậy, thuật toán đơn hình đối ngẫu chỉ cần xoay thêm vài bước trục (pivot) để tìm $$x^{(k+1)}$$ thay vì giải lại LP từ đầu!

### Khung giải thích (nên đọc chậm): Chạy tay 2 vòng lặp thuật toán Mặt phẳng cắt

Xét bài toán quy hoạch nguyên $$\min -x_1 - 2x_2$$ trên tập nới lỏng ban đầu:

$$
C_0 = \{(x_1, x_2) \ge 0 : 2x_1 + 2x_2 \le 3,\quad x_2 \le 1.4\}, \qquad x_1, x_2 \in \mathbb{Z}_+.
$$

1. **Vòng lặp $$k = 0$$ (trên $$C_0$$):**
   Vì hệ số của $$x_2$$ ($$-2$$) âm hơn $$x_1$$ ($$-1$$), ta đẩy $$x_2$$ lên tối đa $$1.4$$, rồi dùng phần dư của $$2x_1 + 2(1.4) \le 3$$ cho $$x_1 = 0.1$$.
   Nghiệm LP là $$x^{(0)} = (0.1,\; 1.4)$$ (phân số!), cận dưới $$z^{(0)} = -0.1 - 2.8 = -2.9$$.
   - *Bài toán tách:* Từ $$x_2 \le 1.4$$ và $$x_2 \in \mathbb{Z}$$, ta sinh lát cắt hợp lệ đầu tiên: $$x_2 \le \lfloor 1.4 \rfloor = 1$$. (Cắt bỏ $$(0.1, 1.4)$$ vì $$1.4 > 1$$).
2. **Vòng lặp $$k = 1$$ (trên $$C_1 = C_0 \cap \{x_2 \le 1\}$$):**
   Đẩy $$x_2 = 1$$, phần dư từ $$2x_1 + 2(1) \le 3$$ cho $$x_1 = 0.5$$.
   Nghiệm LP mới là $$x^{(1)} = (0.5,\; 1)$$ (vẫn phân số!), cận dưới tăng lên $$z^{(1)} = -0.5 - 2 = -2.5$$.
   - *Bài toán tách:* Từ $$2x_1 + 2x_2 \le 3 \Rightarrow x_1 + x_2 \le 1.5$$ và $$x_1 + x_2 \in \mathbb{Z}$$, ta sinh lát cắt hợp lệ thứ hai: $$x_1 + x_2 \le 1$$. (Cắt bỏ $$(0.5, 1)$$ vì $$1.5 > 1$$).
3. **Vòng lặp $$k = 2$$ (trên $$C_2 = C_1 \cap \{x_1 + x_2 \le 1\}$$):**
   Nghiệm LP mới là $$x^{(2)} = (0,\; 1)$$ — **toàn bộ là số nguyên!** Cận dưới tăng lên $$z^{(2)} = -2$$.
   Thuật toán dừng ngay tại $$(0, 1)$$ với giá trị tối ưu chính xác $$-2$$!

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
