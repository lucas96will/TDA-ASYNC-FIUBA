import sys
import os

# Add the path to src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from grafo import Grafo

def obtener_invitados(conocidos):
    grafo = Grafo()
    for (a,b) in conocidos:
        if a not in grafo:
            grafo.agregar_vertice(a)
        if b not in grafo:
            grafo.agregar_vertice(b)
        if not grafo.estan_unidos(a,b):
            grafo.agregar_arista(a,b)

    
    while len(grafo) != 0:
        quitar = []
        
        # veo quienes no cumplen req
        for v in grafo.obtener_vertices():
            if len(grafo.adyacentes(v)) < 4:
                quitar.append(v)
        
        if quitar == []:
            break

        for v in quitar:
            grafo.borrar_vertice(v)

    return [v for v in grafo]



if __name__ == "__main__":
    
    pentacompleto = [
        (1,2),
        (1,3),
        (1,4),
        (1,5),
        (2,3),
        (2,4),
        (2,5),
        (3,4),
        (3,5),
        (4,5)
    ]

    conocidos = obtener_invitados(pentacompleto)

    assert len(conocidos) == 5, "los 5 son conocidos"
    print("correcto")
