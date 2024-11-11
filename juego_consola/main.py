import random
def generar_elementos(elementos:dict)->dict:

    for clave in elementos:
        elementos[clave] = random.randint(100,200)

    return elementos


with open("MOCK_DATA.csv","r") as archivo_cartas:
    diccionario_carta = {}
    # {"nombre":"",
    #  "velocidad":0,
    #  "fuerza":0,
    #  "elemento":"agua",
    #  "peso":0,
    #  "altura":0}
    for linea in archivo_cartas:
        linea = linea.split(",|\n")
        diccionario_carta["nombre"] = linea[0]
        diccionario_carta["velocidad"] = linea[1]
        diccionario_carta["fuerza"] = linea[2]
        diccionario_carta["elemento"] = linea[3]
        diccionario_carta["nombre"] = linea[4]
        diccionario_carta["nombre"] = linea[4]

elementos = {"agua":0 ,"tierra":0, "aire":0, "fuego":0, "electricidad":0}
# jugador_uno = ""
# jugador_dos = ""

# jugador_uno = input("Ingrese su nombre: ")
# jugador_dos = input("Ingrese su nombre: ")

listas_cartas = [
    {"nombre":"",
     "velocidad":0,
     "fuerza":0,
     "elemento":"agua",
     "peso":0,
     "altura":0},

     {"nombre":"",
     "velocidad":0,
     "fuerza":0,
     "elemento":"tierra",
     "peso":0,
     "altura":0},

     {"nombre":"",
     "velocidad":0,
     "fuerza":0,
     "elemento":"fuego",
     "peso":0,
     "altura":0},

     {"nombre":"",
     "velocidad":0,
     "fuerza":0,
     "elemento":"agua",
     "peso":0,
     "altura":0},

     {"nombre":"",
     "velocidad":0,
     "fuerza":0,
     "elemento":"aire",
     "peso":0,
     "altura":0},

     {"nombre":"",
     "velocidad":0,
     "fuerza":0,
     "elemento":"tierra",
     "peso":0,
     "altura":0}
]





