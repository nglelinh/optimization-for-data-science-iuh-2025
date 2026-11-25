---
layout: post
title: 10 Tính Đối Ngẫu trong Quy Hoạch Tuyến Tính
chapter: '10'
order: 1
owner: Wontak Ryu
categories:
- chapter10
lang: vi
---

Mùa thu năm 1947, khi George Dantzig — cha đẻ của thuật toán đơn hình (simplex) — đến thăm Viện Nghiên cứu Cao cấp Princeton để trình bày mô hình quy hoạch tuyến tính (LP) vừa phát minh cho huyền thoại John von Neumann, một khoảnh khắc lịch sử đã xảy ra. Nghe Dantzig trình bày chưa đầy nửa giờ, von Neumann lập tức phác thảo ngay trên bảng đen một "bài toán song sinh" đi kèm mọi bài toán LP — bài toán mà sau này cả thế giới gọi là **bài toán đối ngẫu (dual problem)**.

Tính đối ngẫu là một trong những phép màu kỳ diệu nhất của toán học hiện đại: nó biến câu hỏi *"Làm sao phân bổ tài nguyên để tối đa hóa lợi nhuận?"* thành câu hỏi gương phản chiếu *"Mỗi đơn vị tài nguyên thực sự đáng giá bao nhiêu (giá bóng — shadow price)?"* Chương 10 sẽ dẫn bạn đi từ trực giác sơ cấp về cận dưới, sang định lý đối ngẫu mạnh, rồi chứng kiến cách một khái niệm duy nhất thống nhất cả định lý luồng cực đại – lát cắt cực tiểu trong lý thuyết đồ thị lẫn định lý minimax của von Neumann trong lý thuyết trò chơi!

## Bản đồ kiến thức nền: Bốn trụ cột của tính đối ngẫu trong Quy hoạch tuyến tính

- **Bài toán gốc (Primal) và bài toán đối ngẫu (Dual):** Mọi bài toán LP đều có một bản sao đối ngẫu được xây dựng thuần túy từ ma trận ràng buộc và vector mục tiêu: biến gốc ứng với ràng buộc đối ngẫu, và ràng buộc gốc ứng với biến đối ngẫu.
- **Tính đối ngẫu yếu và mạnh (Weak & Strong Duality):** Giá trị khả thi bất kỳ của bài toán đối ngẫu (cực đại hóa) luôn chặn dưới mọi giá trị khả thi của bài toán gốc (cực tiểu hóa): $$d \le p$$. Với LP, chỉ cần một trong hai bài toán có nghiệm tối ưu hữu hạn, khoảng cách giữa chúng bằng đúng $$0$$ ($$d^* = p^*$$)!
- **Ý nghĩa kinh tế — Giá bóng (Shadow Prices):** Nghiệm đối ngẫu tối ưu $$u_i^*$$ đo chính xác độ nhạy $$\frac{\partial p^*}{\partial b_i}$$ — tức mức tăng giá trị tối ưu nếu ta nới thêm một đơn vị tài nguyên thứ $$i$$.
- **Điều kiện bù (Complementary Slackness) và tính đối hợp:** Ở điểm tối ưu, ràng buộc gốc nào còn dư thừa thì giá bóng tương ứng bằng $$0$$ (và ngược lại); đồng thời lấy đối ngẫu của bài toán đối ngẫu sẽ quay về đúng bài toán gốc ban đầu.

### Khung giải thích (nên đọc chậm): Cặp bài toán gốc – đối ngẫu trên một xưởng mộc nhỏ

Một xưởng mộc làm bàn ($$x_1$$) và ghế ($$x_2$$) từ một nguồn gỗ duy nhất có trữ lượng $$10$$ m³:
- Mỗi bàn cần $$2$$ m³ gỗ, lãi $$4$$ triệu đồng.
- Mỗi ghế cần $$1$$ m³ gỗ, lãi $$1.5$$ triệu đồng.

1. **Bài toán gốc (Góc nhìn chủ xưởng — tối đa hóa lợi nhuận):**
   $$\max_{x_1, x_2 \ge 0} \; 4 x_1 + 1.5 x_2 \quad \text{s.t.} \quad 2 x_1 + x_2 \le 10.$$
   Vì bàn mang lại $$4/2 = 2$$ triệu/m³ còn ghế chỉ $$1.5/1 = 1.5$$ triệu/m³, chủ xưởng đóng toàn bộ $$5$$ bàn ($$x^* = (5, 0)$$) và thu lợi nhuận tối đa $$p^* = 20$$ triệu đồng.
2. **Bài toán đối ngẫu (Góc nhìn nhà đầu tư muốn mua lại toàn bộ kho gỗ với giá $$u \ge 0$$ triệu/m³):**
   Để chủ xưởng đồng ý bán gỗ thay vì tự đóng đồ, giá $$u$$ phải hấp dẫn hơn cả hai phương án sản xuất:
   - Bán $$2$$ m³ gỗ phải thu ít nhất bằng lãi 1 bàn: $$2u \ge 4 \implies u \ge 2$$.
   - Bán $$1$$ m³ gỗ phải thu ít nhất bằng lãi 1 ghế: $$u \ge 1.5$$.
   Nhà đầu tư muốn chi ít nhất để mua $$10$$ m³ gỗ: $$\min_{u \ge 0} 10u$$ sao cho $$u \ge 2, u \ge 1.5$$.
   Nghiệm tối ưu là $$u^* = 2$$ triệu/m³, tổng chi phí $$d^* = 10 \times 2 = 20$$ triệu đồng = $$p^*$$! Giá trị kho gỗ dưới hai góc nhìn khớp nhau tuyệt đối.

Từ chương này, chúng ta bắt đầu tìm hiểu về tính đối ngẫu (duality) — một khái niệm nền tảng trong lý thuyết tối ưu hóa. Trong tối ưu hóa, tính đối ngẫu cho phép xem xét một bài toán từ hai góc độ song hành: bài toán gốc (primal problem) và bài toán đối ngẫu (dual problem).

Trong chương này, chúng ta tập trung vào tính đối ngẫu trong quy hoạch tuyến tính (LP). Thay vì xét ngay các bài toán lồi tổng quát, ta sẽ xây dựng bài toán đối ngẫu trực tiếp từ bài toán quy hoạch tuyến tính gốc, đồng thời làm rõ mối liên hệ giữa hai bài toán và các tính chất tương ứng trong những điều kiện cụ thể.

## Ứng dụng hiện đại (2022–2026)

Bài đọc tùy chọn đi kèm trình bày vai trò của đối ngẫu LP như một chứng chỉ trong kiểm chứng mạng nơ-ron (α,β-CROWN), định giá biên theo vị trí (LMP) trên thị trường điện, bài toán luồng cực đại – lát cắt cực tiểu và vận chuyển tối ưu Kantorovich. Xem [10-07 Ứng dụng hiện đại của đối ngẫu LP]({% multilang_post_url contents/chapter10/2026-09-16-10_07_modern_applications %}).
