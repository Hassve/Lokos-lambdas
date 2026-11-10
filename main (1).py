"""main.py - Menú interactivo de DataLab (Entrega 2). Solo interfaz de consola."""
import analisis
import archivos

ARCHIVO_DATOS = "pinguinos_completo.csv"


def mostrar_registro(encabezados, fila, numero):
    partes = []
    for i in range(len(encabezados)):
        partes.append(encabezados[i] + "=" + fila[i])
    print(f"{numero:>3}. " + " | ".join(partes))


def mostrar_registros(encabezados, filas):
    for i in range(len(filas)):
        mostrar_registro(encabezados, filas[i], i + 1)
    print(f"Se encontraron {len(filas)} registros.")


def elegir_campo(opciones, mensaje):
    """Muestra opciones numeradas y retorna la elegida (o None si no es válida)."""
    print(mensaje)
    for i in range(len(opciones)):
        print(f"  {i + 1}. {opciones[i]}")
    eleccion = input("Ingresa el número de opción: ").strip()
    if eleccion.isdigit() and 1 <= int(eleccion) <= len(opciones):
        return opciones[int(eleccion) - 1]
    print("Opción no válida.")
    return None


def mostrar_menu():
    print("\n==========================================")
    print("   DataLab - Pingüinos de Palmer (E2)")
    print("==========================================")
    print(" 1. Buscar un término")
    print(" 2. Estadísticas básicas de un campo numérico")
    print(" 3. Filtrar registros por valor mínimo")
    print(" 4. Agrupar por categoría")
    print(" 5. Comparar dos grupos")
    print(" 6. Ver historial de consultas")
    print(" 7. Cargar un resultado guardado")
    print(" 8. Ver resumen del dataset")
    print(" 9. Salir")
    print("==========================================")


def ofrecer_guardar(encabezados, filas):
    """Pregunta si se quieren guardar los resultados y, si sí, los escribe en CSV."""
    if len(filas) == 0:
        return
    if input("¿Guardar estos resultados? (s/n): ").strip().lower() != "s":
        return
    nombre = input("Nombre para el archivo (ej. grandes): ")
    ruta = archivos.guardar_resultado(nombre, encabezados, filas)
    if ruta is None:
        print("Nombre no válido, no se guardó.")
    else:
        print(f"Guardado en {ruta}")


def opcion_buscar(encabezados, filas):
    termino = input("Término a buscar (ej. Papua, Biscoe, HEMBRA): ").strip()
    if termino == "":
        print("Escribe algo para buscar.")
        return
    resultados = analisis.buscar(filas, termino)
    mostrar_registros(encabezados, resultados)
    archivos.registrar_historial(f"buscar: {termino}", len(resultados))
    ofrecer_guardar(encabezados, resultados)


def opcion_estadisticas(encabezados, filas):
    campo = elegir_campo(analisis.CAMPOS_NUMERICOS, "¿Qué campo numérico?")
    if campo:
        maximo, minimo, promedio = analisis.estadisticas(encabezados, filas, campo)
        print(f"Máximo: {maximo} · Mínimo: {minimo} · Promedio: {promedio:.1f}")


def opcion_filtrar(encabezados, filas):
    campo = elegir_campo(analisis.CAMPOS_NUMERICOS, "¿Qué campo numérico?")
    if not campo:
        return
    try:
        umbral = float(input(f"Mostrar registros con {campo} mayor a: "))
    except ValueError:
        print("Debes ingresar un número.")
        return
    resultados = analisis.filtrar_mayor_que(encabezados, filas, campo, umbral)
    mostrar_registros(encabezados, resultados)
    archivos.registrar_historial(f"{campo} mayor a {umbral}", len(resultados))
    ofrecer_guardar(encabezados, resultados)


def opcion_agrupar(encabezados, filas):
    campo = elegir_campo(analisis.CAMPOS_TEXTO, "¿Agrupar por qué campo?")
    if campo:
        pares = analisis.agrupar_por(encabezados, filas, campo)
        partes = []
        for categoria, cantidad in pares:
            partes.append(f"{categoria}: {cantidad}")
        print(" · ".join(partes))


