
'''Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.
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

        postulantes_a = 0 
        bandera = True
        edadNB = 0
        edadF = 0
        edadM = 0
        contadorNB = 0
        contadorM = 0
        contadorF = 0
        bandera1 = 0
        contadorJS = 0
        contadorASPNET = 0
        contadorPYTHON = 0
        
        for postulantes in range (10):
            nombre = prompt("","Ingrese su nombre")
            edad = int(prompt("","Ingrese su edad"))
            while edad < 18 :
                edad = int(prompt("","Ingrese su edad") )        
            genero = prompt("","Ingrese su género")
            while genero != "F" or genero != "M" or genero != "NB":
                genero = prompt("","Ingrese  un género válido")
            tecnologia = prompt ("","Ingrese tecnologia")
            while tecnologia != "JS" or tecnologia != "PYTHON" or tecnologia != "ASP.NET":
                tecnologia = prompt("","Ingrese una tcnología válida")
            puesto = prompt ("","Ingrese el puesto por el que se postulará:")
            while puesto != "Js" or puesto != "Ssr" or puesto != "Sr":
                puesto = prompt ("", "Ingrese un puesto válido")
#a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
#cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.

            match genero:
                case "NB":
                    edadNB += edad
                    contadorNB += 1
                    match tecnologia:
                        case "JS"|"ASP.NET":
                            if edad < 25 and edad > 40 and puesto == "Ssr":
                                postulantes_a += 1
                case "M":
                    edadM += edad
                    contadorM += 1
                case "F":
                    edadF += edad
                    contadorF += 1
#b. Nombre del postulante Jr con menor edad.                
            match puesto:
                case "Jr":
                    if bandera == True:
                        menor_edad = edad
                        bandera = False 
                    if menor_edad > edad:
                        edad = menor_edad 
                        nombre_puntob = nombre
                
#c. Promedio de edades por género.
            promedioNB = edadNB / contadorNB
            promedioM = edadM / contadorM
            promedioF = edadF / contadorF
#d. Tecnologia con mas postulantes (solo hay una).
            if tecnologia == "ASP.NET":
                contadorASPNET += 1
            elif tecnologia == "JS":
                contadorJS += 1
            else: 
                contadorPYTHON += 1
            if contadorPYTHON > contadorASPNET and contadorPYTHON > contadorJS:
                mayor_tecnologia = "Python"
            elif contadorASPNET > contadorJS and contadorASPNET > contadorPYTHON:
                mayor_tecnologia = "ASP.NET"
            else:
                mayor_tecnologia = "JS"

                

#e. Porcentaje de postulantes de cada genero.
            porcentajeNB = (contadorNB / 10)*100
            porcentajeM = (contadorM / 10)*100
            porcentajeF = (contadorF / 10)*100
        
        print(f"1) {postulantes_a}. B) {nombre_puntob}. C) Promedio género Femenino: {promedioF}. Promedio género Masculino: {promedioM}. Promedio género NB:{promedioNB}. D) Tecnología con mayor postulantes: {mayor_tecnologia}. E) Los porcentajes son: F:{porcentajeF}, M:{porcentajeM} y NB: {porcentajeNB}" )

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
