from funciones import *
# path = "C:/Users/Usuario/Desktop/Repositorio/Programacion_I_Juego/juego_consola/MOCK_DATA.csv"
path = "juego_consola/prueba_pokemones.csv"
elementos = {"agua":0 ,"tierra":0, "aire":0, "fuego":0, "electricidad":0}


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

lista_cartas = parsear_csv(path)
mostrar_lista(lista_cartas)
#comparar_cartas(lista_cartas, lista_cartas_2, atributo)
