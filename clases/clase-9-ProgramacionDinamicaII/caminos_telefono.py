# Dado el teclado numérico de un celular, y un número inicial k, 
# encontrar la cantidad de posibles números de longitud N empezando por cierto botón. 
# Restricción: solamente se puede presionar un botón si está arriba, abajo, a izquierda, 
# o derecha del botón actual o el botón actual.


def cant_combinaciones(grafo, pasos, tecla_inicial):
    cant = [][]
    for tecla in range(teclas del 0 al 9):
        cant[0][tecla] = 0
        cant[1][tecla] = 1
    for i in range(2, pasos+1):
        for tecla in range(teclas del 0 al 9):
        contador = 0
        for vecino in grafo.adyacentes(tecla):
            contador += cant[i-1][vecino]
        cant[i][tecla] = contador
    return cant[pasos][tecla_inicial]
