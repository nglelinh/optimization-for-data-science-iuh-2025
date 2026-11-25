---
layout: post
title: '21-05 ADMM đồng thuận (Consensus ADMM)'
chapter: '21'
order: 6
owner: Hooncheol Shin
categories:
- chapter21
lang: vi
---

Khi tập dữ liệu huấn luyện khổng lồ tới mức phải rải đều trên $$B = 100$$ máy chủ khác nhau, bài toán tối ưu có dạng tổng $$\min_x \sum_{i=1}^B f_i(x)$$, trong đó mỗi máy chủ $$i$$ chỉ nắm giữ hàm mất mát $$f_i$$ trên mảnh dữ liệu của riêng nó. Thay vì dồn dữ liệu về một chỗ, **ADMM đồng thuận (Consensus ADMM)** làm một phép biến hóa đơn giản đến ngỡ ngàng: cấp cho mỗi máy chủ một bản sao biến riêng $$x_i$$ kèm ràng buộc đồng nhất $$x_i = x$$! Nhờ vậy, bước cập nhật $$x_i$$ chạy **song song tuyệt đối** trên cả 100 máy, còn bước cập nhật biến toàn cục $$x$$ chỉ là **một phép lấy trung bình cộng** duy nhất!

## Kiến thức cần nhớ: Bốn trụ cột của ADMM đồng thuận (Consensus ADMM)

Để cài đặt và mở rộng Consensus ADMM trên hệ thống phân tán thực tế, hãy nắm rõ bốn cơ chế sau:

- **Tách biến đồng nhất ($$x_i = x, \; i = 1, \dots, B$$):** Biến bài toán tối ưu chung biến $$x$$ thành bài toán hai khối $$(x_1, \dots, x_B)$$ và biến đồng thuận $$x$$. Toàn bộ sự liên kết giữa các máy chủ bị cô lập vào duy nhất biến trung tâm $$x$$.
- **Tính chất tự triệt tiêu tổng biến đối ngẫu ($$\bar{w}^{(k)} = 0$$):** Vì bước trung tâm đặt $$x^{(k)} = \bar{x}^{(k)} + \bar{w}^{(k-1)}$$, nên khi cập nhật $$w_i^{(k)} = w_i^{(k-1)} + x_i^{(k)} - x^{(k)}$$, lấy trung bình cộng hai vế lập tức cho $$\bar{w}^{(k)} = \bar{w}^{(k-1)} + \bar{x}^{(k)} - (\bar{x}^{(k)} + \bar{w}^{(k-1)}) = 0$$ với mọi $$k \ge 1$$! Nhờ đó bước trung tâm rút gọn thành đúng trung bình cộng $$x^{(k)} = \frac{1}{B}\sum_{i=1}^B x_i^{(k)}$$!
- **Thêm điều chuẩn chung $$g(x)$$ tại máy chủ trung tâm:** Nếu bài toán là $$\min \sum_{i=1}^B f_i(x) + g(x)$$ (ví dụ phạt Lasso toàn cục $$\lambda\|x\|_1$$), bước trung tâm chỉ cần thay trung bình cộng bằng $$\operatorname{prox}_{g, 1/(B\rho)}(\bar{x}^{(k)})$$!
- **Mở rộng sang đồng thuận cục bộ trên đồ thị (General Consensus):** Khi mỗi nút chỉ dùng một tập con tọa độ của $$x$$ (như mô hình đồ thị hay lưới điện), mỗi tọa độ toàn cục $$x_j$$ chỉ cần lấy trung bình trên tập các nút có chứa tọa độ $$j$$ đó.

### Giải thích: Chạy tay 1 vòng lặp Consensus ADMM trên 3 máy chủ và kiểm chứng $$\bar{w}^{(1)} = 0$$

Xét $$B = 3$$ máy chủ giải bài toán $$\min_x \frac{1}{2}(x - 1)^2 + \frac{1}{2}(x - 4)^2 + \frac{1}{2}(x - 7)^2$$ (nghiệm tối ưu toàn cục là trung bình $$x^\star = \frac{1 + 4 + 7}{3} = 4$$). Chọn $$\rho = 1$$, khởi tạo $$x^{(0)} = 0$$ và $$w_1^{(0)} = w_2^{(0)} = w_3^{(0)} = 0$$:

