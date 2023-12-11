import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        divisores = ""

        numero_ingresado = int(prompt("","Ingrese un número"))

        while numero_ingresado == None or numero_ingresado < 1:
            numero_ingresado = int(prompt("","Ingrese un número válido"))
            
        cantidad_divisores = 0
        for i in range(1, int(numero_ingresado) + 1):
            if numero_ingresado % i == 0:
                divisores += str(i) + " "
                cantidad_divisores += 1

        print(f"Números divisores: {divisores} .Cantidad de números divisores: {cantidad_divisores}")

'''
Al presionar el botón Mostrar pedir un número. mostrar los números divisores desde el 1 al 
número ingresado, 
y mostrar la cantidad de números divisores encontrados.
'''
       
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()