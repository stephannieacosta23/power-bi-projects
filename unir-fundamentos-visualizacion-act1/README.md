# Rediseño de la Figura 1.1 del Banco Mundial

Actividad 1 de Fundamentos de Visualización de Datos, Máster Universitario en Inteligencia de Negocio (UNIR), Equipo 7 - Lote 41.

La actividad pide analizar críticamente una visualización publicada y proponer un rediseño. Elegimos la Figura 1.1 del *Panorama Económico de América Latina y el Caribe* (Banco Mundial, octubre de 2026, [doi:10.1596/978-1-4648-2363-3](https://doi.org/10.1596/978-1-4648-2363-3)), que compara el crecimiento del PIB real de seis regiones y de las seis mayores economías de América Latina (ALC-6) entre 2023 y 2026 con sus promedios de 2010-14 y 2015-19.

El original usa barras agrupadas con cuatro tonos de azul. La propuesta es un gráfico de puntos horizontal: punto relleno para 2025, punto hueco para 2026e, una marca por cada promedio histórico y una tabla con la diferencia de 2026e frente a cada promedio, en puntos porcentuales. América Latina va en azul y el resto en gris.

## Contenido

| Carpeta | Archivo | Qué es |
|---|---|---|
| `powerbi/` | `Actividad_1_FVAD.pbit` | Plantilla de Power BI con el modelo y los dos visuales Deneb (regiones y ALC-6) |
| `datos/` | `Crecimiento_PIB_region_pais_Banco_Mundial.xlsx` | Base preparada por el equipo con las series del Macro Poverty Outlook (Banco Mundial, octubre de 2026) |
| `datos/` | `datos_figura_1_1.csv` | Valores usados en el boceto: 2023-2026e y promedios 2010-14 y 2015-19 |
| `deneb/` | `spec_regiones.json`, `spec_paises_alc6.json` | Especificaciones Vega-Lite para el visual Deneb de Power BI |
| `python/` | `boceto.py`, `versiones.py`, `lineas.py`, `datos.py` | Boceto del rediseño, comparación de propuestas y alternativa en líneas (matplotlib) |

## Cómo usarlo

**Power BI.** Abre `Actividad_1_FVAD.pbit` y, cuando lo pida, apunta al Excel de `datos/`. Los visuales usan [Deneb](https://deneb-viz.github.io/), que se instala desde AppSource.

**Deneb por separado.** En un visual Deneb, agrega a *Values* los campos de la tabla (`Region` o `Country`, los dos promedios y los valores de 2025 y 2026e), elige Vega-Lite y pega el JSON en *Specification*.

**Python.**

```bash
pip install matplotlib
cd python
python boceto.py      # genera boceto_rediseno.png
```

## Notas

- Los promedios son la media simple de las tasas anuales de cada período, calculada por el equipo.
- 2026e es una estimación del Banco Mundial con fecha de corte del 23 de septiembre de 2026.
