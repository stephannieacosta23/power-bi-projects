import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import datos
plt.rcParams["font.family"] = ["Liberation Sans"]
ACC, GRIS, BANDA, TXT, MUTED = "#1F5AA6", "#8C8C8C", "#E3E6EA", "#222222", "#666666"
DARK, LIGHT, ORANGE = "#3A3F45", "#A3A9B0", "#E8A33D"
YRS = ["#C9D3E3", "#9DB0CF", "#5F7FB3"]  # 2023-2025 (ChatGPT: secuencial)

def panel(ax, data, style, destacar):
    items = sorted(data.items(), key=lambda kv: kv[1][3])
    for i, (k, v) in enumerate(items):
        y23, y24, y25, y26, p1, p2 = v
        if style == "claude":
            col = ACC if (destacar is None or k == destacar) else GRIS
            lo, hi = sorted((p1, p2)); ax.barh(i, max(hi - lo, .1), left=lo, height=.55, color=BANDA, zorder=1)
            ax.plot([p1, p1], [i - .3, i + .3], color="#5A5F66", lw=1.6, zorder=2)
            ax.plot([y25, y26], [i, i], color=col, lw=1.6, zorder=3)
            ax.scatter(y25, i, s=55, color=col, zorder=4); ax.scatter(y26, i, s=60, facecolor="white", edgecolor=col, lw=2, zorder=5)
        elif style == "chatgpt":
            col = ACC
            ax.plot([min(v[:4]), max(v[:4])], [i, i], color="#DDDDDD", lw=1.2, zorder=1)
            for x, c in zip((y23, y24, y25), YRS): ax.scatter(x, i, s=40, color=c, zorder=3)
            ax.scatter(y26, i, s=60, color="#0B2E6B", marker="D", zorder=4)
            ax.plot([p1, p1], [i - .3, i + .3], color="black", lw=1.8, zorder=2)
            ax.plot([p2, p2], [i - .3, i + .3], color=ORANGE, lw=1.8, zorder=2)
        else:  # equipo
            col = ACC if (destacar is None or k == destacar) else GRIS
            ax.plot([p1, p1], [i + .19, i + .47], color=DARK, lw=3.0, zorder=2, solid_capstyle="butt")
            ax.plot([p2, p2], [i + .19, i + .47], color=LIGHT, lw=3.0, zorder=2, solid_capstyle="butt")
            ax.plot([y25, y26], [i, i], color=col, lw=1.6, zorder=3)
            ax.scatter(y25, i, s=55, color=col, zorder=4); ax.scatter(y26, i, s=60, facecolor="white", edgecolor=col, lw=2, zorder=5)
        strong = style != "chatgpt" and (destacar is None or k == destacar)
        ax.text(9.9, i, f"{y26:.1f}".replace(".", ",").replace("-", "−"), va="center", ha="right", fontsize=8.5, clip_on=False,
                color=ACC if strong else TXT, fontweight="bold" if strong else "normal")
    ax.set_yticks(range(len(items)))
    ax.set_yticklabels([k.replace("Oriente Medio, Norte de África,\nAfganistán y Pakistán", "O. Medio, N. África,\nAfganistán y Pakistán") for k, _ in items], fontsize=8.5, color=TXT)
    if style != "chatgpt" and destacar:
        for lbl, (k, _) in zip(ax.get_yticklabels(), items):
            if k == destacar: lbl.set_fontweight("bold"); lbl.set_color(ACC)
    ax.set_xlim(-2, 9); ax.set_ylim(-.7, len(items) - .3)
    ax.axvline(0, color="#BBBBBB", lw=.8, zorder=0); ax.grid(axis="x", color="#EEEEEE", lw=.7); ax.set_axisbelow(True)
    for s_ in ("top", "right", "left"): ax.spines[s_].set_visible(False)
    ax.spines["bottom"].set_color("#BBBBBB"); ax.tick_params(axis="y", length=0); ax.tick_params(axis="x", colors=MUTED, labelsize=8)

