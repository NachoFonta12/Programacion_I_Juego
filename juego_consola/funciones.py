import random
def generar_lista_diccionario(path):
    with open(path,"r") as archivo_cartas:
        lista_diccionarios = []
        for linea in archivo_cartas:
            diccionario_carta = {}
            linea = linea.split(",")
            diccionario_carta["nombre"] = linea[0]
            diccionario_carta["velocidad"] = linea[1]
            diccionario_carta["fuerza"] = linea[2]
            diccionario_carta["elemento"] = linea[3]
            diccionario_carta["peso"] = linea[4]
            diccionario_carta["altura"] = linea[5]
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
    lista_jugadores = []
    for i in range(2):
        jugador = str(input("Ingrese su nombre: "))
        lista_jugadores.append(jugador)
    return lista_jugadores

def sortear_atributo(lista: list)->str:
    diccionario = lista[0]
    atributo = random.choice(list(diccionario.keys()))
    while atributo == "nombre":
        atributo = random.choice(list(diccionario.keys()))
    return atributo

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
