import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import datos
plt.rcParams["font.family"] = ["Liberation Sans"]
ACC, GRIS, TXT, MUTED = "#1F5AA6", "#B5B9BE", "#222222", "#666666"
X = [0, 1, 2, 3]; XL = ["2023", "2024", "2025", "2026e"]
fmt = lambda v: f"{v:.1f}".replace(".", ",").replace("-", "−")
nombres = {"Oriente Medio, Norte de África,\nAfganistán y Pakistán": "Oriente Medio y N. África"}

fig = plt.figure(figsize=(12, 9.6))
fig.text(0.03, 0.965, "El crecimiento de ALC se mantiene cerca de 2 % entre 2023 y 2026", fontsize=16, fontweight="bold", color=TXT)
fig.text(0.03, 0.937, "Crecimiento del PIB real (%). Línea continua: datos observados; línea punteada: estimación 2026. Misma escala en todos los paneles.", fontsize=10, color=MUTED)

# Panel A: regiones, ALC resaltada
axA = fig.add_axes([0.06, 0.53, 0.40, 0.34])
for k, v in datos.REGIONES.items():
    y = v[:4]; alc = k == "América Latina y el Caribe"
    c, lw, z = (ACC, 3, 5) if alc else (GRIS, 1.8, 2)
    axA.plot(X[:3], y[:3], color=c, lw=lw, zorder=z, marker="o", ms=4)
    axA.plot(X[2:], y[2:], color=c, lw=lw, zorder=z, ls=(0, (2, 2)))
    axA.scatter(3, y[3], s=40, facecolor="white", edgecolor=c, lw=2, zorder=z + 1)
    lbl = nombres.get(k, k)
    off = {"Asia Oriental y Pacífico": .3, "África Subsahariana": -.2, "Europa y Asia Central": .2, "América Latina y el Caribe": -.25}.get(k, 0)
    axA.text(3.12, y[3] + off, f"{lbl}  {fmt(y[3])}", va="center", fontsize=9, color=c if alc else MUTED, fontweight="bold" if alc else "normal")
axA.set_title("A. Regiones", loc="left", fontsize=12, fontweight="bold", color=TXT)

# Panel B: small multiples ALC-6
pos = [(0.06, 0.08), (0.27, 0.08), (0.48, 0.08), (0.69, 0.08)]
fig.text(0.03, 0.455, "B. ALC-6", fontsize=12, fontweight="bold", color=TXT)
paises = list(datos.PAISES.items())
w, h = 0.135, 0.15
axes = []
for i, (k, v) in enumerate(paises):
    r, c_ = divmod(i, 3)
    ax = fig.add_axes([0.06 + c_ * 0.155, 0.25 - r * 0.2, w, h]); axes.append(ax)
    for k2, v2 in paises:
        if k2 != k: ax.plot(X, v2[:4], color="#E3E6EA", lw=1.2, zorder=1)
    y = v[:4]
    ax.plot(X[:3], y[:3], color=ACC, lw=2.5, marker="o", ms=3.5, zorder=3)
    ax.plot(X[2:], y[2:], color=ACC, lw=2.5, ls=(0, (2, 2)), zorder=3)
    ax.scatter(3, y[3], s=34, facecolor="white", edgecolor=ACC, lw=2, zorder=4)
    ax.text(3.15, y[3], fmt(y[3]), va="center", fontsize=9, color=ACC, fontweight="bold")
    ax.set_title(k, loc="left", fontsize=10, color=TXT, pad=3)
    axes[-1]._row = r

for ax in [axA] + axes:
    ax.set_ylim(-2.5, 8); ax.set_xlim(-0.2, 3.2)
    ax.axhline(0, color="#BBBBBB", lw=.8, zorder=0)
    ax.grid(axis="y", color="#EEEEEE", lw=.7); ax.set_axisbelow(True)
    for s in ("top", "right", "left"): ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color("#BBBBBB")
    ax.tick_params(colors=MUTED, labelsize=8.5, length=0)
    ax.set_xticks(X); ax.set_xticklabels(XL)
for ax in axes:
    ax.set_yticks([0, 4, 8])
    if getattr(ax, "_row", 0) == 0: ax.set_xticklabels([])
# nota a la derecha del panel B
fig.text(0.56, 0.32, "Cada panel muestra un país en azul\ny los otros cinco en gris de fondo,\npara comparar sin mezclar líneas.", fontsize=9.5, color=MUTED, va="center")
fig.text(0.03, 0.015, "Fuente: elaboración propia con datos del Macro Poverty Outlook, Banco Mundial (octubre de 2026).", fontsize=8.5, color=MUTED)
fig.savefig("ejemplo_lineas_2023_2026.png", dpi=170)
print("ok")
