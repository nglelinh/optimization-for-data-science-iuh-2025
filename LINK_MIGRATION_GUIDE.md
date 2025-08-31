# Hướng dẫn xử lý Links trong hệ thống đa ngôn ngữ

## Tổng quan

Với việc chuyển đổi sang cấu trúc đa ngôn ngữ, các links cũ có dạng `contents/chapter06/21-03-20-06_03_02_convex_function_quadratic_upper_bound` đã được xử lý tự động và tương thích với hệ thống mới.

## Các loại links đã được xử lý

### 1. Internal Post Links (Đã tự động cập nhật)

**Trước:**
```liquid
{% post_url contents/chapter06/21-03-20-06_03_02_convex_function_quadratic_upper_bound %}
```

**Sau:**
```liquid
{% multilang_post_url contents/chapter06/21-03-20-06_03_02_convex_function_quadratic_upper_bound %}
```

### 2. Chapter Index Links (Đã tự động cập nhật)

**Trước:**
```liquid
{% link contents/chapter01/index.html %}
```

**Sau:**
```liquid
{% link contents/en/chapter01/index.html %}  <!-- cho tiếng Anh -->
{% link contents/vi/chapter01/index.html %}  <!-- cho tiếng Việt -->
```

### 3. Direct URL Links (Đã tự động cập nhật)

**Trước:**
```markdown
[Link text](/contents/chapter06/)
```

**Sau:**
```markdown
[Link text](/contents/en/chapter06/)  <!-- cho tiếng Anh -->
[Link text](/contents/vi/chapter06/)  <!-- cho tiếng Việt -->
```

## Plugin `multilang_post_url` 

Plugin này tự động xử lý các links cũ và tìm bài viết tương ứng theo ngôn ngữ hiện tại:

### Cách hoạt động:
1. **Ưu tiên ngôn ngữ hiện tại**: Tìm bài viết trong cùng ngôn ngữ với trang hiện tại
2. **Fallback sang ngôn ngữ mặc định**: Nếu không tìm thấy, fallback sang tiếng Anh
3. **Fallback cuối cùng**: Tìm bất kỳ bài viết nào có tên tương tự

### Ví dụ sử dụng:
```liquid
<!-- Cách mới (khuyến nghị) -->
{% multilang_post_url contents/chapter06/21-03-20-06_03_02_convex_function_quadratic_upper_bound %}

<!-- Cách cũ (vẫn hoạt động nhưng không khuyến nghị) -->
{% post_url contents/chapter06/21-03-20-06_03_02_convex_function_quadratic_upper_bound %}
```

## Hệ thống Redirect tự động

Các URL cũ sẽ tự động redirect đến URL mới:

- `/contents/chapter06/` → `/contents/en/chapter06/`
- `/contents/chapter06/21-03-20-06_03_02_convex_function_quadratic_upper_bound/` → `/contents/en/chapter06/21-03-20-06_03_02_convex_function_quadratic_upper_bound/`

## Cách viết links mới

### 1. Links đến bài viết khác

**Khuyến nghị:**
```liquid
{% multilang_post_url contents/chapter06/21-03-20-06_03_02_convex_function_quadratic_upper_bound %}
```

**Hoặc sử dụng tên file đầy đủ:**
```liquid
{% post_url 21-03-20-06_03_02_convex_function_quadratic_upper_bound %}
```

### 2. Links đến chapter index

**Tiếng Anh:**
```liquid
{% link contents/en/chapter06/index.html %}
```

**Tiếng Việt:**
```liquid
{% link contents/vi/chapter06/index.html %}
```

**Tự động theo ngôn ngữ hiện tại:**
```liquid
{% assign current_lang = page.lang | default: site.default_lang %}
{% link contents/{{ current_lang }}/chapter06/index.html %}
```

### 3. Links trong markdown

**Absolute links:**
```markdown
[Gradient Descent](/contents/en/chapter06/)
[Gradient Descent (VI)](/contents/vi/chapter06/)
```

**Relative links (trong cùng chapter):**
```markdown
[Related Post](21-03-20-06_03_02_convex_function_quadratic_upper_bound.md)
```

## Troubleshooting

### 1. Link không hoạt động

**Kiểm tra:**
- File đích có tồn tại không?
- Front matter có đúng `lang` và `chapter` không?
- Tên file có chính xác không?

**Debug:**
```liquid
<!-- Thêm vào template để debug -->
Current language: {{ page.lang | default: site.default_lang }}
Available posts: 
{% for post in site.posts %}
  - {{ post.path }} (lang: {{ post.lang }}, chapter: {{ post.chapter }})
{% endfor %}
```

### 2. Redirect không hoạt động

**Kiểm tra:**
- Plugin `redirect_generator.rb` có được load không?
- Jekyll có rebuild không?
- Browser cache có clear không?

### 3. Plugin multilang_post_url không hoạt động

**Kiểm tra:**
- File `_plugins/multilang_post_url.rb` có tồn tại không?
- Jekyll có restart không?
- Syntax có đúng không?

## Best Practices

### 1. Consistency (Tính nhất quán)
- Luôn sử dụng `multilang_post_url` cho internal links
- Đặt tên file nhất quán giữa các ngôn ngữ
- Sử dụng cùng `chapter` và `order` cho cùng nội dung

### 2. SEO-friendly
- Sử dụng absolute URLs cho external sharing
- Đảm bảo canonical URLs đúng
- Sử dụng hreflang cho multilingual SEO

### 3. User Experience
- Cung cấp fallback cho missing translations
- Hiển thị language indicator rõ ràng
- Smooth navigation giữa các ngôn ngữ

## Scripts hỗ trợ

### 1. Migration script
```bash
ruby migrate_content.rb
```

### 2. Link update script
```bash
ruby update_links.rb
```

### 3. Kiểm tra broken links
```bash
# Tạo script check_links.rb để kiểm tra
ruby check_links.rb
```

## Ví dụ thực tế

### File: `contents/en/chapter06/_posts/21-03-20-06_03_01_convergence_analysis_and_proof.md`

```markdown
---
layout: post
title: 06-03-01 Convergence analysis & Proof
chapter: "06"
order: 8
owner: "Kyeongmin Woo"
lang: en
---

## Proof
If ∇f is Lipschitz continuous and f is convex, then f has a quadratic upper bound 
(see [06-03-02]({% multilang_post_url contents/chapter06/21-03-20-06_03_02_convex_function_quadratic_upper_bound %})).

For more details, check the [chapter overview]({% link contents/en/chapter06/index.html %}).
```

### File: `contents/vi/chapter06/_posts/21-03-20-06_03_01_convergence_analysis_and_proof.md`

```markdown
---
layout: post
title: 06-03-01 Phân tích hội tụ & Chứng minh
chapter: "06"
order: 8
owner: "Kyeongmin Woo"
lang: vi
---

## Chứng minh
Nếu ∇f liên tục Lipschitz và f lồi, thì f có cận trên bậc hai 
(xem [06-03-02]({% multilang_post_url contents/chapter06/21-03-20-06_03_02_convex_function_quadratic_upper_bound %})).

Để biết thêm chi tiết, xem [tổng quan chương]({% link contents/vi/chapter06/index.html %}).
```

## Kết luận

Hệ thống đã tự động xử lý hầu hết các links cũ. Đối với nội dung mới, hãy sử dụng các pattern được khuyến nghị ở trên để đảm bảo tính nhất quán và hoạt động tốt với hệ thống đa ngôn ngữ.
