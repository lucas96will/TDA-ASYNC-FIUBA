# Ejercicio: Caminos posibles en un laberinto

# Dado un laberinto representado por una grilla, queremos calcular la ganancia 
# máxima que existe desde la posición (0,0) hasta la posición NxM
#
# Los movimientos permitidos son, desde la esquina superior izquierda (el 0,0), 
# nos podemos mover hacia abajo o hacia la derecha
#
# Pasar por un casillero determinado i,j nos da una ganancia de Vij
# Si hay algunos lugares por los que no podemos pasar (obstáculos), cómo hay que 
# modificar el algoritmo anterior para resolver el mismo problema?
def caminos(mapa): 



# OPTIMO(actual) = max(vengo de la izq, vengo de arriba) + dinero(actual)

if __name__ == "__main__":
    laberinto = [
        [10, 10, 10, 0, 0],
        [0, 0, 0, 0, 0],
        [10, 10, 10, 0, 0],
        [0, 0, 10, 0, 0],
        [0, 10, 10, 0, 0]
    ]  

    recorrido_mayor_ganancia = caminos(laberinto)

