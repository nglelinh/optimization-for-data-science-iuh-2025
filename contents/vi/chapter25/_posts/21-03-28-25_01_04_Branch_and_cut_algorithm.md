---
layout: post
title: '25-01-04 Thuật toán nhánh và cắt (Branch and cut)'
chapter: '25'
order: 6
owner: YoungJae Choung
categories:
- chapter25
lang: vi
---

Trong suốt thập niên 1960–1980, giới tối ưu từng bị chia làm hai phe gần như đối lập: phe **Nhánh và Cận** (ổn định nhưng cây tìm kiếm phình to khủng khiếp) và phe **Mặt phẳng cắt thuần túy** (ý tưởng đẹp nhưng khi thêm quá nhiều lát cắt Gomory liên tiếp, bảng đơn hình gặp bất ổn định số học và hội tụ chậm dần).

Bước ngoặt lịch sử đến vào năm 1990 khi Sebastian Ceria cùng nhóm nghiên cứu tại Đại học Carnegie Mellon và IBM nhận ra: *tại sao phải chọn một trong hai?* Nếu ta chỉ thêm vài vòng lát cắt thật sắc bén ở nút gốc để siết chặt đa diện, rồi chuyển sang phân nhánh (và thỉnh thoảng thêm lát cắt ngay tại các nút con), hai nhược điểm triệt tiêu nhau hoàn toàn. Sự kết hợp mang tên **Nhánh và Cắt (Branch and Cut)** đó đã mở ra kỷ nguyên tăng tốc hơn 1 triệu lần về mặt thuật toán của các bộ giải MIP hiện đại!

## Bản đồ kiến thức nền: Bốn trụ cột của kiến trúc Branch and Cut

Mọi bộ giải MIP đỉnh cao ngày nay (Gurobi, CPLEX, SCIP, HiGHS) đều vận hành dựa trên sự phối hợp nhịp nhàng của bốn bánh răng sau:

- **Vòng lặp Cắt tại nút gốc (Root-Node Cut Loop):** Trước khi rẽ nhánh lần đầu tiên, bộ giải chạy nhiều vòng sinh lát cắt (Gomory, MIR, clique, cover cuts) để đóng càng nhiều khoảng cách nới lỏng (integrality gap) càng tốt ngay tại nút gốc.
- **Quyết định chuyển từ Cắt sang Nhánh (Cut-vs-Branch Trade-off):** Khi các lát cắt mới không còn cải thiện đáng kể cận dưới (hiện tượng *tailing off*) hoặc làm bài toán LP trở nên quá dày đặc, thuật toán lập tức dừng cắt và chuyển sang phân nhánh.
- **Tích hợp Tiền xử lý và Heuristic gốc (Presolve & Primal Heuristics):** Song song với cắt và nhánh, bộ giải liên tục đơn giản hóa ràng buộc (presolve) và chạy heuristic tìm nghiệm nguyên tốt để hạ nhanh cận trên $$u$$, kích hoạt cắt tỉa mạnh trên toàn cây.
- **Sức mạnh cộng hưởng Thuật toán $$\times$$ Phần cứng:** Như tổng kết kinh điển của Bixby (IBM/Gurobi), tốc độ giải MIP từ 1991 đến 2015 tăng khoảng $$10^9$$ lần — trong đó phần cứng đóng góp khoảng $$10^3$$ lần, còn bản thân thuật toán (nòng cốt là Branch and Cut) đóng góp tới hơn $$10^6$$ lần!

### Khung giải thích (nên đọc chậm): So sánh tay Branch-and-Bound thuần túy với Branch-and-Cut

Xét bài toán quy hoạch nguyên cực tiểu hóa $$\min -5x_1 - 4x_2$$ thỏa mãn $$2x_1 + 2x_2 \le 5,\; x_1, x_2 \in \mathbb{Z}_+$$ (chính là bài toán ta đã mất 5 nút để giải ở bài 24-05!).

1. **Cách 1 — Nhánh và Cận thuần túy (không dùng lát cắt):**
   - Nút gốc LP cho $$(2.5, 0)$$ với cận dưới $$-12.5$$.
   - Ta phải rẽ nhánh $$x_1 \le 2$$ và $$x_1 \ge 3$$, rồi tại nhánh $$x_1 \le 2$$ lại ra $$(2, 0.5)$$ nên phải rẽ thêm $$x_2 \le 0$$ và $$x_2 \ge 1$$, rồi lại rẽ thêm $$x_1 \le 1$$ và $$x_1 \ge 2$$... Tổng cộng **6 lần giải LP** trên 6 nút!
