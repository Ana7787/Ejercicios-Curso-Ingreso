'''
Nomre y apellido: Ana Gonzalez
TP6 WHILE
UTN FRA

De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        suma_edades = 0
        cantidad_candidatos = 0
        respuesta= prompt("?","Desea ingresar datos?")
        flag1 = True
        mas_votos = 0
        menos_votos = 0 
        contador_votos = 0
        candidato_menosvotado = 0
        candidato_masvotado = 0
        edad_candidatomenosvotado = 0
        


        while respuesta == "si":

            nombre= prompt("","Ingrese el nombre del candidato")
            edad= int(prompt("","Ingrese la edad del candidato"))
            while edad < 25:
                edad = int(prompt("","Ingrese una edad válida"))
            votos= int(prompt("","Ingrese cantidad de votos recibidos"))
            while votos < 0:
                votos= int(prompt("","Vuelva a ingresar una cantidad válida"))

            if flag1 == True:
                mas_votos = votos
                menos_votos = votos
                candidato_menosvotado = nombre
                edad_candidatomenosvotado = edad
                flag1= False

            if votos > mas_votos:
                mas_votos= votos
                candidato_masvotado = nombre

            if votos < menos_votos:
                menos_votos = votos
                candidato_menosvotado = nombre
                edad_candidatomenosvotado = edad

            contador_votos = votos + contador_votos

            cantidad_candidatos= cantidad_candidatos + 1
            suma_edades= edad + suma_edades 
            respuesta= prompt("?","Desea ingresar datos?")

        promedio_edades= suma_edades/cantidad_candidatos

        print("El candidato más votado es: "+str(candidato_masvotado)+ ", el nombre del candidato con menos votos es: "+str(candidato_menosvotado)+" y su edad es: "+str(edad_candidatomenosvotado)+", el promedio de edades de los candidatos es: "+str(promedio_edades)+" y el total de los votos emitidos es de: "+str(contador_votos))


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
