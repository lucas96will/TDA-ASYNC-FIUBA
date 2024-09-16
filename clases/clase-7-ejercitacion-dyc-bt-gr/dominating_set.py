import sys
import os

# Add the path to src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from grafo import Grafo


def dominating_set_min(grafo):
    vertices = grafo.obtener_vertices()
    solucion_optima = set(vertices)
    solucion_parcial = set([])
    return list(dominating_set_rec_vacio(grafo, vertices, 0, solucion_parcial, solucion_optima))

def dominating_set_rec_completo(grafo, vertices, indice, solucion_parcial, solucion_optima):
    
    dominating_set_rec(grafo, vertices, indice, solucion_parcial, solucion_optima)

    dominating_set_rec(grafo, vertices, indice, solucion_parcial, solucion_optima )

    
def dominating_set_rec_vacio(grafo, vertices, indice, solucion_parcial, solucion_optima):
    
    if len(solucion_parcial) >= len(solucion_optima):
        return solucion_optima

    if es_dominating_set(grafo, solucion_parcial):
        return set(solucion_parcial)

    if indice == len(vertices):
        return solucion_optima

    v = vertices[indice]
    solucion_parcial.add(v)
    # poda: me ayuda agregar este elemento?
    solucion_optima = dominating_set_rec_vacio(grafo, vertices, indice+1, solucion_parcial, solucion_optima)
   
    solucion_parcial.remove(v)

    return dominating_set_rec_vacio(grafo, vertices, indice+1, solucion_parcial, solucion_optima)


def es_dominating_set(grafo, solucion_parcial):
    for v in grafo.obtener_vertices():
        if v in solucion_parcial:
            continue
        tiene_adyacente = False
        for w in grafo.adyacentes(v):
            if w in solucion_parcial:
                tiene_adyacente = True
                break
        if tiene_adyacente == False:
            return False
    return True



if __name__ == "__main__":

    arr = [
        (1,4),
        (2,4),
        (3,4),
        (5,4),
        (6,4),
        (6,7),
        (5,8),
        (5,7)
    ]

    grafo = Grafo()
    
    for (a,b) in arr:
        if a not in grafo:
            grafo.agregar_vertice(a)
        if b not in grafo:
            grafo.agregar_vertice(b)
        if not grafo.estan_unidos(a,b):
            grafo.agregar_arista(a,b)
    
    solucion = dominating_set_min(grafo)
    print("grafo")
    print(grafo)
    print("Solucion con cantidad de elementos: ", len(solucion))
    print(solucion)
    assert len(solucion) == 2, "el set dominante es 2 elementos"
    print("El set minimo dominante tiene:", len(solucion), " elementos")
