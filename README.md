# DataLab – Análisis exploratorio de pingüinos de Palmer (Entrega 2: Analizador)

**Grupo:** LokosLambda · **Curso:** Programación de Computadores 2026-2 · Universidad Nacional de Colombia

## Descripción
Programa de consola en Python para explorar datos reales de pingüinos del archipiélago de Palmer (especie, isla, medidas de pico, aleta, masa y sexo). En esta entrega el programa carga el dataset completo con el módulo `csv`, organiza los datos en listas, diccionarios y conjuntos, **guarda y recupera resultados** y **registra un historial** de consultas.

## Preguntas que queremos responder
- ¿Qué especie es más pesada y cuánto difiere de las otras?
- ¿Cómo cambian las medidas entre machos y hembras?
- ¿Qué isla concentra más registros de cada especie?

## Datos
- `pinguinos_completo.csv`: 333 registros, 7 columnas (se usa desde la Entrega 2).
- `pinguino_pequeno.csv`: subconjunto de 50 registros (Entrega 1).

Columnas: `especie`, `isla`, `longitud_pico_mm`, `profundidad_pico_mm`, `longitud_aleta_mm`, `masa_corporal_g`, `sexo`.

## Estructura
```
DataLab-Pinguinos/
├── main.py                  ← solo el menú interactivo
├── analisis.py              ← búsqueda, estadísticas, filtro, agrupación, comparación y resumen
├── archivos.py              ← lectura/escritura CSV y JSON, historial y resultados guardados
├── pinguinos_completo.csv
├── pinguino_pequeno.csv
├── historial.csv            ← se genera solo al hacer consultas
├── resumen.json             ← se genera solo al iniciar
├── resultado_<nombre>.csv   ← se generan cuando el usuario guarda resultados
└── README.md
```

## Cómo ejecutar
1. Instala Python 3 (no se necesitan librerías externas).
2. Descarga o clona el repositorio y deja todos los archivos en la misma carpeta.
3. En una terminal, dentro de la carpeta: `python3 main.py` (o `python main.py`).

## Menú
| Opción | Qué hace |
|---|---|
| 1. Buscar un término | Muestra los registros que lo contienen y cuántos hay. Se anota en el historial y ofrece guardar. |
| 2. Estadísticas básicas | Máximo, mínimo y promedio de un campo numérico. |
| 3. Filtrar por valor mínimo | Registros con un campo numérico mayor a un valor. Se anota en el historial y ofrece guardar. |
| 4. Agrupar por categoría | Conteo por especie, isla o sexo, de mayor a menor. |
| 5. Comparar dos grupos *(opcional)* | Cantidad, máximo, mínimo y promedio de dos valores de un campo de texto. |
| 6. Ver historial | Muestra `historial.csv`: fecha y hora, consulta y número de resultados. |
| 7. Cargar resultado guardado | Recupera un `resultado_<nombre>.csv` de una sesión anterior sin reprocesar. |
| 8. Ver resumen *(opcional)* | Muestra `resumen.json`, generado automáticamente al iniciar. |
| 9. Salir | Termina el programa. |

## Estructuras de datos y para qué se usan
- **Lista de listas:** cada fila del dataset, conserva el orden original.
- **Diccionario:** conteos por categoría, resultados de comparaciones y el resumen (se accede por nombre).
- **Conjunto (`set`):** valores únicos de un campo, sin repetidos.

## Archivos y módulos
- `archivos.py`: `cargar_csv`, `guardar_csv`, `cargar_json`, `guardar_json`, `guardar_resultado`, `listar_resultados`, `registrar_historial`, `leer_historial`.
- `analisis.py`: `buscar`, `estadisticas`, `filtrar_mayor_que`, `agrupar_por`, `valores_unicos`, `comparar_grupos`, `generar_resumen`.
- `main.py`: menú y funciones de interacción; no contiene lógica de análisis.

## Notas
- Esta entrega usa solo `csv`, `json`, `os` y `datetime` de la biblioteca estándar (sin Pandas).
- Los campos numéricos y de texto están definidos en `analisis.py` (`CAMPOS_NUMERICOS`, `CAMPOS_TEXTO`).
