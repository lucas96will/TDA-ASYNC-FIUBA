# Mas de la mitad de las veces
# Algoritmo de orden O(nlogn)
# Dado un arreglo de n numeros, devuelve true o false segun
# si existe algun elemento que aparezca mas de la mitad
# de las veces. Justificar el orden!
def mas_de_la_mitad(array):
    
    return _mas_de_la_mitad_dyc(array, 0, len(array) - 1)

def _mas_de_la_mitad_dyc(array, right, left):
    
    if left - right < 1:
        return array[right]
    
    mid = (left + right) // 2

    #llamo a derecha e izquierda
    e1 = _mas_de_la_mitad_dyc(array, right, mid)
    e2 = _mas_de_la_mitad_dyc(array, mid + 1, left)


    return _verificar_combinacion(e1, e2, array, right, left)

def _verificar_combinacion(e1, e2, arr, right, left):
    count_der = count_izq = 0
    for i in range(right, left + 1):
        if e1 == arr[i]:
            count_der += 1 
        if e2 == arr[i]:
            count_izq += 1 

    if count_der > (left - right + 1)//2:
        return e1
    if count_izq > (left - right + 1)//2:
        return e2
    return None

if __name__ == "__main__":
    arrays = [  [1, 2, 1, 2, 3],
                [1, 1, 2, 3],
                [1, 2, 3, 1, 1, 1],
                [1]
              ]
    for array in arrays:
        print(array, "Mas de la mitad ", mas_de_la_mitad(array) != None)


    
