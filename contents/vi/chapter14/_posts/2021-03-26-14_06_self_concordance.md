---
layout: post
title: 14-06 Tự hài hòa (Self concordance)
chapter: '14'
order: 12
owner: Minjoo Lee
categories:
- chapter14
lang: vi
---

Định lý hội tụ ở mục 14-05 rất ấn tượng, nhưng lại mang trong mình một "nghịch lý thẩm mỹ" khiến các nhà toán học tối ưu hồi cuối thế kỷ 20 trăn trở mãi không yên: **bản thân phương pháp Newton hoàn toàn bất biến affine**, thế nhưng cận hội tụ ở mục 14-05 lại phụ thuộc vào ba hằng số $$m, L, M$$ vốn **thay đổi loạn xạ** khi ta đổi hệ tọa độ! Hơn nữa, nhiều hàm cực kỳ quan trọng trong thực tế — tiêu biểu là hàm chắn logarit $$-\log x$$ — thậm chí còn **không** có hằng số Lipschitz toàn cục $$L$$ hay $$M$$ hữu hạn gần biên $$x \to 0^+$$!

Chính nghịch lý này đã thúc đẩy Yurii Nesterov và Arkadi Nemirovskii (1994) tạo ra một bước ngoặt lịch sử: lý thuyết **hàm tự hài hòa (self-concordant functions)**. Thay vì đo tốc độ thay đổi của đạo hàm bậc ba theo chuẩn Euclid cố định, họ đo nó *tương đối theo chính độ cong bậc hai của hàm*, mở ra một phân tích hội tụ hoàn toàn bất biến affine và đặt viên gạch nền móng cho toàn bộ lý thuyết phương pháp điểm trong hiện đại.

## Bản đồ kiến thức nền: Vì sao cần lý thuyết hàm tự hài hòa?

- **Hai lỗ hổng của phân tích cổ điển ($$m, L, M$$):** (1) Các hằng số $$m, L, M$$ hầu như không thể tính trước trong thực tế và phụ thuộc hệ tọa độ; (2) Các hàm có tiệm cận đứng như $$-\log x$$ bị nổ đạo hàm cấp hai và cấp ba gần biên, nên phân tích cổ điển hoàn toàn bất lực.
- **Triết lý "tự đo bằng thước của chính mình":** Một hàm là tự hài hòa nếu đạo hàm bậc ba bị chặn bởi lũy thừa $$3/2$$ của đạo hàm bậc hai: $$\vert f'''(x) \vert \le 2 (f''(x))^{3/2}$$. Khi tiến sát biên $$x \to 0^+$$, cả $$f'''$$ và $$f''$$ cùng bùng nổ nhưng tỷ số $$\vert f''' \vert / (f'')^{3/2}$$ vẫn giữ nguyên hằng số $$2$$!
- **Cầu nối sang Chương 15 (Phương pháp chắn):** Mọi hàm chắn logarit của quy hoạch tuyến tính, bậc hai và nửa xác định đều là hàm tự hài hòa, nhờ đó ta có cận độ phức tạp thời gian đa thức hoàn toàn độc lập với hệ tọa độ.

### Khung giải thích (nên đọc chậm): Thấy tận mắt sự sụp đổ của hằng số $$M$$ và chiến thắng của tỷ số tự hài hòa trên $$f(x) = -\log x$$

Xét hàm $$f(x) = -\log x$$ trên miền $$x > 0$$ tại hai điểm: $$x = 1$$ và $$x = 0.01$$ (gần biên).

1. **Tính các đạo hàm:**
   $$f'(x) = -\frac{1}{x}, \qquad f''(x) = \frac{1}{x^2}, \qquad f'''(x) = -\frac{2}{x^3}.$$
2. **Thử góc nhìn cổ điển ($$m, L, M$$):**
   - Tại $$x = 1$$: $$f''(1) = 1$$, $$\vert f'''(1) \vert = 2$$.
   - Tại $$x = 0.01$$: $$f''(0.01) = 10^4$$, $$\vert f'''(0.01) \vert = 2 \times 10^6$$!
   Khi $$x \to 0^+$$, hằng số Lipschitz $$M = \sup \vert f'''(x) \vert = +\infty$$ — định lý cổ điển ở mục 14-05 không áp dụng được!
3. **Thử góc nhìn tự hài hòa — tính tỷ số $$\frac{\vert f'''(x) \vert}{(f''(x))^{3/2}}$$:**
   - Tại $$x = 1$$: $$\frac{2}{1^{3/2}} = 2$$.
   - Tại $$x = 0.01$$: $$\frac{2 \times 10^6}{(10^4)^{3/2}} = \frac{2 \times 10^6}{10^6} = 2$$!
   - Tổng quát với mọi $$x > 0$$: $$\frac{2/x^3}{(1/x^2)^{3/2}} = \frac{2/x^3}{1/x^3} = 2$$ — **một hằng số bất biến tuyệt đối trên toàn miền $$(0, +\infty)$$!**

---

Phân tích hội tụ ở mục trước cho phương pháp Newton tồn tại hai hạn chế chính [1].

Thứ nhất, trong thực tế rất khó xác định các hằng số xuất hiện trong cận hội tụ như hằng số Lipschitz $$L$$ của gradient, tham số lồi mạnh $$m$$ hay hằng số Lipschitz $$M$$ của Hessian. Vì vậy, dù lý thuyết khẳng định tốc độ hội tụ, ta hầu như không thể tính trước số bước Newton cần thiết cho một bài toán cụ thể.

Thứ hai, bản thân phương pháp Newton bất biến affine, nhưng phân tích hội tụ cổ điển lại không bất biến affine. Với hàm tổng quát, các hằng số $$L, m, M$$ thay đổi theo phép biến đổi tọa độ.

Vì hai lý do trên, mục này giới thiệu lớp **hàm tự hài hòa (self-concordant functions)** nhằm khắc phục cả hai hạn chế.

Các hàm tự hài hòa có vai trò quan trọng vì ba lý do:

1. Các hàm chắn logarit dùng trong phương pháp điểm trong đều là hàm tự hài hòa (khi các ràng buộc bất đẳng thức là hàm affine hoặc bậc hai lồi).
2. Phân tích hội tụ của phương pháp Newton cho hàm tự hài hòa không phụ thuộc vào các hằng số khó ước lượng như $$L, m, M$$.
3. Tính tự hài hòa bất biến affine, nghĩa là cận số vòng lặp Newton không phụ thuộc vào phép biến đổi affine của hệ tọa độ.