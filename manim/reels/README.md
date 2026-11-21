# Optimization reels (Manim)
Render 1080x1920 scenes (`manim -qh`), captions only (no voice-over). Scenes: gd_step.py (GD), subgradient.py (Sub), newton.py (Newton), bfgs_race.py (QN). Shared helpers: common.py, common_b.py. Output goes to public/videos/reels/*_{vi,en}.mp4.
Second wave: prox_shrink.py (Prox), central_path.py (Path), frank_wolfe.py (FW).

Long reels (21/11, 65–95 s, 5 stages: setup, key idea, algorithm with numpy values, contrast, takeaway): r_*.py with shared layout rl.py and numerics o3lib.py.
Render one: `REEL_LANG=vi manim -qh r_cd.py Cd` (env: ~/teaching/.venv-manim, conda-forge manim 0.22). Scene map:
r_gd GD gd-step-sizes | r_sub Sub subgradient-fan | r_newton Newton newton-parabola | r_bfgs QN bfgs-vs-gd | r_prox Prox prox-shrink |
r_path Path central-path | r_fw FW frank-wolfe | r_polyak Polyak polyak-step | r_game Game matrix-game | r_dual Dual dual-lower-bound |
r_ld LassoDual lasso-dual | r_kkt Kkt kkt-normals | r_pd Pdip primal-dual-ipm | r_pn Pn prox-newton | r_dd Dec dual-decomposition |
r_admm Admm admm-lasso | r_cd Cd coordinate-descent | r_bnb Bnb branch-bound | r_cut Cut gomory-cut
