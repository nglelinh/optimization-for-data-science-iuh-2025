---
layout: post
title: 02-02 Một số ví dụ quan trọng
chapter: '02'
order: 8
owner: Wontak Ryu
categories:
- chapter02
lang: vi
lesson_type: required
---

Trong thực hành tối ưu hóa, bạn hiếm khi phải ngồi chứng minh một tập hợp phức tạp là lồi từ con số 0. Thay vào đó, các chuyên gia luôn giữ trong đầu một "bộ sưu tập mẫu chuẩn" gồm các khối gạch lồi cơ bản — nửa không gian, đa diện, hình cầu, ellipsoid, đơn hình xác suất và hình nón ma trận — rồi lắp ghép chúng lại để nhận diện bài toán chỉ trong vài giây.

Phần 02-02 giới thiệu danh mục các tập lồi và hình nón lồi quan trọng nhất xuất hiện dày đặc trong lý thuyết cũng như phần mềm tối ưu hóa.

## Kiến thức cần nhớ: Bốn họ "gạch xây" của miền khả thi lồi

- **Nhóm tuyến tính (Siêu phẳng, Nửa không gian, Đa diện, Đơn hình):** Được định nghĩa bởi các bất đẳng thức và đẳng thức tuyến tính $$Ax \le b,\ Cx = d$$ — lãnh địa của Quy hoạch tuyến tính (LP).
- **Nhóm bậc hai & chuẩn (Hình cầu Euclid, Ellipsoid, Hình cầu $$\ell_1/\ell_\infty$$):** Định nghĩa qua chuẩn hoặc ma trận xác định dương — lãnh địa của tối ưu hóa có điều chuẩn (Ridge/Lasso) và Quy hoạch nón bậc hai (SOCP).
- **Nhóm hình nón (Nón chuẩn, Nón không âm $$\mathbb{R}_+^n$$, Nón PSD $$\mathbb{S}_+^n$$):** Là nền tảng cho tối ưu hóa nón hiện đại (LP $$\subset$$ SOCP $$\subset$$ SDP).

### Giải thích: Đặt cùng một điểm $$x = (0.5, 0.5)^T$$ vào 4 tập lồi kinh điển

Hãy kiểm tra xem điểm $$x = (0.5, 0.5)^T \in \mathbb{R}^2$$ nằm trong, trên biên, hay ngoài 4 tập lồi mẫu sau:

1. **Hình cầu đơn vị Euclid $$B_2 = \{x : \|x\|_2 \le 1\}$$:**
   $$\|x\|_2 = \sqrt{0.5^2 + 0.5^2} = \sqrt{0.5} \approx 0.707 < 1 \implies$$ nằm **chặt bên trong** $$B_2$$.
2. **Hình cầu đơn vị chuẩn $$\ell_1$$ $$B_1 = \{x : \|x\|_1 \le 1\}$$:**
   $$\|x\|_1 = |0.5| + |0.5| = 1 \implies$$ nằm **ngay trên biên** của hình thoi $$B_1$$.
3. **Đơn hình xác suất $$\Delta_2 = \{x \ge 0 : x_1 + x_2 = 1\}$$:**
   $$x_1, x_2 \ge 0$$ và $$0.5 + 0.5 = 1 \implies$$ thuộc $$\Delta_2$$ (biểu diễn phân phối đều 50%–50%).
4. **Nửa không gian $$H^- = \{x : 2x_1 + x_2 \le 1\}$$:**
   $$2(0.5) + 0.5 = 1.5 > 1 \implies$$ nằm **ngoài** $$H^-$$!
   Cùng một tọa độ, nhưng đổi hình dạng ràng buộc là thay đổi hoàn toàn trạng thái khả thi và trạng thái ràng buộc chặt.

---

Phần này liệt kê các ví dụ quan trọng thường gặp về tập lồi:

* Các tập hợp tầm thường: tập rỗng, một điểm, đường thẳng, đoạn thẳng, tia.
* Siêu phẳng: $$\{x : a^T x = b\}$$, với $$a, b$$ cho trước và $$a \ne 0$$.
* Nửa không gian: $$\{x : a^T x \le b \}$$ với $$a \ne 0$$.
* Tập affine: $$\{x : Ax = b\}$$, với $$A, b$$ cho trước.
* Hình cầu Euclidean và ellipsoid.
* Hình cầu chuẩn: $$\{x : \| x \| \le r\}$$, với chuẩn $$\|·\|$$ và bán kính $$r$$ cho trước.
* Hình nón lồi: hình nón chuẩn, hình nón pháp tuyến và hình nón nửa xác định dương.
