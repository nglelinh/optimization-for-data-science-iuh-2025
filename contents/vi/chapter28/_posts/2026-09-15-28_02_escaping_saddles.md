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


Các thuật toán bạn đã biết rời yên ngựa chặt thế nào?

- **Nhiễu giúp.** Ước lượng gradient của SGD không đúng bằng $$\nabla F$$. Một nhiễu ngẫu nhiên có thành phần theo hướng độ cong âm với xác suất cao. GD cả lô có thể ngồi tại yên ngựa nếu đến đó với thành phần không trên hướng ấy (ví dụ $$(0,0)$$ bài trước).
- **GD nhiễu.** Cộng nhiễu đẳng hướng tường minh khi $$\|\nabla F\|$$ nhỏ là họ hàng thân thiện với định lý của SGD (Ge, Huang, Jin, Yuan, rồi Jin et al. về perturbed GD).
- **Momentum** có thể vượt sống phẳng rồi rơi; cũng có thể dao động. Đừng coi đó là bảo đảm thoát yên.
- **Bước bậc hai / độ cong âm** (tích Hessian–vector kiểu Pearlmutter, hoặc kiểu Neon) chủ động đi xuống theo vector riêng âm nhất. Hiếm trong DL sản xuất; hữu ích như mô hình tư duy.

**Cực tiểu sắc và phẳng.** Quanh hai cực tiểu cùng $$F$$, trị riêng Hessian lớn hơn nghĩa là chén *sắc*: một nhiễu tham số nhỏ (hoặc lệch phân phối nhỏ) làm loss tăng nhiều. **SAM** (Foret et al., ICLR 2021) tối ưu một bao max địa phương để ưa vùng phẳng hơn; đó là seminar tùy chọn, không phải thuật toán bắt buộc kỳ này.

Hình học cần giữ: mặt loss không phải hoạt họa 2-D với vài hố. Đó là vật thể chiều cao với **cao nguyên** lớn, **hẻm hẹp** (câu chuyện số điều kiện ở Chương 06 và 26), và đối xứng (hoán vị đơn vị ẩn để $$F$$ bất biến, nên cực tiểu đi thành đa tạp). Khi demo hiện mặt 3-D, hãy hỏi thứ gì đã bị *chiếu mất*.

**Câu hỏi.** Nếu nhiễu SGD là thứ hất bạn khỏi yên ngựa, cơ chế đó ra sao khi batch size $$B\to n$$? Điều đó có thể nói gì với tranh luận “tổng quát hóa batch lớn”?
