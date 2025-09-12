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

Có sự khác biệt về tốc độ hội tụ giữa phương pháp tuần hoàn và phương pháp ngẫu nhiên.

[Tốc độ hội tụ]({% multilang_post_url contents/chapter08/20-03-29-08_01_04_convergence_rate %}) của phương pháp subgradient batch là $$O(G_{batch}^{2}/\epsilon^{2})$$, trong đó $$G_{batch}$$ là hằng số Lipschitz của $$\sum f_i$$.

- **Phương pháp tuần hoàn**: Độ phức tạp lặp của phương pháp tuần hoàn là $$O(m^{3}G^{2}/\epsilon^{2})$$. Nếu một chu kỳ của phương pháp subgradient ngẫu nhiên tuần hoàn được coi là tương đương với một phương pháp subgradient batch, thì mỗi chu kỳ cần $$O(m^{2}G^{2}/\epsilon^{2})$$ lần lặp. ($$G$$ là hằng số Lipschitz của một hàm đơn $$f_i$$)

- **Phương pháp ngẫu nhiên**: Độ phức tạp lặp của phương pháp ngẫu nhiên là $$O(m^{2}G^{2}/\epsilon^{2})$$. Tức là, phương pháp ngẫu nhiên cần $$O(mG^{2}/\epsilon^2)$$ lần lặp, nhanh hơn $$m$$ lần so với phương pháp batch và tuần hoàn với $$O(m^2G^2/\epsilon^2)$$. Về mặt ký hiệu Big-O, nếu $$m$$ lớn, phương pháp ngẫu nhiên có tốc độ hội tụ nhanh hơn.

Mặc dù các cận Big-O cho phương pháp ngẫu nhiên và tuần hoàn khác nhau một hệ số $$m$$, lưu ý rằng cận Big-O của phương pháp tuần hoàn là trường hợp xấu nhất, trong khi của phương pháp ngẫu nhiên là trường hợp trung bình. Trong thực tế, sự khác biệt có thể không lớn như ký hiệu Big-O gợi ý.
