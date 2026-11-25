---
layout: post
title: '20-04-02 Đảm bảo hội tụ'
chapter: '20'
order: 10
owner: Hooncheol Shin
categories:
- chapter20
lang: vi
---

Vì ADMM không giải đồng thời hàm Lagrange tăng cường mà tách ra cập nhật luân phiên $$x$$ rồi $$z$$, câu hỏi sống còn mà mọi nhà toán học đều đặt ra là: *liệu sự "đi tắt" luân phiên đó có làm hỏng tính hội tụ hay đòi hỏi tham số phạt $$\rho$$ phải chọn thật khéo không?* Câu trả lời là một trong những tin vui lớn nhất của tối ưu hóa lồi: dưới những điều kiện cực kỳ nhẹ ($$f, g$$ lồi đóng chính quy và hàm Lagrange có điểm yên ngựa — **không cần $$f, g$$ khả vi, không cần lồi mạnh, thậm chí không cần $$A, B$$ có hạng đầy đủ**), ADMM đảm bảo hội tụ với **mọi $$\rho > 0$$**!

## Bản đồ kiến thức nền: Ba tiêu chuẩn hội tụ và hai phần dư KKT của ADMM

Để theo dõi và chẩn đoán hội tụ của ADMM khi lập trình thực tế, cần nắm vững ba khái niệm sau:

- **Ba khẳng định hội tụ cơ bản:** Với mọi $$\rho > 0$$, khi $$k \to \infty$$ ta luôn có: (1) phần dư gốc $$r^{(k)} = Ax^{(k)} + Bz^{(k)} - c \to 0$$; (2) giá trị hàm mục tiêu $$f(x^{(k)}) + g(z^{(k)}) \to p^\star$$; và (3) biến đối ngẫu $$u^{(k)} \to u^\star$$. (Lưu ý: bản thân $$x^{(k)}, z^{(k)}$$ chỉ chắc chắn hội tụ về nghiệm duy nhất nếu có thêm điều kiện như lồi chặt hoặc hạng cột đầy đủ.)
- **Phần dư gốc và phần dư đối ngẫu làm tiêu chuẩn dừng:** Điều kiện KKT cho bài toán ADMM tách làm hai độ lệch đo được ngay ở mỗi vòng lặp: phần dư gốc $$r^{(k)} = Ax^{(k)} + Bz^{(k)} - c$$ và phần dư đối ngẫu $$s^{(k)} = \rho A^T B(z^{(k)} - z^{(k-1)})$$. Khi cả $$\|r^{(k)}\|_2$$ và $$\|s^{(k)}\|_2$$ đủ nhỏ, ta có chứng chỉ chặt cho độ gần nghiệm tối ưu!
- **Nghịch lý tốc độ của ADMM và vai trò của $$\rho$$:** Dù hội tụ với mọi $$\rho > 0$$, tốc độ thực tế lại rất nhạy với $$\rho$$: $$\rho$$ quá lớn ép $$r^{(k)}$$ về $$0$$ nhanh nhưng làm $$s^{(k)}$$ chậm; $$\rho$$ quá nhỏ thì ngược lại. ADMM thường đạt độ chính xác trung bình ($$10^{-3}\text{–}10^{-4}$$) rất nhanh trong vài chục bước, nhưng để đạt $$10^{-10}$$ có thể chậm nếu không điều chỉnh $$\rho$$ thích nghi.

### Khung giải thích (nên đọc chậm): Tính trực tiếp phần dư gốc $$r^{(k)}$$ và phần dư đối ngẫu $$s^{(k)}$$

Quay lại bài toán $$x - z = 0$$ ($$A = 1, B = -1, c = 0, \rho = 1$$) ở bài 20-04-01. Giả sử qua ba vòng lặp liên tiếp ta thu được:

- Vòng $$0$$: $$z^{(0)} = 2.0$$
- Vòng $$1$$: $$x^{(1)} = 1.0, \; z^{(1)} = 0.0$$
- Vòng $$2$$: $$x^{(2)} = -0.5, \; z^{(2)} = 0.0$$

Hãy tính hai chỉ số dừng chuẩn (theo Boyd et al., 2011) tại vòng 1 và vòng 2:

1. **Tại vòng $$k = 1$$:**
   - Phần dư gốc: $$r^{(1)} = A x^{(1)} + B z^{(1)} - c = 1.0 - 0.0 = +1.0$$ (chưa khớp ràng buộc $$x = z$$).
   - Phần dư đối ngẫu: $$s^{(1)} = \rho A^T B (z^{(1)} - z^{(0)}) = (1)(1)(-1)(0.0 - 2.0) = +2.0$$ (khối $$z$$ vừa thay đổi rất mạnh!).
2. **Tại vòng $$k = 2$$:**
   - Phần dư gốc: $$r^{(2)} = -0.5 - 0.0 = -0.5$$ (độ lớn giảm một nửa từ $$1.0$$ xuống $$0.5$$).
   - Phần dư đối ngẫu: $$s^{(2)} = (1)(1)(-1)(0.0 - 0.0) = 0.0$$!
3. **Diễn giải:** Tại vòng 2, dù phần dư đối ngẫu đã bằng $$0$$ (chứng tỏ $$z$$ đã ổn định đúng vị trí $$0$$), phần dư gốc $$|r^{(2)}| = 0.5$$ vẫn còn lớn nên thuật toán chưa được dừng; chỉ khi cả $$|r^{(k)}| \le \epsilon_{\text{pri}}$$ và $$|s^{(k)}| \le \epsilon_{\text{dual}}$$ thì mới dừng an toàn!

---

# Đảm bảo hội tụ của ADMM

Dưới các điều kiện chuẩn rất nhẹ trên $$f$$ và $$g$$ (đáng chú ý là $$A$$ và $$B$$ không cần có hạng đầy đủ), ADMM đảm bảo các tính chất hội tụ sau với mọi $$\rho > 0$$:

* **Hội tụ phần dư:** Khi $$k \to \infty$$, $$r^{(k)} = Ax^{(k)} + Bz^{(k)} - c \to 0$$, tức là các điểm lặp tiến dần về tập khả thi gốc.

* **Hội tụ giá trị hàm mục tiêu:** $$f(x^{(k)}) + g(z^{(k)}) \to f^{\ast} + g^{\ast}$$, trong đó $$f^{\ast} + g^{\ast}$$ là giá trị tối ưu của bài toán gốc.

* **Hội tụ biến đối ngẫu:** $$u^{(k)} \to u^{\ast}$$, trong đó $$u^{\ast}$$ là nghiệm tối ưu đối ngẫu.

Tốc độ hội tụ tổng quát của ADMM phụ thuộc vào tính chất cụ thể của bài toán (như tính lồi mạnh hay độ trơn) và là chủ đề có nhiều kết quả nghiên cứu chuyên sâu. Về mặt thực hành, tốc độ hội tụ của ADMM thường tương đương hoặc nhỉnh hơn một chút so với các phương pháp bậc nhất.
