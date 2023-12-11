import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Ana Clara Gonzalez
Pacial Ingreso UTN Tecnicatura en Programación
Fecha: 02.08.23

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
            
            nombre = prompt("","Ingrese su nombre:")
            while not nombre.isalpha() or nombre == None:
                nombre = prompt("","Ingrese un nombre válido:")
            seguidores = prompt("","Ingrese la cantidad de seguidores:")
            while not seguidores.isdigit() or (float(seguidores) < 0 and float(seguidores) % 1 != 0):
                seguidores = prompt("","Ingrese una cantidad de seguidores válida")
            seguidores = int(seguidores)
            publicaciones = prompt("","Ingrese la cantidad de publicaciones")
            while not publicaciones.isdigit() or (float(publicaciones)) > 1000 or float(publicaciones) % 1 != 0:
                publicaciones = prompt("","Ingrese un cantidad de publicaciones válida")
            publicaciones = int(publicaciones)
            tipo = prompt ("","Ingrese el tipo de publicación: foto, video o reels")
            while (tipo != "foto" and tipo != "video" and tipo != "reels") or tipo.isdigit:
                tipo = prompt("","Ingrese un tipo de publicacion válida:")

            self.lista_nombre.append(nombre)
            self.lista_seguidores.append(seguidores)
            self.lista_publicaciones.append(publicaciones)
            self.lista_tipo.append(tipo)
 
    def btn_mostrar_on_click(self):

        for i in range (len(self.lista_nombre)):
            print(f"{i} {self.lista_nombre[i]}")


    def btn_informar_on_click(self):

# 0- Muestra el perfil con la mayor cantidad de publicaciones.

        bandera1 = True
        mas_publicaciones = 0

        for i in range (len(self.lista_publicaciones)):
            if bandera1 == True or mas_publicaciones < self.lista_publicaciones[i]:
                mas_publicaciones = self.lista_publicaciones[i]
                mas_usuario = self.lista_nombre[i]
                bandera1 = False
            
        print(f"0)El usuario con mayor cantidad de publicaciones es {mas_usuario} con {mas_publicaciones} publicaciones")


#1- Muestra el perfil con la menor cantidad de publicaciones.
        bandera2 = True

        for i in range (len(self.lista_publicaciones)):
            if bandera2 == True:
                menor_publicaciones = self.lista_publicaciones[i]
                menor_usuario = self.lista_nombre[i]
                bandera2 = False
            if self.lista_publicaciones[i] < menor_publicaciones:
                menor_publicaciones = self.lista_publicaciones[i]
                menor_usuario = self.lista_nombre[i]

        print(f"1)El usuario con menor cantidad de publicaciones es {menor_usuario} con {menor_publicaciones} publicaciones")

#2- Muestra los perfiles con más seguidores que publicaciones.
        self.lista_perfiles_mas_seguidores_que_publicaciones = []

        for i in range (len(self.lista_seguidores)):
            if self.lista_seguidores[i] > self.lista_publicaciones[i]:
                perfiles_mas_seguidores_que_publicaciones = self.lista_nombre[i]
                self.lista_perfiles_mas_seguidores_que_publicaciones.append(perfiles_mas_seguidores_que_publicaciones)


        print(f"2)Los usuarios con más seguidores que publicaciones son: {self.lista_perfiles_mas_seguidores_que_publicaciones}")

#3- Muestra los perfiles con menos seguidores que publicaciones.
        self.lista_perfiles_menos_seguidores_que_publicaciones = []

        for i in range (len(self.lista_seguidores)):
            if self.lista_seguidores[i] < self.lista_publicaciones[i]:
                perfiles_menos_seguidores_que_publicaciones = self.lista_nombre[i]
                self.lista_perfiles_menos_seguidores_que_publicaciones.append(perfiles_menos_seguidores_que_publicaciones)


        print(f"3)Los usuarios con más seguidores que publicaciones son: {self.lista_perfiles_menos_seguidores_que_publicaciones}")


#4- Cantidad de perfiles con más de 1000 seguidores y menos de 50 publicaciones.

        contador_perfiles_4 = 0

        for i in range (len(self.lista_seguidores)):
            if self.lista_seguidores[i] > 1000 and self.lista_publicaciones[i] < 50:
                contador_perfiles_4 += 0

        print(f"4) La cantidad de perfiles con más de 1000 seguidores y menos de 50 publicaciones son: {contador_perfiles_4}")

#5- Cantidad de perfiles con menos de 500 seguidores y mas de 100 publicaciones.

        contador_perfiles_5 = 0

        for i in range (len(self.lista_seguidores)):
            if self.lista_seguidores[i] < 500 and self.lista_publicaciones[i] > 100:
                contador_perfiles_5 += 1

        print(f"5) La cantidad de perfiles con menos de 500 seguidores y más de 100 publicaciones es de: {contador_perfiles_5}")

#6- El tipo que mas publicaciones tuvo.

        mas_publicaciones = 0
        bandera3 = True

        for i in range (len(self.lista_publicaciones)):
            if bandera3 == True or mas_publicaciones < self.lista_publicaciones[i]:
                mas_publicaciones = self.lista_publicaciones[i]
                perfil_mas_publicaciones = self.lista_nombre[i]
                bandera3 = False
        
        print(f"6) El perfil que más publicaciones tuvo es el de: {perfil_mas_publicaciones}")


#7- El tipo que menos seguidores tuvo.
        
        bandera4 = True

        for i in range (len(self.lista_publicaciones)):
            if bandera4 == True or menos_seguidores > self.lista_seguidores[i]:
                menos_seguidores = self.lista_seguidores[i]
                perfil_menos_seguidores = self.lista_nombre[i]
                bandera4 = False
        
        print(f"7) El perfil que menos seguidores tuvo es el de: {perfil_menos_seguidores}")


#8- Mostrar el promedio de seguidores 

        acumulador_seguidores = 0
        promedio_seguidores = 0
        total_seguidores = len(self.lista_seguidores)

        for i in range (len(self.lista_seguidores)):
            acumulador_seguidores = self.lista_seguidores[i] + acumulador_seguidores

        promedio_seguidores = acumulador_seguidores/total_seguidores
        
        print(f"8)El promedio de seguidores es de {promedio_seguidores}")


#9- Mostrar todos los perfiles cuyas publicaciones supere el valor promedio.

        self.lista_perfiles_superen_mayor_promedio = []
        total_publicaciones = len(self.lista_publicaciones)
        acumulador_publicaciones = 0


        for i in range (len(self.lista_publicaciones)):
            acumulador_publicaciones += self.lista_publicaciones[i]
            
        promedio_publicaciones = acumulador_publicaciones/total_publicaciones

        for i in range (len(self.lista_publicaciones)):
            if self.lista_publicaciones[i] > promedio_publicaciones:
                perfiles_pub_superen_promedio = self.lista_nombre[i]
                
                self.lista_perfiles_superen_mayor_promedio.append(perfiles_pub_superen_promedio)

        print(f"9) Los perfiles cuyas publicaciones superan el valor promedio son: {self.lista_perfiles_superen_mayor_promedio}")

       
if __name__ == "__main__":
    app = App()
    app.geometry("200x400")
    app.mainloop()

