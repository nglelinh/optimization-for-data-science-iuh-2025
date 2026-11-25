---
layout: post
title: '25-01 Mặt phẳng cắt'
chapter: '25'
order: 2
owner: YoungJae Choung
categories:
- chapter25
lang: vi
---

Năm 1954, George Dantzig, Ray Fulkerson và Selmer Johnson đã làm chấn động giới toán học khi giải chính xác bài toán Người du lịch (TSP) đi qua 49 thành phố của nước Mỹ — một bài toán có tới $$48!/2 \approx 6 \times 10^{60}$$ hành trình khả dĩ — chỉ bằng máy tính bàn cơ học và giấy bút! Bí mật của họ không phải sức mạnh tính toán mà là một ý tưởng hình học thiên tài: **mặt phẳng cắt (cutting planes)**.

Thay vì cố gắng mô tả toàn bộ hình dáng phức tạp của tập nghiệm nguyên ngay từ đầu, họ bắt đầu bằng một chiếc vỏ nới lỏng LP thật đơn giản, giải nó, và mỗi lần nghiệm LP bị "lòi" ra ngoài tập nguyên (rơi vào một điểm phân số), họ lại dùng một nhát dao siêu phẳng cắt bỏ đúng phần thừa đó đi.

## Kiến thức cần nhớ: Ba trụ cột trực giác của phương pháp Mặt phẳng cắt

Trước khi đi vào các công thức đại số của lát cắt Gomory ở các bài sau, hãy khắc sâu bức tranh hình học của phương pháp này qua ba trụ cột:

- **Hình học ngăn cách (Hyperplane Separation):** Nếu điểm phân số $$x^{\text{LP}}$$ nằm ngoài bao lồi $$S$$ của các điểm nguyên khả thi, định lý siêu phẳng ngăn cách trong giải tích lồi đảm bảo *luôn tồn tại* một siêu phẳng $$\pi^T x = \pi_0$$ sao cho toàn bộ $$S$$ nằm một bên ($$\pi^T x \le \pi_0$$) còn $$x^{\text{LP}}$$ nằm hẳn bên kia ($$\pi^T x^{\text{LP}} > \pi_0$$).
- **Lặp tinh chỉnh đa diện (Iterative Polyhedral Refinement):** Mỗi lần thêm một mặt phẳng cắt, đa diện nới lỏng $$P_k$$ lại co nhỏ thêm một chút và tiến sát hơn tới bao lồi $$S$$, kéo theo cận dưới tăng đơn điệu lên gần nghiệm nguyên tối ưu.
- **Di sản lịch sử (DFJ 1954 → Gomory 1958 → Chvátal 1973):** Từ các lát cắt thiết kế riêng cho từng bài toán (như lát cắt khử chu trình con cho TSP của Dantzig–Fulkerson–Johnson) đến công thức tổng quát tự động của Ralph Gomory cho *mọi* quy hoạch tuyến tính nguyên, mặt phẳng cắt đã mở ra cả ngành lý thuyết tổ hợp đa diện (polyhedral combinatorics).

### Giải thích: Hình dung một nhát cắt gọt đúng về bao lồi nguyên

Xét tập khả thi nguyên $$S = \{(0, 0),\; (1, 0),\; (0, 1)\}$$ nằm bên trong đa diện nới lỏng LP ban đầu:

$$
P = \{(x_1, x_2) \in \mathbb{R}^2 : x_1 \ge 0,\; x_2 \ge 0,\; 2x_1 + 2x_2 \le 3\},
$$

với mục tiêu cực tiểu hóa $$f(x_1, x_2) = -x_1 - x_2$$.

1. **Giải LP trên đa diện ban đầu $$P$$:**
   Cạnh biên $$2x_1 + 2x_2 = 3$$ cắt hai trục tại $$(1.5, 0)$$ và $$(0, 1.5)$$. Mọi điểm trên đoạn nối hai đỉnh này đều đạt giá trị tối ưu LP là $$-1.5$$, nhưng **không có điểm nào là số nguyên**.
