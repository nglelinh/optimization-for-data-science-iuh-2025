---
layout: post
title: 27-01 Đồ thị tính toán
chapter: '27'
order: 2
owner: Nguyen Le Linh
categories:
- chapter27
lang: vi
lesson_type: required
---

Khi bạn viết một dòng code ngắn ngủi như `loss = (w1 * x1 + w2 * x2 - y) ** 2`, bộ vi xử lý không nhìn thấy nó như một công thức toán học trừu tượng — nó thực thi tuần tự từng phép nhân, phép cộng, phép trừ và phép bình phương, lưu từng kết quả tạm vào thanh ghi. Nếu vẽ mỗi kết quả tạm đó thành một nút tròn và nối các mũi tên thể hiện sự phụ thuộc dữ liệu, bạn sẽ thu được một **đồ thị tính toán (computational graph)**.

Nhìn chương trình như một đồ thị có hướng không chu trình (DAG) là bước chuyển hóa tư duy then chốt của Chương 27: nhờ biểu diễn này, việc tính đạo hàm phức tạp cỡ nào cũng rút gọn thành việc **duyệt đồ thị theo thứ tự topo** (từ đầu vào đến đầu ra hoặc ngược lại) và nhân dồn các đạo hàm cục bộ siêu đơn giản trên từng cạnh.

## Kiến thức cần nhớ: Ba trụ cột của Đồ thị tính toán

Để nắm vững cấu trúc dữ liệu đứng sau `torch.autograd` và `jax.make_jaxpr`, hãy hiểu rõ ba trụ cột sau:

- **Phân rã thành Băng Wengert (Wengert Tape / Trace):** Mọi hàm số phức tạp đều phân rã thành một chuỗi tuyến tính các biến trung gian $$v_1, v_2, \dots, v_K$$, trong đó mỗi $$v_k$$ chỉ là kết quả của *một* phép toán nguyên thủy áp lên các nút đi trước. Nhờ đó, thư viện AD chỉ cần biết đạo hàm của khoảng vài chục phép toán cơ bản!
- **Tính phân nhánh (Fan-out) và Quy tắc Cộng dồn (Multivariable Chain Rule):** Khi một biến $$u$$ được dùng làm đầu vào cho *nhiều* nút phía sau (ví dụ vừa vào phép nhân vừa vào hàm $$\cos$$), ảnh hưởng tổng của $$u$$ lên đầu ra bằng **tổng** đóng góp qua tất cả các đường đi xuất phát từ $$u$$ — nguồn gốc của phép cộng dồn `+=` trong lan truyền ngược.
- **Đồ thị động (Define-by-Run) vs. Đồ thị tĩnh (Define-then-Run):** PyTorch dựng băng Wengert ngay khi chạy Python (linh hoạt với `if`/`for` phụ thuộc dữ liệu, cực dễ gỡ lỗi), trong khi JAX (`jit`) và `torch.compile` truy vết thành đồ thị tĩnh để tối ưu hóa cấp trình biên dịch (gộp nhân tử, loại bỏ bộ nhớ thừa).

### Giải thích: Tự tay lập Băng Wengert cho một hàm 2 biến

Hãy phân rã hàm số $$f(x, y) = (x \cdot y + \cos x)^2$$ thành một đồ thị tính toán (băng Wengert) hoàn chỉnh và tính giá trị tại điểm $$(x, y) = (0,\; 2)$$:

| Nút | Phép toán nguyên thủy | Giá trị tại $$(0, 2)$$ | Đạo hàm cục bộ theo các nút cha |
| :--- | :--- | :---: | :--- |
| $$v_1$$ | Đầu vào $$x$$ | $$0$$ | — |
| $$v_2$$ | Đầu vào $$y$$ | $$2$$ | — |
| $$v_3$$ | $$v_1 \cdot v_2$$ | $$0 \cdot 2 = 0$$ | $$\frac{\partial v_3}{\partial v_1} = v_2 = 2,\quad \frac{\partial v_3}{\partial v_2} = v_1 = 0$$ |
| $$v_4$$ | $$\cos(v_1)$$ | $$\cos(0) = 1$$ | $$\frac{\partial v_4}{\partial v_1} = -\sin(v_1) = 0$$ |
| $$v_5$$ | $$v_3 + v_4$$ | $$0 + 1 = 1$$ | $$\frac{\partial v_5}{\partial v_3} = 1,\quad \frac{\partial v_5}{\partial v_4} = 1$$ |
| $$v_6$$ | $$v_5^2$$ | $$1^2 = 1$$ | $$\frac{\partial v_6}{\partial v_5} = 2v_5 = 2$$ |

**Quan sát then chốt:** Nút đầu vào $$v_1 = x$$ có hai mũi tên đi ra (tới $$v_3$$ và tới $$v_4$$). Nhờ lưu sẵn cột "Giá trị" và cột "Đạo hàm cục bộ" trên băng Wengert này, ta đã có đủ mọi mảnh ghép để chạy AD chiều thuận (Bài 27-02) hoặc AD chiều nghịch (Bài 27-03) mà không cần động tới biểu thức gốc nữa!

Một **đồ thị tính toán (computational graph)** là một đồ thị có hướng không chu trình (DAG), trong đó mỗi nút biểu diễn một giá trị trung gian và các cạnh biểu diễn các phép toán sơ cấp ($$+$$, $$\times$$, $$\exp$$, `matmul`, …). Các tham số, dữ liệu đầu vào và hàm mất mát vô hướng đều là các nút được đánh dấu trên đồ thị này.

**Ví dụ.** Xét hàm mất mát logistic trên một mẫu dữ liệu với vector trọng số $$w\in\mathbb{R}^2$$:

$$
z = w_1 x_1 + w_2 x_2, \quad p=\sigma(z), \quad \ell = -y\log p -(1-y)\log(1-p).
$$

Các nút của đồ thị gồm $$x$$, $$w$$, $$z$$, $$p$$ và $$\ell$$. Đồ thị tính toán *chính là* biểu diễn cấu trúc của chương trình. Khi một trọng số thay đổi, mọi nút phía sau đều chịu ảnh hưởng; nhiệm vụ của vi phân tự động là lan truyền độ nhạy từ đầu vào tới $$\ell$$ (chiều thuận) hoặc kéo ngược độ nhạy từ $$\ell$$ về các tham số (chiều nghịch).

Có hai cách triển khai phổ biến trong các thư viện:

* **Ghi băng động / define-by-run** (PyTorch): đồ thị (còn gọi là băng Wengert) được dựng trực tiếp trong lúc hàm `forward` chạy; các cấu trúc rẽ nhánh và vòng lặp dùng thẳng cú pháp Python.
* **Định nghĩa trước khi chạy / define-then-run** (Theano trước đây, hoặc cơ chế truy vết `jit` của JAX): chương trình được biên dịch hoặc truy vết thành một đồ thị tĩnh rồi thực thi lặp lại nhiều lần.

Hiểu cách quản lý đồ thị giải thích trực tiếp vì sao lệnh `y.backward()` trong PyTorch yêu cầu đồ thị còn tồn tại trong bộ nhớ: mặc định sau một lần gọi `backward()`, băng tính toán sẽ được giải phóng trừ khi truyền tham số `retain_graph=True`.

**Bài tập.** Vẽ đồ thị tính toán cho hàm mất mát $$\ell=\|W_2\,\phi(W_1 x)-y\|_2^2$$ của một mạng một lớp ẩn và đếm số phép nhân ma trận ở lượt thuận. Chi phí này sẽ xuất hiện tương ứng ở lượt chiều nghịch.
