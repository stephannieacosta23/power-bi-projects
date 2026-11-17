# Power BI Projects

Dashboards and visualization work in Power BI, from the Master's in Business Intelligence at UNIR. Each project starts from a business or analytical question and includes the report file, the data, the DAX or chart specifications, and screenshots or a rendered sketch. Project documentation is in Spanish.

| Project | Question | Tools |
|---|---|---|
| [Know them to keep them: customer repurchase at AdventureWorks](unir-visualizacion-avanzada-act1) | Which customers buy again, how long do they take, and what do they buy together? | Power BI, Power Query, DAX, star schema, Azure Maps, bookmarks |
| [Redesigning a World Bank growth chart](unir-fundamentos-visualizacion-act1) | Can a grouped bar chart of GDP growth by region be made easier to read? | Power BI, Deneb (Vega-Lite), Python (matplotlib) |

## Opening the files

- `.pbix` files need an up-to-date Power BI Desktop (the AdventureWorks report uses the PBIR format).
- `.pbit` files are templates: Power BI asks for the path to the Excel file in the project's `datos/` folder when you open them.
- If Power BI can't find a data source, go to Transform data → Data source settings → Change source and point it to the file in `datos/`.
