---
layout: post
title: 28-02 Thoát yên ngựa và hình học phong cảnh
chapter: '28'
order: 3
owner: Nguyen Le Linh
categories:
- chapter28
lang: vi
lesson_type: required
---

Biết rằng điểm yên ngựa chặt *luôn có lối thoát* về mặt toán học là một chuyện; liệu thuật toán bậc nhất như Gradient Descent hay SGD có **tìm thấy lối thoát đó trong thời gian đa thức** hay bị mắc kẹt hàng triệu vòng lặp lại là câu chuyện hoàn toàn khác! Một kết quả lý thuyết kinh điển của Du và cộng sự (ICML 2017) chỉ ra rằng Gradient Descent tất định thuần túy có thể mất **thời gian hàm mũ** để thoát khỏi chuỗi điểm yên ngựa nếu đi vào sát mặt ổn định.

Thế nhưng chỉ cần một cú huých cực nhỏ — **nhiễu ngẫu nhiên từ minibatch SGD** hoặc một lượng nhiễu Gaussian đẳng hướng nhỏ (Perturbed GD) — là đủ để biến thời gian hàm mũ thành thời gian đa thức! Và sau khi thoát yên ngựa để đáp xuống đáy cực tiểu, một câu hỏi hình học thứ hai lập tức xuất hiện: *giữa hai cực tiểu cùng có mất mát huấn luyện bằng 0, vì sao đáy phẳng (flat minimum) lại tổng quát hóa tốt hơn đáy sắc (sharp minimum)?*

## Bản đồ kiến thức nền: Ba trụ cột của cơ chế Thoát yên ngựa và Hình học đáy cực tiểu

Bài học này nối kết động lực học tối ưu với khả năng tổng quát hóa thông qua ba trụ cột sau:

- **Khuếch đại theo hàm mũ dọc hướng độ cong âm:** Gần điểm yên ngựa có trị riêng âm $$-\gamma < 0$$, mỗi bước GD nhân thành phần lệch dọc hướng thoát với hệ số $$(1 + \eta\gamma) > 1$$. Chỉ cần nhiễu SGD tạo ra một thành phần lệch ban đầu cỡ $$\delta > 0$$, nó sẽ nở lớn theo hàm mũ $$(1 + \eta\gamma)^k \delta$$ và bắn vọt ra khỏi yên ngựa sau chỉ $$O(\log(1/\delta))$$ bước!
- **Chi phí và Quy mô của các cơ chế thoát yên ngựa:** SGD thoát yên ngựa tự nhiên nhờ phương sai minibatch; Perturbed GD thêm nhiễu chủ động khi $$\|\nabla F\|$$ nhỏ để có bảo đảm lý thuyết; còn các phương pháp khai thác độ cong âm (Hessian–vector product) tìm thẳng hướng thoát nhưng tốn kém hơn trong thực tế mạng lớn.
- **Cực tiểu phẳng vs. Cực tiểu sắc (Flat vs. Sharp Minima):** Khi phân phối tập test hơi dịch chuyển so với tập train (tương đương bề mặt hàm mất mát dịch ngang một đoạn $$\delta$$), mức tăng sai số tỉ lệ thuận với trị riêng lớn nhất của Hessian $$\frac{1}{2}\lambda_{\max} \delta^2$$. Do đó, các đáy phẳng ($$\lambda_{\max}$$ nhỏ, mục tiêu của SAM và SGD lô nhỏ) có sức chống chịu phân phối lệch vượt trội.

### Khung giải thích (nên đọc chậm): Tính tay tốc độ thoát yên ngựa và độ nhạy của đáy sắc vs. đáy phẳng

Hãy tự tay kiểm chứng cả hai hiện tượng cốt lõi của bài học bằng hai phép tính ngắn gọn:

1. **Khuếch đại hàm mũ khi thoát yên ngựa (Perturbed GD):**
   Xét hàm yên ngựa $$F(x, y) = \frac{1}{2}(x^2 - y^2)$$ tại điểm dừng $$(0, 0)$$ với $$\eta = 0.5$$.
   - Không có nhiễu: $$\nabla F(0, 0) = (0, 0) \implies$$ kẹt vĩnh viễn tại $$(0, 0)$$.
   - Thêm một cú huých siêu nhỏ $$\delta = 0.01$$ vào tọa độ $$y$$ (đưa điểm về $$(0,\; 0.01)$$):
     Vì $$\frac{\partial F}{\partial y} = -y$$, quy tắc cập nhật là $$y_{k+1} = y_k - 0.5(-y_k) = 1.5 y_k$$!
     - Sau 1 bước: $$y_1 = 0.015$$.
     - Sau 2 bước: $$y_2 = 0.0225$$.
     - Sau 12 bước: $$y_{12} = (1.5)^{12} \cdot 0.01 \approx 1.30$$ — đã nhảy vọt ra xa hơn **130 lần** chỉ nhờ một hạt nhiễu $$0.01$$!
