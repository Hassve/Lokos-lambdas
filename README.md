[README.md](https://github.com/user-attachments/files/33794012/README.md)
**Datalab Análisis exploratorio de datos de pingüinos**

**Descripción:**

Por medio de este Datalab se ejecuta un programa en python que permite analizar una tabla de datos relacionado a los pingüinos del archipiélago de  Palmer

El programa hace usa de un archico csv con la informacion de los pingúinos, respecto a su especie, isla, medidas de pico, longitud de aletas su masa y sexo

Dentro encontraras un menu interactivo donde se podrá realizar búsquedas, obtener estadísticas descriptivas, filtrar registros y agrupar la información por categorías

**Objetivos y preguntas a responder con el programa**   
Implementar funciones para procesar y analizar datos, leer y organizar la información, aplicar operaciones sobre datos numéricos y de clasificación, permitir la búsqueda y el filtrado de registros según criterios del usuario.

Dentro del programa utilizamos Python 3 como lenguaje principal, dataset en formato CSV formato y la terminal como interfaz de interacción con el usuario.

El programa utiliza las funcionalidades básicas de Python y no requiere bibliotecas externas para las operaciones

**Datos**

El programa utiliza el archivo *`pinguinos_pequeno.csv`*, que contiene 50 registros y 7 columnas.

Las variables incluidas en el conjunto de datos son:

Especie: Especie del pingüino.

Isla: Isla asociada al registro.

Longitud\_pico\_mm: Longitud del pico en milímetros.

Profundidad\_pico\_mm : Profundidad del pico en milímetros. 

Longitud\_aleta\_mm : Longitud de la aleta en milímetros. 

Masa\_corporal\_g: Masa corporal en gramos. 

Sexo: Sexo registrado del pingüino.

**Funciones:**

El programa ofrece un menú interactivo con las siguientes opciones:

**1\. Buscar un término**

Permite buscar un texto dentro de los campos de los registros.

La búsqueda funciona independientemente de si el texto está en mayúsculas o minúsculas, por lo que es posible encontrar coincidencias sin importar cómo se escriba el término.

Los registros encontrados se muestran en la terminal.

**2\. Cálculos estadísticos**

Se selecciona una variable numérica y se obtienen tres medidas descriptivas:

Máximo: valor más alto del campo seleccionado

Mínimo: valor más bajo del campo seleccionado

Promedio: media aritmética de los valores seleccionados

Las variables numéricas disponibles son la longitud del pico, la profundidad del pico, la longitud de la aleta y la masa corporal.

**3\. Filtrar registros**

Permite seleccionar un campo numérico e introducir un umbral/límite

El programa muestra los registros cuyo valor en el campo seleccionado sea estrictamente mayor que el umbral indicado.

Si el usuario introduce un valor que no es numérico, el programa muestra un mensaje de error y lo devuelve al menú.

**4\. Agrupar por categoría**

Permite agrupar los registros según una variable categórica.

Las opciones disponibles son especie, isla y sexo.

El programa cuenta cuántos registros corresponden a cada categoría y presenta los resultados ordenados de mayor a menor frecuencia.

**5\. Salir**

Finaliza la ejecución del programa.

**Estructura**

Los archivos deben estar organizados de la siguiente manera:

DataLab-Pinguinos/  
├── main.py  
├── pinguinos\_pequeno.csv  
└── README.md

* `main.py`: contiene el código fuente y las funciones del programa.  
* `pinguinos_pequeno.csv`: contiene los datos utilizados para el análisis.  
* `README.md`: documenta el proyecto y explica cómo utilizarlo.

**Instalación y ejecución**

**Primero**

* Tener Python 3 instalado.  
* Descargar o disponer de los archivos del proyecto.  
* Contar con una terminal o un editor de código que permita ejecutar Python.

**Para ejecutar**

1. Descarga o clona el repositorio.  
2. Asegúrate de que el archivo CSV se encuentre en la misma carpeta que `main.py`.  
3. Abre una terminal en la carpeta del proyecto.  
4. Ejecuta el siguiente comando:

python3 main.py o python main.py

Al iniciar, el programa carga el conjunto de datos y muestra la cantidad de registros y columnas disponibles.

Después, presenta el menú principal para que el usuario seleccione la operación que desea realizar.

## 

El programa está organizado mediante funciones, cada una encargada de una tarea específica.

Entre las principales funciones se encuentran:

| Función | Que hace |
| ----- | ----- |
| `cargar_dataset()` | Lee el archivo y separa los encabezados de los registros. |
| `mostrar_registro()` | Presenta un registro con los nombres de sus campos. |
| `buscar()` | Busca coincidencias de un término en los registros |
| `estadisticas()` | Calcula el máximo, el mínimo y el promedio de un campo numérico. |
| `filtrar_mayor_que()` | Selecciona los registros que superan un límite seleccionado |
| `agrupar_por()` | Cuenta y ordena las categorías según su frecuencia. |
| `elegir_campo()` | Permite seleccionar un campo desde el menu |
| `mostrar_menu()` | Presenta las opciones disponibles. |
| `main()` | Coordina la ejecución del programa y la interacción  |

Esta organización modular permite separar las distintas operaciones y facilita la lectura y el mantenimiento del código.

**Para tener en cuenta** 

* El archivo CSV debe conservar los encabezados y el orden de las columnas esperados por el programa.  
* Las operaciones estadísticas y de filtrado están diseñadas para campos numéricos   
* El programa está diseñado para ejecutarse desde la terminal mediante un menú de texto.
