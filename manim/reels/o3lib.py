"""Numerics ported from opt-explainers.js (checked independently by the reel scripts' asserts)."""
import numpy as np, itertools, math
LA = np.array([[1.6, 0.7], [0.4, 1.1]]); LB = np.array([2.1, 0.9])
def soft(v, th): return np.sign(v) * np.maximum(np.abs(v) - th, 0)
def lasso_f(x, lam): r = LA @ x - LB; return 0.5 * r @ r + lam * np.abs(x).sum()
def lasso_star(lam):
    L = np.linalg.eigvalsh(LA.T @ LA).max(); x = np.zeros(2)
    for _ in range(20000): x = soft(x - (LA.T @ (LA @ x - LB)) / L, lam / L)
    return x
# ---- ADMM
def admm(lam, rho, n):
    M = np.linalg.inv(LA.T @ LA + rho * np.eye(2)); Atb = LA.T @ LB; z = np.zeros(2); u = np.zeros(2); xs = [np.zeros(2)]; zs = [np.zeros(2)]
    for _ in range(n):
        x = M @ (Atb + rho * (z - u)); z = soft(x + u, lam / rho); u = u + x - z; xs.append(x); zs.append(z.copy())
    return xs, zs
# ---- lse + l1 (prox methods)
def Fl(p): return float(np.logaddexp.reduce([p[0] + 3 * p[1] - .1, p[0] - 3 * p[1] - .1, -p[0] - .1]))
def Gl(p):
    a, b, c = math.exp(p[0] + 3 * p[1] - .1), math.exp(p[0] - 3 * p[1] - .1), math.exp(-p[0] - .1); z = a + b + c
    return np.array([(a + b - c) / z, (3 * a - 3 * b) / z])
def Hl(p):
    a, b, c = math.exp(p[0] + 3 * p[1] - .1), math.exp(p[0] - 3 * p[1] - .1), math.exp(-p[0] - .1); z = a + b + c; g = Gl(p)
    return np.array([[(a + b + c) / z - g[0] ** 2, (3 * a - 3 * b) / z - g[0] * g[1]], [(3 * a - 3 * b) / z - g[0] * g[1], 9 * (a + b) / z - g[1] ** 2]])
def Fobj(p, lam): return Fl(p) + lam * np.abs(p).sum()
def pn_step(p, lam, H, g):
    d = np.zeros(2)
    for _ in range(200):
        for i in range(2):
            j = 1 - i; z = p[i] - (g[i] + H[i, j] * d[j]) / H[i, i]; d[i] = soft(z, lam / H[i, i]) - p[i]
    return d
def prox_methods(start, lam, maxit=300):
    def newton_iter(p):
        g = Gl(p); d = pn_step(p, lam, Hl(p), g); dec = g @ d + lam * (np.abs(p + d).sum() - np.abs(p).sum()); t = 1.0; fp = Fobj(p, lam)
        while Fobj(p + t * d, lam) > fp + .1 * t * dec and t > 1e-12: t *= .5
        return p + t * d
    p = np.array([1.0, .5])
    for _ in range(80): p = newton_iter(p)
    fs = Fobj(p, lam); xs = p.copy(); out = {}
    for kind in ('gd', 'nw'):
        p = np.array(start, float); pts = [p.copy()]; it = 0
        while it < maxit and Fobj(p, lam) - fs >= 1e-10:
            if kind == 'nw': p = newton_iter(p)
            else:
                g = Gl(p); t = 1.0
                while True:
                    q = soft(p - t * g, t * lam); dq = q - p
                    if Fl(q) <= Fl(p) + g @ dq + dq @ dq / (2 * t) or t < 1e-12: break
                    t *= .5
                p = q
            pts.append(p.copy()); it += 1
        out[kind] = pts
    return out, xs, fs
# ---- LP polygon (barrier / primal-dual)
BA = np.array([[-1, 0], [0, -1], [1, 1], [1, 0], [0, 1]], float); BB = np.array([-.2, -.2, 4, 3, 2.6]); BC = np.array([-1, -.7])
def bar_center(t, x):
    steps = 0
    for _ in range(80):
        s = BB - BA @ x; g = t * BC + (BA / s[:, None]).sum(0); H = (BA / s[:, None] ** 2).T @ BA; d = -np.linalg.solve(H, g); dec = -g @ d
        if dec / 2 < 1e-10: break
        phi = lambda y: t * BC @ y - np.log(BB - BA @ y).sum(); s2 = 1.0
        while (BB - BA @ (x + s2 * d) <= 0).any() or phi(x + s2 * d) > phi(x) - .25 * s2 * dec: s2 *= .5
        x = x + s2 * d; steps += 1
    return x, steps
def barrier_run(mu):
    x = np.array([1.5, 1.0]); t = 1.0; pts = [x.copy()]; tot = 0
    while 5 / t > 1e-6: x, s = bar_center(t, x); tot += s; pts.append(x.copy()); t *= mu
    return pts, tot
