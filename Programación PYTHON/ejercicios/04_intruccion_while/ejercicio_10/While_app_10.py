import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre y apellido: Ana Gonzalez
Ejercicio While 10

Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        respuesta= prompt("?","Desea ingresar algún número?")
        contador_positivos=0
        suma_acumulada_positivos=0
        contador_negativos=0
        suma_acumulada_negativos=0
        contador_ceros=0
        diferencia_positivos_negativos=0

        while respuesta!= None:
            numero= int(prompt("Núm", "Ingrese un número"))
            if numero < 0:
                contador_negativos= contador_negativos+1
                suma_acumulada_negativos=numero+suma_acumulada_negativos
            elif numero > 0:
                contador_positivos= contador_positivos+1
                suma_acumulada_positivos=numero+suma_acumulada_positivos
            else:
                contador_ceros= contador_ceros+1
                
            respuesta= prompt("?", "¿Desea seguir ingresando números?")
        diferencia_positivos_negativos=contador_positivos-contador_negativos

        alert(title="Info", message= "Suma de números negativos: "+str(suma_acumulada_negativos)+", suma de números positivos: "+str(suma_acumulada_positivos)+", cantidad números positivos ingresados: "+str(contador_positivos)+", cantidad números negativos ingresados: "+str(contador_negativos)+", cantidad de 0 ingresados: "+str(contador_ceros)+" y la diferencia entre la cantidad de números positivos y negativos ingresados es: "+str(diferencia_positivos_negativos))
                    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
