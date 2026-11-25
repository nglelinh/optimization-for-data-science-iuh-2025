---
layout: post
title: 27 Vi phân tự động
chapter: '27'
order: 1
owner: Nguyen Le Linh
categories:
- chapter27
lang: vi
lesson_type: required
---

Nếu Chương 26 là động cơ lái xe của học sâu (SGD, AdamW), thì **Vi phân tự động (Automatic Differentiation — AD)** ở Chương 27 chính là hệ thống cảm biến cung cấp nhiên liệu gradient cho động cơ đó. Điều đáng kinh ngạc là một mạng nơ-ron hiện đại có thể chứa hàng chục tỷ tham số và hàng nghìn lớp phép toán lồng nhau — vậy mà máy tính vẫn tính được **chính xác toàn bộ vector gradient** chỉ trong một khoảng thời gian xấp xỉ vài lần chạy xuôi hàm mất mát!

Hiểu sai phổ biến nhất của người mới là tưởng AD giống vi phân ký hiệu (như WolframAlpha rút gọn công thức) hoặc giống sai phân hữu hạn (cộng thêm $$\varepsilon$$ nhỏ rồi chia). Thực tế, AD là một phát minh tinh tế hoàn toàn riêng biệt: nó không lấy đạo hàm *biểu thức*, mà lấy đạo hàm **chính dòng chảy thực thi của chương trình máy tính** bằng quy tắc dây chuyền.

## Kiến thức cần nhớ: Ba trụ cột phân biệt AD với các phương pháp tính đạo hàm khác

Trước khi đi vào đồ thị tính toán và hai chế độ thuận/nghịch, hãy đặt AD lên bàn cân cùng hai phương pháp truyền thống:

- **Vi phân ký hiệu (Symbolic Differentiation):** Biến đổi trực tiếp biểu thức toán học thành công thức đạo hàm tường minh. Nhược điểm chí mạng là hiện tượng **bùng nổ biểu thức (expression swell)** và hoàn toàn bó tay trước các câu lệnh lập trình như vòng lặp `for`, nhánh `if-else`.
- **Sai phân hữu hạn (Finite Differences):** Xấp xỉ $$\frac{f(x + \varepsilon e_i) - f(x)}{\varepsilon}$$. Dễ cài nhưng vừa *không chính xác* (kẹt giữa sai số cắt cụt khi $$\varepsilon$$ lớn và sai số triệt tiêu số học khi $$\varepsilon$$ quá nhỏ), vừa tốn tới $$n+1$$ lần chạy hàm cho $$n$$ tham số — bất khả thi khi $$n = 10^8$$.
- **Vi phân tự động (Forward & Reverse Mode AD):** Phân rã chương trình thành dãy phép toán sơ cấp ($$+, \times, \sin, \exp, \dots$$) và truyền đạo hàm qua từng bước bằng quy tắc dây chuyền: *chính xác tuyệt đối đến độ chính xác dấu phẩy động*, chạy được qua nhánh/vòng lặp, và đặc biệt ở chế độ nghịch chỉ tốn $$O(1)$$ lần chạy hàm bất kể $$n$$ lớn cỡ nào!

### Giải thích: So sánh tay Sai phân hữu hạn với AD (Số đối ngẫu) trên $$f(x) = x^2$$

Xét hàm đơn giản $$f(x) = x^2$$ tại điểm $$x = 3$$, nơi đạo hàm chính xác là $$f'(3) = 6$$.

1. **Dùng sai phân hữu hạn $$\frac{f(3 + \varepsilon) - f(3)}{\varepsilon}$$:**
   - Chọn bước hơi lớn $$\varepsilon = 0.1$$: $$\frac{3.1^2 - 3^2}{0.1} = \frac{9.61 - 9}{0.1} = 6.1$$ — **lệch mất $$0.1$$** (sai số cắt cụt).
   - Chọn bước quá nhỏ $$\varepsilon = 10^{-16}$$ trong số thực 64-bit (`float64`): máy tính làm tròn $$3.0 + 10^{-16} = 3.0$$, nên tử số bằng $$9.0 - 9.0 = 0.0$$, kết quả ra **$$0.0$$** — sai hoàn toàn $$100\%$$ (sai số triệt tiêu)!