2. **Đo độ nhạy của cực tiểu phẳng so với cực tiểu sắc dưới độ lệch $$\delta = 0.1$$:**
   Giả sử trên tập train cả hai đều đạt mất mát $$0$$ tại $$w^\star$$, nhưng khi chuyển sang tập test vị trí tối ưu bị dịch lệch $$\delta = 0.1$$:
   - *Đáy phẳng* $$F_{\text{flat}}(w) = 1 \cdot (w - w^\star)^2$$ (Hessian $$H = 2$$): mất mát tăng thêm $$\Delta F_{\text{flat}} = 1 \cdot (0.1)^2 = 0.01$$.
   - *Đáy sắc* $$F_{\text{sharp}}(w) = 100 \cdot (w - w^\star)^2$$ (Hessian $$H = 200$$): mất mát tăng thêm $$\Delta F_{\text{sharp}} = 100 \cdot (0.1)^2 = 1.00$$ — **tệ hơn đúng 100 lần**!

Các thuật toán tối ưu quen thuộc thoát khỏi điểm yên ngựa chặt bằng những cơ chế nào?

* **Nhiễu từ SGD:** Gradient ước lượng trên minibatch không trùng khít với $$\nabla F$$; thành phần nhiễu ngẫu nhiên có hình chiếu khác 0 lên hướng độ cong âm với xác suất cao, giúp đẩy điểm lặp ra khỏi điểm yên ngựa. Ngược lại, gradient descent toàn lô có thể đứng yên vĩnh viễn nếu rơi đúng vào điểm yên ngựa không có thành phần lệch (như điểm $$(0,0)$$ ở bài trước).
* **Gradient descent có nhiễu (Perturbed GD):** Chủ động cộng nhiễu đẳng hướng khi $$\|\nabla F\|$$ nhỏ là phiên bản dễ phân tích lý thuyết của cơ chế trên (Ge, Huang, Jin, Yuan; Jin và cộng sự).
* **Momentum:** Quán tính có thể giúp điểm lặp vượt qua vùng yên phẳng rồi trượt xuống, nhưng cũng có thể gây dao động; tự bản thân momentum không phải là bảo đảm toán học cho việc thoát điểm yên ngựa.
* **Phương pháp bậc hai / khai thác độ cong âm:** Sử dụng tích Hessian–vector (kiểu Pearlmutter hoặc Neon) để chủ động hạ theo vector riêng ứng với trị riêng âm nhỏ nhất. Các phương pháp này ít dùng trực tiếp trong huấn luyện học sâu quy mô lớn nhưng rất hữu ích để hiểu cơ chế hình học.

**Cực tiểu sắc và cực tiểu phẳng.** Giữa hai cực tiểu có cùng giá trị hàm mất mát $$F$$, điểm có các trị riêng Hessian lớn hơn tương ứng với đáy *sắc* hơn: chỉ một nhiễu nhỏ trên tham số (hoặc độ lệch phân phối nhỏ của dữ liệu kiểm tra) cũng có thể làm hàm mất mát tăng mạnh. Thuật toán **SAM** (Foret và cộng sự, ICLR 2021) tối ưu giá trị cực đại trong một lân cận nhỏ để hướng về các vùng phẳng hơn (xem bài seminar tùy chọn 26-06).

Hình dung hình học cần ghi nhớ: bề mặt hàm mất mát của mạng sâu không đơn giản như đồ thị 2 chiều với vài hố riêng lẻ, mà là một cấu trúc nhiều chiều có các **vùng cao nguyên** rộng, các **hẻm hẹp** (gắn với số điều kiện xấu ở Chương 06 và 26), và tính **đối xứng** (hoán vị các nơ-ron ẩn không làm đổi $$F$$, nên các điểm cực tiểu tạo thành những đa tạp liên tục). Khi quan sát hình chiếu 3 chiều trong các công cụ mô phỏng, luôn cần lưu ý những chiều thông tin đã bị chiếu mất.

### Điểm yên ngựa trong khoảng 3 phút

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/saddle-escape_vi.mp4"></video>
</div>

GD bị hút vào yên ngựa của x² − y² + ½y⁴, ngồi lâu khi lệch rất nhỏ, thoát nhờ nhiễu, và vì sao ở chiều cao hầu hết điểm tới hạn là yên ngựa.

**Câu hỏi.** Nếu nhiễu của SGD là cơ chế giúp đẩy điểm lặp khỏi điểm yên ngựa, điều gì xảy ra khi kích thước minibatch $$B \to n$$, và nhận xét này liên hệ thế nào đến cuộc thảo luận về khả năng tổng quát hóa của kích thước lô lớn?
