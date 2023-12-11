import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Ana Gonzalez
Ejercicio FOR 6
Al presionar el botón Mostrar pedir un número. mostrar los números pares desde 
el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero = int(prompt("","Ingrese un número"))
        cantidad_pares = 0

        for numero in range (1, numero+1):
            if numero % 2 == 0:
                cantidad_pares=cantidad_pares+1
                alert("",f"{+numero}")
        
        alert("","La cantidad de números pares ingresados es de: "+str(cantidad_pares))
'''
Al presionar el botón Mostrar pedir un número. mostrar los números pares desde 
el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
'''
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()