2. **Dựng mặt phẳng cắt ngăn cách:**
   Ta cần một bất đẳng thức $$\pi_1 x_1 + \pi_2 x_2 \le \pi_0$$ thỏa mãn hai điều kiện:
   - *Hợp lệ trên $$S$$:* Đúng tại $$(0,0)$$, $$(1,0)$$ và $$(0,1)$$. Chọn $$x_1 + x_2 \le 1$$: cả ba điểm đều cho giá trị $$0 \le 1$$ hoặc $$1 \le 1$$ (hợp lệ!).
   - *Cắt bỏ nghiệm LP:* Tại $$(1.5, 0)$$ và $$(0, 1.5)$$, vế trái bằng $$1.5 > 1$$ — bị vi phạm nghiêm trọng!
3. **Kết quả sau nhát cắt:**
   Đa diện mới $$P' = P \cap \{x_1 + x_2 \le 1\}$$ thu gọn thành đúng tam giác có 3 đỉnh $$(0,0), (1,0), (0,1)$$ — trùng khớp hoàn toàn với bao lồi $$\operatorname{conv}(S)$$! Bây giờ giải LP trên $$P'$$ lập tức trả về đỉnh nguyên $$(1, 0)$$ hoặc $$(0, 1)$$ với giá trị tối ưu chính xác $$-1$$.

Phương pháp mặt phẳng cắt (cutting plane) giải bài toán quy hoạch tuyến tính nguyên bằng cách xuất phát từ bài toán nới lỏng lồi. Nếu nghiệm tìm được chưa thuộc tập khả thi nguyên ban đầu, thuật toán bổ sung các bất đẳng thức tuyến tính — gọi là *lát cắt* (cut) hay *mặt phẳng cắt* — nhằm cắt bỏ vùng chứa nghiệm phân số đó mà không loại bỏ bất kỳ điểm nguyên khả thi nào, dần dẫn nghiệm hội tụ về tập khả thi ban đầu.

## Khái niệm mặt phẳng cắt

Về mặt hình học, mặt phẳng cắt tương ứng với một đường thẳng (hay siêu phẳng trong không gian nhiều chiều) ngăn cách nghiệm nới lỏng nằm ngoài miền nguyên khỏi tập khả thi nguyên ban đầu, như minh họa trong Hình 1.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_cutting_plane_concept.png" alt="[Hình 1] Mặt phẳng cắt">
  <figcaption style="text-align: center;">[Hình 1] Mặt phẳng cắt</figcaption>
</p>
</figure>

* Vùng đỏ: bao lồi của tập khả thi thuộc quy hoạch tuyến tính nguyên ban đầu.
* Vùng xanh: tập khả thi của bài toán nới lỏng lồi.
* Đường xanh lá: mặt phẳng cắt ngăn cách phần thừa của vùng xanh với vùng đỏ.

Thuật toán cụ thể sẽ được trình bày trong các mục tiếp theo.

## Đôi nét lịch sử về mặt phẳng cắt

Phương pháp mặt phẳng cắt trải qua chặng đường dài từ lý thuyết đến triển khai thực tế.

Năm 1954, Dantzig, Fulkerson và Johnson lần đầu áp dụng ý tưởng mặt phẳng cắt cho bài toán người bán hàng du lịch (TSP). Đến năm 1958, Ralph Gomory đề xuất phương pháp mặt phẳng cắt tổng quát cho mọi bài toán quy hoạch tuyến tính nguyên. Tuy nhiên, trong suốt khoảng 30 năm sau đó, các lát cắt Gomory vẫn ít được sử dụng trong thực tiễn do vấn đề ổn định số và tốc độ hội tụ chậm khi chạy độc lập.

Năm 1990, Sebastian Ceria (Đại học Carnegie Mellon) cùng các cộng sự đã kết hợp hiệu quả mặt phẳng cắt với thuật toán nhánh và cận, hình thành thuật toán **nhánh và cắt (branch and cut)**. Từ đó, mặt phẳng cắt trở thành một thành phần không thể thiếu trong hầu hết các bộ giải quy hoạch nguyên thương mại và mã nguồn mở.
