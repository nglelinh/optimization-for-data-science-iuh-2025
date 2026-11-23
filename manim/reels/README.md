# Optimization reels (Manim)
Render 1080x1920 scenes (`manim -qh`), captions only (no voice-over). Scenes: gd_step.py (GD), subgradient.py (Sub), newton.py (Newton), bfgs_race.py (QN). Shared helpers: common.py, common_b.py. Output goes to public/videos/reels/*_{vi,en}.mp4.
Second wave: prox_shrink.py (Prox), central_path.py (Path), frank_wolfe.py (FW).

Long reels (21/11, 65–95 s, 5 stages: setup, key idea, algorithm with numpy values, contrast, takeaway): r_*.py with shared layout rl.py and numerics o3lib.py.
Render one: `REEL_LANG=vi manim -qh r_cd.py Cd` (env: ~/teaching/.venv-manim, conda-forge manim 0.22). Scene map:
r_gd GD gd-step-sizes | r_sub Sub subgradient-fan | r_newton Newton newton-parabola | r_bfgs QN bfgs-vs-gd | r_prox Prox prox-shrink |
r_path Path central-path | r_fw FW frank-wolfe | r_polyak Polyak polyak-step | r_game Game matrix-game | r_dual Dual dual-lower-bound |
r_ld LassoDual lasso-dual | r_kkt Kkt kkt-normals | r_pd Pdip primal-dual-ipm | r_pn Pn prox-newton | r_dd Dec dual-decomposition |
r_admm Admm admm-lasso | r_cd Cd coordinate-descent | r_bnb Bnb branch-bound | r_cut Cut gomory-cut

Third wave (22/11, about 2:40–4 min, same 5 stages, one scene per lesson group; numbers checked by numpy asserts at import):
r_mom Mom momentum-nesterov | r_sgd Sgd sgd-minibatch | r_ada Ada adagrad-rmsprop-adam | r_simplex Simplex simplex-pivots |
r_kktw KktW kkt-water-filling | r_slater Slater strong-duality-slater | r_ls Ls line-search | r_fista Fista ista-fista |
r_maxflow MaxFlow max-flow-min-cut | r_saddle Saddle saddle-escape
Preview fast: `FAST=1 REEL_LANG=vi manim -ql r_mom.py Mom`. Compress: `ffmpeg -i in.mp4 -c:v libx264 -preset slow -crf 26 -pix_fmt yuv420p -movflags +faststart -an out.mp4`.

Fourth wave (23/11, about 2:45–3:10, silent, same 5 stages; numbers checked by numpy asserts at import):
r_cvx Cvx convexity-tests (03-01-01, 03-01-03) | r_foc Foc first-order-optimality (04-03) | r_ndec NDec newton-decrement (14-03) |
r_lbfgs Lbfgs l-bfgs (18-07) | r_admmg AdmmG admm-general (20-04-01) | r_ad Ad autodiff-forward-reverse (27-02, 27-03) |
r_pl Pl pl-condition (28-05) | r_fedavg FedAvg fedavg-drift (29-02)
Preview fast: `FAST=1 REEL_LANG=vi manim -ql r_cvx.py Cvx`. Final: `REEL_LANG=vi manim -qh r_cvx.py Cvx` (and `en`), then the same ffmpeg command as above.
Vietnamese narration drafts for later dubbing, with measured stage/caption times: `vo_scripts_batch2.py` (same `(k, offset, text)` format as `vo/narration_vi.py`).
