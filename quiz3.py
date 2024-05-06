#Nicolás Uribe
#Jackson Monk
#Samuel Ramírez Pérez

import random as r    #importamos la librería random
class Juego:          #creamos la clase Juego
    def __init__(self):     #definimos el constructor
        self.eleccion_usuario = None #se inicializan las variables globales: eleccion_usuario y eleccion_computadora
        self.eleccion_computadora = None

    def obtener_eleccion_usuario(self): #definimos una función para obtener la elección del usuario.
        flag = True
        while flag:
            self.ppt = input("¿Piedra, Papel o Tijera? ").lower()  #se pide al usuario ingresar su elección.
            if self.ppt != "piedra" and self.ppt != "papel" and self.ppt != "tijera":  #se determina si la opción ingresada es válida.
                print("Escoge una opción válida.")
            else:
                self.eleccion_usuario = self.ppt   #se guarda la opción válida en la variable global "eleccion_usuario".
                flag = False

    def generar_eleccion_computadora(self): #definimos una funcion para generar una elección aleatoria de la computadora.
        self.opciones = ["piedra", "papel", "tijera"]
        self.eleccion_computadora = r.choice(self.opciones) #se utiliza la librería random para generar la elección de la computadora aleatoriamente.
        print(self.eleccion_computadora)

    def determinar_ganador(self): #definimos una funcion para determinar el ganador.
        if self.eleccion_usuario == self.eleccion_computadora:
            return print("Empate.")
        elif (self.eleccion_computadora == "piedra" and self.eleccion_usuario == "tijera") or (self.eleccion_computadora == "tijera" and self.eleccion_usuario == "papel") or (self.eleccion_computadora == "papel" and self.eleccion_usuario == "piedra"):
            return print("Gana la computadora.")
        else:
            return print("Ganaste Pibe.") #se determina el ganador dependiendo de las elecciones y si son la misma, queda en empate.
        
    def jugar(self): #definimos una funcion que permite jugar al juego.
        flag = True
        while flag:
            self.obtener_eleccion_usuario()
            self.generar_eleccion_computadora()   #se llama a cada método previamente definido.
            self.determinar_ganador()  
            while True:  #generamos un bucle con condicionales que define si el usuario quiere seguir jugando o no.
                self.seguir_jugando = input("¿Quieres seguir jugando? ").lower()
                if self.seguir_jugando == "si":
                    break
                elif self.seguir_jugando == "no":
                    print("La buena.")
                    flag = False
                    break
                else:
                    print("Ingrese si o no.")
                    


jugar = Juego() #creamos una instancia de la clase llamada "jugar".
jugar.jugar() #de la instancia, se llama la funcion "jugar" para jugar al juego.

