import tkinter as tk
from tkinter import ttk, filedialog, messagebox
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

        self.setup_estereo2mono()
        self.setup_mono2stereo()
        self.setup_codifica()
        self.setup_descodifica()

    # ==== Pestaña Estéreo a Mono ====
    def setup_estereo2mono(self):
        ttk.Label(self.tab_estereo2mono, text="Seleccionar archivo estéreo").pack(pady=10)
        self.entry_estereo2mono = ttk.Entry(self.tab_estereo2mono, width=50)
        self.entry_estereo2mono.pack(pady=5)
        ttk.Button(self.tab_estereo2mono, text="Buscar archivo", command=self.browse_estereo2mono).pack(pady=5)

        ttk.Label(self.tab_estereo2mono, text="Seleccionar archivo mono de salida").pack(pady=10)
        self.entry_mono_output = ttk.Entry(self.tab_estereo2mono, width=50)
        self.entry_mono_output.pack(pady=5)
        ttk.Button(self.tab_estereo2mono, text="Buscar ubicación", command=self.browse_mono_output).pack(pady=5)

        self.cmb_canal = ttk.Combobox(self.tab_estereo2mono, values=["Izquierdo", "Derecho", "Semisuma", "Semidiferencia"], state="readonly")
        self.cmb_canal.set("Semisuma")
        self.cmb_canal.pack(pady=5)

        ttk.Button(self.tab_estereo2mono, text="Convertir a Mono", command=self.convertir_estereo2mono).pack(pady=10)

    # ==== Pestaña Mono a Estéreo ====
    def setup_mono2stereo(self):
        ttk.Label(self.tab_mono2stereo, text="Seleccionar archivo mono izquierdo").pack(pady=10)
        self.entry_mono_izq = ttk.Entry(self.tab_mono2stereo, width=50)
        self.entry_mono_izq.pack(pady=5)
        ttk.Button(self.tab_mono2stereo, text="Buscar archivo", command=self.browse_mono_izq).pack(pady=5)

        ttk.Label(self.tab_mono2stereo, text="Seleccionar archivo mono derecho").pack(pady=10)
        self.entry_mono_der = ttk.Entry(self.tab_mono2stereo, width=50)
        self.entry_mono_der.pack(pady=5)
        ttk.Button(self.tab_mono2stereo, text="Buscar archivo", command=self.browse_mono_der).pack(pady=5)

        ttk.Label(self.tab_mono2stereo, text="Seleccionar archivo estéreo de salida").pack(pady=10)
        self.entry_stereo_output = ttk.Entry(self.tab_mono2stereo, width=50)
        self.entry_stereo_output.pack(pady=5)
        ttk.Button(self.tab_mono2stereo, text="Buscar ubicación", command=self.browse_stereo_output).pack(pady=5)

        ttk.Button(self.tab_mono2stereo, text="Convertir a Estéreo", command=self.convertir_mono2stereo).pack(pady=10)

    # ==== Pestaña Codifica Estéreo ====
    def setup_codifica(self):
        ttk.Label(self.tab_codifica, text="Seleccionar archivo estéreo").pack(pady=10)
        self.entry_codifica = ttk.Entry(self.tab_codifica, width=50)
        self.entry_codifica.pack(pady=5)
        ttk.Button(self.tab_codifica, text="Buscar archivo", command=self.browse_codifica).pack(pady=5)

        ttk.Label(self.tab_codifica, text="Seleccionar archivo codificado de salida").pack(pady=10)
        self.entry_cod_output = ttk.Entry(self.tab_codifica, width=50)
        self.entry_cod_output.pack(pady=5)
        ttk.Button(self.tab_codifica, text="Buscar ubicación", command=self.browse_cod_output).pack(pady=5)

        ttk.Button(self.tab_codifica, text="Codificar Estéreo", command=self.codificar_estereo).pack(pady=10)

    # ==== Pestaña Descodifica Estéreo ====
    def setup_descodifica(self):
        ttk.Label(self.tab_descodifica, text="Seleccionar archivo codificado").pack(pady=10)
        self.entry_descodifica = ttk.Entry(self.tab_descodifica, width=50)
        self.entry_descodifica.pack(pady=5)
        ttk.Button(self.tab_descodifica, text="Buscar archivo", command=self.browse_descodifica).pack(pady=5)

        ttk.Label(self.tab_descodifica, text="Seleccionar archivo estéreo de salida").pack(pady=10)
        self.entry_descod_output = ttk.Entry(self.tab_descodifica, width=50)
        self.entry_descod_output.pack(pady=5)
        ttk.Button(self.tab_descodifica, text="Buscar ubicación", command=self.browse_descod_output).pack(pady=5)

        ttk.Button(self.tab_descodifica, text="Descodificar Estéreo", command=self.descodificar_estereo).pack(pady=10)

    # ==== Funciones browse ====
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

    def browse_mono_izq(self):
        file = filedialog.askopenfilename(filetypes=[("Archivos WAV", "*.wav")])
        if file:
            self.entry_mono_izq.delete(0, tk.END)
            self.entry_mono_izq.insert(0, file)

    def browse_mono_der(self):
        file = filedialog.askopenfilename(filetypes=[("Archivos WAV", "*.wav")])
        if file:
            self.entry_mono_der.delete(0, tk.END)
            self.entry_mono_der.insert(0, file)

    def browse_stereo_output(self):
        file = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("Archivos WAV", "*.wav")])
        if file:
            self.entry_stereo_output.delete(0, tk.END)
            self.entry_stereo_output.insert(0, file)

    def browse_codifica(self):
        file = filedialog.askopenfilename(filetypes=[("Archivos WAV", "*.wav")])
        if file:
            self.entry_codifica.delete(0, tk.END)
            self.entry_codifica.insert(0, file)

    def browse_cod_output(self):
        file = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("Archivos WAV", "*.wav")])
        if file:
            self.entry_cod_output.delete(0, tk.END)
            self.entry_cod_output.insert(0, file)

    def browse_descodifica(self):
        file = filedialog.askopenfilename(filetypes=[("Archivos WAV", "*.wav")])
        if file:
            self.entry_descodifica.delete(0, tk.END)
            self.entry_descodifica.insert(0, file)

    def browse_descod_output(self):
        file = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("Archivos WAV", "*.wav")])
        if file:
            self.entry_descod_output.delete(0, tk.END)
            self.entry_descod_output.insert(0, file)

    # ==== Funciones de procesamiento ====
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

    def convertir_mono2stereo(self):
        izq = self.entry_mono_izq.get()
        der = self.entry_mono_der.get()
        out = self.entry_stereo_output.get()
        if not izq or not der or not out:
            messagebox.showerror("Error", "Debe seleccionar ambos archivos mono y el archivo de salida.")
            return
        try:
            mono2stereo(izq, der, out)
            messagebox.showinfo("Éxito", f"Archivo estéreo creado correctamente: {out}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def codificar_estereo(self):
        entrada = self.entry_codifica.get()
        salida = self.entry_cod_output.get()
        if not entrada or not salida:
            messagebox.showerror("Error", "Debe seleccionar los archivos de entrada y salida.")
            return
        try:
            codEstereo(entrada, salida)
            messagebox.showinfo("Éxito", f"Archivo codificado correctamente: {salida}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def descodificar_estereo(self):
        entrada = self.entry_descodifica.get()
        salida = self.entry_descod_output.get()
        if not entrada or not salida:
            messagebox.showerror("Error", "Debe seleccionar los archivos de entrada y salida.")
            return
        try:
            decEstereo(entrada, salida)
            messagebox.showinfo("Éxito", f"Archivo descodificado correctamente: {salida}")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = MonoApp(root)
    root.mainloop()