from matplotlib.lines import Line2D
from matplotlib.patches import Patch
def leyenda(fig, x0, y, style):
    tk = lambda c: Line2D([], [], color=c, marker="|", ls="none", ms=11, mew=2.5)
    fill = Line2D([], [], color=ACC, marker="o", ls="none", ms=6)
    hol = Line2D([], [], color=ACC, marker="o", ls="none", ms=6, mfc="white", mew=1.6)
    if style == "claude": H = [(Patch(color=BANDA), "Rango de promedios"), (tk("#5A5F66"), "Prom. 2010-14"), (fill, "2025"), (hol, "2026e")]
    elif style == "chatgpt": H = [(Line2D([], [], color=YRS[1], marker="o", ls="none", ms=5), "2023-2025 (azules claros)"), (Line2D([], [], color="#0B2E6B", marker="D", ls="none", ms=5.5), "2026e"), (tk("black"), "Prom. 2010-14"), (tk(ORANGE), "Prom. 2015-19")]
    else: H = [(tk(DARK), "Prom. 2010-14"), (tk(LIGHT), "Prom. 2015-19"), (fill, "2025"), (hol, "2026e")]
    fig.legend([h for h, _ in H], [t for _, t in H], loc="center left", bbox_to_anchor=(x0 - .006, y), ncol=4, frameon=False,
               fontsize=7.8, handletextpad=.3, columnspacing=.9, handlelength=1.2)

COLS = [("claude", "1. Propuesta de Claude (primera versión)", "Franja gris entre promedios; 2025 y 2026e; ALC resaltada"),
        ("chatgpt", "2. Propuesta de ChatGPT", "Cuatro años, dos promedios y escala común; sin región destacada"),
        ("equipo", "3. Propuesta final del equipo", "Una marca por promedio; 2025 y 2026e; ALC resaltada")]

def figura(cols, fname, w):
    fig, axes = plt.subplots(2, len(cols), figsize=(w, 8.6), gridspec_kw={"hspace": .5, "wspace": .62})
    if len(cols) == 1: axes = [[axes[0]], [axes[1]]]
    fig.subplots_adjust(left=.12 if len(cols) > 1 else .3, right=.96, top=.80, bottom=.11)
    for j, (st, tit, sub) in enumerate(cols):
        a, b = axes[0][j], axes[1][j]
        panel(a, datos.REGIONES, st, "América Latina y el Caribe"); panel(b, datos.PAISES, st, None)
        bb = a.get_position(); x0 = bb.x0 - (.11 if len(cols) > 1 else .27)
        fig.text(x0, .905, tit, fontsize=12, fontweight="bold", color=TXT)
        fig.text(x0, .878, sub, fontsize=8.5, color=MUTED)
        leyenda(fig, x0, .845, st)
        a.text(-.6 if len(cols) > 1 else -.5, 1.06, "A. Regiones", transform=a.transAxes, fontsize=9.5, fontweight="bold", color=TXT)
        b.text(-.6 if len(cols) > 1 else -.5, 1.06, "B. ALC-6", transform=b.transAxes, fontsize=9.5, fontweight="bold", color=TXT)
    fig.text(.012, .965, "Tres propuestas de rediseño de la Figura 1.1 con los mismos datos", fontsize=15, fontweight="bold", color=TXT)
    fig.text(.012, .045, "Datos: Banco Mundial, Macro Poverty Outlook (octubre de 2026); promedios calculados por el equipo. Crecimiento del PIB real, %. Eje común de −2 a 9; valor de 2026e a la derecha.\n"
             "La propuesta de ChatGPT es una reconstrucción a partir de su descripción (gráfico de puntos con 2023-2026e, dos promedios y escala compartida), dibujada con los datos oficiales.",
             fontsize=7.8, color=MUTED, va="top")
    fig.savefig(fname, dpi=200); plt.close(fig)

figura(COLS, "comparacion_propuestas.png", 17)
print("ok")
