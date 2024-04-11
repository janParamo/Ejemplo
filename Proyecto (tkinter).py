from tkinter import *
from tkinter import messagebox, ttk

lista_compras = {}

ventana = Tk()
ventana.geometry("800x500")
tcontrol = ttk.Notebook(ventana)
tcontrol1 = ttk.Frame(tcontrol)

label_bienvendia = Label(ventana, text="Bienvenido a la lista de compras", font=("verdana", 25), fg="white", bg="black").pack(anchor=CENTER)

label_opcs = Label(ventana, text="\n1. Agrgear productos a la lista de compras\n2. Mostrar lista de compras creada\n3. Buscar productos\n4. Editar productos\n5. Borrar productos\n6. Salir", font=("verdana", 25)).pack()
label_select = Label(ventana, text="\nSeleccione una opcion (1-6)").pack()
etr_usuario = Entry(ventana, font=("Verdana",15)).pack()

ventana.mainloop()