1. **Bước 1 — 3 máy chủ giải song song độc lập:**
   Mỗi máy giải $$x_i^{(1)} = \arg\min_{x_i} \left(\frac{1}{2}(x_i - c_i)^2 + \frac{1}{2}(x_i - 0 + 0)^2\right) = \frac{c_i}{2}$$:
   - Máy 1 ($$c_1 = 1$$): $$x_1^{(1)} = 0.5$$.
   - Máy 2 ($$c_2 = 4$$): $$x_2^{(1)} = 2.0$$.
   - Máy 3 ($$c_3 = 7$$): $$x_3^{(1)} = 3.5$$.
2. **Bước 2 — Máy chủ trung tâm lấy trung bình cộng:**
   $$x^{(1)} = \frac{0.5 + 2.0 + 3.5}{3} = 2.0.$$
3. **Bước 3 — 3 máy chủ tự cập nhật biến đối ngẫu riêng $$w_i^{(1)} = w_i^{(0)} + x_i^{(1)} - x^{(1)}$$:**
   - $$w_1^{(1)} = 0.5 - 2.0 = -1.5$$.
   - $$w_2^{(1)} = 2.0 - 2.0 = 0.0$$.
   - $$w_3^{(1)} = 3.5 - 2.0 = +1.5$$.
   Kiểm tra tổng biến đối ngẫu: $$\bar{w}^{(1)} = \frac{-1.5 + 0.0 + 1.5}{3} = 0$$ — triệt tiêu chính xác! Và ở vòng 2, $$x_1^{(2)} = \frac{1 + 2 - (-1.5)}{2} = 2.25, \; x_2^{(2)} = 3.0, \; x_3^{(2)} = 3.75 \implies x^{(2)} = 3.0$$, tiến đều đặn về đúng $$x^\star = 4.0$$!

---

# ADMM đồng thuận

## ADMM đồng thuận cơ bản

Xét bài toán tối ưu tổng các hàm mục tiêu sau:
>$$
>\begin{align}
>\min_{x}\sum^{B}_{i=1} f_{i}(x)
>\end{align}
>$$

Để áp dụng ADMM và đồng thời biến đổi bài toán sang dạng dễ tính toán song song, phương pháp ADMM đồng thuận (consensus ADMM) tham số hóa lại bài toán bằng cách gán cho mỗi thành phần một bản sao biến cục bộ $$x_i$$ kèm ràng buộc đồng nhất:
>$$
>\begin{align}
>&\min_{x_{1},...,x_{B},x} &&\sum^{B}_{i=1} f_{i}(x_{i})\\\\
>&\text{subject to } &&x_{i}=x, i = 1,...B
>\end{align}
>$$

## Thuật toán ADMM

Cách tách biến này cho phép suy ra các bước cập nhật ADMM phân rã được theo từng khối:

>$$
>\begin{align}
>x^{(k)}_{i} &= \underset{x_{i}}{\operatorname{argmin}} f_{i}(x_{i})+\frac{\rho}{2}||x_{i}-x^{(k-1)}+w_{i}^{(k-1)}||_{2}^{2}, i=1,...B\\\\
>x^{(k)} &=\frac{1}{B}\sum_{i=1}^{B}(x_{i}^{(k)}+w_{i}^{(k-1)})\\\\
>w_{i}^{(k)} &=w_{i}^{(k-1)}+x_{i}^{(k)}-x^{(k)}, i=1,...,B
>\end{align}
>$$

## Dạng rút gọn

Đặt $$\overline{x}=\frac{1}{B}\sum_{i=1}^{B}x_{i}$$ và $$\overline{w}=\frac{1}{B}\sum_{i=1}^{B}w_{i}$$. Dễ dàng kiểm tra rằng $$\overline{w}^{(k)}=0$$ với mọi vòng lặp $$k \ge 1$$, nhờ đó bước cập nhật biến toàn cục rút gọn thành $$x^{(k)}=\overline{x}^{(k)}$$. Khi đó, thuật toán được viết gọn lại như sau:

