import tkinter as tk
from tkinter import messagebox
import openpyxl

class InterfazVehiculos:
    def __init__(self, master):
        self.master = master
        self.master.title("Predio Mega Autos")
        self.master.geometry("500x300")
        self.master.config(bg="Yellow")

        self.label = tk.Label(master, text="Bienvenido a la Gestion de Vehiculos", font=("Arial", 18), bg="green", fg="white")
        self.label.pack(pady=20, padx=20)

        self.btn_crear = tk.Button(master, text="Crear Vehiculo", font=("Arial", 15), bg="blue", fg="white", command=self.crear_vehiculo)
        self.btn_crear.pack()

        self.btn_editar = tk.Button(master, text="Editar Vehiculo", font=("Arial", 15), bg="blue", fg="white", command=self.editar_vehiculo)
        self.btn_editar.pack()

        self.btn_eliminar = tk.Button(master, text="Eliminar Vehiculo", font=("Arial", 15), bg="orange red", fg="white", command=self.eliminar_vehiculo)
        self.btn_eliminar.pack()

        self.btn_listar = tk.Button(master, text="Listar Vehiculo", font=("Arial", 15), bg="blue", fg="white", command=self.listar_vehiculo)
        self.btn_listar.pack()

    def crear_vehiculo(self):
        messagebox.showinfo("Crear Vehiculo")

    def editar_vehiculo(self):
        messagebox.showinfo("Editar Vehiculo")

    def eliminar_vehiculo(self):
        messagebox.showinfo("Eliminar Vehiculo")

    def listar_vehiculo(self):
        messagebox.showinfo("Listar Vehiculo")


    

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazVehiculos(root)
    root.mainloop()