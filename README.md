Algorismia i Programació Audiovisual
====================================

Examen Final - Primavera de 2025
--------------------------------

<span style="color:red">Importante</span>
-----------------------------------------

Rellene la tabla siguiente con los nombres completos y la nota aspirada de cada participante. Recuerde que
si este examen se realiza en solitario, la nota aspirada es 10; si se realiza entre dos, la suma de las
notas aspiradas tiene que ser igual a 16; y si se realiza entre tres, las suma tiene que ser 18.

| Nombre completo              | Nota Aspirada |
| ---------------------------- | ------------- |
| Eduard Peñas Balart         | 10             |
| Thomas Lessing Lasheras        | 6             |

<span style="color:red">También Importante</span>
-------------------------------------------------

Se recuerda que los ejercicios más parecidos de lo razonable se repartirán la nota. Es decir, si dos ejercicios
merecedores de 10 se parecen mucho, la nota de cada uno será $10/2 = 5$; si
el parecido es entre tres ejercicios, la nota será $10/3=3,33$.

Ejercicio 1: Programa de Normalización de Expresiones Horarias (20%)
----------------------------------------------------------------------

- Construya el programa `normaliza.py`que permita leer un fichero de texto, normalice
  las expresiones horarias en él contenidas según las instrucciones de la tarea APA-T6
  y escriba el resultado en otro fichero de texto.
- El fichero de entrada y el nombre del fichero de salida tendrán la extensión `.txt` y
  se escogerán usando las funciones gráficas de `TkInter.filedialog`.
- No se evaluará la calidad de la normalización (ese aspecto se evalúa en APA-T6).

```python
import re
import tkinter as tk
from tkinter import filedialog

def normalizahoras(fileIn, fileOut):
    """
    Leer lo que contiene fileIn y escribirlo en fileOut
    """
    
    rehm = r"(?P<hh>\d\d?)[hH]((?P<mm>\d\d?)[mM])?"
    rehh_en_punto = r'(?P<hh_en_punto>\d\d?) en punto'
    rehh_y_media = r'(?P<hh_y_media>\d\d?) y media'
    rehh_menos_cuarto = r'(?P<hh_menos_cuarto>\d\d?) menos cuarto'
    rehh_y_cuarto = r'(?P<hh_y_cuarto>\d\d?) y cuarto'
    rehh_12 = r'(?P<hh_12>\d\d?) de la noche'
    renum = r'(?P<num>\d)\s+(?P<texto>[a-zA-ZàÀéÉèÈóÓòÒíÍúÚçÇñ\s]+)'

    with open(fileIn, "rt") as fpIn, open(fileOut, "wt") as fpOut:
        for linea in fpIn:
            while (match := re.search(rehm, linea)):
                fpOut.write(linea[: match.start()])
                if match.group("mm", "hh"):
                    hora = int(match["hh"])
                    min = int(match["mm"]) if match["mm"] else 0
                    if min > 60:
                        hora += 1
                        min -= 60
                fpOut.write(f'{hora:02d}:{min:02d}')
                linea = linea[match.end():]
                
            while (match := re.search(rehh_en_punto, linea)):
                fpOut.write(linea[: match.start()])
                if match.group("hh_en_punto"):
                    hora = int(match["hh_en_punto"])
                    min = 0
                fpOut.write(f'{hora:02d}:{min:02d}')
                linea = linea[match.end():]
                
            while (match := re.search(rehh_y_media, linea)):
                fpOut.write(linea[: match.start()])
                if match.group("hh_y_media"):
                    hora = int(match["hh_y_media"])
                    min = 30
                fpOut.write(f'{hora:02d}:{min:02d}')
                linea = linea[match.end():]
                
            while (match := re.search(rehh_menos_cuarto, linea)):
                fpOut.write(linea[: match.start()])
                if match.group("hh_menos_cuarto"):
                    hora = int(match["hh_menos_cuarto"]) - 1
                    min = 45
                fpOut.write(f'{hora:02d}:{min:02d}')
                linea = linea[match.end():]
                
            while (match := re.search(rehh_y_cuarto, linea)):
                fpOut.write(linea[: match.start()])
                if match.group("hh_y_cuarto"):
                    hora = int(match["hh_y_cuarto"])
                    min = 15
                fpOut.write(f'{hora:02d}:{min:02d}')
                linea = linea[match.end():]
                
            while (match := re.search(rehh_12, linea)):
                fpOut.write(linea[: match.start()])
                if match.group("hh_12"):
                    hora = int(match["hh_12"]) - 12
                    min = 0
                fpOut.write(f'{hora:02d}:{min:02d}')
                linea = linea[match.end():]
                
            while (match := re.search(renum, linea)):
                fpOut.write(linea[: match.start()])
                if match.group("num"):
                    num = int(match["num"])
                    texto = match["texto"]
                    if num == 7:
                        num = str("siete")
                fpOut.write(f'{num} {texto}')
                linea = linea[match.end():]
                
            fpOut.write(linea)

def seleccionar_archivos():
    """
    Abre un cuadro de diálogo para seleccionar archivos de entrada y salida
    y llama a la función normalizahoras.
    """
    root = tk.Tk()
    root.withdraw()  # Ocultamos la ventana principal de Tkinter

    # Seleccionar el archivo de entrada
    fileIn = filedialog.askopenfilename(title="Seleccionar archivo de entrada", filetypes=[("Text files", "*.txt")])

    # Seleccionar el archivo de salida
    fileOut = filedialog.asksaveasfilename(title="Guardar archivo de salida", defaultextension=".txt", filetypes=[("Text files", "*.txt")])

    if fileIn and fileOut:  # Si ambos archivos fueron seleccionados
        normalizahoras(fileIn, fileOut)
        print(f"Archivo normalizado guardado en: {fileOut}")
    else:
        print("No se seleccionaron archivos válidos.")

if __name__ == "__main__":
    seleccionar_archivos()

```
Ejercicio 2: Programa de Manejo de Señales Estéreo (35%)
--------------------------------------------------------

