from funciones import *
# path = "C:/Users/Usuario/Desktop/Repositorio/Programacion_I_Juego/juego_consola/MOCK_DATA.csv"
path = "juego_consola/prueba_pokemones.csv"
elementos = {"agua":0 ,"tierra":0, "aire":0, "fuego":0, "electricidad":0}

seguir_jugando = True
while seguir_jugando == True:
    ganador_final = None
    lista_cartas = parsear_csv(path)
    minimo_rondas_posible = len(lista_cartas) / 2
    #maximo_rondas_posible = len(lista_cartas)
    maximo_rondas_posible = 10
    atributo = sortear_atributo(lista_cartas)
    mezclar_baraja(lista_cartas)
    mazo_jugador_uno = repartir_mazo(lista_cartas, 250)
    mazo_jugador_dos = repartir_mazo(lista_cartas, 250)
    mazo_mesa = []
    rondas = 0

    ganador_ronda = comparar_cartas(mazo_jugador_uno, mazo_jugador_dos, atributo)
    if ganador_ronda == True:
        carta_perdedora = mazo_jugador_dos.pop(0)
        mazo_jugador_uno.append(carta_perdedora)
    elif ganador_ronda == False:
        carta_perdedora = mazo_jugador_uno.pop(0)
        mazo_jugador_dos.append(carta_perdedora)
    else:
        mazo_mesa = llevar_cartas_mesa(mazo_mesa, mazo_jugador_uno, mazo_jugador_dos)

    if rondas >= minimo_rondas_posible:
        ganador_final = determinar_ganador(rondas, mazo_jugador_uno, mazo_jugador_dos, maximo_rondas_posible)
    elif rondas == maximo_rondas_posible:
        ganador_final = determinar_ganador(rondas, mazo_jugador_uno, mazo_jugador_dos, maximo_rondas_posible)
    
    if ganador_final != None:
        seguir_jugando = False
    rondas += 1

if ganador_final == 1:
    print(f"Ganó el jugador uno con {len(mazo_jugador_uno)} cartas.")
elif ganador_final == 2:
    print(f"Ganó el jugador dos con {len(mazo_jugador_dos)} cartas.")
else: print("Hubo un empate.")

print(rondas)
# leer_lista(lista_cartas)
# mezclar_barajas(lista_cartas)
# print("-" * 70)
# leer_lista(lista_cartas)
# atributo = sortear_atributo(lista_cartas)
# repartir_mazo(lista_cartas)
#lista_nombres = asignar_nombres()

fecha_actual = str(date.today())
datos = {}
primer_ganador = {"nombre":"pepe","puntaje":25,"fecha":fecha_actual}
segundo_ganador = {"nombre":"sebastian","puntaje":50,"fecha":fecha_actual}
tercer_ganador = {"nombre":"agustina","puntaje":60,"fecha":fecha_actual}
cuarto_ganador = {"nombre":"florencia","puntaje":55,"fecha":fecha_actual}
datos["estadisticas"] = [primer_ganador,segundo_ganador,tercer_ganador,cuarto_ganador]
path_estadisticas = "juego_consola/estadisticas.json"
# cargar_puntaje_a_json(path_estadisticas,datos)
# aux_datos = leer_puntaje_json(path_estadisticas)
# # print(aux_datos)

# mostrar_estadisticas(aux_datos)


mostrar_lista(lista_cartas)
#comparar_cartas(lista_cartas, lista_cartas_2, atributo)
