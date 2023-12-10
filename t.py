import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk
from statistics import mean, median, mode
from math import sqrt

root = tk.Tk()
root.title("Generador de Tabla de Frecuencia")

def redondeo(numero, cerca=0.5):
    diferencia_superior = numero - int(numero)
    if diferencia_superior >= cerca:
        return int(numero) + 1
    else:
        return numero

ns = [2,4,6,7,3,2,2,4,6,8,7,9,8,6,5]
for ns in ns:

xmax = max(ns)
xmin = min(ns)
rango = xmax - xmin
n = len(ns)
m = sqrt(n)
c = rango / m
decimales_deseados = 2
mr = round(m, decimales_deseados)
cr = round(c, decimales_deseados)
mrr = redondeo(mr)
crr = redondeo(cr)

tabla_frecuencia = []
contador = 0
li = xmin
ls = xmin + crr
while contador <= mrr:
    contador += 1
    if contador > mrr:
        break
    xi = (li + ls) / 2
    li_ls = f"{li} - {ls}"
    fi = sum(1 for num in ns if li <= num < ls)
    Fi = sum(1 for num in ns if num < ls)
    xifi = xi * fi
    tabla_frecuencia.append([li_ls, xi, fi, Fi, xifi])
    li = ls
    ls += crr

def mostrar_tabla():
    ventana = tk.Toplevel(root)
    ventana.title("Tabla de Frecuencia")
    tabla = ttk.Treeview(ventana, columns=("Li - Ls", "Xi", "fi", "Fi", "xifi"))
    tabla.heading("#1", text="Li - Ls")
    tabla.heading("#2", text="Xi")
    tabla.heading("#3", text="fi")
    tabla.heading("#4", text="Fi")
    tabla.heading("#5", text="xifi")

    for fila in tabla_frecuencia:
        tabla.insert("", "end", values=fila)

    tabla.pack()

def mostrar_estadisticas():
    media = mean(ns)
    mediana = median(ns)
    moda = mode(ns)
    messagebox.showinfo("Estadísticas", f"Media: {media}\nMediana: {mediana}\nModa: {moda}")

ld = []

def mds():
    media = mean(ns)
    for desviacion in ns:
        dvc = round(desviacion - media, 1)
        ld.append(dvc)
    
    messagebox.showinfo("a", ld)

ld2 = ld
def dm1():
    global ld2
    for dm1 in range(len(ld2)):
        ld2[dm1] = abs(ld2[dm1])
    sm = sum(ld2)
    cdt = len(ns)
    dm2 = sm / cdt
    messagebox.showinfo("a",dm2)
            
boton_mostrar_tabla = tk.Button(root, text="Mostrar Tabla", command=mostrar_tabla)
boton_mostrar_tabla.pack()

boton_mostrar_estadisticas = tk.Button(root, text="Mostrar Estadísticas", command=mostrar_estadisticas)
boton_mostrar_estadisticas.pack()

botond = tk.Button(root,text="Desviacion",command=mds)
botond.pack()

botondm = tk.Button(root,text="Desviacion media",command=dm1)
botondm.pack()

root.mainloop()