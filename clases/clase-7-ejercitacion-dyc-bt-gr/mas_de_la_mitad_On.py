def mas_de_la_mitad_dyc_on(array):
    
    if len(array) == 0:
        return None

    if len(array) == 1:
        return array[0]
    
    arr_nuevo = []

    for i in range(0, len(array)-1, 2):
        if array[i] == array[i+1]:
            arr_nuevo.append(array[i])

    candidato = mas_de_la_mitad_dyc_on(arr_nuevo)

    return aparece_mas_de_la_mitad(array, candidato)

def aparece_mas_de_la_mitad(array, candidato):
    if candidato is not None and array.count(candidato) > len(array) // 2:
        return candidato
    
    if len(array) % 2 != 0 and array.count(array[-1]) > len(array) // 2:
        return candidato

    return None
    
    
def mas_de_la_mitad(array):
    return mas_de_la_mitad_dyc_on(array)


if __name__ == "__main__":
    arrays = [  [1, 2, 1, 2, 3],
                [1, 1, 2, 3],
                [1, 2, 3, 1, 1, 1],
                [1]
              ]
    for array in arrays:
        print(array, "Mas de la mitad ", mas_de_la_mitad(array) != None)


    
