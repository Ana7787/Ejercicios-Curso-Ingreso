import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre y apellido: Ana Gonzalez
EJERCICIO 4 FOR

Al presionar el botón Mostrar pedir valores por prompt hasta que el usuario ingrese el valor 9 (se deberá utilizar 'BREAK').
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        valor = int (prompt("", "Ingrese un número"))

        for valor in range (99999999999):
            valor = int(prompt("", "Ingrese otro valor"))
            if valor == 9:
                break
            
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()