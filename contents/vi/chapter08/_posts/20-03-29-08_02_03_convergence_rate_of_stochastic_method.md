---
layout: post
title: '08-02-03 Tốc độ Hội tụ của Phương pháp Ngẫu nhiên'
chapter: '08'
order: 14
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---

Tốc độ hội tụ lý thuyết có sự khác biệt giữa cách chọn chỉ số tuần hoàn và cách chọn chỉ số ngẫu nhiên.

[Tốc độ hội tụ]({% multilang_post_url contents/chapter08/20-03-29-08_01_04_convergence_rate %}) của phương pháp subgradient batch là $$O(G_{batch}^{2}/\epsilon^{2})$$, trong đó $$G_{batch}$$ là hằng số Lipschitz của hàm tổng $$\sum f_i$$ (có bậc $$mG$$ nếu mỗi $$f_i$$ có hằng số Lipschitz là $$G$$).

- **Phương pháp tuần hoàn**: Số bước cập nhật cần thiết là $$O(m^{3}G^{2}/\epsilon^{2})$$. Nếu quy đổi một chu kỳ (duyệt qua đủ $$m$$ hàm thành phần) là tương đương về chi phí với một bước của phương pháp subgradient batch, thì phương pháp tuần hoàn cần $$O(m^{2}G^{2}/\epsilon^{2})$$ chu kỳ.
- **Phương pháp ngẫu nhiên**: Số bước cập nhật cần thiết là $$O(m^{2}G^{2}/\epsilon^{2})$$, tương đương $$O(mG^{2}/\epsilon^2)$$ chu kỳ — nhanh hơn $$m$$ lần so với phương pháp batch và phương pháp tuần hoàn ($$O(m^2G^2/\epsilon^2)$$ chu kỳ). Theo đánh giá Big-O, khi $$m$$ lớn, phương pháp ngẫu nhiên có tốc độ hội tụ tốt hơn.

Mặc dù cận Big-O của hai phương pháp chênh nhau một hệ số $$m$$, cần lưu ý rằng cận của phương pháp tuần hoàn là đánh giá cho trường hợp xấu nhất, còn cận của phương pháp ngẫu nhiên là đánh giá theo kỳ vọng (trường hợp trung bình). Trong thực tế, mức chênh lệch có thể không lớn như kết quả tiệm cận gợi ý.
