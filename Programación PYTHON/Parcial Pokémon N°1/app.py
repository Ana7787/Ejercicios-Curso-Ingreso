# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
#El profesor OAK de pueblo paleta quiere que construyas un modelo prototipico de pokedex con algunos pokemones de prueba.

A) Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon
    * El tipo de su elemento (Agua, Psiquico, Electrico)
    * Poder de ataque (validar que sea mayor a 50 y menor a 200)
B) Al presionar el boton mostrar se deberan listar los pokemones y su posicion en la lista (por terminal) 

Del punto C solo debera realizar 3 informes. Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    Informe 1- Tome el ultimo numero de su DNI Personal (Ej 4) y realice ese informe (Ej, Realizar informe 4)
    (Se debera informar por print al presionar el boton "informe 1" por terminal)

    Informe 2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). En caso de que su DNI 
    finalice con el numero 0, debera realizar el informe 9.
    (Se debera informar por print al presionar el boton "informe 2" por terminal)

    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 
C) NOMBRE TIPO PODER ATAQUE
    #! 0) - Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10% extra supere los 100 puntos.
    #! 1) - Cantidad de pokemones de tipo Electrico cuyo poder de pelea con un 15% menos este entre los 100 y los 150 puntos.
    #! 2) - Nombre y Poder del pokemon de tipo electrico con el poder mas alto.
    #! 3) - Nombre y Poder del pokemon de tipo psiquico con el poder mas bajo.
    #! 4) - Porcentaje de pokemones de tipo agua con mas de 100 puntos de poder (Sobre el total de pokemones ingresados).
    #! 5) - Porcentaje de pokemones de tipo psiquico con poder de pelea inferior o igual a 150 (sobre el total de pokemones ingresados).
    #! 6) - tipo de los pokemones(Agua, Psiquico, Electrico) que mas pokemones posea. 
    #! 7) - tipo de los pokemones(Agua, Psiquico, Electrico)  que menos pokemones posea. 
    #! 8) - Listado de todos los pokemones cuyo poder de pelea supere el valor promedio.
    #! 9) - el promedio de poder de todos los pokemones de tipo Electrico.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA - Pokedex")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="Pokedex 🎮", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        self.image = tk.PhotoImage(file='Logo_UTN_App.png')
        
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = 'Banner')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_pokedex_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_mostrar)
        self.btn_informe_1.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_2.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_3.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        # Cargar aca los pokemones
        self.lista_nombre_pokemones = ["Pikachu", "Charizard", "Bulbasaur", "Squirtle", "Jigglypuff", "Psyduck",
                                        "Eevee", "Gengar", "Mewtwo", "Vaporeon"]
        self.lista_poder_pokemones = [80, 150, 70, 90, 60, 100, 75, 120, 180, 95]
        self.lista_tipo_pokemones = ["Electrico", "fuego", "planta", "agua", "normal", "agua", 
                                        "normal", "fantasma", "psíquico", "agua"]
        self.lista_pokemones_mas_poder = []



    def btn_cargar_pokedex_on_click(self):
        for pokemon in range (2):
            nombre = prompt("","Ingrese el nombre:")
            while nombre.isalpha() == False or nombre == None:
                nombre = prompt("","Ingrese el nombre:")
            self.lista_nombre_pokemones.append(nombre)
            tipo = prompt ("","Ingrese su elemento:")
            while tipo.isalpha() == False or tipo == None or tipo != "Agua" and tipo != "Psiquico" and tipo != "Electrico":
                tipo = prompt ("","Ingrese un elemento válido:")
            self.lista_tipo_pokemones.append(tipo)
            poder = int(prompt ( "","Ingrese su poder de ataque:"))
            while poder < 50 or poder > 200:
                poder = int(prompt ( "","Ingrese un poder de ataque válido:"))
            self.lista_poder_pokemones.append(poder)

        alert ("","Carga terminada")

 
    def btn_mostrar_mostrar(self):
        for i in range (len(self.lista_nombre_pokemones)):
            nombres = self.lista_nombre_pokemones[i] 
            print(f"{i+1} {nombres}")
    
    #! 0) - Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10% extra supere los 100 puntos.   
    #! 1) - Cantidad de pokemones de tipo Electrico cuyo poder de pelea con un 15% menos este 
    # entre los 100 y los 150 puntos.
    def btn_mostrar_informe_1(self):

        contador_informe1 = 0

        for i in range (len(self.lista_tipo_pokemones)):
            if self.lista_tipo_pokemones[i] == "Electrico":
                poder_reducido = self.lista_poder_pokemones[i]*0.85
                if poder_reducido < 150 and poder_reducido > 100:
                    contador_informe1 += 1
                    
        print(contador_informe1)

   
    #! 8) - Listado de todos los pokemones cuyo poder de pelea supere el valor promedio. 
    def btn_mostrar_informe_2(self):
        pass
        
    
if __name__ == "__main__":
    app = App()
    app.mainloop()