2. **Dùng Vi phân tự động bằng số đối ngẫu (Dual Number $$x + \dot{x}\epsilon$$ với quy ước $$\epsilon^2 = 0$$):**
   Đưa đầu vào $$3 + 1\cdot\epsilon$$ chạy thẳng qua phép bình phương của chương trình:
   $$f(3 + \epsilon) = (3 + \epsilon)^2 = 3^2 + 2(3)\epsilon + \epsilon^2 = 9 + 6\epsilon + 0 = 9 + 6\epsilon.$$
3. **Đọc kết quả:** Phần thực trả về đúng giá trị hàm $$f(3) = 9$$, còn hệ số của $$\epsilon$$ trả về **chính xác tuyệt đối $$f'(3) = 6$$** — không cần chọn bước $$\varepsilon$$, không có sai số cắt cụt, và không bao giờ gặp lỗi triệt tiêu!

# Vi phân tự động

Mọi bộ tối ưu ở Chương 26 đều cần tính gradient. Trong thực tế hiện nay, gradient hầu như không còn được tính thủ công trên giấy hay xấp xỉ bằng sai phân hữu hạn. **Vi phân tự động (Automatic Differentiation — AD)** tính đạo hàm *chính xác đến sai số dấu phẩy động* của một chương trình bằng cách áp dụng quy tắc dây chuyền (chain rule) một cách hệ thống lên từng phép toán sơ cấp.

Chương này trả lời ba câu hỏi trọng tâm:

1. **Đồ thị tính toán** là gì, và vì sao một hàm mất mát có thể xem như một chương trình?
2. AD **chiều thuận** tính tích Jacobian–vector như thế nào?
3. Vì sao **lan truyền ngược (backpropagation)** chính là AD chiều nghịch, và vì sao chế độ nghịch là lựa chọn mặc định khi bài toán có một hàm mất mát vô hướng và hàng triệu tham số?

Tài liệu tổng quan nền tảng nên tham khảo là Baydin, Pearlmutter, Radul và Siskind, *Automatic Differentiation in Machine Learning: a Survey*, JMLR 18(153), 2018, [jmlr.org/papers/v18/17-468.html](https://www.jmlr.org/papers/v18/17-468.html). Ngay từ giáo trình cổ điển của Nocedal & Wright, bài toán tính đạo hàm đã là một phần thiết yếu của tối ưu số; vi phân tự động hiện đại là bước hoàn thiện về mặt phần mềm cho nền tảng đó.

## Nội dung các bài

1. Đồ thị tính toán.
2. AD chiều thuận.
3. AD chiều nghịch và lan truyền ngược.
4. Khung vi phân tự động và học máy khoa học (tùy chọn) — PyTorch, JAX, Enzyme, PINN.
5. Tối ưu hai mức và siêu gradient (tùy chọn) — tối ưu siêu tham số (HPO) và học siêu cấp (meta-learning) dưới dạng bài toán lồng nhau.

Bài thực hành chính: tự cài đặt AD chiều nghịch trên một mạng ba nút và đối chiếu với `torch.autograd` — nếu kết quả sai lệch, nguyên nhân nằm ở đồ thị tính toán hoặc thao tác `detach` chứ không phải định nghĩa đạo hàm. Bản đồ các khung phần mềm nằm ở bài tùy chọn [27-04]({% multilang_post_url contents/chapter27/2026-09-16-27_04_autodiff_frameworks %}), còn khuôn khổ tối ưu hai mức cho HPO và MAML (khai triển vòng lặp so với vi phân ẩn) nằm ở [27-05]({% multilang_post_url contents/chapter27/2026-09-18-27_05_bilevel_hypergrad %}).
