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


def opcion_comparar(encabezados, filas):
    campo_texto = elegir_campo(analisis.CAMPOS_TEXTO, "¿Qué campo de texto comparar?")
    if not campo_texto:
        return
    unicos = analisis.valores_unicos(encabezados, filas, campo_texto)
    print("Valores disponibles: " + ", ".join(unicos))
    a = input("Primer valor: ").strip()
    b = input("Segundo valor: ").strip()
    if a.lower() not in [u.lower() for u in unicos] or b.lower() not in [u.lower() for u in unicos]:
        print("Alguno de los valores no existe en ese campo.")
        return
    campo_num = elegir_campo(analisis.CAMPOS_NUMERICOS, "¿Qué campo numérico usar?")
    if not campo_num:
        return
    res = analisis.comparar_grupos(encabezados, filas, campo_texto, a, b, campo_num)
    for valor, datos in res.items():
        print(f"{valor}: {datos['cantidad']} registros · "
              f"Máx: {datos['maximo']} · Mín: {datos['minimo']} · "
              f"Promedio: {datos['promedio']:.1f}")


def opcion_historial():
    entradas = archivos.leer_historial()
    if not entradas:
        print("Aún no hay consultas en el historial.")
        return
    for fecha, consulta, cantidad in entradas:
        print(f"{fecha}, {consulta}, {cantidad} resultados")


def opcion_cargar_resultado():
    guardados = archivos.listar_resultados()
    if not guardados:
        print("No hay resultados guardados todavía.")
        return
    ruta = elegir_campo(guardados, "¿Qué resultado quieres cargar?")
    if ruta:
        enc, filas = archivos.cargar_csv(ruta)
        mostrar_registros(enc, filas)


def opcion_resumen():
    try:
        resumen = archivos.cargar_json(archivos.ARCHIVO_RESUMEN)
    except FileNotFoundError:
        print("No se encontró resumen.json.")
        return
    print(f"Total de registros: {resumen['total_registros']}")
    for campo, n in resumen["valores_unicos"].items():
        print(f"  {campo}: {n} valores distintos")
    for campo, d in resumen["numericos"].items():
        print(f"  {campo}: máx {d['maximo']} · mín {d['minimo']} · prom {d['promedio']}")


def main():
    encabezados, filas = archivos.cargar_csv(ARCHIVO_DATOS)
    print(f"Dataset cargado: {len(filas)} registros, {len(encabezados)} columnas.")
    archivos.guardar_json(archivos.ARCHIVO_RESUMEN, analisis.generar_resumen(encabezados, filas))

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            opcion_buscar(encabezados, filas)
        elif opcion == "2":
            opcion_estadisticas(encabezados, filas)
        elif opcion == "3":
            opcion_filtrar(encabezados, filas)
        elif opcion == "4":
            opcion_agrupar(encabezados, filas)
        elif opcion == "5":
            opcion_comparar(encabezados, filas)
        elif opcion == "6":
            opcion_historial()
        elif opcion == "7":
            opcion_cargar_resultado()
        elif opcion == "8":
            opcion_resumen()
        elif opcion == "9":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