- Construya el programa `mono.py` que permita realizar las funciones de la tarea
  APA-T5 en un entorno gráfico usando TkInter.
- El programa contará con cuatro pestañas de `ttk.notebook`:

  - Pestaña `Estéreo a Mono`
  - Pestaña `Mono a Estéreo`
  - Pestaña `Codifica Estéreo`
  - Pestaña `Descodifica Estéreo`

  En cada una de estas pestañas se dispondrán de todos los artilugios necesarios para:
  
  - Seleccionar el o los ficheros de entrada.
  - Realizar la operación correspondiente.
  - Escuchar cada una de las señales involucradas, tanto de entrada como de salida.
  - Escribir la señal resultante en un fichero cuyo nombre se indicará al seleccionar la opción de `Guardar`.

- No se evaluará la corrección de las funciones desarrolladas en la tarea APA-T5, pero el programa deberá
  ser compatible con sus interfaces, de manera que, al susituir el
  `estereo.py` presentado por uno que funcione correctamente, el programa `mono.py` también lo hará.

Ejercicio 3: Programa de Visualización de Cuerpos Sometidos a Atracción Gravitatoria (45%)
---------------------------------------------------------------------------------------------

Realizar un programa de simulación de cuerpos celestes sometidos a la Ley de Gravitación Universal
de Newton. Como mínimo debe tener las mismas funcionalidades del programa `gravedad.exe` subido a Atenea
y hacerlo igual o mejor que éste.

Cosas a poner
- Archivo poder guardar y leer archivos  
- Cuerpos editor de cuerpos 
- Evaluacion 
- Ayuda Acerca de
- Mapear control + y control - para mapear el zoom 
- Entrega
- Hay que hacerlo para que se adapte al tamaño de pantalla del usuario 
-------

Los tres programas deberán estar preparados para ser ejecutados desde la línea de comandos o desde
una sesión `ipython` usando el comando `%run`.
