def lunatico(ganancias):
    k = len(ganancias)
    if k == 0:
        return []
    if k == 1:
        return [0]
    
    if k == 2:
        if ganancias[0] > ganancias[1]:
            return [0]
        else:
            return [1]

    casas_primero, ganancias_primero = _lunatico(ganancias, 0, 1)
    casas_ultimo, ganancias_ultimo = _lunatico(ganancias, 1, 0)
        
    if ganancias_primero > ganancias_ultimo:
        return casas_primero
    else:
        return casas_ultimo

def _lunatico(ganancias, skip_first, skip_last):
    k = len(ganancias)
    np = [0] * (k - skip_last)
    
    np[0+skip_first] = ganancias[0+skip_first]
    np[1+skip_first] = max(ganancias[0+skip_first], ganancias[1+skip_first])

    for i in range(2+skip_first, k-1-skip_last):
        np[i] = max(np[i-2] + ganancias[i], np[i-1]) 

    return reconstruccion(ganancias, np, skip_last, skip_first)

def reconstruccion(ganancias, np, primera, ultima):
    elecciones = []
    total_ganado = 0
    i = len(ganancias) - 1 - primera
    while i >= ultima:
        opt_ayer = np[i-1] if i > 0 else 0
        opt_anteayer = np[i-2] if i > 1 else 0
        valor_hoy = ganancias[i]
        if valor_hoy + opt_anteayer >= opt_ayer:
            elecciones.append(i)
            total_ganado += ganancias[i]
            i -= 2
        else:
            i -= 1

    elecciones.reverse()
    return elecciones, total_ganado



if __name__ == "__main__":
    arr = [15, 1, 10, 20]
    arr2 = [100, 30, 20, 10]
    arr3 = [10, 30, 20, 100]
    casas_a_robar_arr = lunatico(arr)
    print("original: ", arr)
    print("arr", casas_a_robar_arr)
    casas_a_robar_arr2 = lunatico(arr2)
    print("original: ", arr2)
    print("arr2", casas_a_robar_arr2)
    casas_a_robar_arr3 = lunatico(arr3)
    print("original: ", arr3)
    print("arr3", casas_a_robar_arr3)

# si se toma el primero, no se puede tomar el ultimo, por lo que seria un juan-el-vago con k-1 elementos
# si no se toma el primer elemento, es un juan-el-vago con (1, k) elementos
#

def _lunatico_tomando_primero(ganancias, skip_first, skip_last):
    k = len(ganancias)
    np = [0] * (k - skip_last)
    np[0+skip_first] = ganancias[0+skip_first]
    np[1+skip_first] = max(ganancias[0+skip_first], ganancias[1+skip_first])
    for i in range(2+skip_first, k-1-skip_last):
        np[i] = max(np[i-2] + ganancias[i], np[i-1])

            
    return reconstruccion(ganancias, np, 1, 0)


def _lunatico_tomando_ultimo(ganancias, skip_first, skip_last):
    k = len(ganancias)
    np = [0] * (k - skip_last)
    
    np[0+skip_first] = ganancias[0+skip_first]
    np[1+skip_first] = max(ganancias[0+skip_first], ganancias[1+skip_first])

    for i in range(2+skip_first, k-1-skip_last):
        np[i] = max(np[i-2] + ganancias[i], np[i-1]) 

    return reconstruccion(ganancias, np, 0, 1)

def reconstruccion_ultima(ganancias, np):
    elecciones = []
    i = len(ganancias) - 1
    while i >= 1:
        opt_ayer = np[i-1] if i > 0 else 0
        opt_anteayer = np[i-2] if i > 1 else 0
        valor_hoy = ganancias[i]
        if valor_hoy + opt_anteayer >= opt_ayer:
            elecciones.append(i)
            i -= 2
        else:
            i -= 1
    elecciones.reverse()
    return elecciones, total_ganado



def reconstruccion_primera(ganancias, np):
    elecciones = []
    i = len(ganancias) - 2
    while i >= 0:
        opt_ayer = np[i-1] if i > 0 else 0
        opt_anteayer = np[i-2] if i > 1 else 0
        valor_hoy = ganancias[i]
        if valor_hoy + opt_anteayer >= opt_ayer:
            elecciones.append(i)
            i -= 2
        else:
            i -= 1
    elecciones.reverse()
    return elecciones

