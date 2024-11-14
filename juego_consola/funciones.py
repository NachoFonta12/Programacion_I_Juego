import random
import re
import json
from datetime import date
def parsear_csv(path:str)->list:

    with open(path,"r") as archivo_cartas:

        archivo_cartas.readline()

        lista_diccionarios = []
        for linea in archivo_cartas:

            diccionario_carta = {}
            registro = re.split(",|\n",linea)
            diccionario_carta["nombre"] = registro[0]
            diccionario_carta["velocidad"] = registro[1]
            diccionario_carta["fuerza"] = registro[2]
            diccionario_carta["elemento"] = registro[3]
            diccionario_carta["peso"] = registro[4]
            diccionario_carta["altura"] = registro[5]

            lista_diccionarios.append(diccionario_carta)

    return lista_diccionarios

def mezclar_barajas(baraja: list)->list:
    #baraja = random.shuffle(baraja)
    for i in range(len(baraja)):
        indice_mezcla = random.randint(0, len(baraja)-1)
        while indice_mezcla == i:
            indice_mezcla = random.randint(0, len(baraja)-1)
        temporal = baraja[i]
        baraja[i] = baraja[indice_mezcla]
        baraja[indice_mezcla] = temporal
    return baraja

def repartir_mazo(mazo: list)->list:
    mazo_jugador_uno = []
    mazo_jugador_dos = []
    #leer_lista(mazo)
    #print("-" * 70)
    for i in range(len(mazo) // 2):
        carta_uno = mazo.pop(0)
        carta_dos = mazo.pop(0)
        mazo_jugador_uno.append(carta_uno)
        mazo_jugador_dos.append(carta_dos)
    #leer_lista(mazo_jugador_uno)
    #print("-" * 70)
    #leer_lista(mazo_jugador_dos)
    #print("-" * 70)
    #print(len(mazo_jugador_uno))
    #print(len(mazo_jugador_dos))
    return mazo_jugador_uno, mazo_jugador_dos

def generar_elementos(elementos:dict)->dict:
    for clave in elementos:
        elementos[clave] = random.randint(100,200)
    return elementos

def asignar_nombres()->list:
    return [input("Ingrese su nombre: ") for _ in range(2)]

def sortear_atributo(lista: list)->str:
    atributos = list(lista[0].keys())
    atributos.remove("nombre")
    return random.choice(atributos)

def leer_lista(lista: list):
    for i in range(len(lista)):
        print(lista[i])

def comparar_cartas(lista1: list, lista2: list, atributo: str):
    ganador = False
    carta_jugador_uno = lista1.pop(0)
    carta_jugador_dos = lista2.pop(0)
    print(carta_jugador_uno[atributo])
    print(carta_jugador_dos[atributo])
    if carta_jugador_uno[atributo] > carta_jugador_dos[atributo]:
        lista1.append(carta_jugador_dos)
        lista1.append(carta_jugador_uno)
        ganador = True
    elif carta_jugador_uno[atributo] < carta_jugador_dos[atributo]:
        lista2.append(carta_jugador_dos)
        lista2.append(carta_jugador_uno)
        ganador = True
    else:
        while ganador == False:
                carta_jugador_uno = lista1.pop(0)
                carta_jugador_dos = lista2.pop(0)
                if carta_jugador_uno[atributo] > carta_jugador_dos[atributo]:
                    lista1.append(carta_jugador_dos)
                    lista2.append(carta_jugador_uno)
                    ganador = True
                elif carta_jugador_uno[atributo] < carta_jugador_dos[atributo]:
                    lista2.append(carta_jugador_dos)
                    lista2.append(carta_jugador_uno)
                    ganador = True
    #leer_lista(lista1)
    print(len(lista1))
    print("-" * 100)
    #leer_lista(lista2)
    print(len(lista2))

def llevar_cartas_mesa(mazo_mesa: list, mazo_jugador_uno: list, mazo_jugador_dos)->list:
    carta_jugador_uno = mazo_jugador_uno.pop(0)
    carta_jugador_dos = mazo_jugador_dos.pop(0)
    mazo_mesa.append(carta_jugador_uno)
    mazo_mesa.append(mazo_jugador_dos)
    return mazo_mesa

def determinar_ganador(rondas, mazo_jugador_uno, mazo_jugador_dos):
    if len(mazo_jugador_uno) == 0:
        return 2
    elif len(mazo_jugador_dos) == 0:
        return 1
    elif rondas >= 250:
        if len(mazo_jugador_uno) > len(mazo_jugador_dos):
            return 1
        elif len(mazo_jugador_uno) < len(mazo_jugador_dos):
            return 2
    else: return None

def mostrar_lista(lista: list):
    for pokemon in lista:
        print(f"{pokemon["nombre"]:10} - {pokemon["velocidad"]:3} - {pokemon["fuerza"]:3} - {pokemon["elemento"]:15} - {pokemon["peso"]:5} - {pokemon["altura"]:4}")


def cargar_puntaje_a_json(path:str,datos:dict):

    with open(path,"w") as archivo_estadisticas:
        json.dump(datos,archivo_estadisticas,indent=4)

def leer_puntaje_json(path:str)->dict:

    with open(path,"r") as archivo_estadisticas:
        puntajes = json.load(archivo_estadisticas)
        
    return puntajes

def mostrar_estadisticas(puntajes:dict):
    for dato in puntajes["estadisticas"]:
        print(f"{dato["nombre"]:10} - {dato["puntaje"]:4} - {dato["fecha"]:12}")
