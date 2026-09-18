---
layout: post
title: 28 Phong cảnh không lồi cho học sâu
chapter: '28'
order: 1
owner: Nguyen Le Linh
categories:
- chapter28
lang: vi
lesson_type: required
---


# Phong cảnh không lồi cho học sâu

Tính lồi là lan can an toàn của Chương 02–25: cực tiểu địa phương là toàn cục, và điều kiện bậc nhất chứng nhận tối ưu. Hàm mất mát huấn luyện $$F(w)$$ của mạng sâu là **không lồi**. Chương này không vứt lan can; nó hỏi loại không lồi nào mà người thực hành thực sự gặp.

Ta sẽ phân loại **điểm tới hạn** ($$\nabla F(w)=0$$) theo quán tính của Hessian: cực tiểu, cực đại, và **yên ngựa**. Ta sẽ thấy vì sao yên ngựa chiều cao, không phải cực tiểu địa phương lầy lội, mới là chướng ngại thường gặp, và vì sao **quá tham số** (nhiều tham số hơn ràng buộc dữ liệu) có thể khiến hầu hết cực tiểu nội suy — câu chuyện hiện đại “vì sao SGD chạy?” ở độ sâu IUH.

EPFL CS-439 và USC CSCI 599 coi đây là mô-đun nâng cao nhưng kỳ vọng. Ta dừng ở định nghĩa chính xác cộng hình, không phải giới hạn PDE trường trung bình.

Mở [loss_function_landscapes.html](https://nglelinh.github.io/interactive_math/optimization/loss_function_landscapes.html) khi đọc.

## Các bài

1. Điểm tới hạn và yên ngựa
2. Thoát yên ngựa và hình học phong cảnh
3. Quá tham số (và con trỏ tới điều kiện PL)
4. Nghiên cứu tình huống phong cảnh hiện đại (tùy chọn) — liên thông mode, grokking, double descent, cực tiểu phẳng
5. Điều kiện PL và câu chuyện tốc độ hiện đại (tùy chọn) — Karimi et al.; tái sử dụng tốc độ tuyến tính Chương 06 không cần lồi

Cầu PL từ các chứng minh lồi mạnh của 06-03-04 tới một số ERM không lồi nay là một bài, không chỉ một con trỏ arXiv: [28-05]({% multilang_post_url contents/chapter28/2026-09-18-28_05_pl_condition %}). Các hiện tượng 2022–2026 nằm ở [28-04]({% multilang_post_url contents/chapter28/2026-09-16-28_04_modern_landscapes %}).
