---
layout: post
title: 29-03 ADMM so với song song dữ liệu và FedAvg
chapter: '29'
order: 4
owner: Nguyen Le Linh
categories:
- chapter29
lang: vi
lesson_type: required
---

Nếu bạn đã học Chương 21 (ADMM đồng thuận) và vừa học xong Bài 29-02 (FedAvg), một câu hỏi cực kỳ sắc sảo sẽ lập tức nảy ra trong đầu: *cả hai đều giải bài toán tổng $$\sum_{p=1}^P f_p(w)$$ trên nhiều máy tính tách biệt rồi lấy trung bình về biến toàn cục — vậy thực chất chúng giống và khác nhau ở đâu, và tại sao ADMM không bị hiện tượng "trôi cục bộ" như FedAvg?*

Câu trả lời gói gọn trong đúng **một thành phần bị thiếu ở FedAvg nhưng luôn hiện diện ở ADMM**: **biến đối ngẫu cục bộ $$u_p$$**! Nhờ duy trì lực bù đối ngẫu $$u_p$$ tại mỗi nút để cân bằng chính xác gradient cục bộ $$\nabla f_p(z^\star)$$, ADMM đồng thuận hội tụ về đúng nghiệm toàn cục không chút sai lệch ngay cả khi dữ liệu các nút khác nhau hoàn toàn — đổi lại nó đòi hỏi tính lồi và lưu trữ trạng thái đối ngẫu trên từng nút, điều khó làm khi có hàng triệu điện thoại di động chập chờn.

## Kiến thức cần nhớ: Ba trụ cột phân biệt ADMM, Data-Parallel SGD và FedAvg

Bảng so sánh trong bài trở nên cực kỳ dễ nhớ khi bạn đối chiếu ba phương pháp qua ba trụ cột sau:

- **Trạng thái cục bộ (Stateful Dual vs. Stateless Clients):** ADMM là thuật toán *có trạng thái* — mỗi nút $$p$$ phải giữ biến đối ngẫu $$u_p$$ qua mọi vòng để nhớ độ lệch riêng của mình. Ngược lại, FedAvg *không cần trạng thái máy khách* (stateless), rất phù hợp với kịch bản *cross-device* nơi mỗi điện thoại chỉ tham gia vài lần rồi biến mất.
- **Lớp bài toán và Cấu trúc hàm mục tiêu:** ADMM phát huy sức mạnh tối đa trên bài toán **lồi có cấu trúc** (Lasso phân tán, quy hoạch bậc hai, ràng buộc cứng giữa các nút), nơi bước con proximal giải được chính xác. Data-Parallel SGD và FedAvg sinh ra cho **mạng nơ-ron sâu phi lồi** hàng triệu tham số, nơi chỉ có thể chạy vài bước SGD xấp xỉ.
- **Môi trường hạ tầng (Data Center vs. Cross-Silo vs. Cross-Device):** Data-Parallel SGD thống trị cụm GPU tốc độ cao; ADMM và các biến thể có trạng thái (như SCAFFOLD) tỏa sáng trong liên kết liên tổ chức (*cross-silo*, ví dụ 10–50 bệnh viện ổn định); còn FedAvg là chuẩn mực cho hàng triệu thiết bị biên (*cross-device*).

### Giải thích: Tính tay cách biến đối ngẫu ADMM triệt tiêu 100% lỗi trôi cục bộ!

Hãy mang đúng ví dụ 2 máy khách non-IID từ Bài 29-02 (nơi FedAvg bị trôi vĩnh viễn về $$2.0$$ thay vì nghiệm đúng $$z^\star = 3.0$$!) sang giải bằng **ADMM đồng thuận**:

$$
\min_{x_1, x_2, z}\ \underbrace{\frac{1}{2}x_1^2}_{F_1(x_1)} + \underbrace{\frac{3}{2}(x_2 - 4)^2}_{F_2(x_2)} \qquad \text{thỏa mãn } x_1 = z,\quad x_2 = z.
$$

Lagrangian tăng cường của ADMM cho mỗi nút $$p \in \{1, 2\}$$ có dạng $$F_p(x_p) + u_p(x_p - z) + \frac{\rho}{2}(x_p - z)^2$$.

1. **Kiểm tra điều kiện cân bằng tại nghiệm đúng $$x_1 = x_2 = z^\star = 3.0$$:**
   - Tại nút 1: $$\nabla F_1(3) + u_1^\star = 0 \implies 3 + u_1^\star = 0 \implies u_1^\star = -3$$.
   - Tại nút 2: $$\nabla F_2(3) + u_2^\star = 0 \implies 3(3 - 4) + u_2^\star = 0 \implies u_2^\star = +3$$.
   - Kiểm tra điều kiện đối ngẫu toàn cục cho $$z$$: $$u_1^\star + u_2^\star = -3 + 3 = 0$$ (thỏa mãn tuyệt đối!).
