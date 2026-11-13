import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import datos
plt.rcParams["font.family"] = ["Liberation Sans"]
ACC, GRIS, BANDA, TXT, MUTED = "#1F5AA6", "#8C8C8C", "#E3E6EA", "#222222", "#666666"

def panel(ax, data, destacar, titulo):
    items = sorted(data.items(), key=lambda kv: kv[1][3])          # ascendente -> mayor arriba
    for i, (k, v) in enumerate(items):
        _, _, y25, y26, p1, p2 = v
        col = ACC if (destacar is None or k == destacar) else GRIS
        if p1 is not None:
            ax.plot([p1, p1], [i + 0.19, i + 0.47], color="#3A3F45", lw=3.4, zorder=2, solid_capstyle="butt")
        if p2 is not None:
            ax.plot([p2, p2], [i + 0.19, i + 0.47], color="#A3A9B0", lw=3.4, zorder=2, solid_capstyle="butt")
        ax.add_patch(FancyArrowPatch((y25, i), (y26, i), arrowstyle="-", color=col, lw=1.6, zorder=3))
        ax.scatter(y25, i, s=70, color=col, zorder=4)
        ax.scatter(y26, i, s=80, facecolor="white", edgecolor=col, linewidth=2, zorder=5)
        f = lambda x: f"{x:.1f}".replace(".", ",").replace("-", "−")
        d = lambda x: ("+" if x >= 0 else "−") + f"{abs(x):.1f}".replace(".", ",")
        strong = col == ACC
        for xc, txt in ((10.5, f(y26)), (12.0, d(y26 - p1)), (13.5, d(y26 - p2))):
            ax.text(xc, i, txt, va="center", ha="right", fontsize=10.5, clip_on=False,
                    color=ACC if strong else TXT, fontweight="bold" if (strong and xc == 10.5) else "normal")
    ax.set_yticks(range(len(items)))
    ax.set_yticklabels([k for k, _ in items], fontsize=10, color=TXT)
    for lbl, (k, _) in zip(ax.get_yticklabels(), items):
        if destacar and k == destacar: lbl.set_fontweight("bold"); lbl.set_color(ACC)
    ax.set_xlim(-2, 9); ax.set_ylim(-0.7, len(items) - 0.4)
    ax.axvline(0, color="#BBBBBB", lw=1, zorder=0)
    ax.grid(axis="x", color="#EEEEEE", lw=0.8); ax.set_axisbelow(True)
    for s in ("top", "right", "left"): ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color("#BBBBBB")
    ax.tick_params(axis="y", length=0); ax.tick_params(axis="x", colors=MUTED, labelsize=9)
    ax.text(-0.44, 1.07, titulo, transform=ax.transAxes, fontsize=11.5, fontweight="bold", color=TXT)
    for xc, h in ((10.5, "2026e"), (12.0, "− Prom.\n2010-14"), (13.5, "− Prom.\n2015-19")):
        ax.text(xc, len(items) - 0.45, h, ha="right", va="bottom", fontsize=8.5, color=MUTED, clip_on=False, linespacing=1.0)

fig, (a, b) = plt.subplots(2, 1, figsize=(10.2, 8.4), gridspec_kw={"height_ratios": [1, 1], "hspace": 0.42})
fig.subplots_adjust(left=0.265, right=0.76, top=0.83, bottom=0.12)
fig.text(0.02, 0.965, "ALC crecería 2,2 % en 2026: por encima de 2015-19, pero lejos de su ritmo de 2010-14",
         fontsize=13, fontweight="bold", color=TXT)
fig.text(0.02, 0.935, "Crecimiento del PIB real (%). Mismo eje en ambos paneles; filas ordenadas por 2026e. A la derecha, diferencia de 2026e con cada promedio (p.p.).",
         fontsize=9.5, color=MUTED)
# leyenda dibujada (arriba, cerca de los datos)
ly = 0.895
fig.lines.append(plt.Line2D([0.025, 0.025], [ly - 0.013, ly + 0.013], transform=fig.transFigure, color="#3A3F45", lw=3.4))
fig.text(0.035, ly, "Promedio 2010-14", va="center", fontsize=9, color=TXT)
fig.lines.append(plt.Line2D([0.19, 0.19], [ly - 0.013, ly + 0.013], transform=fig.transFigure, color="#A3A9B0", lw=3.4))
fig.text(0.2, ly, "Promedio 2015-19", va="center", fontsize=9, color=TXT)
fig.lines.append(plt.Line2D([0.36], [ly], transform=fig.transFigure, marker="o", ms=8, color=ACC))
fig.text(0.37, ly, "2025", va="center", fontsize=9, color=TXT)
fig.lines.append(plt.Line2D([0.43], [ly], transform=fig.transFigure, marker="o", ms=8, mfc="white", mec=ACC, mew=2))
fig.text(0.44, ly, "2026e: estimación", va="center", fontsize=9, color=TXT)
fig.text(0.62, ly, "Azul: América Latina y el Caribe", va="center", fontsize=9, color=ACC, fontweight="bold")

panel(a, datos.REGIONES, "América Latina y el Caribe", "A. Regiones: 5 de 6 crecerían por debajo de su promedio 2010-14")
panel(b, datos.PAISES, None, "B. ALC-6: ninguno alcanza su promedio 2010-14; Brasil y Argentina superan el de 2015-19")
fig.text(0.02, 0.05, "Fuente: elaboración propia con datos del Macro Poverty Outlook del Banco Mundial (Reuniones Anuales, octubre de 2026), base de la Figura 1.1\n"
         "del Panorama Económico de América Latina y el Caribe. Promedios: media simple de las tasas anuales. Diferencias en puntos porcentuales; cálculo propio.",
         fontsize=7.8, color=MUTED, va="top")
fig.savefig("boceto_rediseno.png", dpi=220)
print("ok")
