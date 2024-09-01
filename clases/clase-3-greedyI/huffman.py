def huffman(texto):
    frecuencias = calcular_frecuencias(texto)
    q = heap_crear()
    for caracter in frecuencia:
        q.encolar(Hoja(caracter, frecuencia))
    while q.cantidad() > 1:
        t1 = q.desencolar()
        t2 = q.desencolar()
        q.encolar(Arbol(t1,t2, t1.frecuencia + t2.frecuencia))
    return codificar(q.desencolar())