2. **Cách 2 — Nhánh và Cắt (thêm 1 vòng cắt ngay tại nút gốc):**
   - Nút gốc LP ban đầu cho $$(2.5, 0)$$ với cận dưới $$-12.5$$.
   - Thay vì rẽ nhánh ngay, ta sinh lát cắt Chvátal–Gomory từ ràng buộc $$2x_1 + 2x_2 \le 5$$ (chia 2 rồi làm tròn xuống vế phải):
     $$x_1 + x_2 \le \left\lfloor \frac{5}{2} \right\rfloor = 2.$$
   - Giải lại LP tại **chính nút gốc** với ràng buộc mới $$x_1 + x_2 \le 2$$: nghiệm LP nhảy thẳng sang đỉnh $$(2, 0)$$ với giá trị $$-10$$.
3. **Kết quả chấn động:** Điểm $$(2, 0)$$ đã là **nghiệm nguyên**! Thuật toán kết thúc ngay tại nút gốc (0 nhánh, chỉ 2 lần giải LP) thay vì phải đào cây xuống nhiều tầng. Trên bài toán lớn, việc khép 80% khoảng cách cận ngay tại nút gốc giúp giảm kích thước cây từ hàng triệu nút xuống còn vài chục nút!

Năm 1990, Sebastian Ceria tại Đại học Carnegie Mellon đã triển khai thành công sự kết hợp giữa phương pháp mặt phẳng cắt và thuật toán nhánh và cận, tạo nên thuật toán **nhánh và cắt (branch and cut)**. Kể từ đó, cách tiếp cận này trở thành nền tảng cốt lõi của các bộ giải tối ưu thương mại hiện đại.

## Thuật toán nhánh và cắt

Xét bài toán quy hoạch nguyên (IP), trong đó $$f : \mathbb{R}^{n} \to \mathbb{R}$$ là hàm lồi, $$C \subseteq \mathbb{R}^{n}$$ là tập lồi và $$J \subseteq \{1, \dots, n\}$$:

> $$
> \begin{align}
>           \min_{x} & \quad {f(x)} \\
> \text{subject to } & \quad  x \in C \\
>                    & \quad  x_j \in \mathbb{Z}, \quad j \in J
> \end{align}
> $$

### Các bước thực hiện

Ký hiệu bài toán nới lỏng lồi là (CR) và quy hoạch nguyên là (IP):

1. Giải bài toán nới lỏng lồi (CR):

> $$
> \begin{align}
> \min_{x} & \quad {f(x)} \\\\
> \text{subject to } & \quad  x \in C
> \end{align}
> $$

2. Nếu (CR) vô nghiệm $$\Rightarrow$$ (IP) vô nghiệm (dừng). <br>
3. Nếu nghiệm $$x^{\star}$$ của (CR) khả thi cho (IP) $$\Rightarrow$$ $$x^{\star}$$ là nghiệm tối ưu của (IP) (dừng). <br>
4. Nếu $$x^{\star}$$ chưa thỏa mãn ràng buộc nguyên, chọn một trong hai thao tác: <br>
$$\quad$$ 4.1 Thêm một hoặc nhiều mặt phẳng cắt (cut) rồi quay lại bước 1. <br>
$$\quad$$ 4.2 Phân nhánh (branch) thành các bài toán con và giải đệ quy.

Như vậy, thuật toán nhánh và cắt tích hợp mặt phẳng cắt trực tiếp vào bên trong cây nhánh và cận: tại mỗi nút, bộ giải có thể siết chặt bài toán nới lỏng bằng lát cắt trước khi quyết định phân nhánh.

## Tiến bộ của công nghệ giải quy hoạch nguyên

Các bộ giải hiện đại như Gurobi, CPLEX và FICO Xpress sở hữu những cài đặt rất hiệu quả của phương pháp đơn hình (simplex) và điểm trong (interior-point). Riêng với quy hoạch nguyên hỗn hợp, hầu hết các bộ giải đều dùng kiến trúc nhánh và cắt, khai thác mạnh nới lỏng lồi và khởi động nóng (warm start).

Trong khoảng 30 năm qua, tốc độ giải quy hoạch nguyên đã tăng lên rất lớn, giúp nhiều bài toán thực tế từng không thể giải nay giải được trong thời gian ngắn:

* Tăng tốc nhờ cải tiến thuật toán (1990–2016): hơn $$500{,}000$$ lần.
* Tăng tốc nhờ cải tiến phần cứng (1990–2016): hơn $$500{,}000$$ lần.
* Tổng mức tăng tốc: hơn $$250$$ tỷ lần ($$2{,}5 \cdot 10^{11}$$).
