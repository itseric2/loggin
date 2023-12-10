from tkinter import *
from tkinter import simpledialog, messagebox

root = Tk()
root.title("Basic GUI Layout")
root.maxsize(900, 600)
root.config(bg="skyblue")

def resize_image():
    try:
        w = simpledialog.askinteger("Ancho", "Ingrese el ancho de la imagen:")
        h = simpledialog.askinteger("Altura", "Ingrese la altura de la imagen:")
        
        image = PhotoImage(file="OneDrive/Escritorio/programas py/programas/ardilla.png")
        l = Label(framed, image=image).grid(row=0,column=0, padx=5, pady=5)
        l = image.subsample(w, h)

        label.config(image=l)
        label.image = l

    except ValueError:
        messagebox.showinfo("Error", "Los datos ingresados no son correctos")

framei = Frame(root, width=200, height=400, bg='grey')
framei.grid(row=0, column=0, padx=10, pady=5)
framed = Frame(root, width=650, height=400, bg='grey')
framed.grid(row=0, column=1, padx=10, pady=5)

Label(framei, text="Original Image").grid(row=0, column=0, padx=5, pady=5)

image = PhotoImage(file="OneDrive/Escritorio/programas py/programas/ardilla.png")
original_image = image.subsample(3, 3)

l = Label(framed, image=image).grid(row=0,column=0, padx=5, pady=5)

label = Label(framei, image=original_image)
label.grid(row=1, column=0, padx=5, pady=5)

frame2 = Frame(framei, width=180, height=185)
frame2.grid(row=2, column=0, padx=5, pady=5)

Label(frame2, text="Herramientas", relief=RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10)
Label(frame2, text="Filtros", relief=RAISED).grid(row=0, column=1, padx=5, pady=3, ipadx=10)

Label(frame2, text="Seleccionar").grid(row=1, column=0, padx=5, pady=5)
Label(frame2, text="Rotar y voltear").grid(row=3, column=0, padx=5, pady=5)
B = Button(frame2, text="Configurar Tamaño", command=resize_image).grid(row=4, column=0, padx=5, pady=5)

root.mainloop()