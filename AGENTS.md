# Agent notes — Optimization in Data Science (IUH)

## Canonical course

The **canonical course site is this GitHub repository**:

[https://github.com/nglelinh/optimization-for-data-science-iuh-2025](https://github.com/nglelinh/optimization-for-data-science-iuh-2025)

Published notes: [https://nglelinh.github.io/optimization-for-data-science-iuh-2025/](https://nglelinh.github.io/optimization-for-data-science-iuh-2025/)

Lessons live in `contents/en/chapterXX/` and `contents/vi/chapterXX/`. Do not treat an upstream COFA clone, a nested `convex-optimization-for-all.github.io/` tree, or a local Mac folder as the source of truth.

## Mac folders (easy to confuse)

| Folder (typical Mac path) | What it actually is | What to do |
|---------------------------|---------------------|------------|
| **`LinearAlgebra/`** | Misnamed partial Jekyll scaffold. Same `_config.yml` title / `baseurl` as this course, but mostly Chapter 00, often no `.git`, sometimes a linear-algebra lab PDF mixed in. | Do **not** publish from here. Do not rename this repo to match that folder. If you need Ch.00 work, copy into *this* repo. |
| **`Optimization/`** | Teaching **ops**: labs, books, midterm, final exam, `tests_thuchanh`, attendance. May nest an upstream COFA site. Not the deployed Jekyll curriculum. | Use for exams and lab packets. Do not merge it over `contents/`. |

## Content conventions

- Front matter: `layout`, `title`, `chapter`, `order`, `lang`, `categories`, `lesson_type` (required / optional).
- Display math uses Jekyll / MathJax `$$...$$` (and `$$` in the site’s existing lessons).
- New 2026 modules are Chapters **26–29**. Bibliography pages stay under `reference/` (sidebar chapter **99**), not 26.
- Interactive HTML demos: [INTERACTIVE_DEMOS.md](INTERACTIVE_DEMOS.md) and [nglelinh/interactive_math](https://github.com/nglelinh/interactive_math) (`optimization/*.html`). Remotion shorts use the filename pattern `optimization--*-vo.mp4`.
- Do not commit `_site/`, binaries, or a full rewrite of Chapters 00–25 unless asked.

## Build

```bash
bundle install
bundle exec jekyll build
# or: bundle exec jekyll serve
```
