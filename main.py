

ARCHIVO = "pinguinos_pequeno.csv"

CAMPOS_NUMERICOS = ["longitud_pico_mm", "profundidad_pico_mm", "longitud_aleta_mm", "masa_corporal_g"]
CAMPOS_TEXTO = ["especie", "isla", "sexo"]





def cargar_dataset(ruta):
    filas = []
    encabezados = []
    with open(ruta, "r", encoding="utf-8") as archivo:
        primera = True
        for linea in archivo:
            linea = linea.strip()
            if linea == "":
                continue
            campos = linea.split(",")
            if primera:
                encabezados = campos
                primera = False
            else:
                filas.append(campos)
    return encabezados, filas 


def mostrar_registro(encabezados, fila, numero):
    partes = []
    for i in range(len(encabezados)):
        partes.append(encabezados[i] + "=" + fila[i])
    print(f"{numero:>3}. " + " | ".join(partes))

def buscar(filas, termino):
    termino = termino.lower()
    encontrados = []
    for fila in filas:
        for campo in fila:
            if termino in campo.lower():
                encontrados.append(fila)
                break
    return encontrados


def estadisticas(encabezados, filas, campo):               
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
    indice = encabezados.index(campo)
    resultado = []
    for fila in filas:
        if float(fila[indice]) > umbral:
            resultado.append(fila)
    return resultado


def agrupar_por(encabezados, filas, campo):
    indice = encabezados.index(campo)
    valores = []
    conteos = []
    for fila in filas:
        v = fila[indice]
        if v in valores:
            conteos[valores.index(v)] += 1
        else:
            valores.append(v)
            conteos.append(1)

    for i in range(len(conteos)):
        mayor = i
        for j in range(i + 1, len(conteos)):
            if conteos[j] > conteos[mayor]:
                mayor = j
        conteos[i], conteos[mayor] = conteos[mayor], conteos[i]
        valores[i], valores[mayor] = valores[mayor], valores[i]
    return valores, conteos


def elegir_campo(opciones, mensaje):
    """Muestra una lista de opciones al usuario y retorna la opción seleccionada si es válida."""
    print(mensaje)
    for i in range(len(opciones)):
        print(f"  {i + 1}. {opciones[i]}")
    eleccion = input("Ingresa el número de opción: ").strip()
    if eleccion.isdigit() and 1 <= int(eleccion) <= len(opciones):
        return opciones[int(eleccion) - 1]
    print("Opción no válida. Inténtalo de nuevo.")
    return None


def mostrar_menu():
    """Muestra el menú principal de opciones de DataLab."""
    print("\n==========================================")
    print("     DataLab - Pingüinos de Palmer        ")
    print("==========================================")
    print("  1. Buscar un término")
    print("  2. Estadísticas básicas de un campo numérico")
    print("  3. Filtrar registros por valor mínimo (opcional)")
    print("  4. Agrupar por categoría (opcional)")
    print("  5. Salir")
    print("==========================================")




def main():
    encabezados, filas = cargar_dataset(ARCHIVO)
    print(f"Dataset cargado: {len(filas)} registros, {len(encabezados)} columnas.")

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            termino = input("Término a buscar (ej. Papua, Biscoe, HEMBRA): ").strip()
            print("Escribe algo para buscar.")
            resultados = buscar(filas, termino)
            for i in range(len(resultados)):
                mostrar_registro(encabezados, resultados[i], i + 1)
            print(f"Se encontraron {len(resultados)} registros.")

        elif opcion == "2":
            campo = elegir_campo(CAMPOS_NUMERICOS, "¿Qué campo numérico?")
            if campo:
                maximo, minimo, promedio = estadisticas(encabezados, filas, campo)
                print(f"Máximo: {maximo} · Mínimo: {minimo} · Promedio: {promedio:.1f}")

        elif opcion == "3":
            campo = elegir_campo(CAMPOS_NUMERICOS, "¿Qué campo numérico?")
            if campo:
                try:
                    umbral = float(input(f"Mostrar registros con {campo} mayor a: "))
                except ValueError:
                    print("Debes ingresar un número.")
                    continue
                resultados = filtrar_mayor_que(encabezados, filas, campo, umbral)
                for i in range(len(resultados)):
                    mostrar_registro(encabezados, resultados[i], i + 1)
                print(f"Se encontraron {len(resultados)} registros.")

        elif opcion == "4":
            campo = elegir_campo(CAMPOS_TEXTO, "¿Agrupar por qué campo?")
            if campo:
                valores, conteos = agrupar_por(encabezados, filas, campo)
                partes = []
                for i in range(len(valores)):
                    partes.append(f"{valores[i]}: {conteos[i]}")
                print(" · ".join(partes))

        elif opcion == "5":
            print("¡Hasta pronto!")
            break

        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
