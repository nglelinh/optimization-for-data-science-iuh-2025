---
layout: post
title: 19-01 Proximal Newton method
chapter: '19'
order: 2
owner: Hooncheol Shin
categories:
- chapter19
lang: en
---

In this section, we will review the **proximal gradient method** and examine how the **proximal newton method** emerged from it.

We will also examine the definition of the **proximal newton method** and the scaled proximal map that has good properties such as uniqueness and non-expansiveness compared to the general proximal map.

### Proximal Newton in 18 seconds

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/prox-newton_en.mp4"></video>
</div>

Proximal gradient uses a scalar step; proximal Newton minimises the quadratic model with the true Hessian plus $$\lambda\|x\|_1$$, so it needs far fewer iterations.

### Try it yourself: proximal gradient vs proximal Newton

<div class="opx-explainer" data-opx="pn" data-lang="en"></div>
