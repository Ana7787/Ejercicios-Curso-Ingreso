import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                             columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.lista = []

    def btn_comenzar_ingreso_on_click(self):
        rta = "si"
        suma_negativos = 0
        suma_positivos = 0
        cantidad_negativos = 0
        cantidad_positivos = 0
        cantidad_ceros = 0
        bandera = True
        maximo_positivos = 0
        maximo_negativos = 0
        minimo_negativos = 0
        minimo_positivos = 0

        while rta != None:
            rta = prompt("","¿Desea ingresar algún número?")
            numero = int(prompt ("", "Ingrese un número"))
            if numero < 0:
                suma_negativos += numero
                cantidad_negativos += 1
            elif numero > 0:
                suma_positivos += numero
                cantidad_positivos += 1
            else:
                cantidad_ceros += 1
            while bandera == True:
                bandera = False
                if numero < 0:
                    numero = minimo_negativos
                    numero = maximo_negativos
                else:
                    numero = minimo_positivos 
                    numero = maximo_positivos
            if numero < 0:
                if numero < minimo_negativos:
                    minimo_negativos = numero
                elif numero > maximo_positivos:
                    maximo_positivos = numero
                promedio_negativos = suma_negativos/ cantidad_negativos
       
        self.lista.append(suma_negativos,suma_positivos, cantidad_positivos, cantidad_negativos, cantidad_ceros,minimo_negativos,maximo_positivo,
        promedio_negativos)

    def btn_mostrar_estadisticas_on_click(self):
        print ("",self.lista )
'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

'''

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
