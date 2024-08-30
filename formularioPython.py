




from csv import writer
from struct import pack
import tkinter as tk
from tkinter import messagebox
## Definicion de funciones
def limpiar_campos():
    tbNombre.delete(0, tk.END)
    tbApellido.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    var_genero.set(0)

def borrar():
    limpiar_campos()

def guardar_valores():
    # Obtener valores de los entrys
    nombre = tbNombre.get()
    apellido = tbApellido.get()
    edad = tbEdad.get()
    estatura = tbEstatura.get()
    telefono = tbTelefono.get()
    genero = ""
    if var_genero.get() == 1:
        genero = "Hombre"
    elif var_genero.get() == 2:
        genero = "Mujer"
    datos = "Nombre: " + nombre + "\n" + "Apellido: " + apellido + "\n" + "Edad: " + edad + "\n" + "Estatura: " + estatura + "\n" + "Telefono" + telefono + "\n" + "Genero: " + genero + "\n"
    ## Guardar datos en archivo
    with open("datos.txt", "a") as archivo:
        archivo.write(datos + "\n\n")
    ## Mostrar mensaje de confiemacion
    messagebox.showinfo("Informacion", "Datos guardados con exito: \n\n" + datos)
    tbNombre.delete(0, tk.END)
    tbApellido.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    var_genero.set(0)


## Creacion de ventana
ventana = tk.Tk()
ventana.geometry('520x500')
ventana.title('Formulario Vr.01')
## Creacion de variable para RadioButton
var_genero = tk.IntVar()
## Creacion de etiquetas y campos de entrada
## Nombre
lbNombre = tk.Label(ventana, text = "Nombre: ")
lbNombre.pack()
tbNombre = tk.Entry()
tbNombre.pack()
## Apellido
lbApellido = tk.Label(ventana, text = "Apellido: ")
lbApellido.pack()
tbApellido = tk.Entry()
tbApellido.pack()
## Edad
lbEdad = tk.Label(ventana, text =   "Edad: ")
lbEdad.pack()
tbEdad = tk.Entry()
tbEdad.pack()
## Estatura
lbEstatura = tk.Label(ventana, text = "Estatura: ")
lbEstatura.pack()
tbEstatura = tk.Entry()
tbEstatura.pack()
## Telefono
lbTelefono = tk.Label(ventana, text = "Telefono: ")
lbTelefono.pack()
tbTelefono = tk.Entry()
tbTelefono.pack()
## Genero
lbGenero = tk.Label(ventana, text = "Genero: ")
lbGenero.pack()
rbttGenMasculino = tk.Radiobutton(ventana, text = "Hombre", variable = var_genero, value = 1)
rbttGenMasculino.pack()
rbttGenFemenino = tk.Radiobutton(ventana, text = "Mujer", variable = var_genero, value = 2)
rbttGenFemenino.pack()
## Creacion de botones
## Borrar
bttBorrar = tk.Button(ventana, text = "Borrar valores", command = borrar)
bttBorrar.pack()
## Guardar
bttGuardar = tk.Button(ventana, text = "Guardar valores", command = guardar_valores)
bttGuardar.pack()

ventana.mainloop()
