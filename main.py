import tkinter as tk

# todo el automata completo son 52 en total
automata = {
    'q0': {'0': 'q1', '1': 'q2', '2': 'q3', '8': 'q4'},
    'q1': {'8': 'q5'},
    'q5': {'4': 'q40'},
    'q40': {'1': 'q41'},
    'q41': {'1': 'q42'},
    'q42': {'2': 'q43'},
    'q43': {'2': 'q44'},
    'q2': {'4': 'q6', '8': 'q7'},
    'q6': {'1': 'q9'},
    'q9': {'1': 'q10'},
    'q10': {'1': 'q11'},
    'q11': {'2': 'q12'},
    'q12': {'1': 'q13'},
    'q7': {'9': 'q14'},
    'q14': {'0': 'q15'},
    'q15': {'i': 'q16'},
    'q16': {'2': 'q17'},
    'q17': {'2': 'q18'},
    'q18': {},
    'q13': {},
    'q44': {},
    'q3': {'0': 'q8', '1': 'q19', '2': 'q20', '5': 'q21'},
    'q8': {'1': 'q22'},
    'q22': {'4': 'q23'},
    'q23': {'1': 'q24'},
    'q24': { '8': 'q25' },
    'q25': {},
    'q19': {'9': 'q26'},
    'q26': {'6': 'q27'},
    'q27': {'j': 'q28'},
    'q28': {'2': 'q29'},
    'q29': { '2': 'q30' },
    'q30': {},
    'q20': {'j': 'q31', '6': 'q32'},
    'q31': {'0': 'q33'},
    'q32': {'5': 'q36'},
    'q33': {'1': 'q34'},
    'q34': {'8': 'q35'},
    'q35': {'2': 'q36'},
    'q36': {'k': 'q37'},
    'q37': { '2': 'q38' },
    'q38': { '1': 'q39' },
    'q39': {},
    'q21': {'3': 'q45'},
    'q45': {'4': 'q46'},
    'q46': { '2': 'q47' },
    'q47': {},
    'q4': {'0': 'q48'},
    'q48': {'9': 'q49'},
    'q49': {'1': 'q50'},
    'q50': {'1': 'q51'},
    'q51': {'2': 'q52'},
    'q52': {'1': 'q53'},
}

def validar_secuencia(secuencia):
    estado_actual = 'q0'
    secuencia_autómata = [estado_actual]  # Lista para almacenar la secuencia de estados
    for caracter in secuencia:
        if caracter in automata[estado_actual]:
            estado_actual = automata[estado_actual][caracter]
            secuencia_autómata.append(estado_actual)  # Agregar el estado actual a la lista
        else:
            return False, secuencia_autómata  # Devolver False y la secuencia hasta ahora
    # estos son los 9 estados finales
    estados_finales = {'q44', 'q13', 'q18', 'q25', 'q30', 'q35', 'q39', 'q47', 'q53'}
    return estado_actual in estados_finales, secuencia_autómata

#aqui validamos las entradas y convertimos las mayusculas en minusculas
def validar():
    secuencia = entrada.get().lower()  # Convertir a minúsculas
    es_valida, secuencia_autómata = validar_secuencia(secuencia)
    resultado.config(text="Válida" if es_valida else "No válida")
    secuencia_label.config(text="Secuencia del autómata: " + " -> ".join(secuencia_autómata))

# creamos la ventana en el tkinter
ventana = tk.Tk()
ventana.title("Automata Chido xD")
ventana.geometry("400x200")

etiqueta = tk.Label(ventana, text="Ingrese el numero de lote :")
etiqueta.pack(pady=10)

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Validar UwU", command=validar)
boton.pack(pady=10)

resultado = tk.Label(ventana, text="")
resultado.pack()

secuencia_label = tk.Label(ventana, text="")
secuencia_label.pack()

ventana.mainloop()