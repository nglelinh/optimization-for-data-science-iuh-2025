---
layout: post
title: 18-05 Lớp Broyden
chapter: '18'
order: 6
owner: Hooncheol Shin
categories:
- chapter18
lang: vi
---

Sau khi thấy SR1, DFP và BFGS lần lượt xuất hiện với những công thức trông vừa giống vừa khác nhau, một câu hỏi rất tự nhiên của người làm toán là: *chúng là ba thuật toán rời rạc, hay thực ra chỉ là ba điểm nằm trên cùng một đường thẳng?* Câu trả lời của Charles Broyden là một bức tranh thống nhất tuyệt đẹp: mọi tổ hợp affine $$(1 - \phi) B^+_{\text{BFGS}} + \phi B^+_{\text{DFP}}$$ đều tạo thành một họ duy nhất gọi là **lớp Broyden**, trong đó BFGS ($$\phi=0$$), DFP ($$\phi=1$$) và thậm chí cả SR1 đều chỉ là những điểm đặc biệt trên cùng một trục tham số $$\phi$$!

## Bản đồ kiến thức nền: Bức tranh thống nhất của lớp Broyden

Ba ý tưởng dưới đây giúp bạn nắm trọn ý nghĩa hình học và lý thuyết hội tụ của lớp Broyden:

- **Tổ hợp affine bảo toàn phương trình secant:** Vì cả $$B^+_{\text{BFGS}}$$ và $$B^+_{\text{DFP}}$$ đều đối xứng và thỏa mãn $$B^+ s = y$$, nên mọi tổ hợp $$(1-\phi) B^+_{\text{BFGS}} + \phi B^+_{\text{DFP}}$$ với $$\phi \in \mathbb{R}$$ tự động kế thừa tính đối xứng và phương trình secant.
- **Lớp Broyden hạn chế ($$\phi \in [0, 1]$$):** Khi $$\phi \in [0, 1]$$, ma trận $$B^+$$ là tổ hợp lồi của hai ma trận xác định dương nên **luôn bảo toàn tính xác định dương** dưới điều kiện $$y^T s > 0$$. Mọi phương pháp trong lớp hạn chế đều có tính bất biến đáng kinh ngạc: trên hàm bậc hai với tìm kiếm đường thẳng chính xác, chúng sinh ra **cùng một dãy điểm lặp** $$x_k$$ (định lý Dixon, 1972)!
- **SR1 nằm ngoài đoạn $$[0, 1]$$:** Tham số $$\phi_{\text{SR1}} = \frac{y^T s}{y^T s - s^T B s}$$ có thể nhỏ hơn $$0$$ hoặc lớn hơn $$1$$ (thậm chí tiến tới vô cùng khi $$y^T s = s^T B s$$). Đó chính là lý do sâu xa giải thích vì sao SR1 không đảm bảo giữ được tính xác định dương như lớp hạn chế.

### Khung giải thích (nên đọc chậm): Nội suy trực tiếp trên trục $$\phi$$ nối BFGS, DFP và SR1

Tiếp nối đúng hai ma trận ta vừa tính tay ở Bài 18-03 và 18-04 với $$B_0 = I, s = (1, 0)^T, y = (2, 1)^T$$ ($$s^T B_0 s = 1, y^T s = 2$$):

$$B_1^{\text{BFGS}} = \begin{bmatrix} 2 & 1 \\ 1 & 1.5 \end{bmatrix}, \qquad B_1^{\text{DFP}} = (H_1^{\text{DFP}})^{-1} = \frac{1}{0.4}\begin{bmatrix} 0.8 & 0.4 \\ 0.4 & 0.7 \end{bmatrix} = \begin{bmatrix} 2 & 1 \\ 1 & 1.75 \end{bmatrix}.$$

1. **Tính công thức tổng quát lớp Broyden theo $$\phi$$:**
   $$B_1(\phi) = (1 - \phi)\begin{bmatrix} 2 & 1 \\ 1 & 1.5 \end{bmatrix} + \phi\begin{bmatrix} 2 & 1 \\ 1 & 1.75 \end{bmatrix} = \begin{bmatrix} 2 & 1 \\ 1 & 1.5 + 0.25\phi \end{bmatrix}.$$
2. **Thử điểm giữa lớp hạn chế ($$\phi = 0.5$$):**
   $$B_1(0.5) = \begin{bmatrix} 2 & 1 \\ 1 & 1.625 \end{bmatrix}, \qquad \det = 3.25 - 1 = 2.25 > 0 \quad (\text{xác định dương}).$$
3. **Thử thay công thức tham số SR1:**
   $$\phi_{\text{SR1}} = \frac{y^T s}{y^T s - s^T B_0 s} = \frac{2}{2 - 1} = 2.$$
   Thay $$\phi = 2$$ vào $$B_1(\phi)$$ ta được:
   $$B_1(2) = \begin{bmatrix} 2 & 1 \\ 1 & 1.5 + 0.25(2) \end{bmatrix} = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}.$$
4. **Kiểm chứng độc lập bằng công thức SR1 gốc:** Với $$y - B_0 s = (1, 1)^T$$ và $$(y - B_0 s)^T s = 1$$, công thức SR1 cho $$B_1^{\text{SR1}} = I + \frac{1}{1}\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$$ — trùng khớp từng phần tử một! Và nhìn vào $$1.5 + 0.25\phi$$, bạn cũng thấy ngay nếu $$\phi \le -4$$ thì $$\det(B_1(\phi)) \le 0$$, ma trận sẽ mất tính xác định dương.

---

Lớp Broyden (Broyden class) là họ công thức tổng quát hóa cả BFGS, DFP và SR1 theo biểu thức tổ hợp tuyến tính sau:

* **Lưu ý:** $$B^+_{\text{BFGS}}$$ và $$B^+_{\text{DFP}}$$ lần lượt ký hiệu ma trận $$B^+$$ thu được từ công thức cập nhật BFGS và DFP.

>$$
>B^+ = (1 - \phi)B^+_{\text{BFGS}} + \phi B^+_{\text{DFP}}, \text{ với } \phi \in \mathbb{R}.
>$$

Đặt $$v = \frac{y}{y^Ts} - \frac{Bs}{s^TBs}$$, công thức trên có thể viết lại thành:

>$$
>B^+ = B - \frac{Bss^TB}{s^TBs} + \frac{yy^T}{y^Ts} + \phi(s^TBs)vv^T.
>$$

Nhận xét:
* Khi $$\phi = 0$$, công thức trùng với cập nhật BFGS.
* Khi $$\phi = 1$$, công thức trùng với cập nhật DFP.
* Khi $$\phi = \frac{y^Ts}{y^Ts - s^TBs}$$, công thức trùng với cập nhật SR1.

**Tham khảo:** Trường hợp giới hạn tham số $$\phi \in [0, 1]$$ được gọi là **lớp Broyden hạn chế (restricted Broyden class)** [14].