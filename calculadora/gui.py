import tkinter as tk
from operaciones import sumar, restar, multiplicar, dividir

def calcular(operacion):
    try:
        a = float(entrada1.get())
        b = float(entrada2.get())
        if operacion == 'sumar':
            resultado.set(sumar(a, b))
        elif operacion == 'restar':
            resultado.set(restar(a, b))
        elif operacion == 'multiplicar':
            resultado.set(multiplicar(a, b))
        elif operacion == 'dividir':
            resultado.set(dividir(a, b))
    except Exception as e:
        resultado.set(f"Error: {e}")

root = tk.Tk()
root.title("Calculadora")

entrada1 = tk.Entry(root)
entrada1.pack()

entrada2 = tk.Entry(root)
entrada2.pack()

resultado = tk.StringVar()
tk.Label(root, textvariable=resultado).pack()

tk.Button(root, text="Sumar", command=lambda: calcular('sumar')).pack()
tk.Button(root, text="Restar", command=lambda: calcular('restar')).pack()
tk.Button(root, text="Multiplicar", command=lambda: calcular('multiplicar')).pack()
tk.Button(root, text="Dividir", command=lambda: calcular('dividir')).pack()

root.mainloop()
