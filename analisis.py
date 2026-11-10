CAMPOS_NUMERICOS = ["longitud_pico_mm", "profundidad_pico_mm",
                    "longitud_aleta_mm", "masa_corporal_g"]
CAMPOS_TEXTO = ["especie", "isla", "sexo"]


def buscar(filas, termino):
    """Retorna las filas con algún campo que contenga el término (sin importar mayúsculas)."""
    termino = termino.lower()
    encontrados = []
    for fila in filas:
        for campo in fila:
            if termino in campo.lower():
                encontrados.append(fila)
                break
    return encontrados


def estadisticas(encabezados, filas, campo):
    """Retorna (máximo, mínimo, promedio) de un campo numérico con acumuladores."""
    indice = encabezados.index(campo)
    maximo = None
    minimo = None
    suma = 0.0
    cantidad = 0
    for fila in filas:
        valor = float(fila[indice])
        if maximo is None or valor > maximo:
            maximo = valor
        if minimo is None or valor < minimo:
            minimo = valor
        suma += valor
        cantidad += 1
    if cantidad == 0:
        return None, None, None
    return maximo, minimo, suma / cantidad


def filtrar_mayor_que(encabezados, filas, campo, umbral):
    """Retorna las filas cuyo valor en `campo` es estrictamente mayor que `umbral`."""
    indice = encabezados.index(campo)
    resultado = []
    for fila in filas:
        if float(fila[indice]) > umbral:
            resultado.append(fila)
    return resultado


def agrupar_por(encabezados, filas, campo):
    """Cuenta registros por categoría con un diccionario.

    Retorna una lista de pares (categoría, cantidad) de mayor a menor.
    """
    indice = encabezados.index(campo)
    conteos = {}
    for fila in filas:
        categoria = fila[indice]
        conteos[categoria] = conteos.get(categoria, 0) + 1
    return sorted(conteos.items(), key=lambda par: par[1], reverse=True)


def valores_unicos(encabezados, filas, campo):
    """Retorna la lista ordenada de valores distintos de un campo (usa un set)."""
    indice = encabezados.index(campo)
    unicos = set()
    for fila in filas:
        unicos.add(fila[indice])
    return sorted(unicos)


def comparar_grupos(encabezados, filas, campo_texto, valor_a, valor_b, campo_num):
    """Opcional 1: compara dos valores de un campo de texto.

    Retorna un diccionario {valor: {"cantidad", "maximo", "minimo", "promedio"}}.
    """
    indice = encabezados.index(campo_texto)
    resultado = {}
    for valor in (valor_a, valor_b):
        grupo = []
        for fila in filas:
            if fila[indice].lower() == valor.lower():
                grupo.append(fila)
        maximo, minimo, promedio = estadisticas(encabezados, grupo, campo_num)
        resultado[valor] = {"cantidad": len(grupo), "maximo": maximo,
                            "minimo": minimo, "promedio": promedio}
    return resultado


def generar_resumen(encabezados, filas):
    """Opcional 2: diccionario con estadísticas clave del dataset (para resumen.json)."""
    resumen = {"total_registros": len(filas), "valores_unicos": {}, "numericos": {}}
    for campo in CAMPOS_TEXTO:
        resumen["valores_unicos"][campo] = len(valores_unicos(encabezados, filas, campo))
    for campo in CAMPOS_NUMERICOS:
        maximo, minimo, promedio = estadisticas(encabezados, filas, campo)
        resumen["numericos"][campo] = {"maximo": maximo, "minimo": minimo,
                                       "promedio": round(promedio, 2)}
    return resumen
