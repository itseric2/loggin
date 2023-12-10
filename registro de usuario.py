from tkinter import *
from tkinter import simpledialog, messagebox
import sqlite3 as sql

window = Tk()
window.maxsize(270,400)
window.geometry("270x400")
window.config(bg="lightgrey")

ln = Label(window,text="Name:",bg="lightgrey").grid(row=1,column=0,padx=5,pady=5)
name = Entry(window,bd=3)
name.grid(row=1,column=1,padx=5,pady=5)

plabel = Label(window,text="Password:",bg="lightgrey").grid(row=2,column=0,padx=5,pady=5)
password = Entry(window,bd=3, show="*")
password.grid(row=2,column=1,padx=5,pady=5)

def connect():
    conn = sql.connect("us.db")
    conn.commit()
    conn.close()

def table():
    conn = sql.connect("us.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE us (
        name text,
        password text
        )"""
    )
    conn.commit()
    conn.close()

def add_user(namep,passwordp):
    n = name.get()
    pw = password.get()
    conn = sql.connect("us.db")
    cursor = conn.cursor()
    instruction1 = f"SELECT * FROM us WHERE name ='{n}'"
    cursor.execute(instruction1)
    data_name = cursor.fetchall()
    instruction2 = f"SELECT * FROM us WHERE password = '{pw}'"
    cursor.execute(instruction2)
    data_password = cursor.fetchall()
    if data_name or data_password:
        messagebox.showinfo("Error", "Username or password is already in use")
    else:
        instruccion = f"INSERT INTO us VALUES (?, ?)"
        cursor.execute(instruccion, (namep, passwordp))
        conn.commit()
        messagebox.showinfo("success", "Successfully registered user")
    conn.close()
    
def au():
    n = name.get()
    pw = password.get()
    add_user(n, pw)
    name.delete(0, END)
    password.delete(0, END)

def read_user():
    conn = sql.connect("us.db")
    cursor = conn.cursor()
    instruction = f"SELECT * FROM us"
    cursor.execute(instruction)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    messagebox.showinfo("Users", f"{datos}")



def loggin():
    n = name.get()
    pw = password.get()
    name.delete(0, END)
    password.delete(0, END)
    conn = sql.connect("us.db")
    cursor = conn.cursor()
    instruction = f"SELECT * FROM us WHERE name ='{n}' AND password = '{pw}'"
    cursor.execute(instruction)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    if datos:
        messagebox.showinfo("User Found", "Everything went correctly")
    else:
        messagebox.showinfo("User Not Found", "The user has not been found")

def agenda_window():
    aw = Tk()
    aw.maxsize(270,400)
    aw.geometry("270x400")

def delete_section():
    pass

def add_section():
    pass

def rename_section():
    pass

rb = Button(window, text="Register User", bg="lightgreen", command=au)
rb.grid(row=11, column=1, padx=5, pady=5)

ru = Button(window, text="Read Users", bg="lightblue", command=read_user)
ru.grid(row=10, column=1, padx=5, pady=5)

s = Button(window, text="Loggin", bg="lightgrey", command=loggin)
s.grid(row=9, column=1, padx=5, pady=5)

""" Delete table
conexion = sql.connect('us.db')
cursor = conexion.cursor()
nombre_tabla = 'us'
sentencia_sql = f'DROP TABLE IF EXISTS {nombre_tabla};'
cursor.execute(sentencia_sql)
conexion.commit()
conexion.close()
""" 

window.mainloop()