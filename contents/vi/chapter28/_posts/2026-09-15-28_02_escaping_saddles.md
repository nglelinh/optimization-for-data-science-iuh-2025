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


Các thuật toán tối ưu quen thuộc thoát khỏi điểm yên ngựa chặt bằng những cơ chế nào?

* **Nhiễu từ SGD:** Gradient ước lượng trên minibatch không trùng khít với $$\nabla F$$; thành phần nhiễu ngẫu nhiên có hình chiếu khác 0 lên hướng độ cong âm với xác suất cao, giúp đẩy điểm lặp ra khỏi điểm yên ngựa. Ngược lại, gradient descent toàn lô có thể đứng yên vĩnh viễn nếu rơi đúng vào điểm yên ngựa không có thành phần lệch (như điểm $$(0,0)$$ ở bài trước).
* **Gradient descent có nhiễu (Perturbed GD):** Chủ động cộng nhiễu đẳng hướng khi $$\|\nabla F\|$$ nhỏ là phiên bản dễ phân tích lý thuyết của cơ chế trên (Ge, Huang, Jin, Yuan; Jin và cộng sự).
* **Momentum:** Quán tính có thể giúp điểm lặp vượt qua vùng yên phẳng rồi trượt xuống, nhưng cũng có thể gây dao động; tự bản thân momentum không phải là bảo đảm toán học cho việc thoát điểm yên ngựa.
* **Phương pháp bậc hai / khai thác độ cong âm:** Sử dụng tích Hessian–vector (kiểu Pearlmutter hoặc Neon) để chủ động hạ theo vector riêng ứng với trị riêng âm nhỏ nhất. Các phương pháp này ít dùng trực tiếp trong huấn luyện học sâu quy mô lớn nhưng rất hữu ích để hiểu cơ chế hình học.

**Cực tiểu sắc và cực tiểu phẳng.** Giữa hai cực tiểu có cùng giá trị hàm mất mát $$F$$, điểm có các trị riêng Hessian lớn hơn tương ứng với đáy *sắc* hơn: chỉ một nhiễu nhỏ trên tham số (hoặc độ lệch phân phối nhỏ của dữ liệu kiểm tra) cũng có thể làm hàm mất mát tăng mạnh. Thuật toán **SAM** (Foret và cộng sự, ICLR 2021) tối ưu giá trị cực đại trong một lân cận nhỏ để hướng về các vùng phẳng hơn (xem bài seminar tùy chọn 26-06).

Hình dung hình học cần ghi nhớ: bề mặt hàm mất mát của mạng sâu không đơn giản như đồ thị 2 chiều với vài hố riêng lẻ, mà là một cấu trúc nhiều chiều có các **vùng cao nguyên** rộng, các **hẻm hẹp** (gắn với số điều kiện xấu ở Chương 06 và 26), và tính **đối xứng** (hoán vị các nơ-ron ẩn không làm đổi $$F$$, nên các điểm cực tiểu tạo thành những đa tạp liên tục). Khi quan sát hình chiếu 3 chiều trong các công cụ mô phỏng, luôn cần lưu ý những chiều thông tin đã bị chiếu mất.

**Câu hỏi.** Nếu nhiễu của SGD là cơ chế giúp đẩy điểm lặp khỏi điểm yên ngựa, điều gì xảy ra khi kích thước minibatch $$B \to n$$, và nhận xét này liên hệ thế nào đến cuộc thảo luận về khả năng tổng quát hóa của kích thước lô lớn?
