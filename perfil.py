from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title("Perfil")
root.geometry("450x290")
root.maxsize(450, 290)
root.config(bg="lightgrey")
"""
imagen = PhotoImage(file="OneDrive/escritorio/programas py/programas/ardilla.png")
pimg = imagen.subsample(1,1)

img = Label(root, image=pimg)
img.grid(row=0, column=0, rowspan=6, padx=5, pady=5)

def ai():
    aip = filedialog.askopenfilename()
    if aip:
        aimg = Image.open(aip)
        taimg = ImageTk.PhotoImage(aimg)
        imgn = Label(root, image=taimg)
        imgn.image = taimg
        imgn.grid(row=0, column=0, rowspan=6,padx=5, pady=5)
        img.destroy()
        
def ri():
    img.destroy()

    imagen2 = PhotoImage(file="OneDrive/escritorio/programas py/programas/ardilla.png")
    pimg2 = imagen2.subsample(1,1)
    img2 = Label(root, image=pimg2)
    img2.grid(row=0, column=0, rowspan=6, padx=5, pady=5)

bai = Button(root,text="Abrir Imagen",command=ai).grid(row=6,column=0, padx=5, pady=5)
bri = Button(root,text="Retirar Imagen",command=ri).grid(row=7,column=0, padx=5, pady=5)
"""
ei = Label(root, text="Por favor ingrese su información: ", bg="lightgrey")
ei.grid(row=0, column=1, columnspan=4, padx=5, pady=5)

Label(root, text="Name", bg="lightgrey").grid(row=1, column=1, padx=5, pady=5, sticky=E)

name = Entry(root, bd=3)
name.grid(row=1, column=2, padx=5, pady=5)

gender = Menubutton(root, text="Gender")
gender.grid(row=2, column=2, padx=5, pady=5, sticky=W)
gender.papa = Menu(gender, tearoff=0)
gender["menu"] = gender.papa
gender.papa.add_cascade(label="Male")
gender.papa.add_cascade(label="Female")
gender.grid()

Label(root, text="Eye Color", bg="lightgrey").grid(row=3, column=1, padx=5, pady=5, sticky=E)
eyes = Entry(root, bd=3)
eyes.grid(row=3, column=2, padx=5, pady=5)

Label(root, text="Height", bg="lightgrey").grid(row=4, column=1, padx=5, pady=5, sticky=E)
Label(root, text="cm", bg="lightgrey").grid(row=4, column=3, sticky=W)

height = Entry(root, bd=3)
height.grid(row=4, column=2, padx=5, pady=5)

Label(root, text="Weight", bg="lightgrey").grid(row=5, column=1, padx=5, pady=5, sticky=E)
Label(root, text="kg", bg="lightgrey").grid(row=5, column=3, sticky=W)

weight = Entry(root, bd=3)
weight.grid(row=5, column=2, padx=5, pady=5)

root.mainloop()