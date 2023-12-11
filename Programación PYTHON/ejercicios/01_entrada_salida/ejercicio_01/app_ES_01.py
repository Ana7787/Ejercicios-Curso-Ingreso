import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Ana Gonzalez

Enunciado:


Análisis de Perfiles de Instagram
A) Para ello, deberás programar el botón "Cargar Perfiles" para poder cargar 10 perfiles de Instagram con sus respectivas publicaciones.

    Los datos que deberás pedir para cada perfil son:

    Nombre de usuario del perfil.
    Número de seguidores (debe ser un número entero positivo).
    Número de publicaciones (debe ser un número entero positivo, hasta 1000).
    Tipo ("Foto", "Video", "Reels")
    
B) Al presionar el botón "Mostrar", deberás listar los perfiles de Instagram y su posición en la lista (por terminal).

Del punto C solo debera realizar dos informes,
para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

C) Al presionar el boton Informar 
    0- Muestra el perfil con la mayor cantidad de publicaciones.
    1- Muestra el perfil con la menor cantidad de publicaciones.
    2- Muestra los perfiles con más seguidores que publicaciones.
    3- Muestra los perfiles con menos seguidores que publicaciones.
    4- Cantidad de perfiles con más de 1000 seguidores y menos de 50 publicaciones.
    5- Cantidad de perfiles con menos de 500 seguidores y mas de 100 publicaciones.
    6- El tipo que mas publicaciones tuvo.
    7- El tipo que menos seguidores tuvo.
    8- Mostrar el promedio de seguidores 
    9- Mostrar todos los perfiles cuyas publicaciones supere el valor promedio.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("EXAMEN INGRESO")
        
        self.btn_agregar = customtkinter.CTkButton(master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_nombre = [
            "therock",
            "selenagomez",
            "cristiano",
            "beyonce",
            "kimkardashian",
            "kyliejenner",
            "elonmusk",
            "leomessi",
            "katyperry",
            "nasa"
        ]
        self.lista_seguidores = [20000, 150000, 300000, 14000, 2200, 1900, 60000, 180000000, 1600, 4000]
        self.lista_publicaciones = [500, 750, 800, 999, 700, 900, 300, 850, 998, 200]
        self.lista_tipo = ["Foto", "Foto", "Video", "Foto", "Video", "Reels", "Foto", "Video", "Video", "Foto"]

    def btn_agregar_on_click(self):
        for usuarios in range (10):
            nombre = prompt("","Ingrese su nombre")
            while nombre.isdigit():
                nombre = prompt("","Ingrese un nombre correcto")
            seguidores = prompt("","Ingrese la cantidad de seguidores")
            while seguidores % 1 != 0:
                    seguidores = prompt("","Ingrese una cantidad de seguidores correcta")
            seguidores = int(seguidores)
            publicaciones = int(prompt("","Ingrese la cantidad de publicaciones"))
            while publicaciones > 1000:
                publicaciones = int(prompt("","Ingrese la cantidad de publicaciones"))
            tipo = prompt ("","Ingrese el tipo de publicación: foto, video o reels")
            self.lista_nombre.append(nombre)
            self.lista_seguidores.append(seguidores)
            self.lista_publicaciones.append(publicaciones)
            self.lista_tipo.append(tipo)
 
    def btn_mostrar_on_click(self):

        for i in range (len(self.lista_nombre)):
            print(f"{i} {self.lista_nombre[i]}")


    def btn_informar_on_click(self):
#1- Muestra el perfil con la menor cantidad de publicaciones.
        bandera = True

        for i in range (len(self.lista_publicaciones)):
            if bandera == True:
                menor_publicaciones = self.lista_publicaciones[i]
                menor_usuario = self.lista_nombre[i]
                bandera = False
            if self.lista_publicaciones[i] < menor_publicaciones:
                menor_publicaciones = self.lista_publicaciones[i]
                menor_usuario = self.lista_nombre[i]
        print(f"El usuario con menor cantidad de publicaciones es {menor_usuario} con {menor_publicaciones} publicaciones")

#8- Mostrar el promedio de seguidores 

        acumulador_seguidores = 0
        promedio_seguidores = 0
        total_seguidores = len(self.lista_seguidores)

        for i in range (len(self.lista_seguidores)):
            acumulador_seguidores = self.lista_seguidores[i] + acumulador_seguidores

        promedio_seguidores = acumulador_seguidores/total_seguidores
        print(f"El promedio de seguidores es de {promedio_seguidores}")




       
if __name__ == "__main__":
    app = App()
    app.geometry("200x400")
    app.mainloop()

