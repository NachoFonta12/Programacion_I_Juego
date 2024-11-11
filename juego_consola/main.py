from funciones import *
path = "C:/Users/Usuario/Desktop/Repositorio/Programacion_I_Juego/juego_consola/MOCK_DATA.csv"
elementos = {"agua":0 ,"tierra":0, "aire":0, "fuego":0, "electricidad":0}

lista_cartas = generar_lista_diccionario(path)
leer_lista(lista_cartas)
mezclar_barajas(lista_cartas)
print("-" * 70)
leer_lista(lista_cartas)
atributo = sortear_atributo(lista_cartas)
repartir_mazo(lista_cartas)
#lista_nombres = asignar_nombres()



print(atributo)
#comparar_cartas(lista_cartas, lista_cartas_2, atributo)