2. **Thử cho mỗi nút giải CHÍNH XÁC bài toán cục bộ ADMM ($$E \to \infty$$) từ $$z = 3.0$$ với $$u_1^\star = -3, u_2^\star = +3$$ và $$\rho = 1$$:**
   - *Nút 1 cực tiểu hóa* $$\frac{1}{2}x_1^2 - 3(x_1 - 3) + \frac{1}{2}(x_1 - 3)^2$$:
     Đạo hàm bằng $$0 \implies x_1 - 3 + (x_1 - 3) = 0 \implies x_1 = 3.0$$!
   - *Nút 2 cực tiểu hóa* $$\frac{3}{2}(x_2 - 4)^2 + 3(x_2 - 3) + \frac{1}{2}(x_2 - 3)^2$$:
     Đạo hàm bằng $$0 \implies 3(x_2 - 4) + 3 + (x_2 - 3) = 4x_2 - 12 = 0 \implies x_2 = 3.0$$!
3. **Điểm vỡ òa:** Nhờ biến đối ngẫu $$u_1 = -3$$ kéo nút 1 sang phải và $$u_2 = +3$$ kéo nút 2 sang trái, cả hai nút **đứng im chính xác tại $$3.0$$ với 0% trôi cục bộ**! Đây chính là bản chất sâu sắc phân tách ADMM với FedAvg!

[Chương 21]({{ site.baseurl }}/contents/vi/chapter21/) đã trình bày **phương pháp hướng luân phiên của các nhân tử (ADMM)**. Dạng đồng thuận giải bài toán:

$$
\min_{x_1,\ldots,x_P,z} \sum_{p=1}^P f_p(x_p) \quad\text{subject to}\quad x_p=z,
$$

thông qua hàm Lagrangian tăng cường: cập nhật các biến gốc cục bộ $$x_p$$ (thường dưới dạng toán tử proximal), lấy trung bình cập nhật biến toàn cục $$z$$, và cập nhật biến đối ngẫu theo phần dư. Khi mỗi $$f_p$$ lồi và các bước con được giải đủ chính xác, ADMM có lý thuyết hội tụ hoàn chỉnh và là công cụ chuẩn mực cho các bài toán tách **lồi có cấu trúc** (Lasso phân tán, quy hoạch bậc hai đồng thuận, một số bài toán nới lỏng SDP).

Ngược lại, SGD song song dữ liệu và FedAvg được thiết kế cho bối cảnh khác hẳn:

| Tiêu chí | ADMM (Ch. 21) | SGD song song dữ liệu | FedAvg |
|----------|---------------|-----------------------|--------|
| Hàm mục tiêu $$f$$ điển hình | lồi, thường có cấu trúc hợp thành | ERM không lồi / mạng sâu | không lồi, ERM cục bộ *không đồng nhất* |
| Đại lượng lấy trung bình | biến gốc $$z$$ và biến đối ngẫu | **gradient** (hoặc trọng số đồng bộ) mỗi bước | **trọng số** sau $$E$$ bước cục bộ |
| Biến đối ngẫu | có, phần dư thúc đẩy đồng thuận | không | không |
| Tài nguyên khan hiếm | số vòng lặp của bài toán lồi cỡ vừa | băng thông kết nối liên nút mỗi bước | **số vòng truyền thông** (thiết bị gián đoạn, Wi-Fi) |
| Tiêu chí chứng nhận | khoảng cách đối ngẫu / phần dư | không (bài toán không lồi) | không |

Gọi FedAvg là “ADMM bỏ biến đối ngẫu” dễ làm mờ đi sự khác biệt bản chất: FedAvg *chủ động* cho phép các máy khách chạy nhiều bước cục bộ và chấp nhận độ trôi trước khi trung bình hóa tham số, trong khi ADMM *phạt trực tiếp* sự sai lệch giữa các nút qua biến đối ngẫu ở mọi vòng lặp. Nên dùng ADMM khi bài toán viết được dưới dạng đồng thuận lồi và cần theo dõi phần dư; dùng SGD song song dữ liệu khi huấn luyện mô hình lớn trên cụm máy chủ tập trung; và dùng FedAvg khi dữ liệu phải ở lại thiết bị đầu cuối còn chi phí truyền thông là nút thắt chính.

**Bài thực hành.** Với 3 máy khách chia nhau dữ liệu của một bài toán hồi quy logistic lồi, hãy giải cùng bài toán bằng (i) ADMM đồng thuận và (ii) FedAvg với $$E\in\{1,5\}$$, sau đó so sánh hàm mất mát huấn luyện theo *số vòng truyền thông* thay vì theo số lượt tính gradient cục bộ.

**Câu hỏi.** Trong những tình huống nào một phương pháp không cần phép chiếu hoặc phương pháp tách biến (như Frank–Wolfe hay ADMM) vẫn có thể vượt trội hơn SGD song song dữ liệu trên cùng một cụm tính toán?
