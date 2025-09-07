# Convex Optimization for All
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-12-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

- [Book](<https://convex-optimization-for-all.github.io/>)
- If you want to contribute to OpenSource
  - [Initial Settings](<https://convex-optimization-for-all.github.io/contribution/2021/01/27/initial_settings/>)
  - [Conventions](<https://convex-optimization-for-all.github.io/contribution/2021/02/03/conventions/>)
  - [How to Contribute](<https://convex-optimization-for-all.github.io/contribution/2021/01/27/how_to_contribute/>)

## Author's Preface

As machine learning attracts public attention, interest in optimization is also rising day by day. However, we felt regret that many people struggle with the entry barrier due to the lack of abundant Korean materials for beginners. Therefore, we established a Convex Optimization course at ModuLabs' Full-Leaf School, and started this project with the goodwill of participants who wanted to practice knowledge sharing. Through this activity, we hope to contribute to the intellectual growth of all citizens and the popularization of convex optimization in Korea.

The overall content of this document references [Carnegie Mellon University lecture materials](http://www.stat.cmu.edu/~ryantibs/convexopt-F16/), and uses [Stanford University lecture materials](https://web.stanford.edu/~boyd/cvxbook/) as supplementary materials. It would be good to study using these two lecture materials as references centered around this ebook.

www.jwpark.co.kr@gmail.com / Jinwoo Park (Convex Optimization Full-Leaf School, ModuLabs)

## Translator's Preface

With the continuous development of machine learning recently, various research is being conducted, and movements to apply this to real-world problems are also growing. However, without a deep understanding of the mathematics that forms the foundation of machine learning, understanding and application can only be superficial.

Convex Optimization is an attractive field for those studying machine learning because it is not only directly related to machine learning but also includes various sub-fields of mathematics such as linear algebra, calculus, and numerical analysis. However, since the content is substantial to handle alone and the field itself has a high level of difficulty, we gathered people to study together and started the 2021 Convex Optimization Study. This blog is a trace of the study we conducted together and was created to help those who want to study alone later.

The main content of this blog consists of materials migrated with the consent of the authors of [Convex Optimization for All](<https://wikidocs.net/book/1896>). The original content is the most well-known Korean content about Convex Optimization and is also sufficient in terms of content. In this blog, we aim to make it open source by inheriting the existing WikiDocs content. Therefore, anyone can raise issues about the content and contribute by creating pull requests directly. Through this, we hope to make a small contribution to the 'intellectual growth of all citizens and popularization of convex optimization in Korea,' which is also the intention of the authors of [Convex Optimization for All](<https://wikidocs.net/book/1896>).

wgm0601@gmail.com / Kyeongmin Woo (MakinaRocks)


## Contents Covered

| idx | Title | Book | Lecture | Slide |
|:---:|:---:|:---:|:---:|:---:|
| 1 | Introduction | [Page](<https://convex-optimization-for-all.github.io/contents/chapter01/>)  | [CMU Lecture](<https://www.youtube.com/watch?v=XFKBNJ14UmY&ab_channel=RyanT>)  | [CMU Note](<http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/intro.pdf>)  |
| 2 | Convex Sets | [Page](<https://convex-optimization-for-all.github.io/contents/chapter02/>)  | [Stanford Lecture](<https://www.youtube.com/watch?v=P3W_wFZ2kUo&list=PL3940DD956CDF0622&index=3&ab_channel=Stanford>)  | [Stanford Note](<https://web.stanford.edu/class/ee364a/lectures/sets.pdf>)  |
| 3 | Convex Functions | [Page](<https://convex-optimization-for-all.github.io/contents/chapter03/>)  | [Stanford Lecture](<https://www.youtube.com/watch?v=kcOodzDGV4c&list=PL3940DD956CDF0622&index=4&ab_channel=Stanford>)  | [Stanford Note](<https://see.stanford.edu/materials/lsocoee364a/03ConvexFunctions.pdf>)  |
| 4 | Convex Optimization Basis | [Page](<https://convex-optimization-for-all.github.io/contents/chapter04/>)  | [CMU Lecture](<https://www.youtube.com/watch?v=Gij3dlqLUN8&list=PLjbUi5mgii6AVdvImLB9-Hako68p9MpIC&index=5&ab_channel=RyanT>)  | [CMU Note](<http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/convex-opt.pdf>)  |
| 5 | Canonical Problems | [Page](<https://convex-optimization-for-all.github.io/contents/chapter05/>)  | [CMU Lecture](<https://www.youtube.com/watch?v=pfxVy4EUqzE&ab_channel=RyanT>)  | [CMU Note](<http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/canonical-probs.pdf>)  | 
| 6 | Gradient Descent | [Page](<https://convex-optimization-for-all.github.io/contents/chapter06/>)  | [CMU Lecture](<https://www.youtube.com/watch?v=sLMJal3KwPs&ab_channel=RyanT>)  | [CMU Note](<http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/grad-descent.pdf>)  |
| 7 | Subgradient | [Page](<https://convex-optimization-for-all.github.io/contents/chapter07/>)  | [CMU Lecture](<https://www.youtube.com/watch?v=58pUZYUvpdQ&ab_channel=RyanT>)  | [CMU Note](<http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/subgrad.pdf>)  |
| 8 | Subgradient Method | [Page](<https://convex-optimization-for-all.github.io/contents/chapter08/>)  | [CMU Lecture](<https://www.youtube.com/watch?v=n_6MxWriulk&ab_channel=RyanT>)  | [CMU Note](<http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/sg-method.pdf>)  |
| 9 | Proximal Gradient Descent and Acceleration | [Page](<https://convex-optimization-for-all.github.io/contents/chapter09/>)  | [CMU Lecture](<https://www.youtube.com/watch?v=h7dniG0c2ng&ab_channel=RyanT>)  | [CMU Note](<http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/prox-grad.pdf>)  |
| 10 | Duality in Linear Programs | [Page](<https://convex-optimization-for-all.github.io/contents/chapter10/>)  | [CMU Lecture](<https://www.youtube.com/watch?v=OQncSb3PIWA&ab_channel=RyanT>)  | [CMU Note](<http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/dual-lps.pdf>)  | 
| 11 | Duality in General Programs | [Page](<https://convex-optimization-for-all.github.io/contents/chapter11/>)  | [CMU Lecture](<https://www.youtube.com/watch?v=LBHKx8PmcnQ&ab_channel=RyanT>)  | [CMU Note](<http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/dual-gen.pdf>)  | 
| 12 | KKT Conditions | [Page](<https://convex-optimization-for-all.github.io/contents/chapter12/>)  | [CMU Lecture](<https://www.youtube.com/watch?v=V6sL3uXNZ3g&ab_channel=RyanT>)  | [CMU Note](<http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/kkt.pdf>)  | 
| 13 | Duality uses and correspondences | [Page](<https://convex-optimization-for-all.github.io/contents/chapter13/>)  | [CMU Lecture](<https://www.youtube.com/watch?v=AST64aGULkk&ab_channel=RyanT>)  | [CMU Note](<http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/dual-corres.pdf>)  |
| 14 | Newton's Method | [Page](<https://convex-optimization-for-all.github.io/contents/chapter14/>)  | [CMU Lecture](<https://www.youtube.com/watch?v=1B918uZBOss&ab_channel=RyanT>)  | [CMU Note](<http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/newton.pdf>)  |
| 15 | Barrier Method | [Page](<https://convex-optimization-for-all.github.io/contents/chapter15/>)  | [CMU Lecture](<https://www.youtube.com/watch?v=_DD17Mj5Y6Y&ab_channel=RyanT>)  | [CMU Note](<http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/barr-method.pdf>)  |
| 16 | Duality Revisited | [Page](<https://convex-optimization-for-all.github.io/contents/chapter16/>)  | [CMU Lecture](<https://www.youtube.com/watch?v=MwOjRfU2aU8&ab_channel=RyanT>)  | [CMU Note](<http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/dual-revisited.pdf>)  |
| 17 | Primal-Dual Interior-Point Methods | [Page](<https://convex-optimization-for-all.github.io/contents/chapter17/>)  | [CMU Lecture](<https://www.youtube.com/watch?v=haktqAajo70&ab_channel=RyanT>)  | [CMU Note](<http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/primal-dual.pdf>)  |
| 18 | Quasi-Newton Methods | [Page](<https://convex-optimization-for-all.github.io/contents/chapter18/>)  | [CMU Lecture](<https://www.youtube.com/watch?v=2eSrCuyPscg&ab_channel=RyanT>)  | [CMU Note](<http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/quasi-newton.pdf>)  |
| 19 | Proximal Netwon Method | [Page](<https://convex-optimization-for-all.github.io/contents/chapter19/>)  | [CMU Lecture](<https://www.youtube.com/watch?v=dFqMgOO6DT0&ab_channel=RyanT>)  | [CMU Note](<http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/prox-newton.pdf>)  | 
| 20 | Dual Methods | [Page](<https://convex-optimization-for-all.github.io/contents/chapter20/>)  | [CMU Lecture](<https://www.youtube.com/watch?v=OsnQ_QC4Fjc&ab_channel=RyanT>)  | [CMU Note](<http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/dual-meth.pdf>)  |
| 21 | Alternating Direction Method of Mulipliers | [Page](<https://convex-optimization-for-all.github.io/contents/chapter21/>)  | [CMU Lecture](<https://www.youtube.com/watch?v=1tyl_F8j3wA&ab_channel=RyanT>)  | [CMU Note](<http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/admm.pdf>)  |
| 22 | Conditional Gradient Method | [Page](<https://convex-optimization-for-all.github.io/contents/chapter22/>)  | [CMU Lecture](<https://www.youtube.com/watch?v=6u0XyY3aeBo&ab_channel=RyanT>)  | [CMU Note](<http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/cond-grad.pdf>)  |
| 23 | Coordinate Descent | [Page](<https://convex-optimization-for-all.github.io/contents/chapter23/>)  | [CMU Lecture](<https://www.youtube.com/watch?v=6u0XyY3aeBo&ab_channel=RyanT>)  | [CMU Note](<http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/coord-desc.pdf>)  |
| 24 | Mixed Integer Programming 1 | [Page](<https://convex-optimization-for-all.github.io/contents/chapter24/>)  | [CMU Lecture](<https://www.youtube.com/watch?v=RQmFpY9W40c&ab_channel=RyanT>)  | [CMU Note](<http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/integer1.pdf>)  |
| 25 | Mixed Integer Programming 2 | [Page](<https://convex-optimization-for-all.github.io/contents/chapter25/>)  | [CMU Lecture](<https://www.youtube.com/watch?v=E9VP8sfGiIc&ab_channel=RyanT>)  | [CMU Note](<http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/integer2.pdf>)  |

## Referenced Materials

- [Convex Optimization - Boyd and Vandenberghe](<https://web.stanford.edu/~boyd/cvxbook/>)
- [Stanford Convex Optimization Lecture 2014](<https://www.youtube.com/playlist?list=PL3940DD956CDF0622>)
- [CMU Convex Optimization Lecture 2016](<http://www.stat.cmu.edu/~ryantibs/convexopt-F16/>)
- [CMU Convex Optimization Lecture 2019](<http://www.stat.cmu.edu/~ryantibs/convexopt/>)

## Original Authors and Reviewers

### Original Authors (Alphabetical Order)

- Kibum Kim (astroblasterr@gmail.com)
- Jeong-Hoon Kim (placidus36@gmail.com)
- Won-Jong Roh (wnoh27@naver.com)
- Jinwoo Park (www.jwpark.co.kr@gmail.com)
- Seong-Jin Yoon (sjyoon@gmail.com)
- Gyu-Bok Lee (gyubokl@gmail.com)
- Young-Il Han (thinkingtoyihan@gmail.com)
- Hye-Jin Hwang (brillianthhj@gmail.com)

### Reviewers (Alphabetical Order)

- Juhee Lee (juhee1108@gmail.com)
- Seung-Hwan Jang (schang.math@gmail.com)
- Tae-Soo Chung (tcheong@korea.ac.kr)

[Detailed Introduction of Original Authors and Reviewers](./AUTHORS.md)

## Theme

- [Lanyon](https://github.com/poole/lanyon) by [Mark Otto](https://github.com/mdo)

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="http://www.linkedin.com/in/enfow"><img src="https://avatars.githubusercontent.com/u/31348169?v=4?s=100" width="100px;" alt="KyeongMin WOO"/><br /><sub><b>KyeongMin WOO</b></sub></a><br /><a href="https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io/commits?author=enfow" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/RRoundTable"><img src="https://avatars.githubusercontent.com/u/27891090?v=4?s=100" width="100px;" alt="Wontak Ryu"/><br /><sub><b>Wontak Ryu</b></sub></a><br /><a href="https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io/commits?author=RRoundTable" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/LEEMINJOO"><img src="https://avatars.githubusercontent.com/u/42792260?v=4?s=100" width="100px;" alt="LEEMINJOO"/><br /><sub><b>LEEMINJOO</b></sub></a><br /><a href="https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io/commits?author=LEEMINJOO" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/hunhoon21"><img src="https://avatars.githubusercontent.com/u/36983960?v=4?s=100" width="100px;" alt="HoonCheol Shin"/><br /><sub><b>HoonCheol Shin</b></sub></a><br /><a href="https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io/commits?author=hunhoon21" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/curt-park/"><img src="https://avatars.githubusercontent.com/u/14961526?v=4?s=100" width="100px;" alt="Jinwoo Park (Curt)"/><br /><sub><b>Jinwoo Park (Curt)</b></sub></a><br /><a href="https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io/commits?author=Curt-Park" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/YoungJaeChoung"><img src="https://avatars.githubusercontent.com/u/29696891?v=4?s=100" width="100px;" alt="YoungJaeChoung"/><br /><sub><b>YoungJaeChoung</b></sub></a><br /><a href="https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io/commits?author=YoungJaeChoung" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/isingmodel"><img src="https://avatars.githubusercontent.com/u/31462012?v=4?s=100" width="100px;" alt="Kibum Fred Kim"/><br /><sub><b>Kibum Fred Kim</b></sub></a><br /><a href="https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io/commits?author=isingmodel" title="Code">💻</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/cneyang"><img src="https://avatars.githubusercontent.com/u/50402681?v=4?s=100" width="100px;" alt="Eugene Yang"/><br /><sub><b>Eugene Yang</b></sub></a><br /><a href="https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io/issues?q=author%3Acneyang" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://seong7.github.io"><img src="https://avatars.githubusercontent.com/u/52827441?v=4?s=100" width="100px;" alt="Seongjin Kim"/><br /><sub><b>Seongjin Kim</b></sub></a><br /><a href="https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io/commits?author=seong7" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://hgs3896.github.io"><img src="https://avatars.githubusercontent.com/u/1921149?v=4?s=100" width="100px;" alt="Ham Ji Seong"/><br /><sub><b>Ham Ji Seong</b></sub></a><br /><a href="https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io/commits?author=hgs3896" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://seolhokim.github.io"><img src="https://avatars.githubusercontent.com/u/38997792?v=4?s=100" width="100px;" alt="seolhokim"/><br /><sub><b>seolhokim</b></sub></a><br /><a href="#maintenance-seolhokim" title="Maintenance">🚧</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/RektPunk"><img src="https://avatars.githubusercontent.com/u/110188257?v=4?s=100" width="100px;" alt="RektPunk"/><br /><sub><b>RektPunk</b></sub></a><br /><a href="https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io/commits?author=RektPunk" title="Documentation">📖</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
