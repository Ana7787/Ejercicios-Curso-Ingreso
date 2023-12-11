import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        contadordivisores = 0

        numero_ingresado = int(prompt("","Ingrese un número"))

        while numero_ingresado == None or not numero_ingresado.isdigit:
            numero_ingresado = int(prompt("","Ingrese un número válido"))
        if numero_ingresado < 0:
            mensaje= "No se ha ingresado un número primo"

        
        for divisor in range(1, numero_ingresado + 1):
            if numero_ingresado % divisor == 0:
                contadordivisores += 1

        if contadordivisores == 2:
            mensaje = "El número ingresado es primo"
        else:
            mensaje = "El número ingresado no es primo"
        print(mensaje)                     
'''
Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
'''    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()