>$$
>\begin{align}
>x^{(k)}_{i} &= \underset{x_{i}}{\operatorname{argmin}} f_{i}(x_{i})+\frac{\rho}{2}||x_{i}-\overline{x}^{(k-1)}+w_{i}^{(k-1)}||_{2}^{2},  i=1,...B\\\\
>w_{i}^{(k)} &=w_{i}^{(k-1)}+x_{i}^{(k)}-\overline{x}^{(k)},  i=1,...,B.
>\end{align}
>$$

## Trực giác

Các bước cập nhật $$x_{i}$$ ($$i = 1,\ldots,B$$) hoàn toàn độc lập nên có thể tính song song.

Từ dạng rút gọn trên, ta có thể hiểu trực quan cơ chế của ADMM đồng thuận: mỗi bước cập nhật $$x_{i}$$ vừa tìm cách cực tiểu hóa hàm mục tiêu riêng $$f_{i}(x_{i})$$, vừa chịu số hạng phạt $$l_{2}$$ kéo $$x_{i}$$ tiến về giá trị trung bình toàn cục $$\overline{x}$$. Nếu $$x_{i}$$ lớn hơn mức trung bình, biến đối ngẫu $$w_{i}$$ sẽ tăng lên, khiến số hạng phạt ở vòng lặp kế tiếp tạo lực kéo mạnh hơn để giảm $$x_{i}$$ về lại gần trung bình.

## ADMM đồng thuận tổng quát

ADMM đồng thuận có thể mở rộng cho lớp bài toán có phép biến đổi affine của $$x$$ và thêm một hàm chính quy hóa bất kỳ $$g$$:

>$$
>\begin{align}
>\min_{x}\sum_{i=1}^{B} f_{i}(a^{T}_{i}x+b_{i})+g(x)
>\end{align}
>$$

Ta tiếp tục tham số hóa lại bài toán bằng các ràng buộc đồng thuận:
>$$
>\begin{align}
>&\min_{x_{1},..x_{B},x} &&\sum^{B}_{i=1}f_{i}(a_{i}^{T}x_{i}+b_{i})+g(x)\\\\
>&\text{subject to } &&x_{i} = x, i=1,...B
>\end{align}
>$$ 

Từ đó thu được các bước cập nhật ADMM phân rã được:
>$$
>\begin{align}
>x_{i}^{(k)} &= \underset{x_{i}}{\operatorname{argmin}}f_{i}(a_{i}^{T}x_{i}+b_{i})+\frac{\rho}{2}||x_{i}-x^{(k-1)}+w_{i}^{(k-1)}||^{2}_{2}\\\\
>x^{(k)}&=\underset{x}{\operatorname{argmin}} \frac{B\rho}{2}||x-\overline{x}^{(k)}-\overline{w}^{(k-1)}||^{2}_{2}+g(x)\\\\
>w_{i}^{(k)}&=w_{i}^{(k-1)}+x_{i}^{(k)}-x^{(k)}, i=1,...B
>\end{align}
>$$ 

## Những điểm khác biệt chính

So với dạng cơ bản, ADMM đồng thuận tổng quát có các đặc điểm sau:

* Do bước cập nhật $$x^{(k)}$$ không còn rút gọn thành trung bình đơn thuần, tính chất $$\overline{w}^{(k)}=0$$ không còn giữ nguyên.
* Các biến cục bộ $$x_{i}$$ ($$i=1,\ldots,B$$) vẫn được cập nhật song song.
* Mỗi bước cập nhật $$x_{i}$$ tương ứng với việc cực tiểu hóa thành phần mất mát cục bộ kết hợp với số hạng phạt $$l_2$$.
* Bước cập nhật biến toàn cục $$x$$ trở thành một phép tính toán tử proximal đối với hàm $$g$$ (thường là số hạng chính quy hóa).
* Các cách tham số hóa lại khác nhau sẽ dẫn đến những biến thể thuật toán ADMM khác nhau.

Chi tiết tham khảo thêm tại [danh mục bài báo tham khảo của Chương 21]({% multilang_post_url contents/chapter21/21-03-29-21_00_Alternating_Direction_Method_of_Multipliers %}).
