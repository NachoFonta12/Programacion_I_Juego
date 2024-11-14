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

def mezclar_baraja(baraja: list)->list:
    #baraja = random.shuffle(baraja)
    for i in range(len(baraja)):
        indice_mezcla = random.randint(0, len(baraja)-1)
        while indice_mezcla == i:
            indice_mezcla = random.randint(0, len(baraja)-1)
        temporal = baraja[i]
        baraja[i] = baraja[indice_mezcla]
        baraja[indice_mezcla] = temporal
    return baraja

def repartir_mazo(mazo: list, cantidad_cartas)->list:
    mazo_jugador = []
    for i in range(cantidad_cartas):
        carta = mazo.pop(0)
        mazo_jugador.append(carta)
    return mazo_jugador

def generar_elementos(elementos:dict)->dict:
    for clave in elementos:
        elementos[clave] = random.randint(100,200)
    return elementos

def asignar_nombres()->list:
    nombre = input("Ingrese su nombre: ")
    return nombre

def sortear_atributo(lista: list)->str:
    atributos = list(lista[0].keys())
    atributos.remove("nombre")
    return random.choice(atributos)

def leer_lista(lista: list):
    for i in range(len(lista)):
        print(lista[i])

def comparar_cartas(mazo_jugador_uno: list, mazo_jugador_dos: list, atributo: str)->None|bool:
    #True: gano la ronda el jugador 1
    #False: gano la ronda el jugador 2
    #none: hubo empate en la ronda
    estado_ronda = None

    carta_jugador_uno = mazo_jugador_uno[0]
    carta_jugador_dos = mazo_jugador_dos[0]

    # PRINT(ATRIBUTO)
    # PRINT(CARTA_JUGADOR_UNO[ATRIBUTO])
    # PRINT(CARTA_JUGADOR_DOS[ATRIBUTO])


    if carta_jugador_uno[atributo] > carta_jugador_dos[atributo]:
        estado_ronda = True
    elif carta_jugador_uno[atributo] < carta_jugador_dos[atributo]:
        estado_ronda = False
    
    return estado_ronda

def llevar_cartas_mesa(mazo_mesa: list, mazo_jugador_uno: list, mazo_jugador_dos)->list:
    carta_jugador_uno = mazo_jugador_uno.pop(0)
    carta_jugador_dos = mazo_jugador_dos.pop(0)
    # print(type(carta_jugador_uno))
    # print(type(carta_jugador_dos))
    mazo_mesa.append(carta_jugador_uno)
    mazo_mesa.append(carta_jugador_dos)
    return mazo_mesa

def determinar_ganador(rondas, mazo_jugador_uno, mazo_jugador_dos, maximo_rondas_posible: list = 250):
    if len(mazo_jugador_uno) == 0:
        return 2
    elif len(mazo_jugador_dos) == 0:
        return 1
    elif rondas >= maximo_rondas_posible:
        if len(mazo_jugador_uno) > len(mazo_jugador_dos):
            return 1
        elif len(mazo_jugador_uno) < len(mazo_jugador_dos):
            return 2
    else: return None

def mostrar_lista(lista: list):
    for pokemon in lista:
        print(f"{pokemon["nombre"]:10} - {pokemon["velocidad"]:3} - {pokemon["fuerza"]:3} - {pokemon["elemento"]:15} - {pokemon["peso"]:5} - {pokemon["altura"]:4}")

def cargar_puntaje_a_json(path:str,datos:dict):

    with open(path,"w", encoding="utf8") as archivo_estadisticas:
        json.dump(datos,archivo_estadisticas,indent=4)

def crear_puntaje(ganador: str, cantidad_cartas: int)->dict:
    fecha_actual = str(date.today())
    diccionario = {"nombre" : ganador, "puntaje" : cantidad_cartas, "fecha" : fecha_actual}
    return diccionario

def leer_puntaje_json(path:str)->dict:

    with open(path,"r") as archivo_estadisticas:
        puntajes = json.load(archivo_estadisticas)
        
    return puntajes

def mostrar_estadisticas(puntajes:dict):
    for dato in puntajes["estadisticas"]:
        print(f"{dato["nombre"]:10} - {dato["puntaje"]:4} - {dato["fecha"]:12}")


def iniciar_juego(path):
        
    rondas = 0
    seguir_jugando = True
    nombre_jugador_uno = asignar_nombres()
    nombre_jugador_dos = asignar_nombres()

    ganador_final = None
    lista_cartas = parsear_csv(path)
    minimo_rondas_posible = len(lista_cartas) / 2
    maximo_rondas_posible = len(lista_cartas)

    mezclar_baraja(lista_cartas)
    mazo_jugador_uno = repartir_mazo(lista_cartas, 250)
    mazo_jugador_dos = repartir_mazo(lista_cartas, 250)
    mazo_mesa = []

    while seguir_jugando == True:
        atributo = sortear_atributo(mazo_jugador_dos)
        ganador_ronda = comparar_cartas(mazo_jugador_uno, mazo_jugador_dos, atributo)
        if ganador_ronda == True:
            carta_perdedora = mazo_jugador_dos.pop(0)
            mazo_jugador_uno.append(carta_perdedora)
            for _ in range(len(mazo_mesa)):
                carta_empatada = mazo_mesa.pop(0)
                mazo_jugador_uno.append(carta_empatada)
        elif ganador_ronda == False:
            carta_perdedora = mazo_jugador_uno.pop(0)
            mazo_jugador_dos.append(carta_perdedora)
            for _ in range(len(mazo_mesa)):
                carta_empatada = mazo_mesa.pop(0)
                mazo_jugador_dos.append(carta_empatada)
        else:
            mazo_mesa = llevar_cartas_mesa(mazo_mesa, mazo_jugador_uno, mazo_jugador_dos)
        print(f"Mazo 1: {len(mazo_jugador_uno)} - Mazo 2: {len(mazo_jugador_dos)}")
        rondas += 1
        if rondas >= minimo_rondas_posible:
            ganador_final = determinar_ganador(rondas, mazo_jugador_uno, mazo_jugador_dos, maximo_rondas_posible)
        elif rondas == maximo_rondas_posible:
            ganador_final = determinar_ganador(rondas, mazo_jugador_uno, mazo_jugador_dos, maximo_rondas_posible)
        if ganador_final is not None or rondas >= maximo_rondas_posible:
            seguir_jugando = False

    if ganador_final == 1:
        nombre_ganador = nombre_jugador_uno
        mazo_ganador = mazo_jugador_uno
    elif ganador_final == 2:
        nombre_ganador = nombre_jugador_dos
        mazo_ganador = mazo_jugador_dos
    else: print("Hubo un empate.")

    print(f"Ganó {nombre_ganador} con {len(mazo_ganador)} cartas.")
    datos_ganador = crear_puntaje(nombre_ganador, len(mazo_ganador))
    cargar_puntaje_a_json("juego_consola/estadisticas.json", datos_ganador)
    leer_puntaje_json("juego_consola/estadisticas.json")