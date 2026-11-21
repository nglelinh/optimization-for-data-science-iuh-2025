/* Optimization explainers (vanilla JS, no dependencies). Loaded only on chapters that use them.
 * Containers: <div class="opx-explainer" data-opx="KIND" data-lang="vi|en"></div>
 *   gd    : gradient descent on a rotated quadratic: fixed / backtracking / exact step (06-02-01)
 *   subg  : test a slope as a subgradient of a piecewise-linear convex function (07-01)
 *   cl    : constrained form vs Lagrange form for the l1 ball (12-05)
 *   newton: gradient descent vs Newton on a log-sum-exp function (14-07)
 *   bfgs  : gradient descent vs BFGS (and Newton) on the same function (18-04)
 *   ista  : ISTA on a 2-D lasso with soft-thresholding (09-01)
 *   barrier: central path of a small LP (15-02)
 *   fw    : Frank-Wolfe on a triangle (22-02)
 * State is exposed as data-* attributes so tests can read it. */
(function () {
    'use strict';
    var PI = Math.PI;
    var COL = { bg: '#0f1320', card: '#161b2c', ink: '#e8ecf6', dim: '#8a93aa', sky: '#4cc9f0', sun: '#ffd166', pink: '#ff7eb6', mint: '#80ed99', ora: '#ff9f43', grid: '#252c42' };
    function css() {
        if (document.getElementById('opx-css')) return;
        var s = document.createElement('style'); s.id = 'opx-css';
        s.textContent = '.opx{box-sizing:border-box;max-width:560px;margin:1.2rem auto;padding:14px;background:' + COL.bg + ';color:' + COL.ink + ';border-radius:14px;font:15px/1.45 -apple-system,Segoe UI,Roboto,sans-serif;text-align:left}' +
            '.opx *{box-sizing:border-box}.opx h4{margin:0 0 6px;font-size:17px;color:' + COL.sun + ';text-align:center;border:0}' +
            '.opx-note{margin:0 0 10px;color:' + COL.dim + ';font-size:13.5px}.opx canvas{display:block;width:100%;background:' + COL.card + ';border-radius:10px;touch-action:none}' +
            '.opx-row{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0}.opx button{min-height:44px;min-width:44px;padding:8px 12px;border:1px solid #39425f;border-radius:10px;background:#222a44;color:' + COL.ink + ';font-size:14px;cursor:pointer}' +
            '.opx button.on{background:' + COL.sun + ';color:#1b1b1b;border-color:' + COL.sun + '}.opx-sl{margin:10px 0 2px}.opx-sl label{display:flex;justify-content:space-between;font-size:13.5px;color:' + COL.ink + '}' +
            '.opx-sl input[type=range]{width:100%;height:44px;accent-color:' + COL.sun + ';margin:0}' +
            '.opx-stats{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0}.opx-st{flex:1 1 90px;background:' + COL.card + ';border-radius:10px;padding:8px 6px;text-align:center}.opx-st b{display:block;font-size:17px}.opx-st span{font-size:12px;color:' + COL.dim + '}' +
            '.opx-msg{margin:8px 0 0;font-size:14px;min-height:42px}.opx-ok{color:' + COL.mint + '}.opx-warn{color:' + COL.ora + '}.opx-bad{color:' + COL.pink + '}';
        document.head.appendChild(s);
    }
    function el(tag, cls, txt) { var e = document.createElement(tag); if (cls) e.className = cls; if (txt != null) e.textContent = txt; return e; }
    function U(lang) { return function (en, vi) { return lang === 'vi' ? vi : en; }; }
    function fmt(v, d, lang) { var s = (+v).toFixed(d); return lang === 'vi' ? s.replace('.', ',') : s; }
    function setd(root, o) { for (var k in o) root.setAttribute('data-' + k, String(o[k])); }
    function btn(label, cls, fn) { var b = el('button', cls || '', label); b.type = 'button'; b.addEventListener('click', fn); return b; }
    function row() { return el('div', 'opx-row'); }
    function stat(label) { var b = el('div', 'opx-st'), v = el('b', '', '-'), l = el('span', '', label); b.appendChild(v); b.appendChild(l); return { box: b, set: function (t) { v.textContent = t; } }; }
    function slider(label, min, max, step, val, onch, show) {
        var w = el('div', 'opx-sl'), lab = el('label'), a = el('span', '', label), b = el('span', '', ''), inp = el('input');
        inp.type = 'range'; inp.min = min; inp.max = max; inp.step = step; inp.value = val; lab.appendChild(a); lab.appendChild(b); w.appendChild(lab); w.appendChild(inp);
        function upd() { b.textContent = show(+inp.value); }
        inp.addEventListener('input', function () { upd(); onch(+inp.value); }); upd();
        return { wrap: w, input: inp, set: function (v) { inp.value = v; upd(); } };
    }
    function msgBox(root) { var m = el('p', 'opx-msg'); root.appendChild(m); return { set: function (t, c) { m.textContent = t; m.className = 'opx-msg ' + (c || ''); } }; }
    function canvas(aspect) {
        var c = el('canvas'), o = { c: c, ctx: null, w: 300, h: 300 };
        o.size = function () { var r = c.getBoundingClientRect(), w = Math.max(200, Math.round(r.width || c.parentNode.clientWidth || 300)), d = window.devicePixelRatio || 1; o.w = w; o.h = Math.round(w * aspect); c.width = Math.round(w * d); c.height = Math.round(o.h * d); c.style.height = o.h + 'px'; o.ctx = c.getContext('2d'); o.ctx.setTransform(d, 0, 0, d, 0, 0); };
        return o;
    }
    function after(fn) { if (document.readyState === 'complete') setTimeout(fn, 0); else window.addEventListener('load', function () { setTimeout(fn, 0); }); }
    function shell(root, title) { root.classList.add('opx'); root.innerHTML = ''; root.appendChild(el('h4', '', title)); }
    function txt(ctx, s, x, y, col, al) { ctx.fillStyle = col || COL.dim; ctx.font = '12px sans-serif'; ctx.textAlign = al || 'left'; ctx.fillText(s, x, y); }
    function view(cv, x0, x1, y0, y1, pad) { var p = pad == null ? 8 : pad; return { X: function (x) { return p + (cv.w - 2 * p) * (x - x0) / (x1 - x0); }, Y: function (y) { return cv.h - p - (cv.h - 2 * p) * (y - y0) / (y1 - y0); }, ix: function (px) { return x0 + (px - p) / (cv.w - 2 * p) * (x1 - x0); }, iy: function (py) { return y0 + (cv.h - p - py) / (cv.h - 2 * p) * (y1 - y0); } }; }
    function tapPos(cv, ev, cb) { var r = cv.c.getBoundingClientRect(); var pt = ev.touches && ev.touches.length ? ev.touches[0] : (ev.changedTouches && ev.changedTouches.length ? ev.changedTouches[0] : ev); cb(pt.clientX - r.left, pt.clientY - r.top); }
    function pointer(cv, cb) {
        var down = false;
        cv.c.addEventListener('pointerdown', function (e) { down = true; try { cv.c.setPointerCapture(e.pointerId); } catch (x) { } tapPos(cv, e, cb); });
        cv.c.addEventListener('pointermove', function (e) { if (down) tapPos(cv, e, cb); });
        cv.c.addEventListener('pointerup', function () { down = false; }); cv.c.addEventListener('pointercancel', function () { down = false; });
    }
    function line(ctx, pts, col, w, dash) { ctx.strokeStyle = col; ctx.lineWidth = w || 2; ctx.setLineDash(dash || []); ctx.beginPath(); for (var i = 0; i < pts.length; i++) { if (i) ctx.lineTo(pts[i][0], pts[i][1]); else ctx.moveTo(pts[i][0], pts[i][1]); } ctx.stroke(); ctx.setLineDash([]); }
    function dot(ctx, x, y, r, col) { ctx.fillStyle = col; ctx.beginPath(); ctx.arc(x, y, r, 0, 2 * PI); ctx.fill(); }

    /* ---------------- 06-02-01: gradient descent on a rotated quadratic ---------------- */
    function initGD(root, t, lang) {
        var tx = U(lang), TH = 25 * PI / 180, c = Math.cos(TH), s = Math.sin(TH);
        var kappa = 8, tl = 1.0, rule = 'fixed', P0 = [2.0, 1.2];
        shell(root, tx('Step size on a stretched bowl', 'Kích thước bước trên một cái bát bị kéo dài'));
        root.appendChild(el('p', 'opx-note', tx('f(x) = ½ xᵀAx with eigenvalues L and 1 (the bowl is turned by 25°). Tap the plot to move the start. Compare a fixed step with backtracking and exact line search.', 'f(x) = ½ xᵀAx với trị riêng L và 1 (cái bát xoay 25°). Chạm vào hình để đổi điểm xuất phát. So sánh bước cố định với backtracking và tìm kiếm đường chính xác.')));
        var rr = row(), bs = {};
        [['fixed', tx('Fixed step', 'Bước cố định')], ['bt', tx('Backtracking', 'Backtracking')], ['exact', tx('Exact line search', 'Đường chính xác')]].forEach(function (a) { bs[a[0]] = btn(a[1], a[0] === 'fixed' ? 'on' : '', function () { rule = a[0]; upd(); }); rr.appendChild(bs[a[0]]); });
        root.appendChild(rr);
        var sk = slider(tx('Condition number L (smallest eigenvalue is 1)', 'Số điều kiện L (trị riêng nhỏ nhất là 1)'), 2, 30, 1, kappa, function (v) { kappa = v; upd(); }, function (v) { return String(v); });
        var st = slider(tx('Fixed step t · L', 'Bước cố định t · L'), 0.05, 2.4, 0.01, tl, function (v) { tl = v; upd(); }, function (v) { return fmt(v, 2, lang); });
        root.appendChild(sk.wrap); root.appendChild(st.wrap);
        var cv = canvas(0.85); root.appendChild(cv.c);
        var sts = el('div', 'opx-stats'), sI = stat(tx('steps', 'số bước')), sF = stat(tx('final f', 'f cuối')), sS = stat(tx('verdict', 'kết luận'));
        [sI, sF, sS].forEach(function (q) { sts.appendChild(q.box); }); root.appendChild(sts);
        var msg = msgBox(root), V = null, path = [];
        function A(p) { var u = c * p[0] + s * p[1], v = -s * p[0] + c * p[1]; return [c * kappa * u - s * v, s * kappa * u + c * v]; }
        function f(p) { var g = A(p); return 0.5 * (p[0] * g[0] + p[1] * g[1]); }
        function run() {
            var p = P0.slice(), pts = [p.slice()], f0 = f(p), tfix = tl / kappa, it = 0, status = 'slow', MAXIT = 200;
            while (it < MAXIT) {
                if (f(p) < 1e-8 * f0) { status = 'converged'; break; }
                var g = A(p), gg = g[0] * g[0] + g[1] * g[1], tt;
                if (rule === 'fixed') tt = tfix;
                else if (rule === 'exact') { var Ag = A(g); tt = gg / (g[0] * Ag[0] + g[1] * Ag[1]); }
                else { tt = 1; var fp = f(p), q; for (var k = 0; k < 60; k++) { q = [p[0] - tt * g[0], p[1] - tt * g[1]]; if (f(q) <= fp - 0.3 * tt * gg) break; tt *= 0.7; } }
                p = [p[0] - tt * g[0], p[1] - tt * g[1]]; pts.push(p.slice()); it++;
                if (!isFinite(f(p)) || f(p) > 1e6 * f0) { status = 'diverged'; break; }
            }
            if (status === 'slow' && f(p) < 1e-8 * f0) status = 'converged';
            return { pts: pts, it: it, f: f(p), status: status };
        }
        cv.draw = function () {
            if (!cv.ctx) cv.size();
            var ctx = cv.ctx; ctx.clearRect(0, 0, cv.w, cv.h); V = view(cv, -3, 3, -2.55, 2.55);
            ctx.strokeStyle = COL.grid; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(V.X(-3), V.Y(0)); ctx.lineTo(V.X(3), V.Y(0)); ctx.moveTo(V.X(0), V.Y(-2.55)); ctx.lineTo(V.X(0), V.Y(2.55)); ctx.stroke();
            var f0 = f(P0), sc = (cv.w - 16) / 6;
            [1, 0.5, 0.25, 0.1, 0.03, 0.008].forEach(function (cc) { var lev = cc * f0, a = Math.sqrt(2 * lev / kappa) * sc, b = Math.sqrt(2 * lev) * sc; ctx.strokeStyle = '#3a4466'; ctx.lineWidth = 1; ctx.beginPath(); ctx.ellipse(V.X(0), V.Y(0), a, b, -TH, 0, 2 * PI); ctx.stroke(); });
            var pts = path.filter(function (p) { return Math.abs(p[0]) < 6 && Math.abs(p[1]) < 6; });
            line(ctx, pts.map(function (p) { return [V.X(p[0]), V.Y(p[1])]; }), rule === 'fixed' ? COL.sun : rule === 'bt' ? COL.sky : COL.mint, 2);
            pts.forEach(function (p, i) { if (i < 80) dot(ctx, V.X(p[0]), V.Y(p[1]), 2.4, COL.ink); });
            dot(ctx, V.X(P0[0]), V.Y(P0[1]), 6, COL.pink); dot(ctx, V.X(0), V.Y(0), 4, COL.mint);
            txt(ctx, 'x*', V.X(0) + 7, V.Y(0) - 6, COL.mint);
        };
        pointer(cv, function (px, py) { if (!V) return; var x = V.ix(px), y = V.iy(py); if (Math.abs(x) > 2.9 || Math.abs(y) > 2.45) return; if (x * x + y * y < 0.04) return; P0 = [x, y]; upd(); });
        function upd() {
            Object.keys(bs).forEach(function (k) { bs[k].className = k === rule ? 'on' : ''; });
            st.input.disabled = rule !== 'fixed';
            var r = run(); path = r.pts;
            sI.set(r.status === 'diverged' ? '∞' : (r.status === 'slow' ? '> ' + r.it : String(r.it)));
            sF.set(r.status === 'diverged' ? '∞' : r.f.toExponential(1)); sS.set(r.status === 'converged' ? tx('converges', 'hội tụ') : r.status === 'diverged' ? tx('diverges', 'phân kỳ') : tx('too slow', 'quá chậm'));
            setd(root, { rule: rule, kappa: kappa, t: (rule === 'fixed' ? tl / kappa : 0).toFixed(4), tl: rule === 'fixed' ? tl.toFixed(2) : '', iters: r.it, status: r.status, start: P0[0].toFixed(2) + ',' + P0[1].toFixed(2) });
            msg.set(r.status === 'diverged' ? tx('The steps overshoot more than they fix: the iterates move away from x*.', 'Các bước vượt quá nhiều hơn mức sửa: điểm lặp đi xa khỏi x*.')
                : r.status === 'slow' ? tx('Still far from x* after 200 steps: the steps are too timid for the flat direction.', 'Sau 200 bước vẫn còn xa x*: bước quá rụt rè theo hướng phẳng.')
                    : tx('Reached f < 10⁻⁸ f(start) in ' + r.it + ' steps.', 'Đạt f < 10⁻⁸ f(xuất phát) sau ' + r.it + ' bước.'), r.status === 'converged' ? 'opx-ok' : r.status === 'diverged' ? 'opx-bad' : 'opx-warn');
            cv.draw();
        }
        after(function () { cv.size(); upd(); });
    }

    /* ---------------- 07-01: is this slope a subgradient? ---------------- */
    var SL = [[-2, -1], [0.5, 0], [2, -3]];
    function fS(x) { return Math.max(SL[0][0] * x + SL[0][1], SL[1][0] * x + SL[1][1], SL[2][0] * x + SL[2][1]); }
    function subInterval(x) {
        var v = fS(x), act = SL.filter(function (l) { return Math.abs(l[0] * x + l[1] - v) < 1e-9; }).map(function (l) { return l[0]; });
        return [Math.min.apply(null, act), Math.max.apply(null, act)];
    }
    function initSubg(root, t, lang) {
        var tx = U(lang), x0 = -1.2, g = 0, rev = false;
        shell(root, tx('Is this slope a subgradient?', 'Độ dốc này có là gradient dưới không?'));
        root.appendChild(el('p', 'opx-note', tx('f(x) = max{ −2x − 1, x/2, 2x − 3 }. Pick a point and a slope g. The line f(x₀) + g(y − x₀) is a valid subgradient line only if it stays below f everywhere.', 'f(x) = max{ −2x − 1, x/2, 2x − 3 }. Chọn một điểm và một độ dốc g. Đường f(x₀) + g(y − x₀) chỉ hợp lệ nếu nằm dưới f ở mọi nơi.')));
        var sx = slider('x₀', -3, 4, 0.05, x0, function (v) { x0 = v; upd(); }, function (v) { return fmt(v, 2, lang); });
        var sg = slider('g', -3, 3, 0.05, g, function (v) { g = v; upd(); }, function (v) { return fmt(v, 2, lang); });
        root.appendChild(sx.wrap); root.appendChild(sg.wrap);
        var rr = row();
        rr.appendChild(btn(tx('Go to left kink', 'Tới điểm gãy trái'), '', function () { x0 = -0.4; sx.set(x0); upd(); }));
        rr.appendChild(btn(tx('Go to right kink', 'Tới điểm gãy phải'), '', function () { x0 = 2; sx.set(x0); upd(); }));
        var rb = btn(tx('Show all valid slopes', 'Hiện mọi độ dốc hợp lệ'), '', function () { rev = !rev; upd(); }); rr.appendChild(rb); root.appendChild(rr);
        var cv = canvas(0.72); root.appendChild(cv.c);
        var sts = el('div', 'opx-stats'), sV = stat(tx('line below f?', 'đường nằm dưới f?')), sR = stat(tx('valid slopes', 'độ dốc hợp lệ')); [sV, sR].forEach(function (q) { sts.appendChild(q.box); }); root.appendChild(sts);
        var msg = msgBox(root);
        function valid() { var y0 = fS(x0), ok = true; for (var i = 0; i <= 700; i++) { var y = -3 + 7 * i / 700; if (fS(y) < y0 + g * (y - x0) - 1e-9) { ok = false; break; } } return ok; }
        cv.draw = function () {
            if (!cv.ctx) cv.size();
            var ctx = cv.ctx; ctx.clearRect(0, 0, cv.w, cv.h); var V = view(cv, -3, 4, -1.6, 6.4);
            ctx.strokeStyle = COL.grid; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(V.X(-3), V.Y(0)); ctx.lineTo(V.X(4), V.Y(0)); ctx.moveTo(V.X(0), V.Y(-1.6)); ctx.lineTo(V.X(0), V.Y(6.4)); ctx.stroke();
            var ok = valid(), y0 = fS(x0), col = ok ? COL.mint : COL.pink;
            ctx.save(); ctx.beginPath(); ctx.rect(V.X(-3), V.Y(6.4), V.X(4) - V.X(-3), V.Y(-1.6) - V.Y(6.4)); ctx.clip();
            line(ctx, [[V.X(-3), V.Y(y0 + g * (-3 - x0))], [V.X(4), V.Y(y0 + g * (4 - x0))]], col, 2.5, ok ? [] : [6, 4]);
            if (rev) { var iv = subInterval(x0); [iv[0], iv[1]].forEach(function (gg) { line(ctx, [[V.X(-3), V.Y(y0 + gg * (-3 - x0))], [V.X(4), V.Y(y0 + gg * (4 - x0))]], COL.ora, 1.2, [3, 3]); }); }
            var pts = []; for (var i = 0; i <= 140; i++) { var x = -3 + 7 * i / 140; pts.push([V.X(x), V.Y(fS(x))]); } line(ctx, pts, COL.sky, 3.5);
            ctx.restore(); dot(ctx, V.X(x0), V.Y(y0), 6, COL.sun); txt(ctx, 'f', V.X(3.7), V.Y(fS(3.7)) - 8, COL.sky);
        };
        function upd() {
            var ok = valid(), iv = subInterval(x0), uniq = iv[1] - iv[0] < 1e-9;
            sV.set(ok ? tx('yes', 'có') : tx('no', 'không')); sR.set(rev ? (uniq ? '{' + fmt(iv[0], 2, lang) + '}' : '[' + fmt(iv[0], 2, lang) + ', ' + fmt(iv[1], 2, lang) + ']') : '?');
            rb.className = rev ? 'on' : '';
            setd(root, { x0: x0.toFixed(2), g: g.toFixed(2), valid: ok ? 1 : 0, lo: iv[0], hi: iv[1], reveal: rev ? 1 : 0 });
            msg.set(ok ? (uniq ? tx('Smooth point: only the slope f′(x₀) works.', 'Điểm trơn: chỉ có độ dốc f′(x₀) dùng được.') : tx('At a kink more than one slope works: they fill an interval.', 'Tại điểm gãy có nhiều độ dốc dùng được: chúng lấp đầy một đoạn.'))
                : tx('The line cuts through the graph, so g is not a subgradient at this point.', 'Đường cắt qua đồ thị nên g không phải gradient dưới tại điểm này.'), ok ? 'opx-ok' : 'opx-bad');
            cv.draw();
        }
        after(function () { cv.size(); upd(); });
    }

    /* ---------------- 12-05: constrained form vs Lagrange form (l1 ball) ---------------- */
    function initCL(root, t, lang) {
        var tx = U(lang), b = [2.6, -1.2], tt = 1.5, lam = 0, cur = 't';
        shell(root, tx('Same solution, two descriptions', 'Cùng một nghiệm, hai cách mô tả'));
        root.appendChild(el('p', 'opx-note', tx('(C): min ½‖x − b‖² subject to ‖x‖₁ ≤ t.   (L): min ½‖x − b‖² + λ‖x‖₁. Move either slider and read off the other parameter. Tap the plot to move b.', '(C): min ½‖x − b‖² với ‖x‖₁ ≤ t.   (L): min ½‖x − b‖² + λ‖x‖₁. Kéo một thanh trượt và đọc tham số còn lại. Chạm vào hình để đổi b.')));
        var s1 = slider('t  (C)', 0, 3.8, 0.01, tt, function (v) { tt = v; cur = 't'; upd(); }, function (v) { return fmt(v, 2, lang); });
        var s2 = slider('λ  (L)', 0, 2.6, 0.01, 0, function (v) { lam = v; cur = 'l'; upd(); }, function (v) { return fmt(v, 2, lang); });
        root.appendChild(s1.wrap); root.appendChild(s2.wrap);
        var cv = canvas(0.8); root.appendChild(cv.c);
        var sts = el('div', 'opx-st-wrap opx-stats'), sX = stat('x*'), sL = stat('λ*(t)'), sT = stat('‖x*‖₁'), sM = stat(tx('(C) = (L)?', '(C) = (L)?'));
        [sX, sL, sT, sM].forEach(function (q) { sts.appendChild(q.box); }); root.appendChild(sts);
        var msg = msgBox(root), V = null;
        function soft(lm) { return b.map(function (v) { return Math.sign(v) * Math.max(Math.abs(v) - lm, 0); }); }
        function lamOf(tv) {
            var a = Math.abs(b[0]), c = Math.abs(b[1]), hi = Math.max(a, c), lo = Math.min(a, c);
            if (tv >= a + c) return 0; if (tv <= hi - lo) return hi - tv; return (a + c - tv) / 2;
        }
        function l1(x) { return Math.abs(x[0]) + Math.abs(x[1]); }
        cv.draw = function () {
            if (!cv.ctx) cv.size();
            var ctx = cv.ctx; ctx.clearRect(0, 0, cv.w, cv.h); V = view(cv, -4, 4, -3.2, 3.2);
            ctx.strokeStyle = COL.grid; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(V.X(-4), V.Y(0)); ctx.lineTo(V.X(4), V.Y(0)); ctx.moveTo(V.X(0), V.Y(-3.2)); ctx.lineTo(V.X(0), V.Y(3.2)); ctx.stroke();
            var tv = tt, x = soft(lamOf(tv)), sc = (cv.w - 16) / 8, r = Math.hypot(x[0] - b[0], x[1] - b[1]);
            ctx.fillStyle = 'rgba(255,209,102,0.16)'; ctx.strokeStyle = COL.sun; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(V.X(tv), V.Y(0)); ctx.lineTo(V.X(0), V.Y(tv)); ctx.lineTo(V.X(-tv), V.Y(0)); ctx.lineTo(V.X(0), V.Y(-tv)); ctx.closePath(); if (tv > 0.005) { ctx.fill(); ctx.stroke(); }
            ctx.strokeStyle = COL.sky; ctx.lineWidth = 1.5; ctx.setLineDash([5, 4]); ctx.beginPath(); ctx.arc(V.X(b[0]), V.Y(b[1]), r * sc, 0, 2 * PI); ctx.stroke(); ctx.setLineDash([]);
            dot(ctx, V.X(b[0]), V.Y(b[1]), 6, COL.pink); txt(ctx, 'b', V.X(b[0]) + 8, V.Y(b[1]) - 6, COL.pink);
            dot(ctx, V.X(x[0]), V.Y(x[1]), 6, COL.mint); txt(ctx, 'x*', V.X(x[0]) + 8, V.Y(x[1]) + 14, COL.mint);
        };
        pointer(cv, function (px, py) { if (!V) return; var x = V.ix(px), y = V.iy(py); if (Math.abs(x) > 3.6 || Math.abs(y) > 2.9 || (Math.abs(x) < 0.15 && Math.abs(y) < 0.15)) return; b = [Math.round(x * 10) / 10, Math.round(y * 10) / 10]; var m = Math.abs(b[0]) + Math.abs(b[1]); s1.input.max = m.toFixed(2); s2.input.max = Math.max(Math.abs(b[0]), Math.abs(b[1])).toFixed(2); tt = Math.min(tt, m); cur = 't'; upd(); });
        function upd() {
            var mx = Math.abs(b[0]) + Math.abs(b[1]);
            if (cur === 'l') { var xl = soft(lam); tt = l1(xl); }
            tt = Math.min(Math.max(tt, 0), mx);
            var lm = lamOf(tt), xc = soft(lm), xl2 = soft(lm);
            var same = Math.hypot(xc[0] - xl2[0], xc[1] - xl2[1]) < 1e-9 && l1(xc) <= tt + 1e-9;
            if (cur === 't') { lam = lm; }
            s1.set(tt); s2.set(lam);
            sX.set('(' + fmt(xc[0], 2, lang) + ', ' + fmt(xc[1], 2, lang) + ')'); sL.set(fmt(lm, 2, lang)); sT.set(fmt(l1(xc), 2, lang)); sM.set(same ? tx('same x*', 'cùng x*') : '?');
            setd(root, { t: tt.toFixed(3), lam: lm.toFixed(3), x1: xc[0].toFixed(3), x2: xc[1].toFixed(3), b: b[0] + ',' + b[1], same: same ? 1 : 0 });
            msg.set(lm < 1e-9 ? tx('t is big enough that the constraint is inactive: λ = 0 and x* = b.', 't đủ lớn để ràng buộc không tác dụng: λ = 0 và x* = b.')
                : tx('The constraint is active (‖x*‖₁ = t) and the multiplier is λ* = ' + fmt(lm, 2, lang) + '. Solving (L) with this λ gives the very same x*.', 'Ràng buộc đang tác dụng (‖x*‖₁ = t) và nhân tử là λ* = ' + fmt(lm, 2, lang) + '. Giải (L) với λ này cho đúng cùng x*.'), 'opx-ok');
            cv.draw();
        }
        after(function () { cv.size(); upd(); });
    }

    /* ---------------- 14-07 / 18-04: first-order vs second-order on log-sum-exp ---------------- */
    function F(p) { var a = Math.exp(p[0] + 3 * p[1] - 0.1), b = Math.exp(p[0] - 3 * p[1] - 0.1), c = Math.exp(-p[0] - 0.1); return Math.log(a + b + c); }
    function G(p) { var a = Math.exp(p[0] + 3 * p[1] - 0.1), b = Math.exp(p[0] - 3 * p[1] - 0.1), c = Math.exp(-p[0] - 0.1), z = a + b + c; return [(a + b - c) / z, (3 * a - 3 * b) / z]; }
    function Hs(p) { var a = Math.exp(p[0] + 3 * p[1] - 0.1), b = Math.exp(p[0] - 3 * p[1] - 0.1), c = Math.exp(-p[0] - 0.1), z = a + b + c, gx = (a + b - c) / z, gy = (3 * a - 3 * b) / z; return [(a + b + c) / z - gx * gx, (3 * a - 3 * b) / z - gx * gy, 9 * (a + b) / z - gy * gy]; }
    function solve2(h, g) { var d = h[0] * h[2] - h[1] * h[1]; return [(h[2] * g[0] - h[1] * g[1]) / d, (-h[1] * g[0] + h[0] * g[1]) / d]; }
    var FSTAR = (function () { var p = [0, 0]; for (var i = 0; i < 60; i++) { var d = solve2(Hs(p), G(p)); p = [p[0] - d[0], p[1] - d[1]]; } return { p: p, f: F(p) }; })();
    function runMethod(kind, start, maxit) {
        var p = start.slice(), pts = [p.slice()], fs = [F(p) - FSTAR.f], Hm = [1, 0, 1], gprev = G(p), it = 0;
        while (it < maxit && fs[fs.length - 1] > 1e-10) {
            var g = G(p), d;
            if (kind === 'newton') { var q = solve2(Hs(p), g); d = [-q[0], -q[1]]; }
            else if (kind === 'bfgs') d = [-(Hm[0] * g[0] + Hm[1] * g[1]), -(Hm[1] * g[0] + Hm[2] * g[1])];
            else d = [-g[0], -g[1]];
            var tt = 1, fp = F(p), gd = g[0] * d[0] + g[1] * d[1], k = 0;
            while (F([p[0] + tt * d[0], p[1] + tt * d[1]]) > fp + 0.1 * tt * gd && k < 80) { tt *= 0.7; k++; }
            var pn = [p[0] + tt * d[0], p[1] + tt * d[1]], gn = G(pn);
            if (kind === 'bfgs') {
                var sv = [pn[0] - p[0], pn[1] - p[1]], yv = [gn[0] - g[0], gn[1] - g[1]], sy = sv[0] * yv[0] + sv[1] * yv[1];
                if (sy > 1e-14) { var r = 1 / sy, Hy = [Hm[0] * yv[0] + Hm[1] * yv[1], Hm[1] * yv[0] + Hm[2] * yv[1]], yHy = yv[0] * Hy[0] + yv[1] * Hy[1], f1 = 1 + yHy * r;
                    Hm = [Hm[0] + f1 * r * sv[0] * sv[0] - r * (Hy[0] * sv[0] + sv[0] * Hy[0]), Hm[1] + f1 * r * sv[0] * sv[1] - r * (Hy[0] * sv[1] + sv[0] * Hy[1]), Hm[2] + f1 * r * sv[1] * sv[1] - r * (Hy[1] * sv[1] + sv[1] * Hy[1])]; }
            }
            p = pn; pts.push(p.slice()); fs.push(Math.max(F(p) - FSTAR.f, 1e-16)); it++;
        }
        return { pts: pts, fs: fs, it: it, ok: fs[fs.length - 1] <= 1e-10 };
    }
    function contourSegs(levels, x0, x1, y0, y1, n) {
        var out = [], vals = [], i, j; for (i = 0; i <= n; i++) { vals.push([]); for (j = 0; j <= n; j++) vals[i].push(F([x0 + (x1 - x0) * i / n, y0 + (y1 - y0) * j / n])); }
        function pt(i, j, k, l, lv) { var a = vals[i][j], b = vals[k][l], t = (lv - a) / (b - a); return [x0 + (x1 - x0) * (i + t * (k - i)) / n, y0 + (y1 - y0) * (j + t * (l - j)) / n]; }
        levels.forEach(function (lv) { for (i = 0; i < n; i++) for (j = 0; j < n; j++) {
            var c = [vals[i][j] > lv, vals[i + 1][j] > lv, vals[i + 1][j + 1] > lv, vals[i][j + 1] > lv], e = [];
            if (c[0] !== c[1]) e.push(pt(i, j, i + 1, j, lv)); if (c[1] !== c[2]) e.push(pt(i + 1, j, i + 1, j + 1, lv)); if (c[3] !== c[2]) e.push(pt(i, j + 1, i + 1, j + 1, lv)); if (c[0] !== c[3]) e.push(pt(i, j, i, j + 1, lv));
            if (e.length === 2) out.push([e[0], e[1]]); else if (e.length === 4) { out.push([e[0], e[1]]); out.push([e[2], e[3]]); } } });
        return out;
    }
    var CSEG = null;
    function initRace(root, t, lang, mode) {
        var tx = U(lang), STARTS = [[1.6, 1.1], [-2.0, -1.4], [0.6, -2.0]], si = 0, on = { gd: true, newton: mode === 'newton', bfgs: mode === 'bfgs' }, K = 0, play = null;
        var names = { gd: tx('Gradient descent', 'Gradient descent'), newton: tx('Newton', 'Newton'), bfgs: 'BFGS' }, cols = { gd: COL.sun, newton: COL.sky, bfgs: COL.mint };
        shell(root, mode === 'newton' ? tx('Gradient descent vs Newton', 'Gradient descent và Newton') : tx('Gradient descent vs BFGS', 'Gradient descent và BFGS'));
        root.appendChild(el('p', 'opx-note', tx('Minimise f(x) = log(e^(x₁+3x₂−0.1) + e^(x₁−3x₂−0.1) + e^(−x₁−0.1)) with backtracking line search (α = 0.1, β = 0.7). Slide through the iterations and watch the gap f − f*.', 'Cực tiểu hóa f(x) = log(e^(x₁+3x₂−0.1) + e^(x₁−3x₂−0.1) + e^(−x₁−0.1)) với backtracking (α = 0,1; β = 0,7). Kéo qua các bước lặp và xem khoảng cách f − f*.')));
        var r1 = row(), sb = [];
        STARTS.forEach(function (p, i) { sb.push(btn(tx('Start ', 'Điểm đầu ') + (i + 1), i === 0 ? 'on' : '', function () { si = i; K = 0; upd(); })); r1.appendChild(sb[i]); }); root.appendChild(r1);
        var r2 = row(), mb = {};
        ['gd', 'newton', 'bfgs'].forEach(function (k) { mb[k] = btn(names[k], on[k] ? 'on' : '', function () { if (on[k] && Object.keys(on).filter(function (q) { return on[q]; }).length === 1) return; on[k] = !on[k]; upd(); }); r2.appendChild(mb[k]); }); root.appendChild(r2);
        var sk = slider(tx('Iteration', 'Bước lặp'), 0, 40, 1, 0, function (v) { K = v; stop(); draw(); setd(root, { k: K }); }, function (v) { return String(v); });
        root.appendChild(sk.wrap);
        var pb = btn(tx('▶ Play', '▶ Chạy'), '', function () { if (play) { stop(); return; } if (K >= maxK) K = 0; pb.textContent = tx('■ Stop', '■ Dừng'); play = setInterval(function () { K++; if (K >= maxK) { K = maxK; stop(); } sk.set(K); draw(); setd(root, { k: K }); }, 450); });
        var r3 = row(); r3.appendChild(pb); root.appendChild(r3);
        function stop() { if (play) clearInterval(play); play = null; pb.textContent = tx('▶ Play', '▶ Chạy'); }
        var cv = canvas(0.78), cv2 = canvas(0.5); root.appendChild(cv.c); root.appendChild(cv2.c);
        var sts = el('div', 'opx-stats'), sG = stat(names.gd), sN = stat(names.newton), sB = stat('BFGS'); [sG, sN, sB].forEach(function (q) { sts.appendChild(q.box); }); root.appendChild(sts);
        var msg = msgBox(root), R = {}, maxK = 40;
        function draw() {
            if (!cv.ctx) { cv.size(); cv2.size(); }
            var ctx = cv.ctx; ctx.clearRect(0, 0, cv.w, cv.h); var V = view(cv, -2.6, 2.4, -2.6, 2.4);
            CSEG = CSEG || contourSegs([FSTAR.f + 0.05, FSTAR.f + 0.25, FSTAR.f + 0.7, FSTAR.f + 1.5, FSTAR.f + 2.6], -2.6, 2.4, -2.6, 2.4, 70);
            ctx.strokeStyle = '#34405f'; ctx.lineWidth = 1; ctx.beginPath(); CSEG.forEach(function (s) { ctx.moveTo(V.X(s[0][0]), V.Y(s[0][1])); ctx.lineTo(V.X(s[1][0]), V.Y(s[1][1])); }); ctx.stroke();
            ['gd', 'newton', 'bfgs'].forEach(function (k) { if (!on[k]) return; var r = R[k], n = Math.min(K, r.it), pts = r.pts.slice(0, n + 1).map(function (p) { return [V.X(p[0]), V.Y(p[1])]; }); line(ctx, pts, cols[k], 2); pts.forEach(function (q) { dot(ctx, q[0], q[1], 2.6, cols[k]); }); dot(ctx, pts[pts.length - 1][0], pts[pts.length - 1][1], 5, cols[k]); });
            dot(ctx, V.X(STARTS[si][0]), V.Y(STARTS[si][1]), 5, COL.pink); dot(ctx, V.X(FSTAR.p[0]), V.Y(FSTAR.p[1]), 4, COL.ink); txt(ctx, 'x*', V.X(FSTAR.p[0]) + 6, V.Y(FSTAR.p[1]) - 6, COL.ink);
            var c2 = cv2.ctx, L = 34, T = 8, w = cv2.w - L - 10, h = cv2.h - T - 22; c2.clearRect(0, 0, cv2.w, cv2.h);
            for (var e = 0; e >= -10; e -= 2) { var yy = T + h * (-e) / 10 * 1; c2.strokeStyle = COL.grid; c2.lineWidth = 1; c2.beginPath(); c2.moveTo(L, yy); c2.lineTo(L + w, yy); c2.stroke(); txt(c2, '1e' + e, L - 4, yy + 4, COL.dim, 'right'); }
            ['gd', 'newton', 'bfgs'].forEach(function (k) { if (!on[k]) return; var r = R[k], n = Math.min(K, r.it), pts = []; for (var i = 0; i <= n; i++) pts.push([L + w * i / maxK, T + h * (-Math.log10(Math.max(r.fs[i], 1e-10))) / 10]); line(c2, pts, cols[k], 2.2); });
            txt(c2, tx('iteration', 'bước lặp'), L + w / 2, cv2.h - 4, COL.dim, 'center'); txt(c2, 'f − f*', L + 2, T + 10, COL.dim);
        }
        function upd() {
            Object.keys(mb).forEach(function (k) { mb[k].className = on[k] ? 'on' : ''; }); sb.forEach(function (b, i) { b.className = i === si ? 'on' : ''; });
            ['gd', 'newton', 'bfgs'].forEach(function (k) { R[k] = runMethod(k, STARTS[si], 400); });
            maxK = Math.max(Math.min(40, Math.max.apply(null, ['gd', 'newton', 'bfgs'].filter(function (k) { return on[k]; }).map(function (k) { return R[k].it; }))), 1);
            sk.input.max = maxK; if (K > maxK) K = maxK; sk.set(K);
            sG.set(R.gd.it + (R.gd.ok ? '' : '+')); sN.set(String(R.newton.it)); sB.set(String(R.bfgs.it));
            setd(root, { mode: mode, start: si + 1, gd: R.gd.it, newton: R.newton.it, bfgs: R.bfgs.it, fstar: FSTAR.f.toFixed(6), k: K, on: Object.keys(on).filter(function (k) { return on[k]; }).join('+'), maxk: maxK });
            msg.set(mode === 'newton' ? tx('Steps needed to get f − f* below 10⁻¹⁰: gradient descent ' + R.gd.it + ', Newton ' + R.newton.it + '. Newton pays for a 2×2 linear solve each step and then closes the gap very fast.', 'Số bước để f − f* < 10⁻¹⁰: gradient descent ' + R.gd.it + ', Newton ' + R.newton.it + '. Newton phải giải hệ tuyến tính 2×2 mỗi bước rồi thu hẹp khoảng cách rất nhanh.')
                : tx('Steps for f − f* < 10⁻¹⁰: gradient descent ' + R.gd.it + ', BFGS ' + R.bfgs.it + '. BFGS never forms the Hessian: it learns curvature from the gradients it has already seen.', 'Số bước để f − f* < 10⁻¹⁰: gradient descent ' + R.gd.it + ', BFGS ' + R.bfgs.it + '. BFGS không dựng Hessian: nó học độ cong từ các gradient đã thấy.'), 'opx-ok');
            draw();
        }
        after(function () { cv.size(); cv2.size(); upd(); });
    }

    /* ---------------- 09-01: ISTA for a 2-D lasso ---------------- */
    var LA = [[1.6, 0.7], [0.4, 1.1]], LB = [2.1, 0.9];
    function lassoF(x, lam) { var r0 = LA[0][0] * x[0] + LA[0][1] * x[1] - LB[0], r1 = LA[1][0] * x[0] + LA[1][1] * x[1] - LB[1]; return 0.5 * (r0 * r0 + r1 * r1) + lam * (Math.abs(x[0]) + Math.abs(x[1])); }
    function lassoL() { var a = LA[0][0] * LA[0][0] + LA[1][0] * LA[1][0], b = LA[0][0] * LA[0][1] + LA[1][0] * LA[1][1], d = LA[0][1] * LA[0][1] + LA[1][1] * LA[1][1]; return (a + d) / 2 + Math.sqrt(Math.pow((a - d) / 2, 2) + b * b); }
    function soft(v, th) { return v > th ? v - th : v < -th ? v + th : 0; }
    function istaRun(x0, lam, t, n) {
        var x = x0.slice(), pts = [x.slice()];
        for (var k = 0; k < n; k++) {
            var r0 = LA[0][0] * x[0] + LA[0][1] * x[1] - LB[0], r1 = LA[1][0] * x[0] + LA[1][1] * x[1] - LB[1];
            var g0 = LA[0][0] * r0 + LA[1][0] * r1, g1 = LA[0][1] * r0 + LA[1][1] * r1;
            x = [soft(x[0] - t * g0, t * lam), soft(x[1] - t * g1, t * lam)]; pts.push(x.slice());
            if (!isFinite(x[0]) || Math.abs(x[0]) > 1e6 || Math.abs(x[1]) > 1e6) break;
        }
        return pts;
    }
    function initISTA(root, t, lang) {
        var tx = U(lang), LL = lassoL(), lam = 0.8, tl = 1.0, P0 = [-1.8, 1.9], V = null, cache = null;
        shell(root, tx('ISTA for a small lasso', 'ISTA cho một bài lasso nhỏ'));
        root.appendChild(el('p', 'opx-note', tx('Minimise ½‖Ax − b‖² + λ‖x‖₁ in two variables. Each step is a gradient step on the smooth part followed by soft-thresholding. Tap the plot to move the start.', 'Cực tiểu hóa ½‖Ax − b‖² + λ‖x‖₁ với hai biến. Mỗi bước là một bước gradient trên phần trơn rồi co ngưỡng mềm. Chạm vào hình để đổi điểm xuất phát.')));
        var sl = slider('λ', 0, 3, 0.05, lam, function (v) { lam = v; cache = null; upd(); }, function (v) { return fmt(v, 2, lang); });
        var st = slider(tx('Step t · L (L = largest eigenvalue of AᵀA)', 'Bước t · L (L = trị riêng lớn nhất của AᵀA)'), 0.1, 2.3, 0.01, tl, function (v) { tl = v; upd(); }, function (v) { return fmt(v, 2, lang); });
        root.appendChild(sl.wrap); root.appendChild(st.wrap);
        var cv = canvas(0.85); root.appendChild(cv.c);
        var sts = el('div', 'opx-stats'), sI = stat(tx('steps', 'số bước')), sN = stat(tx('nonzeros', 'số khác 0')), sS = stat(tx('verdict', 'kết luận')); [sI, sN, sS].forEach(function (q) { sts.appendChild(q.box); }); root.appendChild(sts);
        var msg = msgBox(root), path = [], xs = [0, 0];
        function solution() { var p = istaRun([0, 0], lam, 1 / LL, 4000); return p[p.length - 1]; }
        function bounds() { return { x0: -2.6, x1: 2.6, y0: -2.6, y1: 3.2 }; }
        function drawHeat(ctx) {
            var B = bounds(), N = 56, i, j, fx = [], mn = Infinity;
            V = view(cv, B.x0, B.x1, B.y0, B.y1, 0);
            var fs = lassoF(xs, lam), cw = cv.w / N, ch = cv.h / N;
            for (i = 0; i < N; i++) for (j = 0; j < N; j++) {
                var x = V.ix((i + 0.5) * cw), y = V.iy((j + 0.5) * ch), v = lassoF([x, y], lam) - fs, b = Math.min(7, Math.floor(Math.log(1 + v * 2) * 3));
                ctx.fillStyle = 'hsl(222,' + (38 - b * 2) + '%,' + (24 - b * 2.2) + '%)'; ctx.fillRect(i * cw, j * ch, cw + 0.6, ch + 0.6);
            }
            ctx.strokeStyle = COL.grid; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(0, V.Y(0)); ctx.lineTo(cv.w, V.Y(0)); ctx.moveTo(V.X(0), 0); ctx.lineTo(V.X(0), cv.h); ctx.stroke();
        }
        cv.draw = function () {
            if (!cv.ctx) cv.size(); var ctx = cv.ctx; ctx.clearRect(0, 0, cv.w, cv.h); drawHeat(ctx);
            var pts = path.filter(function (p) { return Math.abs(p[0]) < 5 && Math.abs(p[1]) < 5; });
            line(ctx, pts.map(function (p) { return [V.X(p[0]), V.Y(p[1])]; }), COL.sun, 2);
            pts.forEach(function (p, i) { if (i < 60) dot(ctx, V.X(p[0]), V.Y(p[1]), 2.4, COL.ink); });
            dot(ctx, V.X(P0[0]), V.Y(P0[1]), 6, COL.pink); dot(ctx, V.X(xs[0]), V.Y(xs[1]), 5, COL.mint); txt(ctx, 'x*', V.X(xs[0]) + 7, V.Y(xs[1]) - 6, COL.mint);
            txt(ctx, 'x₁', cv.w - 18, V.Y(0) - 5, COL.dim); txt(ctx, 'x₂', V.X(0) + 5, 12, COL.dim);
        };
        pointer(cv, function (px, py) { if (!V) return; var x = V.ix(px), y = V.iy(py); if (Math.abs(x) > 2.5 || y > 3.1 || y < -2.5) return; P0 = [x, y]; upd(); });
        function upd() {
            xs = solution(); path = istaRun(P0, lam, tl / LL, 300);
            var last = path[path.length - 1], it = path.length - 1, status = 'slow', k;
            var dist = function (p) { return Math.hypot(p[0] - xs[0], p[1] - xs[1]); };
            if (!isFinite(last[0]) || Math.abs(last[0]) > 1e5 || Math.abs(last[1]) > 1e5) status = 'diverged';
            else { for (k = 0; k < path.length; k++) { if (dist(path[k]) < 1e-6) { status = 'converged'; it = k; break; } } }
            if (status !== 'converged' && tl > 2) status = 'diverged';
            var nnz = (Math.abs(last[0]) > 1e-9 ? 1 : 0) + (Math.abs(last[1]) > 1e-9 ? 1 : 0);
            sI.set(status === 'diverged' ? '∞' : (status === 'slow' ? '> 300' : String(it))); sN.set(String(nnz));
            sS.set(status === 'converged' ? tx('converges', 'hội tụ') : status === 'diverged' ? tx('no convergence', 'không hội tụ') : tx('slow', 'chậm'));
            var xn = (Math.abs(xs[0]) > 1e-9 ? 1 : 0) + (Math.abs(xs[1]) > 1e-9 ? 1 : 0);
            msg.set(status === 'diverged' ? tx('With t·L > 2 the gradient step overshoots, and soft-thresholding cannot repair it: the iterates bounce around instead of settling.', 'Khi t·L > 2 bước gradient vượt quá, và co ngưỡng mềm không sửa được: các điểm lặp nảy qua lại thay vì ổn định.')
                : xn === 0 ? tx('λ is large enough that the minimiser is exactly 0: every coordinate is shrunk away.', 'λ đủ lớn nên nghiệm đúng bằng 0: mọi tọa độ đều bị co về 0.')
                : xn === 1 ? tx('The minimiser has an exact zero coordinate: the ℓ₁ term produces sparsity, and ISTA lands on it exactly.', 'Nghiệm có một tọa độ bằng đúng 0: số hạng ℓ₁ tạo ra tính thưa, và ISTA đạt được đúng điểm đó.')
                    : tx('Both coordinates are nonzero here. Increase λ to push one of them to exactly zero.', 'Cả hai tọa độ đều khác 0. Tăng λ để đẩy một tọa độ về đúng 0.'), status === 'diverged' ? 'opx-bad' : 'opx-ok');
            setd(root, { lam: fmt(lam, 2), tl: fmt(tl, 2), iters: status === 'converged' ? it : status, nnz: nnz, status: status, xstar: xs[0].toFixed(4) + ',' + xs[1].toFixed(4), start: P0[0].toFixed(2) + ',' + P0[1].toFixed(2), nnzstar: xn });
            cv.draw();
        }
        after(function () { cv.size(); upd(); });
    }

    /* ---------------- 15-02: central path of a small LP ---------------- */
    var BA = [[-1, 0], [0, -1], [1, 1], [1, 0], [0, 1]], BB = [-0.2, -0.2, 4, 3, 2.6], BC = [-1, -0.7], BPSTAR = -3.7;
    function bPhi(x, t) { var v = t * (BC[0] * x[0] + BC[1] * x[1]); for (var i = 0; i < 5; i++) { var s = BB[i] - BA[i][0] * x[0] - BA[i][1] * x[1]; if (s <= 0) return Infinity; v -= Math.log(s); } return v; }
    function bCenter(t, x0, tol) {
        var x = x0.slice(), steps = 0;
        for (var it = 0; it < 80; it++) {
            var g = [t * BC[0], t * BC[1]], H = [[0, 0], [0, 0]];
            for (var i = 0; i < 5; i++) { var s = BB[i] - BA[i][0] * x[0] - BA[i][1] * x[1], q = 1 / s; g[0] += q * BA[i][0]; g[1] += q * BA[i][1]; for (var a = 0; a < 2; a++) for (var b = 0; b < 2; b++) H[a][b] += q * q * BA[i][a] * BA[i][b]; }
            var det = H[0][0] * H[1][1] - H[0][1] * H[1][0], d = [-(H[1][1] * g[0] - H[0][1] * g[1]) / det, -(-H[1][0] * g[0] + H[0][0] * g[1]) / det];
            var dec = -(g[0] * d[0] + g[1] * d[1]);
            if (dec / 2 < (tol || 1e-10)) break;
            var s2 = 1, f0 = bPhi(x, t); while (bPhi([x[0] + s2 * d[0], x[1] + s2 * d[1]], t) > f0 - 0.25 * s2 * dec) s2 *= 0.5;
            x = [x[0] + s2 * d[0], x[1] + s2 * d[1]]; steps++;
        }
        return { x: x, steps: steps };
    }
    function initBarrier(root, t, lang) {
        var tx = U(lang), lt = 0.5, V = null, X0 = [1.5, 1.0];
        shell(root, tx('Central path of a linear program', 'Đường trung tâm của một bài quy hoạch tuyến tính'));
        root.appendChild(el('p', 'opx-note', tx('Maximise x₁ + 0.7x₂ over the polygon (five inequalities, so m = 5). For each t the barrier problem min t·cᵀx − Σ log(bᵢ − aᵢᵀx) has one solution x*(t). Slide t and watch it travel to the optimal vertex.', 'Cực đại hóa x₁ + 0.7x₂ trên đa giác (năm bất đẳng thức, nên m = 5). Với mỗi t, bài toán rào cản min t·cᵀx − Σ log(bᵢ − aᵢᵀx) có một nghiệm x*(t). Kéo t để thấy nó đi tới đỉnh tối ưu.')));
        var sl = slider(tx('t (log scale)', 't (thang log)'), -0.5, 3.3, 0.01, lt, function (v) { lt = v; upd(); }, function (v) { return fmt(Math.pow(10, v), v < 1 ? 2 : 1, lang); });
        root.appendChild(sl.wrap);
        var cv = canvas(0.8); root.appendChild(cv.c);
        var sts = el('div', 'opx-stats'), sG = stat(tx('actual gap', 'khoảng cách thật')), sB = stat(tx('bound m/t', 'cận m/t')), sN = stat(tx('Newton steps', 'bước Newton')); [sG, sB, sN].forEach(function (q) { sts.appendChild(q.box); }); root.appendChild(sts);
        var msg = msgBox(root), pathPts = [], cur = null;
        (function () { var x = [1.5, 1.0]; for (var k = -10; k <= 36; k++) { var tt = Math.pow(10, k / 10 - 0.0 * 1), r = bCenter(tt, x, 1e-12); x = r.x; pathPts.push([tt, x.slice()]); } })();
        function bounds() { return { x0: -0.1, x1: 3.5, y0: -0.1, y1: 3.0 }; }
        cv.draw = function () {
            if (!cv.ctx) cv.size(); var ctx = cv.ctx, B = bounds(); ctx.clearRect(0, 0, cv.w, cv.h); V = view(cv, B.x0, B.x1, B.y0, B.y1, 10);
            var poly = [[0.2, 0.2], [3, 0.2], [3, 1], [1.4, 2.6], [0.2, 2.6]];
            ctx.beginPath(); poly.forEach(function (p, i) { if (i) ctx.lineTo(V.X(p[0]), V.Y(p[1])); else ctx.moveTo(V.X(p[0]), V.Y(p[1])); }); ctx.closePath(); ctx.fillStyle = '#1d2540'; ctx.fill(); ctx.strokeStyle = COL.sky; ctx.lineWidth = 2; ctx.stroke();
            var pts = pathPts.filter(function (p) { return p[0] <= Math.pow(10, lt) * 1.0001; }).map(function (p) { return [V.X(p[1][0]), V.Y(p[1][1])]; });
            var all = pathPts.map(function (p) { return [V.X(p[1][0]), V.Y(p[1][1])]; }); line(ctx, all, '#46507a', 1.5, [4, 4]); line(ctx, pts, COL.sun, 2.5);
            dot(ctx, V.X(3), V.Y(1), 5, COL.mint); txt(ctx, tx('optimal vertex', 'đỉnh tối ưu'), V.X(3) - 6, V.Y(1) + 16, COL.mint, 'right');
            dot(ctx, V.X(pathPts[0][1][0]), V.Y(pathPts[0][1][1]), 3.5, COL.dim);
            if (cur) { dot(ctx, V.X(cur.x[0]), V.Y(cur.x[1]), 7, COL.pink); txt(ctx, 'x*(t)', V.X(cur.x[0]) + 9, V.Y(cur.x[1]) - 7, COL.pink); }
            var L = 0.7; ctx.strokeStyle = COL.ora; ctx.lineWidth = 2.5; ctx.beginPath(); ctx.moveTo(V.X(0.4), V.Y(1.9)); ctx.lineTo(V.X(0.4 + L * 0.82), V.Y(1.9 + L * 0.57)); ctx.stroke(); txt(ctx, tx('increase x₁ + 0.7x₂', 'tăng x₁ + 0.7x₂'), V.X(0.4), V.Y(1.9) + 16, COL.ora);
        };
        function upd() {
            var tt = Math.pow(10, lt), r = bCenter(tt, X0, 1e-12), prev = bCenter(tt / 10, X0, 1e-12).x, warm = bCenter(tt, prev, 1e-9);
            cur = r; var val = BC[0] * r.x[0] + BC[1] * r.x[1], gap = val - BPSTAR;
            sG.set(gap.toExponential(1)); sB.set((5 / tt).toExponential(1)); sN.set(String(warm.steps));
            msg.set(tt < 10 ? tx('Small t: the barrier dominates, so x*(t) stays near the middle of the polygon.', 't nhỏ: rào cản chiếm ưu thế nên x*(t) ở gần giữa đa giác.')
                : tx('Large t: the objective dominates and x*(t) hugs the optimal vertex. The actual gap never exceeds m/t. "Newton steps" counts the steps needed to re-centre after raising t tenfold.', 't lớn: hàm mục tiêu chiếm ưu thế và x*(t) áp sát đỉnh tối ưu. Khoảng cách thật không bao giờ vượt m/t. "Bước Newton" là số bước để định tâm lại sau khi tăng t lên mười lần.'), 'opx-ok');
            setd(root, { t: tt.toFixed(3), x1: r.x[0].toFixed(5), x2: r.x[1].toFixed(5), gap: gap.toExponential(4), bound: (5 / tt).toExponential(4), newton: warm.steps });
            cv.draw();
        }
        after(function () { cv.size(); upd(); });
    }

    /* ---------------- 22-02: Frank-Wolfe on a triangle ---------------- */
    var FV = [[-1.6, -1.0], [1.7, -0.9], [0.1, 1.8]];
    function projSeg(p, a, b) { var dx = b[0] - a[0], dy = b[1] - a[1], u = Math.max(0, Math.min(1, ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / (dx * dx + dy * dy))); return [a[0] + u * dx, a[1] + u * dy]; }
    function inTri(p) { var s = 0; for (var i = 0; i < 3; i++) { var a = FV[i], b = FV[(i + 1) % 3], c = (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0]); if (c < -1e-12) return false; } return true; }
    function projTri(p) { if (inTri(p)) return p.slice(); var best = null, bd = Infinity; for (var i = 0; i < 3; i++) { var q = projSeg(p, FV[i], FV[(i + 1) % 3]), d = (q[0] - p[0]) * (q[0] - p[0]) + (q[1] - p[1]) * (q[1] - p[1]); if (d < bd) { bd = d; best = q; } } return best; }
    function fwRun(p, n) {
        var x = FV[0].slice(), out = [{ x: x.slice(), s: -1, gap: NaN }];
        for (var k = 0; k < n; k++) {
            var g = [x[0] - p[0], x[1] - p[1]], bi = 0, bv = Infinity; for (var i = 0; i < 3; i++) { var v = g[0] * FV[i][0] + g[1] * FV[i][1]; if (v < bv) { bv = v; bi = i; } }
            var gap = g[0] * x[0] + g[1] * x[1] - bv, gm = 2 / (k + 2); out[out.length - 1].s = bi; out[out.length - 1].gap = gap;
            x = [(1 - gm) * x[0] + gm * FV[bi][0], (1 - gm) * x[1] + gm * FV[bi][1]]; out.push({ x: x.slice(), s: -1, gap: NaN });
        }
        var g2 = [x[0] - p[0], x[1] - p[1]], bv2 = Infinity, bi2 = 0; for (var j = 0; j < 3; j++) { var w = g2[0] * FV[j][0] + g2[1] * FV[j][1]; if (w < bv2) { bv2 = w; bi2 = j; } } out[out.length - 1].s = bi2; out[out.length - 1].gap = g2[0] * x[0] + g2[1] * x[1] - bv2;
        return out;
    }
    function initFW(root, t, lang) {
        var tx = U(lang), P = [2.1, 1.0], K = 0, MAXK = 40, V = null, play = null;
        shell(root, tx('Frank-Wolfe on a triangle', 'Frank-Wolfe trên một tam giác'));
        root.appendChild(el('p', 'opx-note', tx('Minimise f(x) = ½‖x − p‖² over the triangle. Each step moves toward the vertex that minimises the linear model, never leaving the set and never projecting. Tap the plot to move p.', 'Cực tiểu hóa f(x) = ½‖x − p‖² trên tam giác. Mỗi bước đi về phía đỉnh làm cực tiểu mô hình tuyến tính, không bao giờ rời tập và không cần chiếu. Chạm vào hình để đổi p.')));
        var sl = slider(tx('Iteration k', 'Bước lặp k'), 0, MAXK, 1, K, function (v) { K = v; upd(); }, function (v) { return String(v); });
        var rr = row(), pb = btn(tx('▶ Play', '▶ Chạy'), '', function () { if (play) { stop(); return; } if (K >= MAXK) K = 0; pb.textContent = tx('■ Stop', '■ Dừng'); play = setInterval(function () { K++; if (K >= MAXK) stop(); sl.set(K); upd(); }, 220); });
        function stop() { clearInterval(play); play = null; pb.textContent = tx('▶ Play', '▶ Chạy'); }
        rr.appendChild(pb); rr.appendChild(btn(tx('Reset', 'Đặt lại'), '', function () { stop(); K = 0; sl.set(0); upd(); }));
        root.appendChild(sl.wrap); root.appendChild(rr);
        var cv = canvas(0.85); root.appendChild(cv.c);
        var sts = el('div', 'opx-stats'), sF = stat(tx('f − f*', 'f − f*')), sG = stat(tx('FW gap', 'khoảng cách FW')), sV = stat(tx('vertex', 'đỉnh')); [sF, sG, sV].forEach(function (q) { sts.appendChild(q.box); }); root.appendChild(sts);
        var msg = msgBox(root), R = null, xs = null;
        function f(x) { return 0.5 * ((x[0] - P[0]) * (x[0] - P[0]) + (x[1] - P[1]) * (x[1] - P[1])); }
        cv.draw = function () {
            if (!cv.ctx) cv.size(); var ctx = cv.ctx; ctx.clearRect(0, 0, cv.w, cv.h); V = view(cv, -2.8, 3.2, -2.2, 2.6, 8);
            ctx.beginPath(); FV.forEach(function (p, i) { if (i) ctx.lineTo(V.X(p[0]), V.Y(p[1])); else ctx.moveTo(V.X(p[0]), V.Y(p[1])); }); ctx.closePath(); ctx.fillStyle = '#1d2540'; ctx.fill(); ctx.strokeStyle = COL.sky; ctx.lineWidth = 2; ctx.stroke();
            [0.5, 1.5, 3].forEach(function (r) { ctx.strokeStyle = '#2f3a5e'; ctx.lineWidth = 1; ctx.beginPath(); ctx.arc(V.X(P[0]), V.Y(P[1]), r * (V.X(1) - V.X(0)), 0, 2 * PI); ctx.stroke(); });
            var pts = R.slice(0, K + 1).map(function (r) { return [V.X(r.x[0]), V.Y(r.x[1])]; }); line(ctx, pts, COL.sun, 2);
            pts.forEach(function (p, i) { dot(ctx, p[0], p[1], i === K ? 5 : 2.4, i === K ? COL.pink : COL.ink); });
            FV.forEach(function (v, i) { dot(ctx, V.X(v[0]), V.Y(v[1]), R[K].s === i ? 8 : 4.5, R[K].s === i ? COL.mint : COL.sky); });
            var cx = R[K].x, s = FV[R[K].s]; line(ctx, [[V.X(cx[0]), V.Y(cx[1])], [V.X(s[0]), V.Y(s[1])]], COL.mint, 1.5, [5, 4]);
            dot(ctx, V.X(P[0]), V.Y(P[1]), 6, COL.ora); txt(ctx, 'p', V.X(P[0]) + 8, V.Y(P[1]) - 6, COL.ora);
            dot(ctx, V.X(xs[0]), V.Y(xs[1]), 3.5, COL.mint); txt(ctx, 'x*', V.X(xs[0]) + 6, V.Y(xs[1]) + 14, COL.mint);
        };
        pointer(cv, function (px, py) { if (!V) return; var x = V.ix(px), y = V.iy(py); if (x < -2.7 || x > 3.1 || y < -2.1 || y > 2.5) return; P = [x, y]; upd(); });
        function upd() {
            R = fwRun(P, MAXK); xs = projTri(P); var r = R[K], fg = f(r.x) - f(xs);
            sF.set(fg.toExponential(1)); sG.set(r.gap.toExponential(1)); sV.set(String(r.s + 1));
            var inside = inTri(P);
            msg.set(inside ? tx('p is inside the triangle, so f* = 0 and the iterates close in on p, zig-zagging between vertices.', 'p nằm trong tam giác nên f* = 0 và các điểm lặp tiến gần p, zig-zag giữa các đỉnh.')
                : tx('p is outside: the minimiser x* is the projection of p onto the triangle, and the iterates are always inside the triangle.', 'p nằm ngoài: nghiệm x* là hình chiếu của p lên tam giác, và các điểm lặp luôn nằm trong tam giác.'), 'opx-ok');
            setd(root, { p: P[0].toFixed(2) + ',' + P[1].toFixed(2), k: K, fgap: fg.toExponential(4), gap: r.gap.toExponential(4), vertex: r.s + 1, inside: inside ? 1 : 0, x: r.x[0].toFixed(4) + ',' + r.x[1].toFixed(4) });
            cv.draw();
        }
        after(function () { cv.size(); upd(); });
    }

    /* ================= wave 3 helpers ================= */
    function heat(cv, V, fn, fs, N) {
        var ctx = cv.ctx, cw = cv.w / N, ch = cv.h / N, i, j;
        for (i = 0; i < N; i++) for (j = 0; j < N; j++) {
            var v = fn(V.ix((i + 0.5) * cw), V.iy((j + 0.5) * ch)) - fs, b = Math.min(7, Math.floor(Math.log(1 + Math.max(v, 0) * 2) * 3));
            ctx.fillStyle = 'hsl(222,' + (38 - b * 2) + '%,' + (24 - b * 2.2) + '%)'; ctx.fillRect(i * cw, j * ch, cw + 0.6, ch + 0.6);
        }
    }
    function axes0(ctx, cv, V, x0, x1, y0, y1) { ctx.strokeStyle = COL.grid; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(V.X(x0), V.Y(0)); ctx.lineTo(V.X(x1), V.Y(0)); ctx.moveTo(V.X(0), V.Y(y0)); ctx.lineTo(V.X(0), V.Y(y1)); ctx.stroke(); }
    function stats3(root, arr) { var sts = el('div', 'opx-stats'), o = arr.map(function (l) { var s = stat(l); sts.appendChild(s.box); return s; }); root.appendChild(sts); return o; }
    function sgn(v) { return v > 0 ? 1 : v < 0 ? -1 : 0; }

    /* ---------- 08-01-06: subgradient step-size rules on f = |x1-1| + 2|x2+0.5| ---------- */
    function sgmF(x) { return Math.abs(x[0] - 1) + 2 * Math.abs(x[1] + 0.5); }
    function sgmRun(rule, a, n, x0) {
        var x = x0.slice(), best = sgmF(x), fb = [best], xb = x.slice();
        for (var k = 0; k < n; k++) {
            var g = [sgn(x[0] - 1), 2 * sgn(x[1] + 0.5)], gg = g[0] * g[0] + g[1] * g[1]; if (gg === 0) { fb.push(best); continue; }
            var st = rule === 'const' ? a : rule === 'dim' ? a / (k + 1) : (sgmF(x) - 0) / gg;
            x = [x[0] - st * g[0], x[1] - st * g[1]]; var v = sgmF(x); if (v < best) { best = v; xb = x.slice(); } fb.push(best);
        }
        return fb;
    }
    function initSGM(root, t, lang) {
        var tx = U(lang), a = 0.3, K = 60, X0 = [-2.3, 1.7];
        shell(root, tx('Three step-size rules for the subgradient method', 'Ba quy tắc kích thước bước cho phương pháp subgradient'));
        root.appendChild(el('p', 'opx-note', tx('f(x) = |x₁ − 1| + 2|x₂ + ½|, so f* = 0. The plot shows the best value so far, f_best, for a constant step, a diminishing step a/(k+1), and the Polyak step (f(x) − f*)/‖g‖².', 'f(x) = |x₁ − 1| + 2|x₂ + ½| nên f* = 0. Hình vẽ giá trị tốt nhất cho tới nay f_best với bước cố định, bước giảm dần a/(k+1), và bước Polyak (f(x) − f*)/‖g‖².')));
        var sa = slider(tx('Step constant a', 'Hằng số bước a'), 0.02, 1.0, 0.01, a, function (v) { a = v; upd(); }, function (v) { return fmt(v, 2, lang); });
        var sk = slider(tx('Iterations', 'Số bước lặp'), 10, 200, 1, K, function (v) { K = v; upd(); }, function (v) { return String(v); });
        root.appendChild(sa.wrap); root.appendChild(sk.wrap);
        var cv = canvas(0.7); root.appendChild(cv.c);
        var S = stats3(root, [tx('constant', 'cố định'), tx('diminishing', 'giảm dần'), 'Polyak']), msg = msgBox(root), R = {};
        cv.draw = function () {
            if (!cv.ctx) cv.size(); var ctx = cv.ctx, W = cv.w, H = cv.h, i; ctx.clearRect(0, 0, W, H);
            var V = view(cv, 0, K, -12, 1.5, 26); ctx.strokeStyle = COL.grid; ctx.lineWidth = 1; for (i = -12; i <= 0; i += 3) { ctx.beginPath(); ctx.moveTo(V.X(0), V.Y(i)); ctx.lineTo(V.X(K), V.Y(i)); ctx.stroke(); txt(ctx, '1e' + i, 2, V.Y(i) - 3, COL.dim); }
            [['const', COL.sun], ['dim', COL.sky], ['pol', COL.mint]].forEach(function (c) { var fb = R[c[0]], pts = []; fb.forEach(function (v, k) { pts.push([V.X(k), V.Y(Math.max(Math.log10(Math.max(v, 1e-12)), -12))]); }); line(ctx, pts, c[1], 2.5); });
            txt(ctx, 'k', W - 12, V.Y(-12) - 4, COL.dim); txt(ctx, 'log₁₀ f_best', 30, 12, COL.dim);
        };
        function upd() {
            R = { const: sgmRun('const', a, K, X0), dim: sgmRun('dim', a, K, X0), pol: sgmRun('pol', a, K, X0) };
            var e = function (k) { var v = R[k][K]; return v < 1e-12 ? '< 1e-12' : v.toExponential(1); };
            S[0].set(e('const')); S[1].set(e('dim')); S[2].set(e('pol'));
            msg.set(tx('A constant step stalls at a floor set by its size, a diminishing step creeps down slowly, and the Polyak step uses f* to land on the minimiser. It needs f*, which is rarely known.', 'Bước cố định bị kẹt ở một mức phụ thuộc vào độ lớn của nó, bước giảm dần đi xuống chậm, còn bước Polyak dùng f* để rơi đúng vào điểm cực tiểu. Nó cần f*, điều hiếm khi biết trước.'), 'opx-ok');
            setd(root, { a: fmt(a, 2), k: K, fconst: R.const[K].toExponential(6), fdim: R.dim[K].toExponential(6), fpolyak: R.pol[K].toExponential(6) });
            cv.draw();
        }
        after(function () { cv.size(); upd(); });
    }

    /* ---------- 10-05: matrix game ---------- */
    var MP = [[2, 0, -1], [-3, 1, 2]];
    function initMG(root, t, lang) {
        var tx = U(lang), x1 = 0.3, y1 = 0.3, view2 = 'J';
        shell(root, tx('A matrix game, seen from both sides', 'Một trò chơi ma trận nhìn từ cả hai phía'));
        root.appendChild(el('p', 'opx-note', tx('Payout matrix P = [[2, 0, −1], [−3, 1, 2]]: J picks a row, R picks a column, J pays R the entry. J mixes the rows with probability x₁, 1 − x₁.', 'Ma trận chi trả P = [[2, 0, −1], [−3, 1, 2]]: J chọn hàng, R chọn cột, J trả cho R giá trị của ô. J trộn hai hàng với xác suất x₁, 1 − x₁.')));
        var rr = row(), bJ = btn(tx("J's view", 'Góc nhìn của J'), 'on', function () { view2 = 'J'; upd(); }), bR = btn(tx("R's view", 'Góc nhìn của R'), '', function () { view2 = 'R'; upd(); }); rr.appendChild(bJ); rr.appendChild(bR); root.appendChild(rr);
        var sx = slider('x₁ (J)', 0, 1, 0.005, x1, function (v) { x1 = v; upd(); }, function (v) { return fmt(v, 3, lang); });
        var sy = slider(tx('y₁ (R mixes columns 1 and 2)', 'y₁ (R trộn cột 1 và 2)'), 0, 1, 0.005, y1, function (v) { y1 = v; upd(); }, function (v) { return fmt(v, 3, lang); });
        root.appendChild(sx.wrap); root.appendChild(sy.wrap);
        var cv = canvas(0.75); root.appendChild(cv.c);
        var S = stats3(root, [tx('guarantee', 'đảm bảo'), tx('best reply', 'phản ứng tốt nhất'), tx('game value', 'giá trị trò chơi')]), msg = msgBox(root), cur = {};
        function colv(j, x) { return MP[0][j] * x + MP[1][j] * (1 - x); }
        function rowv(i, y) { return MP[i][0] * y + MP[i][1] * (1 - y); }
        cv.draw = function () {
            if (!cv.ctx) cv.size(); var ctx = cv.ctx, W = cv.w, H = cv.h; ctx.clearRect(0, 0, W, H);
            var V = view(cv, 0, 1, -3.4, 2.4, 24), cols = [COL.sky, COL.ora, COL.pink], i, j;
            ctx.strokeStyle = COL.grid; ctx.beginPath(); ctx.moveTo(V.X(0), V.Y(0)); ctx.lineTo(V.X(1), V.Y(0)); ctx.stroke();
            if (view2 === 'J') {
                for (j = 0; j < 3; j++) { line(ctx, [[V.X(0), V.Y(colv(j, 0))], [V.X(1), V.Y(colv(j, 1))]], cols[j], 1.5, [4, 4]); txt(ctx, tx('col ', 'cột ') + (j + 1), V.X(1) - 4, V.Y(colv(j, 1)) + (j === 1 ? 14 : -4), cols[j], 'right'); }
                var env = []; for (i = 0; i <= 100; i++) { var x = i / 100; env.push([V.X(x), V.Y(Math.max(colv(0, x), colv(1, x), colv(2, x)))]); } line(ctx, env, COL.sun, 4);
                var m = Math.max(colv(0, x1), colv(1, x1), colv(2, x1)); dot(ctx, V.X(x1), V.Y(m), 6, COL.pink); dot(ctx, V.X(2 / 3), V.Y(1 / 3), 4, COL.mint); txt(ctx, 'x₁ = 2/3', V.X(2 / 3), V.Y(1 / 3) + 16, COL.mint, 'center'); txt(ctx, 'x₁', W - 14, V.Y(0) - 4, COL.dim);
            } else {
                for (i = 0; i < 2; i++) { line(ctx, [[V.X(0), V.Y(rowv(i, 0))], [V.X(1), V.Y(rowv(i, 1))]], cols[i], 1.5, [4, 4]); txt(ctx, tx('row ', 'hàng ') + (i + 1), V.X(0) + 4, V.Y(rowv(i, 0)) + (i ? 14 : -4), cols[i]); }
                var lo = []; for (i = 0; i <= 100; i++) { var y = i / 100; lo.push([V.X(y), V.Y(Math.min(rowv(0, y), rowv(1, y)))]); } line(ctx, lo, COL.sun, 4);
                var m2 = Math.min(rowv(0, y1), rowv(1, y1)); dot(ctx, V.X(y1), V.Y(m2), 6, COL.pink); dot(ctx, V.X(1 / 6), V.Y(1 / 3), 4, COL.mint); txt(ctx, 'y₁ = 1/6', V.X(1 / 6) + 8, V.Y(1 / 3) - 8, COL.mint); txt(ctx, 'y₁', W - 14, V.Y(0) - 4, COL.dim);
            }
        };
        function upd() {
            bJ.className = view2 === 'J' ? 'on' : ''; bR.className = view2 === 'R' ? 'on' : ''; sx.input.disabled = view2 !== 'J'; sy.input.disabled = view2 !== 'R';
            if (view2 === 'J') { var v = [colv(0, x1), colv(1, x1), colv(2, x1)], m = Math.max.apply(null, v); S[0].set(fmt(m, 3, lang)); S[1].set(tx('column ', 'cột ') + (v.indexOf(m) + 1)); cur = { v: m, who: 'J', best: v.indexOf(m) + 1 }; }
            else { var w = [rowv(0, y1), rowv(1, y1)], mm = Math.min(w[0], w[1]); S[0].set(fmt(mm, 3, lang)); S[1].set(tx('row ', 'hàng ') + (w.indexOf(mm) + 1)); cur = { v: mm, who: 'R', best: w.indexOf(mm) + 1 }; }
            S[2].set('1/3');
            msg.set(view2 === 'J' ? tx('J wants the lowest point of the gold curve: the largest payout R can force. It is lowest at x₁ = 2/3, where it equals 1/3.', 'J muốn điểm thấp nhất của đường vàng: khoản chi trả lớn nhất mà R có thể ép được. Nó thấp nhất tại x₁ = 2/3, bằng 1/3.')
                : tx('R wants the highest point of the gold curve: the smallest payout J can force. It is highest at y₁ = 1/6, where it equals 1/3. The two views meet: the minimax theorem.', 'R muốn điểm cao nhất của đường vàng: khoản chi trả nhỏ nhất mà J có thể ép được. Nó cao nhất tại y₁ = 1/6, bằng 1/3. Hai góc nhìn gặp nhau: định lý minimax.'), 'opx-ok');
            setd(root, { view: view2, x1: fmt(x1, 4), y1: fmt(y1, 4), value: cur.v.toFixed(5), best: cur.best });
            cv.draw();
        }
        after(function () { cv.size(); upd(); });
    }

    /* ---------- 11-03: Lagrange dual function of min (x-2)^2 s.t. x <= 1/2 ---------- */
    function initD1(root, t, lang) {
        var tx = U(lang), lam = 1;
        shell(root, tx('The dual function is a lower bound', 'Hàm đối ngẫu là một cận dưới'));
        root.appendChild(el('p', 'opx-note', tx('Minimise f₀(x) = (x − 2)² subject to x ≤ ½. For each λ ≥ 0 the Lagrangian L(x, λ) = f₀(x) + λ(x − ½) is a parabola; its lowest point is g(λ). Slide λ.', 'Cực tiểu hóa f₀(x) = (x − 2)² với x ≤ ½. Với mỗi λ ≥ 0, hàm Lagrange L(x, λ) = f₀(x) + λ(x − ½) là một parabol; điểm thấp nhất của nó là g(λ). Kéo λ.')));
        var sl = slider('λ', 0, 6, 0.01, lam, function (v) { lam = v; upd(); }, function (v) { return fmt(v, 2, lang); }); root.appendChild(sl.wrap);
        var cv = canvas(0.6), cv2 = canvas(0.45); root.appendChild(cv.c); root.appendChild(cv2.c);
        var S = stats3(root, ['g(λ)', 'p*', tx('gap p* − g', 'khoảng cách p* − g')]), msg = msgBox(root);
        var P = 2.25, g = function (l) { return 1.5 * l - l * l / 4; };
        cv.draw = function () {
            if (!cv.ctx) cv.size(); var ctx = cv.ctx; ctx.clearRect(0, 0, cv.w, cv.h); var V = view(cv, -1, 4, -1, 9, 12), i, pts = [];
            ctx.fillStyle = 'rgba(128,237,153,0.10)'; ctx.fillRect(V.X(-1), 0, V.X(0.5) - V.X(-1), cv.h); axes0(ctx, cv, V, -1, 4, -1, 9);
            for (i = 0; i <= 100; i++) { var x = -1 + 5 * i / 100; pts.push([V.X(x), V.Y((x - 2) * (x - 2))]); } line(ctx, pts, COL.dim, 2, [5, 4]);
            pts = []; for (i = 0; i <= 100; i++) { var x2 = -1 + 5 * i / 100; pts.push([V.X(x2), V.Y((x2 - 2) * (x2 - 2) + lam * (x2 - 0.5))]); } line(ctx, pts, COL.sun, 3);
            var xm = 2 - lam / 2; dot(ctx, V.X(xm), V.Y(g(lam)), 6, COL.pink); line(ctx, [[V.X(-1), V.Y(P)], [V.X(4), V.Y(P)]], COL.mint, 1.5, [3, 4]);
            txt(ctx, 'p* = 2.25', V.X(4) - 4, V.Y(P) - 5, COL.mint, 'right'); txt(ctx, tx('f₀', 'f₀'), V.X(3.6), V.Y(2.6 * 2.6 - 2) , COL.dim); txt(ctx, 'L(x, λ)', V.X(-0.9), 14, COL.sun); txt(ctx, tx('feasible x ≤ ½', 'x khả thi ≤ ½'), V.X(-0.9), cv.h - 8, COL.mint);
        };
        cv2.draw = function () {
            if (!cv2.ctx) cv2.size(); var ctx = cv2.ctx; ctx.clearRect(0, 0, cv2.w, cv2.h); var V = view(cv2, 0, 6, -3, 3, 14), i, pts = []; axes0(ctx, cv2, V, 0, 6, -3, 3);
            for (i = 0; i <= 100; i++) { var l = 6 * i / 100; pts.push([V.X(l), V.Y(g(l))]); } line(ctx, pts, COL.sky, 3); line(ctx, [[V.X(0), V.Y(P)], [V.X(6), V.Y(P)]], COL.mint, 1.5, [3, 4]);
            dot(ctx, V.X(lam), V.Y(g(lam)), 6, COL.pink); txt(ctx, 'g(λ)', V.X(0.1), 14, COL.sky); txt(ctx, 'λ', cv2.w - 14, V.Y(0) - 4, COL.dim);
        };
        function upd() {
            var gv = g(lam); S[0].set(fmt(gv, 3, lang)); S[1].set(fmt(P, 3, lang)); S[2].set(fmt(P - gv, 3, lang));
            msg.set(Math.abs(lam - 3) < 0.04 ? tx('At λ = 3 the bound is tight: g = p*, strong duality, and the minimiser of L sits exactly at the constraint x = ½.', 'Tại λ = 3 cận này khít: g = p*, đối ngẫu mạnh, và điểm cực tiểu của L nằm đúng tại ràng buộc x = ½.')
                : tx('Every λ ≥ 0 gives g(λ) ≤ p* (weak duality). The dual problem looks for the λ with the highest bound.', 'Mọi λ ≥ 0 đều cho g(λ) ≤ p* (đối ngẫu yếu). Bài toán đối ngẫu tìm λ cho cận cao nhất.'), 'opx-ok');
            setd(root, { lam: fmt(lam, 3), g: gv.toFixed(5), p: P, gap: (P - gv).toFixed(5), xmin: (2 - lam / 2).toFixed(4) }); cv.draw(); cv2.draw();
        }
        after(function () { cv.size(); cv2.size(); upd(); });
    }

    /* ---------- 20-02-01: dual decomposition with a price ---------- */
    var DW = [1, 2, 4], DA = [3, 2, 1], DC = 4, DNU = 8 / 7;
    function initDD(root, t, lang) {
        var tx = U(lang), nu = 0, al = 0.5, k = 0, path = [0];
        shell(root, tx('Dual decomposition: a price coordinates three agents', 'Phân rã đối ngẫu: một mức giá điều phối ba tác tử'));
        root.appendChild(el('p', 'opx-note', tx('Agents i = 1, 2, 3 minimise ½wᵢ(xᵢ − aᵢ)² with w = (1, 2, 4), a = (3, 2, 1), but must share Σxᵢ = 4. Given a price ν each agent solves its own problem. Dual ascent moves ν along the constraint violation.', 'Các tác tử i = 1, 2, 3 cực tiểu ½wᵢ(xᵢ − aᵢ)² với w = (1, 2, 4), a = (3, 2, 1), nhưng phải thỏa Σxᵢ = 4. Với mức giá ν, mỗi tác tử tự giải bài của mình. Dual ascent dịch ν theo mức vi phạm ràng buộc.')));
        var sn = slider(tx('Price ν', 'Mức giá ν'), -1, 3, 0.01, nu, function (v) { nu = v; path = [nu]; upd(); }, function (v) { return fmt(v, 2, lang); });
        var sa = slider(tx('Step α', 'Bước α'), 0.1, 1.4, 0.01, al, function (v) { al = v; upd(); }, function (v) { return fmt(v, 2, lang); });
        var rr = row(); rr.appendChild(btn(tx('One ascent step', 'Một bước ascent'), '', function () { nu = nu + al * (res(nu)); sn.set(Math.max(-1, Math.min(3, nu))); path.push(nu); upd(); }));
        rr.appendChild(btn(tx('Run 30 steps', 'Chạy 30 bước'), '', function () { for (var i = 0; i < 30; i++) { nu = nu + al * res(nu); path.push(nu); } sn.set(Math.max(-1, Math.min(3, nu))); upd(); }));
        root.appendChild(sn.wrap); root.appendChild(sa.wrap); root.appendChild(rr);
        var cv = canvas(0.55); root.appendChild(cv.c);
        var S = stats3(root, [tx('Σx − 4', 'Σx − 4'), 'g(ν)', tx('steps taken', 'số bước đã chạy')]), msg = msgBox(root);
        function xs(v) { return DA.map(function (a, i) { return a - v / DW[i]; }); }
        function res(v) { return xs(v).reduce(function (s, q) { return s + q; }, 0) - DC; }
        function g(v) { var x = xs(v); return x.reduce(function (s, q, i) { return s + 0.5 * DW[i] * (q - DA[i]) * (q - DA[i]) + v * q; }, 0) - v * DC; }
        cv.draw = function () {
            if (!cv.ctx) cv.size(); var ctx = cv.ctx; ctx.clearRect(0, 0, cv.w, cv.h); var V = view(cv, -1, 3, 0, 4, 14), i, pts = []; axes0(ctx, cv, V, -1, 3, 0, 4);
            for (i = 0; i <= 100; i++) { var v = -1 + 4 * i / 100; pts.push([V.X(v), V.Y(Math.max(g(v), -2))]); } line(ctx, pts, COL.sky, 3);
            path.slice(-40).forEach(function (p, j) { if (p >= -1 && p <= 3) dot(ctx, V.X(p), V.Y(g(p)), 3, COL.sun); }); dot(ctx, V.X(Math.max(-1, Math.min(3, nu))), V.Y(g(Math.max(-1, Math.min(3, nu)))), 6, COL.pink); dot(ctx, V.X(DNU), V.Y(g(DNU)), 4, COL.mint);
            txt(ctx, 'g(ν)', V.X(-0.9), 14, COL.sky); txt(ctx, 'ν', cv.w - 14, V.Y(0) - 4, COL.dim);
        };
        function upd() {
            var x = xs(nu), r = res(nu), ok = Math.abs(r) < 1e-4;
            var big = function (v) { return Math.abs(v) > 1e4 ? v.toExponential(1) : fmt(v, 3, lang); }; S[0].set(big(r)); S[1].set(big(g(nu))); S[2].set(String(path.length - 1));
            var wild = Math.abs(nu) > 6;
            msg.set(wild ? tx('The price is running away: this step α is too large for dual ascent, which now diverges. Lower α.', 'Mức giá đang chạy mất kiểm soát: bước α này quá lớn đối với dual ascent nên nó phân kỳ. Hãy giảm α.') : ok ? tx('The agents\' demands add up to exactly 4: x = (' + x.map(function (q) { return q.toFixed(3); }).join(', ') + ').', 'Tổng nhu cầu của các tác tử đúng bằng 4: x = (' + x.map(function (q) { return q.toFixed(3).replace('.', ','); }).join('; ') + ').')
                : r > 0 ? tx('Demand exceeds the supply of 4: raise the price.', 'Tổng nhu cầu vượt 4: hãy tăng giá.') : tx('Demand is below 4: lower the price.', 'Tổng nhu cầu thấp hơn 4: hãy giảm giá.'), ok ? 'opx-ok' : 'opx-warn');
            var bad = !isFinite(nu) || Math.abs(nu) > 1e6;
            setd(root, { nu: bad ? 'inf' : nu.toFixed(5), resid: bad ? 'inf' : r.toFixed(6), g: bad ? 'inf' : g(nu).toFixed(5), steps: path.length - 1, al: fmt(al, 2), x: bad ? '' : x.map(function (q) { return q.toFixed(4); }).join(',') }); cv.draw();
        }
        after(function () { cv.size(); upd(); });
    }

    /* ---------- 21-03: ADMM for the 2-D lasso ---------- */
    function admmRun(lam, rho, n) {
        var a = LA[0][0] * LA[0][0] + LA[1][0] * LA[1][0] + rho, b = LA[0][0] * LA[0][1] + LA[1][0] * LA[1][1], d = LA[0][1] * LA[0][1] + LA[1][1] * LA[1][1] + rho, det = a * d - b * b;
        var Atb = [LA[0][0] * LB[0] + LA[1][0] * LB[1], LA[0][1] * LB[0] + LA[1][1] * LB[1]], z = [0, 0], u = [0, 0], xs = [[0, 0]], zs = [[0, 0]], conv = -1;
        for (var k = 1; k <= n; k++) {
            var r = [Atb[0] + rho * (z[0] - u[0]), Atb[1] + rho * (z[1] - u[1])], x = [(d * r[0] - b * r[1]) / det, (-b * r[0] + a * r[1]) / det], zp = z;
            z = [soft(x[0] + u[0], lam / rho), soft(x[1] + u[1], lam / rho)]; u = [u[0] + x[0] - z[0], u[1] + x[1] - z[1]]; xs.push(x); zs.push(z);
            if (conv < 0 && Math.hypot(x[0] - z[0], x[1] - z[1]) < 1e-6 && rho * Math.hypot(z[0] - zp[0], z[1] - zp[1]) < 1e-6) conv = k;
        }
        return { xs: xs, zs: zs, conv: conv };
    }
    function initADMM(root, t, lang) {
        var tx = U(lang), lam = 0.8, rho = 1, K = 8, R, V;
        shell(root, tx('ADMM on a small lasso', 'ADMM trên một bài lasso nhỏ'));
        root.appendChild(el('p', 'opx-note', tx('Same lasso as in chapter 9, split as min ½‖Ax − b‖² + λ‖z‖₁ subject to x = z. The x-update is a ridge solve, the z-update is soft-thresholding, and u collects the disagreement x − z.', 'Cùng bài lasso như chương 9, tách thành min ½‖Ax − b‖² + λ‖z‖₁ với x = z. Bước x là một phép giải ridge, bước z là co ngưỡng mềm, và u tích lũy sự bất đồng x − z.')));
        var sl = slider('λ', 0, 3, 0.05, lam, function (v) { lam = v; upd(); }, function (v) { return fmt(v, 2, lang); }), sr = slider('ρ', 0.1, 10, 0.05, rho, function (v) { rho = v; upd(); }, function (v) { return fmt(v, 2, lang); }), sk = slider(tx('Iteration k', 'Bước lặp k'), 0, 60, 1, K, function (v) { K = v; upd(); }, function (v) { return String(v); });
        root.appendChild(sl.wrap); root.appendChild(sr.wrap); root.appendChild(sk.wrap);
        var cv = canvas(0.8); root.appendChild(cv.c);
        var S = stats3(root, [tx('steps to converge', 'bước để hội tụ'), '‖x − z‖', tx('nonzeros in z', 'số khác 0 của z')]), msg = msgBox(root);
        cv.draw = function () {
            if (!cv.ctx) cv.size(); var ctx = cv.ctx; ctx.clearRect(0, 0, cv.w, cv.h); V = view(cv, -0.6, 2.6, -1.0, 1.9, 0); var xs = R.zs[R.zs.length - 1];
            heat(cv, V, function (x, y) { return lassoF([x, y], lam); }, lassoF(R.zs[60], lam), 50); axes0(ctx, cv, V, -0.6, 2.6, -1, 1.9);
            line(ctx, R.xs.slice(0, K + 1).map(function (p) { return [V.X(p[0]), V.Y(p[1])]; }), COL.sky, 2); line(ctx, R.zs.slice(0, K + 1).map(function (p) { return [V.X(p[0]), V.Y(p[1])]; }), COL.pink, 2);
            dot(ctx, V.X(R.xs[K][0]), V.Y(R.xs[K][1]), 5, COL.sky); dot(ctx, V.X(R.zs[K][0]), V.Y(R.zs[K][1]), 5, COL.pink); dot(ctx, V.X(R.zs[60][0]), V.Y(R.zs[60][1]), 3.5, COL.mint);
            txt(ctx, 'x_k', 8, 14, COL.sky); txt(ctx, 'z_k', 40, 14, COL.pink); txt(ctx, 'x₁', cv.w - 18, V.Y(0) - 5, COL.dim);
        };
        function upd() {
            R = admmRun(lam, rho, 400); var dx = Math.hypot(R.xs[K][0] - R.zs[K][0], R.xs[K][1] - R.zs[K][1]), nz = (Math.abs(R.zs[K][0]) > 1e-9 ? 1 : 0) + (Math.abs(R.zs[K][1]) > 1e-9 ? 1 : 0);
            S[0].set(R.conv < 0 ? '> 400' : String(R.conv)); S[1].set(dx.toExponential(1)); S[2].set(String(nz));
            msg.set(tx('x (blue) and z (pink) start apart and are pulled together by u. A very small or very large ρ slows ADMM down; moderate ρ is fastest.', 'x (xanh) và z (hồng) bắt đầu cách xa nhau và được u kéo lại gần nhau. ρ quá nhỏ hoặc quá lớn đều làm ADMM chậm; ρ vừa phải là nhanh nhất.'), 'opx-ok');
            var zf = R.zs[R.zs.length - 1]; setd(root, { lam: fmt(lam, 2), rho: fmt(rho, 2), k: K, conv: R.conv, zstar: zf[0].toFixed(4) + ',' + zf[1].toFixed(4), gap: dx.toExponential(3) }); cv.draw();
        }
        after(function () { cv.size(); upd(); });
    }

    /* ---------- 19-01-02: proximal gradient vs proximal Newton on lse + lambda*l1 ---------- */
    function pnObj(p, lam) { return F(p) + lam * (Math.abs(p[0]) + Math.abs(p[1])); }
    function pnStep(p, lam, H, g) { // minimise g.d + 1/2 d'Hd + lam|p+d|_1 by coordinate descent
        var d = [0, 0], i, s;
        for (s = 0; s < 200; s++) for (i = 0; i < 2; i++) { var j = 1 - i, hii = i === 0 ? H[0] : H[2], hij = H[1], c = g[i] + hij * d[j], z = p[i] - c / hii; d[i] = soft(z, lam / hii) - p[i]; }
        return d;
    }
    function pnRun(kind, start, lam, maxit) {
        var p = start.slice(), pts = [p.slice()], it = 0, ts = 1;
        while (it < maxit) {
            var fp = pnObj(p, lam); if (fp - PNSTAR(lam) < 1e-10) break;
            var g = G(p), d, pn;
            if (kind === 'newton') { d = pnStep(p, lam, Hs(p), g); var dec = g[0] * d[0] + g[1] * d[1] + lam * (Math.abs(p[0] + d[0]) + Math.abs(p[1] + d[1]) - Math.abs(p[0]) - Math.abs(p[1])), t = 1, k = 0; while (pnObj([p[0] + t * d[0], p[1] + t * d[1]], lam) > fp + 0.1 * t * dec && k < 60) { t *= 0.5; k++; } pn = [p[0] + t * d[0], p[1] + t * d[1]]; }
            else { var t2 = 1, k2 = 0; for (; k2 < 60; k2++) { var q = [soft(p[0] - t2 * g[0], t2 * lam), soft(p[1] - t2 * g[1], t2 * lam)], dq = [q[0] - p[0], q[1] - p[1]]; if (F(q) <= F(p) + g[0] * dq[0] + g[1] * dq[1] + (dq[0] * dq[0] + dq[1] * dq[1]) / (2 * t2)) break; t2 *= 0.5; } pn = q; }
            p = pn; pts.push(p.slice()); it++;
        }
        return { pts: pts, it: it, ok: pnObj(p, lam) - PNSTAR(lam) < 1e-10 };
    }
    var PNC = {}; function PNSTAR(lam) { var key = lam.toFixed(3); if (!(key in PNC)) { var p = [1.0, 0.5]; for (var i = 0; i < 80; i++) { var d = pnStep(p, lam, Hs(p), G(p)), t = 1, fp = pnObj(p, lam), g = G(p), dec = g[0] * d[0] + g[1] * d[1] + lam * (Math.abs(p[0] + d[0]) + Math.abs(p[1] + d[1]) - Math.abs(p[0]) - Math.abs(p[1])), k = 0; while (pnObj([p[0] + t * d[0], p[1] + t * d[1]], lam) > fp + 0.1 * t * dec && k < 60) { t *= 0.5; k++; } p = [p[0] + t * d[0], p[1] + t * d[1]]; } PNC[key] = { f: pnObj(p, lam), p: p }; } return PNC[key].f; }
    function initPN(root, t, lang) {
        var tx = U(lang), lam = 0.1, si = 0, K = 0, STARTS = [[1.6, 1.1], [-2.0, -1.4], [0.6, -2.0]], V, R;
        shell(root, tx('Proximal gradient vs proximal Newton', 'Gradient gần kề so với Newton gần kề'));
        root.appendChild(el('p', 'opx-note', tx('Minimise F(x) = log(e^(x₁+3x₂−0.1) + e^(x₁−3x₂−0.1) + e^(−x₁−0.1)) + λ‖x‖₁. Proximal Newton replaces the quadratic ½t‖·‖² by the true curvature, and solves each subproblem exactly.', 'Cực tiểu hóa F(x) = log(e^(x₁+3x₂−0.1) + e^(x₁−3x₂−0.1) + e^(−x₁−0.1)) + λ‖x‖₁. Newton gần kề thay ½t‖·‖² bằng độ cong thật và giải chính xác từng bài toán con.')));
        var r1 = row(), sb = []; STARTS.forEach(function (p, i) { sb.push(btn(tx('Start ', 'Điểm đầu ') + (i + 1), i === 0 ? 'on' : '', function () { si = i; K = 0; upd(); })); r1.appendChild(sb[i]); }); root.appendChild(r1);
        var sl = slider('λ', 0, 1, 0.01, lam, function (v) { lam = v; K = 0; upd(); }, function (v) { return fmt(v, 2, lang); }), sk = slider(tx('Iteration', 'Bước lặp'), 0, 40, 1, K, function (v) { K = v; upd(); }, function (v) { return String(v); });
        root.appendChild(sl.wrap); root.appendChild(sk.wrap);
        var cv = canvas(0.85); root.appendChild(cv.c);
        var S = stats3(root, [tx('prox-gradient', 'gradient gần kề'), tx('prox-Newton', 'Newton gần kề'), tx('nonzeros at x*', 'số khác 0 tại x*')]), msg = msgBox(root);
        cv.draw = function () {
            if (!cv.ctx) cv.size(); var ctx = cv.ctx; ctx.clearRect(0, 0, cv.w, cv.h); V = view(cv, -2.6, 2.4, -2.6, 2.4, 0); PNSTAR(lam); var xs = PNC[lam.toFixed(3)].p;
            heat(cv, V, function (x, y) { return pnObj([x, y], lam); }, PNC[lam.toFixed(3)].f, 46); axes0(ctx, cv, V, -2.6, 2.4, -2.6, 2.4);
            [['gd', COL.sun], ['nw', COL.mint]].forEach(function (c) { var pts = R[c[0]].pts.slice(0, K + 1); line(ctx, pts.map(function (p) { return [V.X(p[0]), V.Y(p[1])]; }), c[1], 2); pts.forEach(function (p, i) { if (i < 60) dot(ctx, V.X(p[0]), V.Y(p[1]), 2.4, c[1]); }); });
            dot(ctx, V.X(STARTS[si][0]), V.Y(STARTS[si][1]), 5, COL.pink); dot(ctx, V.X(xs[0]), V.Y(xs[1]), 4, COL.ink); txt(ctx, 'x*', V.X(xs[0]) + 6, V.Y(xs[1]) - 6, COL.ink);
        };
        function upd() {
            sb.forEach(function (b, i) { b.className = i === si ? 'on' : ''; }); R = { gd: pnRun('gd', STARTS[si], lam, 300), nw: pnRun('newton', STARTS[si], lam, 60) };
            var xs = (PNSTAR(lam), PNC[lam.toFixed(3)].p), nz = (Math.abs(xs[0]) > 1e-9 ? 1 : 0) + (Math.abs(xs[1]) > 1e-9 ? 1 : 0);
            S[0].set(String(R.gd.it)); S[1].set(String(R.nw.it)); S[2].set(String(nz));
            msg.set(tx('Steps until F − F* < 10⁻¹⁰. Proximal gradient (gold) uses only a scalar step; proximal Newton (green) uses the Hessian, so it aims straight at x*, including the exact zeros.', 'Số bước đến khi F − F* < 10⁻¹⁰. Gradient gần kề (vàng) chỉ dùng bước vô hướng; Newton gần kề (xanh) dùng Hessian nên nhắm thẳng vào x*, kể cả các thành phần bằng 0 đúng.'), 'opx-ok');
            var mx = Math.max(R.gd.it, R.nw.it); sk.input.max = Math.min(60, mx); K = Math.min(K, mx);
            setd(root, { lam: fmt(lam, 2), start: si + 1, gd: R.gd.it, newton: R.nw.it, nnz: nz, fstar: PNC[lam.toFixed(3)].f.toFixed(6), k: K }); cv.draw();
        }
        after(function () { cv.size(); upd(); });
    }

    /* ---------- 17-02-03: primal-dual interior point vs barrier method on the central-path LP ---------- */
    function pdRun(mu) {
        var x = [1.5, 1.0], lam = [1, 1, 1, 1, 1], pts = [x.slice()], it = 0, eps = 1e-6, m = 5;
        function res(x, l, tt) { var rd = [BC[0] + BA.reduce(function (s, a, i) { return s + a[0] * l[i]; }, 0), BC[1] + BA.reduce(function (s, a, i) { return s + a[1] * l[i]; }, 0)], rc = BA.map(function (a, i) { var f = a[0] * x[0] + a[1] * x[1] - BB[i]; return -l[i] * f - 1 / tt; }); return { rd: rd, rc: rc }; }
        var guard = 0;
        while (guard++ < 200) {
            var s = BA.map(function (a, i) { return BB[i] - a[0] * x[0] - a[1] * x[1]; }), eta = s.reduce(function (acc, q, i) { return acc + q * lam[i]; }, 0), tt = mu * m / eta, r = res(x, lam, tt);
            if (Math.hypot(r.rd[0], r.rd[1]) < 1e-9 && eta < eps) break;
            // reduced Newton: dx from  (A' diag(l/s) A) dx = -rd - A' (rc... ) -- eliminate dlam
            var H = [[0, 0], [0, 0]], rhs = [-r.rd[0], -r.rd[1]];
            for (var i = 0; i < m; i++) { var w = lam[i] / s[i]; for (var a = 0; a < 2; a++) for (var b = 0; b < 2; b++) H[a][b] += w * BA[i][a] * BA[i][b]; var q = (r.rc[i]) / s[i]; /* dlam_i = (rc_i... ) */ }
            // dlam_i = -(rc_i + lam_i * a_i.dx * ... ) derived below
            // Newton system: A' dlam = -rd ; -diag(l) A dx - diag(f) dlam = -rc  with f=Ax-b=-s  =>  s_i dlam_i = l_i a_i.dx - rc_i  => dlam_i = (l_i a_i.dx - rc_i)/s_i
            // substitute: sum_i a_i (l_i a_i.dx - rc_i)/s_i = -rd  =>  H dx = -rd + sum a_i rc_i/s_i
            for (i = 0; i < m; i++) { rhs[0] += BA[i][0] * r.rc[i] / s[i]; rhs[1] += BA[i][1] * r.rc[i] / s[i]; }
            var det = H[0][0] * H[1][1] - H[0][1] * H[1][0], dx = [(H[1][1] * rhs[0] - H[0][1] * rhs[1]) / det, (-H[1][0] * rhs[0] + H[0][0] * rhs[1]) / det];
            var dl = BA.map(function (a, i) { return (lam[i] * (a[0] * dx[0] + a[1] * dx[1]) - r.rc[i]) / s[i]; });
            var smax = 1; dl.forEach(function (q, i) { if (q < 0) smax = Math.min(smax, -lam[i] / q); }); var st = 0.99 * smax, nr = Math.hypot(r.rd[0], r.rd[1], Math.hypot.apply(null, r.rc));
            for (var k = 0; k < 60; k++) { var xn = [x[0] + st * dx[0], x[1] + st * dx[1]], ln = lam.map(function (v, j) { return v + st * dl[j]; }); if (BA.every(function (a, j) { return a[0] * xn[0] + a[1] * xn[1] < BB[j]; })) { var r2 = res(xn, ln, tt); if (Math.hypot(r2.rd[0], r2.rd[1], Math.hypot.apply(null, r2.rc)) <= (1 - 0.01 * st) * nr) break; } st *= 0.5; }
            x = [x[0] + st * dx[0], x[1] + st * dx[1]]; lam = lam.map(function (v, j) { return v + st * dl[j]; }); pts.push(x.slice()); it++;
        }
        return { pts: pts, it: it };
    }
    function barRun(mu) {
        var x = [1.5, 1.0], t = 1, pts = [x.slice()], tot = 0, outer = 0;
        while (5 / t > 1e-6 && outer < 60) { var r = bCenter(t, x, 1e-10); x = r.x; tot += r.steps; pts.push(x.slice()); t *= mu; outer++; }
        return { pts: pts, it: tot };
    }
    function initPDIPM(root, t, lang) {
        var tx = U(lang), lmu = 1, V, A, B;
        shell(root, tx('Primal-dual interior point vs barrier', 'Điểm trong gốc - đối ngẫu so với phương pháp rào cản'));
        root.appendChild(el('p', 'opx-note', tx('The same LP as in 15-02. The barrier method re-centres exactly after every increase of t. The primal-dual method takes one damped Newton step on the perturbed KKT system, moving x and λ together.', 'Cùng bài LP như ở 15-02. Phương pháp rào cản định tâm chính xác lại sau mỗi lần tăng t. Phương pháp gốc - đối ngẫu chỉ thực hiện một bước Newton có giảm bước trên hệ KKT nhiễu, di chuyển x và λ cùng lúc.')));
        var sm = slider(tx('Update factor μ (log scale)', 'Hệ số tăng μ (thang log)'), 0.3, 1.7, 0.01, lmu, function (v) { lmu = v; upd(); }, function (v) { return fmt(Math.pow(10, v), 1, lang); }); root.appendChild(sm.wrap);
        var cv = canvas(0.75); root.appendChild(cv.c);
        var S = stats3(root, [tx('primal-dual steps', 'bước gốc - đối ngẫu'), tx('barrier Newton steps', 'bước Newton của rào cản'), tx('final gap', 'khoảng cách cuối')]), msg = msgBox(root);
        cv.draw = function () {
            if (!cv.ctx) cv.size(); var ctx = cv.ctx; ctx.clearRect(0, 0, cv.w, cv.h); var V = view(cv, -0.1, 3.5, -0.1, 3.0, 10);
            var poly = [[0.2, 0.2], [3, 0.2], [3, 1], [1.4, 2.6], [0.2, 2.6]]; ctx.beginPath(); poly.forEach(function (p, i) { if (i) ctx.lineTo(V.X(p[0]), V.Y(p[1])); else ctx.moveTo(V.X(p[0]), V.Y(p[1])); }); ctx.closePath(); ctx.fillStyle = '#1d2540'; ctx.fill(); ctx.strokeStyle = COL.sky; ctx.lineWidth = 2; ctx.stroke();
            line(ctx, B.pts.map(function (p) { return [V.X(p[0]), V.Y(p[1])]; }), COL.sun, 2); B.pts.forEach(function (p) { dot(ctx, V.X(p[0]), V.Y(p[1]), 3, COL.sun); });
            line(ctx, A.pts.map(function (p) { return [V.X(p[0]), V.Y(p[1])]; }), COL.mint, 2); A.pts.forEach(function (p) { dot(ctx, V.X(p[0]), V.Y(p[1]), 3, COL.mint); }); dot(ctx, V.X(3), V.Y(1), 5, COL.pink);
            txt(ctx, tx('primal-dual', 'gốc - đối ngẫu'), 10, 16, COL.mint); txt(ctx, tx('barrier (centred points)', 'rào cản (các điểm trung tâm)'), 10, 32, COL.sun);
        };
        function upd() {
            var mu = Math.pow(10, lmu); A = pdRun(mu); B = barRun(mu); var last = A.pts[A.pts.length - 1], gap = -last[0] - 0.7 * last[1] + 3.7;
            S[0].set(String(A.it)); S[1].set(String(B.it)); S[2].set(gap.toExponential(1));
            msg.set(tx('Steps until the duality gap is below 10⁻⁶. The primal-dual path need not stay on the central path, and it spends far fewer Newton steps.', 'Số bước đến khi khoảng cách đối ngẫu dưới 10⁻⁶. Đường gốc - đối ngẫu không cần nằm trên đường trung tâm, và tốn ít bước Newton hơn nhiều.'), 'opx-ok');
            setd(root, { mu: mu.toFixed(2), pd: A.it, barrier: B.it, gap: gap.toExponential(4), x: last[0].toFixed(5) + ',' + last[1].toFixed(5) }); cv.draw();
        }
        after(function () { cv.size(); upd(); });
    }

    /* ---------- 16-02: KKT multipliers for a projection onto a wedge ---------- */
    var KA = [[1, 1], [1, -2]], KB = [1.2, 1.0];
    function kktSolve(p) {
        var feas = function (x) { return KA.every(function (a, i) { return a[0] * x[0] + a[1] * x[1] <= KB[i] + 1e-9; }); };
        if (feas(p)) return { x: p.slice(), l: [0, 0], act: [] };
        var best = null;
        for (var i = 0; i < 2; i++) { var a = KA[i], n2 = a[0] * a[0] + a[1] * a[1], lam = (a[0] * p[0] + a[1] * p[1] - KB[i]) / n2, x = [p[0] - lam * a[0], p[1] - lam * a[1]]; if (lam >= 0 && feas(x)) { var l = [0, 0]; l[i] = lam; return { x: x, l: l, act: [i] }; } }
        var det = KA[0][0] * KA[1][1] - KA[0][1] * KA[1][0], x2 = [(KB[0] * KA[1][1] - KA[0][1] * KB[1]) / det, (KA[0][0] * KB[1] - KB[0] * KA[1][0]) / det], r = [p[0] - x2[0], p[1] - x2[1]];
        var l0 = (-r[0] * KA[1][1] + r[1] * KA[1][0]) / (-det) , l1 = 0; // solve r = l0 a0 + l1 a1 ... (-grad = r)
        var M = [[KA[0][0], KA[1][0]], [KA[0][1], KA[1][1]]], dM = M[0][0] * M[1][1] - M[0][1] * M[1][0]; l0 = (r[0] * M[1][1] - M[0][1] * r[1]) / dM; l1 = (M[0][0] * r[1] - r[0] * M[1][0]) / dM;
        return { x: x2, l: [l0, l1], act: [0, 1] };
    }
    function initKKT(root, t, lang) {
        var tx = U(lang), P = [1.6, 1.2], V;
        shell(root, tx('KKT: gradients and multipliers', 'KKT: gradient và nhân tử'));
        root.appendChild(el('p', 'opx-note', tx('Minimise f(x) = ½‖x − p‖² over the wedge x₁ + x₂ ≤ 1.2, x₁ − 2x₂ ≤ 1. At the solution, −∇f(x*) = p − x* is a nonnegative combination of the normals of the active constraints. Tap the plot to move p.', 'Cực tiểu hóa f(x) = ½‖x − p‖² trên góc x₁ + x₂ ≤ 1,2, x₁ − 2x₂ ≤ 1. Tại nghiệm, −∇f(x*) = p − x* là tổ hợp không âm của các pháp tuyến của các ràng buộc đang tác dụng. Chạm vào hình để đổi p.')));
        var pr = row(); [[tx('Feasible p', 'p khả thi'), [0, 0]], [tx('One active', 'Một ràng buộc'), [1.6, 1.2]], [tx('Corner', 'Tại đỉnh'), [2.2, -1.2]]].forEach(function (q) { pr.appendChild(btn(q[0], '', function () { P = q[1].slice(); upd(); })); }); root.appendChild(pr);
        var cv = canvas(0.9); root.appendChild(cv.c);
        var S = stats3(root, ['λ₁', 'λ₂', tx('active', 'đang tác dụng')]), msg = msgBox(root), sol;
        cv.draw = function () {
            if (!cv.ctx) cv.size(); var ctx = cv.ctx; ctx.clearRect(0, 0, cv.w, cv.h); V = view(cv, -2.4, 3.0, -2.2, 2.6, 8); var big = 12;
            ctx.beginPath(); var pts = [[1.4, -1.2 * 0 + 0], [0, 0]]; // polygon: intersection point and far corners
            var xi = [(KB[0] * KA[1][1] - KA[0][1] * KB[1]) / (KA[0][0] * KA[1][1] - KA[0][1] * KA[1][0]), (KA[0][0] * KB[1] - KB[0] * KA[1][0]) / (KA[0][0] * KA[1][1] - KA[0][1] * KA[1][0])];
            var poly = [xi, [xi[0] - 8, KB[0] - (xi[0] - 8)], [-8, -8], [xi[0] + 8, (xi[0] + 8 - KB[1]) / 2]]; ctx.beginPath(); poly.forEach(function (q, i) { if (i) ctx.lineTo(V.X(q[0]), V.Y(q[1])); else ctx.moveTo(V.X(q[0]), V.Y(q[1])); }); ctx.closePath(); ctx.fillStyle = '#1d2540'; ctx.fill(); ctx.strokeStyle = COL.sky; ctx.lineWidth = 2; ctx.stroke();
            axes0(ctx, cv, V, -2.4, 3.0, -2.2, 2.6);
            var x = sol.x; line(ctx, [[V.X(P[0]), V.Y(P[1])], [V.X(x[0]), V.Y(x[1])]], COL.dim, 1.5, [4, 4]);
            var sc = 0.6; [[0, COL.ora], [1, COL.mint]].forEach(function (c) { var i = c[0]; if (sol.l[i] > 1e-9) { var nrm = KA[i]; line(ctx, [[V.X(x[0]), V.Y(x[1])], [V.X(x[0] + sc * nrm[0]), V.Y(x[1] + sc * nrm[1])]], c[1], 2.5); } });
            line(ctx, [[V.X(x[0]), V.Y(x[1])], [V.X(x[0] + (P[0] - x[0])), V.Y(x[1] + (P[1] - x[1]))]], COL.pink, 3);
            dot(ctx, V.X(P[0]), V.Y(P[1]), 6, COL.pink); dot(ctx, V.X(x[0]), V.Y(x[1]), 5, COL.sun); txt(ctx, 'p', V.X(P[0]) + 8, V.Y(P[1]) - 6, COL.pink); txt(ctx, 'x*', V.X(x[0]) + 8, V.Y(x[1]) + 14, COL.sun);
            txt(ctx, tx('pink = −∇f(x*) = p − x*, orange/green = constraint normals', 'hồng = −∇f(x*) = p − x*, cam/xanh = pháp tuyến ràng buộc'), 6, cv.h - 8, COL.dim);
        };
        pointer(cv, function (px, py) { if (!V) return; var x = V.ix(px), y = V.iy(py); if (x < -2.3 || x > 2.9 || y < -2.1 || y > 2.5) return; P = [x, y]; upd(); });
        function upd() {
            sol = kktSolve(P); var rx = [sol.x[0] - P[0] + sol.l[0] * KA[0][0] + sol.l[1] * KA[1][0], sol.x[1] - P[1] + sol.l[0] * KA[0][1] + sol.l[1] * KA[1][1]], st = Math.hypot(rx[0], rx[1]);
            S[0].set(fmt(sol.l[0], 3, lang)); S[1].set(fmt(sol.l[1], 3, lang)); S[2].set(sol.act.length ? sol.act.map(function (i) { return i + 1; }).join(' + ') : tx('none', 'không'));
            msg.set(sol.act.length === 0 ? tx('p is feasible: no constraint is active, both multipliers are 0 and x* = p.', 'p khả thi: không ràng buộc nào tác dụng, cả hai nhân tử bằng 0 và x* = p.') : sol.act.length === 1 ? tx('One constraint is active. The multiplier is the distance p travels along its normal.', 'Một ràng buộc đang tác dụng. Nhân tử là độ dài mà p di chuyển dọc pháp tuyến của nó.') : tx('Both constraints are active at the corner; p − x* is a nonnegative combination of both normals.', 'Cả hai ràng buộc cùng tác dụng tại đỉnh; p − x* là tổ hợp không âm của cả hai pháp tuyến.'), 'opx-ok');
            setd(root, { p: P[0].toFixed(2) + ',' + P[1].toFixed(2), x: sol.x[0].toFixed(5) + ',' + sol.x[1].toFixed(5), l1: sol.l[0].toFixed(5), l2: sol.l[1].toFixed(5), active: sol.act.map(function (i) { return i + 1; }).join(''), stat: st.toExponential(3) }); cv.draw();
        }
        after(function () { cv.size(); upd(); });
    }

    /* ---------- 13-04-01: lasso dual ---------- */
    function initLD(root, t, lang) {
        var tx = U(lang), lam = 0.8, V;
        shell(root, tx('The lasso and its dual', 'Lasso và bài toán đối ngẫu'));
        root.appendChild(el('p', 'opx-note', tx('Primal: min ½‖Ax − b‖² + λ‖x‖₁. Dual: max ½‖b‖² − ½‖b − u‖² subject to ‖Aᵀu‖∞ ≤ λ. At the optimum u* = b − Ax*, and |aᵢᵀu*| = λ exactly where x*ᵢ ≠ 0.', 'Bài gốc: min ½‖Ax − b‖² + λ‖x‖₁. Bài đối ngẫu: max ½‖b‖² − ½‖b − u‖² với ‖Aᵀu‖∞ ≤ λ. Tại nghiệm tối ưu u* = b − Ax*, và |aᵢᵀu*| = λ đúng ở các thành phần x*ᵢ ≠ 0.')));
        var sl = slider('λ', 0, 3.5, 0.01, lam, function (v) { lam = v; upd(); }, function (v) { return fmt(v, 2, lang); }); root.appendChild(sl.wrap);
        var cv = canvas(0.6); root.appendChild(cv.c);
        var S = stats3(root, [tx('primal value', 'giá trị gốc'), tx('dual value', 'giá trị đối ngẫu'), tx('active ᵢ', 'chỉ số tác dụng')]), msg = msgBox(root), cur;
        cv.draw = function () {
            if (!cv.ctx) cv.size(); var ctx = cv.ctx, W = cv.w, H = cv.h; ctx.clearRect(0, 0, W, H); var m = 4.2, V2 = view(cv, 0, 3, -0.3, m, 22), i;
            ctx.fillStyle = 'rgba(255,209,102,0.12)'; ctx.fillRect(0, V2.Y(lam), W, V2.Y(0) - V2.Y(lam)); line(ctx, [[0, V2.Y(lam)], [W, V2.Y(lam)]], COL.sun, 2, [5, 4]); txt(ctx, 'λ = ' + fmt(lam, 2, lang), W - 6, V2.Y(lam) - 5, COL.sun, 'right');
            for (i = 0; i < 2; i++) { var v = Math.abs(cur.at[i]), x0 = V2.X(0.5 + 1.5 * i), bw = 0.7 * (V2.X(1.5) - V2.X(0.5)); ctx.fillStyle = Math.abs(v - lam) < 1e-6 ? COL.mint : COL.sky; ctx.fillRect(x0 - bw / 2, V2.Y(v), bw, V2.Y(0) - V2.Y(v)); txt(ctx, '|a' + (i + 1) + 'ᵀu*|', x0, H - 6, COL.ink, 'center'); txt(ctx, 'x*' + (i + 1) + ' = ' + fmt(cur.x[i], 3, lang), x0, V2.Y(v) - 6, COL.ink, 'center'); }
        };
        function upd() {
            var p = istaRun([0, 0], lam, 1 / lassoL(), 6000), x = p[p.length - 1], r = [LB[0] - LA[0][0] * x[0] - LA[0][1] * x[1], LB[1] - LA[1][0] * x[0] - LA[1][1] * x[1]];
            var at = [LA[0][0] * r[0] + LA[1][0] * r[1], LA[0][1] * r[0] + LA[1][1] * r[1]], pv = lassoF(x, lam), dv = 0.5 * (LB[0] * LB[0] + LB[1] * LB[1]) - 0.5 * (( LB[0] - r[0]) * (LB[0] - r[0]) + (LB[1] - r[1]) * (LB[1] - r[1])); cur = { x: x, u: r, at: at };
            var act = [0, 1].filter(function (i) { return Math.abs(Math.abs(at[i]) - lam) < 1e-6; }).map(function (i) { return i + 1; });
            S[0].set(fmt(pv, 4, lang)); S[1].set(fmt(dv, 4, lang)); S[2].set(act.length ? act.join(', ') : tx('none', 'không'));
            msg.set(tx('The two values coincide (strong duality). A bar reaches the λ line exactly when the matching coefficient of x* is nonzero: the dual tells you the support of the lasso solution.', 'Hai giá trị trùng nhau (đối ngẫu mạnh). Một cột chạm đường λ đúng khi hệ số tương ứng của x* khác 0: bài đối ngẫu cho biết giá của nghiệm lasso.'), 'opx-ok');
            setd(root, { lam: fmt(lam, 2), primal: pv.toFixed(6), dual: dv.toFixed(6), active: act.join(''), x: x[0].toFixed(5) + ',' + x[1].toFixed(5), u: r[0].toFixed(5) + ',' + r[1].toFixed(5), at: at[0].toFixed(5) + ',' + at[1].toFixed(5) }); cv.draw();
        }
        after(function () { cv.size(); upd(); });
    }

    /* ---------- 23-02: coordinate descent vs gradient descent ---------- */
    function cdRun(rho, kind, b) {
        b = [1 + 0.5 * rho, rho + 0.5]; var x = [-2.0, 1.5], xs = [[-2.0, 1.5]], fst = 0, det = 1 - rho * rho, xo = [(b[0] - rho * b[1]) / det, (b[1] - rho * b[0]) / det], f = function (p) { return 0.5 * (p[0] * p[0] + 2 * rho * p[0] * p[1] + p[1] * p[1]) - b[0] * p[0] - b[1] * p[1]; }; fst = f(xo); var it = 0, L = 1 + rho;
        while (f(x) - fst > 1e-10 && it < 5000) {
            if (kind === 'cd') { x = [b[0] - rho * x[1], x[1]]; xs.push(x.slice()); x = [x[0], b[1] - rho * x[0]]; xs.push(x.slice()); }
            else { var g = [x[0] + rho * x[1] - b[0], rho * x[0] + x[1] - b[1]]; x = [x[0] - g[0] / L, x[1] - g[1] / L]; xs.push(x.slice()); }
            it++;
        }
        return { xs: xs, it: it, xo: xo, f: f, fs: fst };
    }
    function initCD(root, t, lang) {
        var tx = U(lang), rho = 0.6, K = 6, R, V, b = [1, 0.5];
        shell(root, tx('Coordinate descent vs gradient descent', 'Coordinate descent so với gradient descent'));
        root.appendChild(el('p', 'opx-note', tx('f(x) = ½(x₁² + 2ρx₁x₂ + x₂²) − bᵀx with b chosen so that x* = (1, ½) for every ρ. One coordinate-descent sweep updates x₁ then x₂ exactly; one gradient step uses the step 1/L. ρ is the correlation between the coordinates.', 'f(x) = ½(x₁² + 2ρx₁x₂ + x₂²) − bᵀx, với b chọn sao cho x* = (1, ½) với mọi ρ. Một lượt coordinate descent cập nhật chính xác x₁ rồi x₂; một bước gradient dùng bước 1/L. ρ là mức tương quan giữa hai tọa độ.')));
        var sr = slider('ρ', 0, 0.95, 0.01, rho, function (v) { rho = v; upd(); }, function (v) { return fmt(v, 2, lang); }), sk = slider(tx('Sweeps / steps shown', 'Số lượt / bước hiển thị'), 0, 40, 1, K, function (v) { K = v; upd(); }, function (v) { return String(v); });
        root.appendChild(sr.wrap); root.appendChild(sk.wrap);
        var cv = canvas(0.8); root.appendChild(cv.c);
        var S = stats3(root, [tx('CD sweeps', 'lượt CD'), tx('GD steps', 'bước GD'), tx('ratio', 'tỉ lệ')]), msg = msgBox(root);
        cv.draw = function () {
            if (!cv.ctx) cv.size(); var ctx = cv.ctx; ctx.clearRect(0, 0, cv.w, cv.h); V = view(cv, -2.6, 2.6, -1.9, 2.3, 0); heat(cv, V, function (x, y) { return R.cd.f([x, y]); }, R.cd.fs, 46); axes0(ctx, cv, V, -2.6, 2.6, -1.9, 2.3);
            var a = R.cd.xs.slice(0, 2 * K + 1), g = R.gd.xs.slice(0, K + 1); line(ctx, g.map(function (p) { return [V.X(p[0]), V.Y(p[1])]; }), COL.sun, 2); line(ctx, a.map(function (p) { return [V.X(p[0]), V.Y(p[1])]; }), COL.mint, 2);
            g.forEach(function (p) { dot(ctx, V.X(p[0]), V.Y(p[1]), 2.5, COL.sun); }); a.forEach(function (p, i) { if (i % 2 === 0) dot(ctx, V.X(p[0]), V.Y(p[1]), 2.5, COL.mint); });
            dot(ctx, V.X(-2), V.Y(1.5), 5, COL.pink); dot(ctx, V.X(R.cd.xo[0]), V.Y(R.cd.xo[1]), 4, COL.ink); txt(ctx, tx('coordinate descent', 'coordinate descent'), 8, 14, COL.mint); txt(ctx, tx('gradient descent', 'gradient descent'), 8, 30, COL.sun);
        };
        function upd() {
            R = { cd: cdRun(rho, 'cd', b), gd: cdRun(rho, 'gd', b) }; S[0].set(String(R.cd.it)); S[1].set(String(R.gd.it)); S[2].set(R.cd.it ? fmt(R.gd.it / R.cd.it, 1, lang) + '×' : '-');
            msg.set(rho < 0.05 ? tx('With uncorrelated coordinates one sweep solves the problem exactly.', 'Khi các tọa độ không tương quan, một lượt giải chính xác bài toán.') : tx('Steps until f − f* < 10⁻¹⁰. The more correlated the coordinates, the more both methods zig-zag, and the more the staircase path of coordinate descent costs.', 'Số bước đến khi f − f* < 10⁻¹⁰. Các tọa độ càng tương quan thì cả hai phương pháp càng zig-zag, và đường bậc thang của coordinate descent càng tốn kém.'), 'opx-ok');
            setd(root, { rho: fmt(rho, 2), cd: R.cd.it, gd: R.gd.it, k: K, xo: R.cd.xo[0].toFixed(5) + ',' + R.cd.xo[1].toFixed(5) }); cv.draw();
        }
        after(function () { cv.size(); upd(); });
    }

    /* ---------- 24-05 / 25-01: tiny integer program  max 5x1 + 4x2  s.t. 6x1+4x2<=24, x1+2x2<=6, x>=0 ---------- */
    var ILP = { c: [5, 4], rows: [[6, 4, 24], [1, 2, 6], [-1, 0, 0], [0, -1, 0]] };
    function lpSolve(rows) { // maximise c.x over rows a.x <= b (2-D), by vertex enumeration
        var best = null, v = [], i, j, bx = null;
        for (i = 0; i < rows.length; i++) for (j = i + 1; j < rows.length; j++) {
            var a = rows[i], b = rows[j], det = a[0] * b[1] - a[1] * b[0]; if (Math.abs(det) < 1e-12) continue;
            var x = [(a[2] * b[1] - a[1] * b[2]) / det, (a[0] * b[2] - a[2] * b[0]) / det];
            if (rows.every(function (r) { return r[0] * x[0] + r[1] * x[1] <= r[2] + 1e-9; })) { v.push(x); var val = ILP.c[0] * x[0] + ILP.c[1] * x[1]; if (best === null || val > best + 1e-12) { best = val; bx = x; } }
        }
        return best === null ? null : { val: best, x: bx, verts: v };
    }
    function hull(pts) { if (pts.length < 3) return pts.slice(); var cx = pts.reduce(function (s, p) { return s + p[0]; }, 0) / pts.length, cy = pts.reduce(function (s, p) { return s + p[1]; }, 0) / pts.length; return pts.slice().sort(function (p, q) { return Math.atan2(p[1] - cy, p[0] - cx) - Math.atan2(q[1] - cy, q[0] - cx); }); }
    function bnbRun() {
        var nodes = [], bestV = -Infinity, bestX = null, stack = [{ rows: ILP.rows, label: tx0('root'), parent: -1 }];
        function tx0(s) { return s; }
        while (stack.length) {
            var nd = stack.pop(), r = lpSolve(nd.rows), id = nodes.length; nd.id = id;
            var rec = { id: id, parent: nd.parent, label: nd.label, rows: nd.rows, lp: r };
            if (!r) rec.status = 'infeasible'; else if (r.val <= bestV + 1e-9) rec.status = 'pruned';
            else { var fr = [0, 1].filter(function (i) { return Math.abs(r.x[i] - Math.round(r.x[i])) > 1e-6; });
                if (!fr.length) { rec.status = 'integer'; if (r.val > bestV) { bestV = r.val; bestX = r.x.map(Math.round); } }
                else { var i = fr[0], f = Math.floor(r.x[i] + 1e-9); rec.status = 'branch'; rec.var = i; rec.f = f;
                    var up = [0, 0, 0], dn = [0, 0, 0]; dn[i] = 1; dn[2] = f; up[i] = -1; up[2] = -(f + 1);
                    stack.push({ rows: nd.rows.concat([up]), label: 'x' + (i + 1) + ' ≥ ' + (f + 1), parent: id }); stack.push({ rows: nd.rows.concat([dn]), label: 'x' + (i + 1) + ' ≤ ' + f, parent: id }); } }
            rec.best = bestV; nodes.push(rec);
        }
        return { nodes: nodes, best: bestV, bx: bestX };
    }
    function initBNB(root, t, lang) {
        var tx = U(lang), K = 0, R = bnbRun(), V;
        shell(root, tx('Branch and bound on a tiny integer program', 'Nhánh cận trên một bài quy hoạch nguyên nhỏ'));
        root.appendChild(el('p', 'opx-note', tx('max 5x₁ + 4x₂ subject to 6x₁ + 4x₂ ≤ 24, x₁ + 2x₂ ≤ 6, x ≥ 0 integer. Step through the nodes: each solves an LP relaxation, then either branches on a fractional variable, stops because it is integral, or is pruned by the incumbent.', 'max 5x₁ + 4x₂ với 6x₁ + 4x₂ ≤ 24, x₁ + 2x₂ ≤ 6, x ≥ 0 nguyên. Duyệt qua các nút: mỗi nút giải một LP nới lỏng, rồi hoặc rẽ nhánh theo biến phân số, hoặc dừng vì đã nguyên, hoặc bị loại bởi nghiệm tốt nhất hiện có.')));
        var sk = slider(tx('Node', 'Nút'), 0, R.nodes.length - 1, 1, K, function (v) { K = v; upd(); }, function (v) { return String(v); }); root.appendChild(sk.wrap);
        var cv = canvas(0.75); root.appendChild(cv.c);
        var S = stats3(root, [tx('LP bound', 'cận LP'), tx('incumbent', 'nghiệm tốt nhất'), tx('status', 'trạng thái')]), msg = msgBox(root);
        var STAT = { infeasible: tx('infeasible', 'vô nghiệm'), pruned: tx('pruned', 'bị loại'), integer: tx('integral', 'nguyên'), branch: tx('branch', 'rẽ nhánh') };
        cv.draw = function () {
            if (!cv.ctx) cv.size(); var ctx = cv.ctx; ctx.clearRect(0, 0, cv.w, cv.h); V = view(cv, -0.3, 5.3, -0.3, 4.3, 12); var nd = R.nodes[K], i, j;
            for (i = 0; i <= 5; i++) for (j = 0; j <= 4; j++) dot(ctx, V.X(i), V.Y(j), 2.2, COL.dim);
            if (nd.lp) { var h = hull(nd.lp.verts); ctx.beginPath(); h.forEach(function (p, q) { if (q) ctx.lineTo(V.X(p[0]), V.Y(p[1])); else ctx.moveTo(V.X(p[0]), V.Y(p[1])); }); ctx.closePath(); ctx.fillStyle = 'rgba(76,201,240,0.18)'; ctx.fill(); ctx.strokeStyle = COL.sky; ctx.lineWidth = 2; ctx.stroke(); dot(ctx, V.X(nd.lp.x[0]), V.Y(nd.lp.x[1]), 6, COL.pink); txt(ctx, '(' + nd.lp.x.map(function (q) { return fmt(q, 2, lang); }).join('; ') + ')', V.X(nd.lp.x[0]) + 8, V.Y(nd.lp.x[1]) - 8, COL.pink); }
            if (R.bx && nd.best > -1e8) dot(ctx, V.X(R.bx[0]), V.Y(R.bx[1]), 5, COL.mint);
            txt(ctx, tx('node ', 'nút ') + nd.id + (nd.label !== 'root' ? ': ' + nd.label : ': root'), 8, 14, COL.sun); txt(ctx, 'x₁', cv.w - 16, V.Y(0) - 5, COL.dim);
        };
        function upd() {
            var nd = R.nodes[K]; S[0].set(nd.lp ? fmt(nd.lp.val, 2, lang) : '—'); S[1].set(nd.best > -1e8 ? fmt(nd.best, 0, lang) : '—'); S[2].set(STAT[nd.status]);
            msg.set(nd.status === 'branch' ? tx('The LP optimum has a fractional x' + (nd.var + 1) + '. Branch: x' + (nd.var + 1) + ' ≤ ' + nd.f + ' or x' + (nd.var + 1) + ' ≥ ' + (nd.f + 1) + '. No integer point lies in between.', 'Nghiệm LP có x' + (nd.var + 1) + ' phân số. Rẽ nhánh: x' + (nd.var + 1) + ' ≤ ' + nd.f + ' hoặc x' + (nd.var + 1) + ' ≥ ' + (nd.f + 1) + '. Không có điểm nguyên nào ở giữa.')
                : nd.status === 'integer' ? tx('Integral LP optimum: a feasible integer solution, the new incumbent if it is better.', 'Nghiệm LP nguyên: một nghiệm nguyên khả thi, trở thành nghiệm tốt nhất mới nếu tốt hơn.') : nd.status === 'pruned' ? tx('The LP bound is no better than the incumbent, so this whole subtree is discarded.', 'Cận LP không tốt hơn nghiệm hiện có nên cả cây con này bị loại.') : tx('The relaxation is infeasible: nothing to explore here.', 'Bài nới lỏng vô nghiệm: không còn gì để khám phá ở đây.'), 'opx-ok');
            setd(root, { k: K, nodes: R.nodes.length, status: nd.status, lp: nd.lp ? nd.lp.val.toFixed(4) : 'none', x: nd.lp ? nd.lp.x[0].toFixed(4) + ',' + nd.lp.x[1].toFixed(4) : '', inc: nd.best > -1e8 ? nd.best : 'none', best: R.best, bx: R.bx ? R.bx.join(',') : '' }); cv.draw();
        }
        after(function () { cv.size(); upd(); });
    }
    function cutRun() {
        var rows = ILP.rows.slice(), rounds = [], r = lpSolve(rows), k = 0;
        rounds.push({ rows: rows.slice(), lp: r, cut: null });
        while (k < 8) {
            var fr = [0, 1].filter(function (i) { return Math.abs(r.x[i] - Math.round(r.x[i])) > 1e-6; }); if (!fr.length) break;
            var act = []; rows.forEach(function (q, i) { if (Math.abs(q[0] * r.x[0] + q[1] * r.x[1] - q[2]) < 1e-7) act.push(i); }); if (act.length < 2) break;
            var found = null;
            for (var ai = 0; ai < act.length && !found; ai++) for (var aj = ai + 1; aj < act.length && !found; aj++) {
                var a = rows[act[ai]], b = rows[act[aj]], det = a[0] * b[1] - a[1] * b[0]; if (Math.abs(det) < 1e-9) continue;
                var Bi = [[b[1] / det, -a[1] / det], [-b[0] / det, a[0] / det]]; // inverse of [[a0,a1],[b0,b1]]: columns correspond to the two rows
                // x = Binv * (b_a, b_b): x_i = Bi[i][0]*ba + Bi[i][1]*bb ; Gomory/CG multipliers u = frac(Bi[i][.]) for a fractional x_i
                for (var q = 0; q < 2 && !found; q++) { var i = q; if (Math.abs(r.x[i] - Math.round(r.x[i])) < 1e-6) continue; var u = [Bi[i][0] - Math.floor(Bi[i][0] + 1e-9), Bi[i][1] - Math.floor(Bi[i][1] + 1e-9)];
                    var cx = [Math.floor(u[0] * a[0] + u[1] * b[0] + 1e-9), Math.floor(u[0] * a[1] + u[1] * b[1] + 1e-9)], cb = Math.floor(u[0] * a[2] + u[1] * b[2] + 1e-9);
                    if (cx[0] * r.x[0] + cx[1] * r.x[1] > cb + 1e-7) found = [cx[0], cx[1], cb]; } }
            if (!found) break; rows = rows.concat([found]); r = lpSolve(rows); k++; rounds.push({ rows: rows.slice(), lp: r, cut: found });
        }
        return rounds;
    }
    function initCuts(root, t, lang) {
        var tx = U(lang), K = 0, R = cutRun(), V;
        shell(root, tx('Cutting planes: shaving off the fractional point', 'Mặt phẳng cắt: cắt bỏ điểm phân số'));
        root.appendChild(el('p', 'opx-note', tx('Same integer program as in chapter 24. Each round solves the LP, builds a Chvátal-Gomory cut from the basis rows of the fractional vertex, and adds it. No integer point is ever removed.', 'Cùng bài quy hoạch nguyên ở chương 24. Mỗi vòng giải LP, dựng một mặt cắt Chvátal-Gomory từ các hàng cơ sở của đỉnh phân số rồi thêm vào. Không điểm nguyên nào bị loại.')));
        var sk = slider(tx('Cut rounds', 'Số vòng cắt'), 0, R.length - 1, 1, K, function (v) { K = v; upd(); }, function (v) { return String(v); }); root.appendChild(sk.wrap);
        var cv = canvas(0.75); root.appendChild(cv.c);
        var S = stats3(root, [tx('LP bound', 'cận LP'), tx('integer optimum', 'tối ưu nguyên'), tx('LP optimum', 'tối ưu LP')]), msg = msgBox(root);
        cv.draw = function () {
            if (!cv.ctx) cv.size(); var ctx = cv.ctx; ctx.clearRect(0, 0, cv.w, cv.h); V = view(cv, -0.3, 5.3, -0.3, 4.3, 12); var rd = R[K], i, j;
            var h = hull(rd.lp.verts); ctx.beginPath(); h.forEach(function (p, q) { if (q) ctx.lineTo(V.X(p[0]), V.Y(p[1])); else ctx.moveTo(V.X(p[0]), V.Y(p[1])); }); ctx.closePath(); ctx.fillStyle = 'rgba(76,201,240,0.18)'; ctx.fill(); ctx.strokeStyle = COL.sky; ctx.lineWidth = 2; ctx.stroke();
            for (i = 0; i <= 5; i++) for (j = 0; j <= 4; j++) { var feas = ILP.rows.every(function (r) { return r[0] * i + r[1] * j <= r[2]; }); dot(ctx, V.X(i), V.Y(j), feas ? 3.5 : 2, feas ? COL.ink : COL.dim); }
            if (rd.cut) { var c = rd.cut, pts = []; for (var x = -0.3; x <= 5.3; x += 0.1) { if (Math.abs(c[1]) > 1e-9) { var y = (c[2] - c[0] * x) / c[1]; if (y >= -0.3 && y <= 4.3) pts.push([V.X(x), V.Y(y)]); } } if (pts.length > 1) line(ctx, pts, COL.ora, 2.5, [6, 4]); }
            dot(ctx, V.X(rd.lp.x[0]), V.Y(rd.lp.x[1]), 6, COL.pink); dot(ctx, V.X(4), V.Y(0), 4, COL.mint);
            txt(ctx, '(' + rd.lp.x.map(function (q) { return fmt(q, 2, lang); }).join('; ') + ')', V.X(rd.lp.x[0]) + 8, V.Y(rd.lp.x[1]) - 8, COL.pink); txt(ctx, rd.cut ? tx('cut: ', 'mặt cắt: ') + rd.cut[0] + 'x₁ + ' + rd.cut[1] + 'x₂ ≤ ' + rd.cut[2] : tx('no cuts yet', 'chưa có mặt cắt'), 8, 14, COL.ora);
        };
        function upd() {
            var rd = R[K], integral = [0, 1].every(function (i) { return Math.abs(rd.lp.x[i] - Math.round(rd.lp.x[i])) < 1e-6; });
            S[0].set(fmt(rd.lp.val, 2, lang)); S[1].set('20'); S[2].set('(' + rd.lp.x.map(function (q) { return fmt(q, 2, lang); }).join('; ') + ')');
            msg.set(integral ? tx('The LP optimum is now an integer point, so the cutting-plane method has solved the integer program.', 'Nghiệm LP đã là điểm nguyên nên phương pháp mặt phẳng cắt đã giải xong bài quy hoạch nguyên.') : tx('Each cut removes the fractional vertex but keeps every integer point (white dots), so the bound can only go down.', 'Mỗi mặt cắt loại bỏ đỉnh phân số nhưng giữ mọi điểm nguyên (chấm trắng), nên cận chỉ có thể giảm.'), 'opx-ok');
            setd(root, { k: K, rounds: R.length - 1, lp: rd.lp.val.toFixed(4), x: rd.lp.x[0].toFixed(4) + ',' + rd.lp.x[1].toFixed(4), cut: rd.cut ? rd.cut.join(',') : 'none', integral: integral ? 1 : 0 }); cv.draw();
        }
        after(function () { cv.size(); upd(); });
    }

    var INIT = { gd: initGD, subg: initSubg, cl: initCL, newton: function (r, t, l) { initRace(r, t, l, 'newton'); }, bfgs: function (r, t, l) { initRace(r, t, l, 'bfgs'); }, ista: initISTA, barrier: initBarrier, fw: initFW, sgm: initSGM, mgame: initMG, d1: initD1, dd: initDD, admm: initADMM, pn: initPN, pdipm: initPDIPM, kkt: initKKT, ld: initLD, cd: initCD, bnb: initBNB, cuts: initCuts };
    function initAll() {
        css();
        var nodes = document.querySelectorAll('.opx-explainer');
        for (var i = 0; i < nodes.length; i++) { var n = nodes[i]; if (n.getAttribute('data-opx-ready')) continue; var k = n.getAttribute('data-opx'), lang = n.getAttribute('data-lang') || 'en'; if (INIT[k]) { n.setAttribute('data-opx-ready', '1'); try { INIT[k](n, null, lang); } catch (e) { if (window.console) console.error('opx ' + k, e); } } }
    }
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
    window.OPX = { fstar: FSTAR, run: runMethod, F: F };
})();