def pd_run(mu):
    x = np.array([1.5, 1.0]); lam = np.ones(5); pts = [x.copy()]; it = 0; m = 5
    def res(x, l, tt): return np.concatenate([BC + BA.T @ l, -l * (BA @ x - BB) - 1 / tt])
    for _ in range(200):
        s = BB - BA @ x; eta = s @ lam; tt = mu * m / eta; r = res(x, lam, tt)
        if np.linalg.norm(r[:2]) < 1e-9 and eta < 1e-6: break
        H = (BA * (lam / s)[:, None]).T @ BA; rhs = -r[:2] + BA.T @ (r[2:] / s); dx = np.linalg.solve(H, rhs); dl = (lam * (BA @ dx) - r[2:]) / s
        smax = min([1.0] + [-lam[i] / dl[i] for i in range(5) if dl[i] < 0]); st = .99 * smax; nr = np.linalg.norm(r)
        for _ in range(60):
            xn = x + st * dx; ln = lam + st * dl
            if (BA @ xn < BB).all() and np.linalg.norm(res(xn, ln, tt)) <= (1 - .01 * st) * nr: break
            st *= .5
        x = x + st * dx; lam = lam + st * dl; pts.append(x.copy()); it += 1
    return pts, it
# ---- coordinate descent
def cd_gd(rho, kind, b=None):
    b = np.array([1 + .5 * rho, rho + .5]); Q = np.array([[1, rho], [rho, 1]]); xo = np.linalg.solve(Q, b); f = lambda p: .5 * p @ Q @ p - b @ p
    x = np.array([-2.0, 1.5]); xs = [x.copy()]; it = 0
    while f(x) - f(xo) > 1e-10 and it < 5000:
        if kind == 'cd': x[0] = b[0] - rho * x[1]; xs.append(x.copy()); x[1] = b[1] - rho * x[0]; xs.append(x.copy())
        else: x = x - (Q @ x - b) / (1 + rho); xs.append(x.copy())
        it += 1
    return xs, it, xo, f
# ---- integer program
ILP_C = (5, 4); ILP_ROWS = [(6, 4, 24), (1, 2, 6), (-1, 0, 0), (0, -1, 0)]
def lp_solve(rows):
    best = None; bx = None; verts = []
    for a, b in itertools.combinations(rows, 2):
        det = a[0] * b[1] - a[1] * b[0]
        if abs(det) < 1e-12: continue
        x = ((a[2] * b[1] - a[1] * b[2]) / det, (a[0] * b[2] - a[2] * b[0]) / det)
        if all(r[0] * x[0] + r[1] * x[1] <= r[2] + 1e-9 for r in rows):
            verts.append(x); v = ILP_C[0] * x[0] + ILP_C[1] * x[1]
            if best is None or v > best + 1e-12: best, bx = v, x
    return None if best is None else (best, bx, verts)
def hull(pts):
    cx = sum(p[0] for p in pts) / len(pts); cy = sum(p[1] for p in pts) / len(pts)
    return sorted(pts, key=lambda p: math.atan2(p[1] - cy, p[0] - cx))
def bnb():
    nodes = []; best = -1e18; bx = None; stack = [(ILP_ROWS, 'root', -1)]
    while stack:
        rows, label, par = stack.pop(); r = lp_solve(rows); rec = dict(rows=rows, label=label, lp=r, par=par, id=len(nodes))
        if r is None: rec['st'] = 'infeasible'
        elif r[0] <= best + 1e-9: rec['st'] = 'pruned'
        else:
            fr = [i for i in (0, 1) if abs(r[1][i] - round(r[1][i])) > 1e-6]
            if not fr:
                rec['st'] = 'integer'
                if r[0] > best: best = r[0]; bx = tuple(round(v) for v in r[1])
            else:
                i = fr[0]; f = math.floor(r[1][i] + 1e-9); rec['st'] = 'branch'; rec['var'] = i; rec['f'] = f; dn = [0, 0, 0]; up = [0, 0, 0]; dn[i] = 1; dn[2] = f; up[i] = -1; up[2] = -(f + 1)
                stack.append((rows + [tuple(up)], 'x%d >= %d' % (i + 1, f + 1), rec['id'])); stack.append((rows + [tuple(dn)], 'x%d <= %d' % (i + 1, f), rec['id']))
        rec['best'] = best; nodes.append(rec)
    return nodes, best, bx
def cuts():
    rows = list(ILP_ROWS); r = lp_solve(rows); rounds = [dict(rows=list(rows), lp=r, cut=None)]
    for _ in range(8):
        x = r[1]; fr = [i for i in (0, 1) if abs(x[i] - round(x[i])) > 1e-6]
        if not fr: break
        act = [i for i, q in enumerate(rows) if abs(q[0] * x[0] + q[1] * x[1] - q[2]) < 1e-7]; found = None
        for ai, aj in itertools.combinations(act, 2):
            a, b = rows[ai], rows[aj]; det = a[0] * b[1] - a[1] * b[0]
            if abs(det) < 1e-9: continue
            Bi = [[b[1] / det, -a[1] / det], [-b[0] / det, a[0] / det]]
            for i in (0, 1):
                if abs(x[i] - round(x[i])) < 1e-6: continue
                u = [Bi[i][0] - math.floor(Bi[i][0] + 1e-9), Bi[i][1] - math.floor(Bi[i][1] + 1e-9)]
                cx = (math.floor(u[0] * a[0] + u[1] * b[0] + 1e-9), math.floor(u[0] * a[1] + u[1] * b[1] + 1e-9)); cb = math.floor(u[0] * a[2] + u[1] * b[2] + 1e-9)
                if cx[0] * x[0] + cx[1] * x[1] > cb + 1e-7: found = (cx[0], cx[1], cb); break
            if found: break
        if not found: break
        rows = rows + [found]; r = lp_solve(rows); rounds.append(dict(rows=list(rows), lp=r, cut=found))
    return rounds
