---
layout: post
title: '17-03 Một chút lịch sử'
chapter: '17'
order: 7
owner: Minjoo Lee
categories:
- chapter17
lang: vi
---

Năm 1984, một bài báo của Narendra Karmarkar tại Bell Labs đã làm chấn động không chỉ giới toán học mà cả trang nhất tờ *New York Times*: ông tuyên bố tìm ra một thuật toán thời gian đa thức giải quy hoạch tuyến tính nhanh gấp hàng chục lần phương pháp đơn hình kinh điển của George Dantzig. Cuộc tranh luận nảy lửa kéo dài cả thập kỷ sau đó — giữa những người bảo vệ Simplex đi men theo các đỉnh đa diện và phe điểm trong (Interior-Point) xuyên thẳng qua lòng đa diện — cuối cùng đã sinh ra kỷ nguyên vàng của tối ưu hóa lồi hiện đại và các bộ giải lai (hybrid solvers) ngày nay.

## Bản đồ kiến thức nền: Bốn cột mốc lịch sử định hình ngành tối ưu hóa

Nhìn lại hành trình từ thập niên 1940 đến cuối thế kỷ XX giúp ta hiểu rõ sự khác biệt giữa độ phức tạp lý thuyết (worst-case) và hiệu năng thực tế:

- **Kỷ nguyên Đơn hình (Simplex — Dantzig, 1947):** Đi dọc theo các cạnh và đỉnh của đa diện khả thi. Trong thực tế, Simplex cực nhanh và dễ khởi động nóng (warm-start), nhưng Klee và Minty (1972) đã chứng minh nó có thể mất số bước hàm mũ $$2^n$$ trên các đa diện bị bóp méo.
- **Bước ngoặt Lý thuyết (Ellipsoid — Khachiyan, 1979):** Chứng minh lần đầu tiên rằng quy hoạch tuyến tính thuộc lớp độ phức tạp đa thức **P**. Tuy nhiên, phương pháp ellipsoid hội tụ quá chậm trong thực tế nên chủ yếu có ý nghĩa lý thuyết.
- **Cuộc cách mạng Điểm trong (Karmarkar 1984 → Renegar 1988 → Mehrotra 1992):** Kết nối phép chiếu xạ ảnh của Karmarkar với hàm chắn logarit cổ điển (Fiacco–McCormick) và phương pháp Newton gốc–đối ngẫu, đạt cận độ phức tạp $$O(\sqrt{n}\log(1/\epsilon))$$ và hiệu năng thực chiến cực mạnh.
- **Tổng quát hóa lên Quy hoạch Nón (Nesterov & Nemirovskii, 1994):** Lý thuyết hàm tự phù hợp (self-concordant barriers) mở rộng toàn bộ sức mạnh của phương pháp điểm trong từ quy hoạch tuyến tính sang quy hoạch nón bậc hai (SOCP) và quy hoạch bán xác định (SDP).

### Khung giải thích (nên đọc chậm): So sánh con số tăng trưởng giữa Simplex (Klee–Minty) và Điểm trong

Để cảm nhận sức mạnh của bước nhảy từ độ phức tạp hàm mũ sang độ phức tạp đa thức $$O(\sqrt{n}\log(1/\epsilon))$$, hãy tính thử với một bài toán LP kích thước khiêm tốn $$n = 50$$ biến và độ chính xác yêu cầu $$\epsilon = 10^{-8}$$:

1. **Trường hợp xấu nhất của Simplex trên hình lập phương Klee–Minty:**
   - Với $$n = 3$$, hình lập phương biến dạng có $$2^3 = 8$$ đỉnh; Simplex đi qua cả 8 đỉnh (7 bước xoay).
   - Với $$n = 50$$, số đỉnh cần duyệt lên tới $$2^{50} = 1{,}125{,}899{,}906{,}842{,}624 \approx 1.13 \times 10^{15}$$ bước! Dù mỗi giây thực hiện $$10^9$$ phép xoay, máy tính vẫn mất hơn **13 ngày** chỉ cho một bài toán 50 biến.
2. **Cận lý thuyết của phương pháp điểm trong (Renegar, 1988):**
   - Số vòng lặp Newton bị chặn trên bởi cỡ $$C \sqrt{n}\ln(1/\epsilon)$$.
   - Với $$n = 50$$ và $$\epsilon = 10^{-8}$$, ta có $$\sqrt{50} \approx 7.07$$ và $$\ln(10^8) \approx 18.42$$, nên tích $$\sqrt{n}\ln(1/\epsilon) \approx 130$$ vòng lặp! Trong thực tế với kỹ thuật predictor-corrector của Mehrotra, số vòng lặp thường chỉ khoảng **15–30 bước**, gần như không tăng theo kích thước $$n$$.
3. **Vì sao cả hai vẫn cùng tồn tại?** Simplex vượt trội khi giải bài toán nhỏ hoặc cần giải lại hàng nghìn lần sau khi thêm vài ràng buộc (như trong nhánh-và-cận của quy hoạch nguyên), trong khi điểm trong tỏa sáng ở các bài toán cỡ lớn và các bài toán nón phi tuyến (SOCP, SDP) nơi khái niệm "đỉnh đa diện" không còn tồn tại.

---

Nhìn chung, các bộ giải quy hoạch tuyến tính (LP) hiện đại hàng đầu đều kết hợp cả phương pháp đơn hình (Simplex) và phương pháp điểm trong.

* Dantzig (thập niên 1940): Phương pháp đơn hình — phương pháp đầu tiên giải LP dạng tổng quát và tìm được nghiệm chính xác sau một số hữu hạn bước. Đến nay, đây vẫn là một trong những thuật toán nổi tiếng và được nghiên cứu nhiều nhất cho LP.

* Klee và Minty (1972): Xây dựng một lớp bài toán LP "bệnh lý" (Klee–Minty cube) gồm $$n$$ biến và $$2n$$ ràng buộc, khiến phương pháp đơn hình cần tới $$2^n$$ vòng lặp trong trường hợp xấu nhất.

* Khachiyan (1979): Đề xuất thuật toán thời gian đa thức đầu tiên cho LP dựa trên phương pháp ellipsoid của Nemirovski và Yudin (1976); kết quả này có ý nghĩa lý thuyết lớn nhưng không hiệu quả trong thực tế.

* Karmarkar (1984): Đề xuất phương pháp điểm trong thời gian đa thức cho LP có hiệu năng thực tế tốt, tạo bước ngoặt lớn cho lĩnh vực tối ưu hóa (Bằng sáng chế Hoa Kỳ 4,744,026, hết hạn năm 2006).

* Renegar (1988): Phát triển thuật toán điểm trong dựa trên phương pháp Newton cho LP, đạt độ phức tạp tính toán lý thuyết tốt nhất cho đến khi có các cải tiến gần đây hơn của Lee–Sidford.
