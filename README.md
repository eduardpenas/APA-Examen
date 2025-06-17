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

```python
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from estereo import estereo2mono, mono2stereo, codEstereo, decEstereo

class MonoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Procesador de Audio Mono")
        self.root.geometry("600x400")
        
        # Crear el notebook (pestañas)
        self.notebook = ttk.Notebook(self.root)
        
        # Pestañas
        self.tab_estereo2mono = ttk.Frame(self.notebook)
        self.tab_mono2stereo = ttk.Frame(self.notebook)
        self.tab_codifica = ttk.Frame(self.notebook)
        self.tab_descodifica = ttk.Frame(self.notebook)
        
        self.notebook.add(self.tab_estereo2mono, text="Estéreo a Mono")
        self.notebook.add(self.tab_mono2stereo, text="Mono a Estéreo")
        self.notebook.add(self.tab_codifica, text="Codifica Estéreo")
        self.notebook.add(self.tab_descodifica, text="Descodifica Estéreo")
        
        self.notebook.pack(expand=True, fill="both")
        
        # Pestaña Estéreo a Mono
        self.setup_estereo2mono()
        # Pestaña Mono a Estéreo
        self.setup_mono2stereo()
        # Pestaña Codifica Estéreo
        self.setup_codifica()
        # Pestaña Descodifica Estéreo
        self.setup_descodifica()

    def setup_estereo2mono(self):
        # Widgets para la pestaña "Estéreo a Mono"
        ttk.Label(self.tab_estereo2mono, text="Seleccionar archivo estéreo").pack(pady=10)
        self.entry_estereo2mono = ttk.Entry(self.tab_estereo2mono, width=50)
        self.entry_estereo2mono.pack(pady=5)
        
        self.btn_browse_estereo2mono = ttk.Button(self.tab_estereo2mono, text="Buscar archivo", command=self.browse_estereo2mono)
        self.btn_browse_estereo2mono.pack(pady=5)
        
        ttk.Label(self.tab_estereo2mono, text="Seleccionar archivo mono de salida").pack(pady=10)
        self.entry_mono_output = ttk.Entry(self.tab_estereo2mono, width=50)
        self.entry_mono_output.pack(pady=5)
        
        self.btn_browse_mono_output = ttk.Button(self.tab_estereo2mono, text="Buscar ubicación", command=self.browse_mono_output)
        self.btn_browse_mono_output.pack(pady=5)
        
        self.cmb_canal = ttk.Combobox(self.tab_estereo2mono, values=["Izquierdo", "Derecho", "Semisuma", "Semidiferencia"], state="readonly")
        self.cmb_canal.set("Semisuma")
        self.cmb_canal.pack(pady=5)
        
        self.btn_convertir = ttk.Button(self.tab_estereo2mono, text="Convertir a Mono", command=self.convertir_estereo2mono)
        self.btn_convertir.pack(pady=10)
        
    def setup_mono2stereo(self):
        # Widgets para la pestaña "Mono a Estéreo"
        ttk.Label(self.tab_mono2stereo, text="Seleccionar archivo mono izquierdo").pack(pady=10)
        self.entry_mono_izq = ttk.Entry(self.tab_mono2stereo, width=50)
        self.entry_mono_izq.pack(pady=5)
        
        self.btn_browse_mono_izq = ttk.Button(self.tab_mono2stereo, text="Buscar archivo", command=self.browse_mono_izq)
        self.btn_browse_mono_izq.pack(pady=5)
        
        ttk.Label(self.tab_mono2stereo, text="Seleccionar archivo mono derecho").pack(pady=10)
        self.entry_mono_der = ttk.Entry(self.tab_mono2stereo, width=50)
        self.entry_mono_der.pack(pady=5)
        
        self.btn_browse_mono_der = ttk.Button(self.tab_mono2stereo, text="Buscar archivo", command=self.browse_mono_der)
        self.btn_browse_mono_der.pack(pady=5)
        
        ttk.Label(self.tab_mono2stereo, text="Seleccionar archivo estéreo de salida").pack(pady=10)
        self.entry_stereo_output = ttk.Entry(self.tab_mono2stereo, width=50)
        self.entry_stereo_output.pack(pady=5)
        
        self.btn_browse_stereo_output = ttk.Button(self.tab_mono2stereo, text="Buscar ubicación", command=self.browse_stereo_output)
        self.btn_browse_stereo_output.pack(pady=5)
        
        self.btn_convertir_stereo = ttk.Button(self.tab_mono2stereo, text="Convertir a Estéreo", command=self.convertir_mono2stereo)
        self.btn_convertir_stereo.pack(pady=10)
        
    def setup_codifica(self):
        # Widgets para la pestaña "Codifica Estéreo"
        ttk.Label(self.tab_codifica, text="Seleccionar archivo estéreo").pack(pady=10)
        self.entry_codifica = ttk.Entry(self.tab_codifica, width=50)
        self.entry_codifica.pack(pady=5)
        
        self.btn_browse_codifica = ttk.Button(self.tab_codifica, text="Buscar archivo", command=self.browse_codifica)
        self.btn_browse_codifica.pack(pady=5)
        
        ttk.Label(self.tab_codifica, text="Seleccionar archivo codificado de salida").pack(pady=10)
        self.entry_cod_output = ttk.Entry(self.tab_codifica, width=50)
        self.entry_cod_output.pack(pady=5)
        
        self.btn_browse_cod_output = ttk.Button(self.tab_codifica, text="Buscar ubicación", command=self.browse_cod_output)
        self.btn_browse_cod_output.pack(pady=5)
        
        self.btn_codificar = ttk.Button(self.tab_codifica, text="Codificar Estéreo", command=self.codificar_estereo)
        self.btn_codificar.pack(pady=10)
        
    def setup_descodifica(self):
        # Widgets para la pestaña "Descodifica Estéreo"
        ttk.Label(self.tab_descodifica, text="Seleccionar archivo codificado").pack(pady=10)
        self.entry_descodifica = ttk.Entry(self.tab_descodifica, width=50)
        self.entry_descodifica.pack(pady=5)
        
        self.btn_browse_descodifica = ttk.Button(self.tab_descodifica, text="Buscar archivo", command=self.browse_descodifica)
        self.btn_browse_descodifica.pack(pady=5)
        
        ttk.Label(self.tab_descodifica, text="Seleccionar archivo estéreo de salida").pack(pady=10)
        self.entry_descod_output = ttk.Entry(self.tab_descodifica, width=50)
        self.entry_descod_output.pack(pady=5)
        
        self.btn_browse_descod_output = ttk.Button(self.tab_descodifica, text="Buscar ubicación", command=self.browse_descod_output)
        self.btn_browse_descod_output.pack(pady=5)
        
        self.btn_descodificar = ttk.Button(self.tab_descodifica, text="Descodificar Estéreo", command=self.descodificar_estereo)
        self.btn_descodificar.pack(pady=10)

    # Funciones de manejo de archivos y operaciones
    def browse_estereo2mono(self):
        file = filedialog.askopenfilename(filetypes=[("Archivos WAV", "*.wav")])
        if file:
            self.entry_estereo2mono.delete(0, tk.END)
            self.entry_estereo2mono.insert(0, file)
    
    def browse_mono_output(self):
        file = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("Archivos WAV", "*.wav")])
        if file:
            self.entry_mono_output.delete(0, tk.END)
            self.entry_mono_output.insert(0, file)
    
    def convertir_estereo2mono(self):
        input_file = self.entry_estereo2mono.get()
        output_file = self.entry_mono_output.get()
        canal = self.cmb_canal.get()
        
        canal_dict = {"Izquierdo": 0, "Derecho": 1, "Semisuma": 2, "Semidiferencia": 3}
        canal_valor = canal_dict.get(canal, 2)
        
        if not input_file or not output_file:
            messagebox.showerror("Error", "Debe seleccionar los archivos de entrada y salida.")
            return
        
        try:
            estereo2mono(input_file, output_file, canal_valor)
            messagebox.showinfo("Éxito", f"Archivo convertido correctamente: {output_file}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        
    # Similar para las otras funciones (mono2stereo, codificar, descodificar)
    # Funciones similares para los botones de las otras pestañas.

if __name__ == "__main__":
    root = tk.Tk()
    app = MonoApp(root)
    root.mainloop()

```
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
