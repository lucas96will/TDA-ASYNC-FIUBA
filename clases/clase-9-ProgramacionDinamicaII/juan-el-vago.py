# Ejercicios: Juan el vago
# Juan es ambicioso pero también algo vago. Dispone de varias ofertas de trabajo diarias, 
# pero no quiere trabajar dos días seguidos. Dado un arreglo con el monto esperado a ganar 
# cada día, determinar por programación dinámica el máximo monto a ganar, sabiendo que no 
# aceptará trabajar dos días seguidos.
#
# Si Juan quiere planificar su semana, tendríamos un arreglo con los montos
# esperados para los 5 días laborables. ¿Cuales son los mejores días en los que 
# Juan puede trabajar respetando nuestra sagrada ley de mínimo esfuerzo? 


# Regla: no trabajar dos dias seguidos, maximizando la ganancia total
# lunes,martes,miercoles,jueves,viernes
# pagos = [100, 20, 30, 70, 20]
# lunes: 100 
# martes: 100 
# miercoles: 100, 30 
# jueves: max(martes + 70, miercoles) = 170 que es martes + 70
# viernes: max(miercoles + 20, jueves)

# creo que la ecuacion de recurrencia es E(N) = MAX(E(N-2) + 1, E(N-1))
# o bien puedo tomar el pago actual y el pago de la solucion al dia anterior del anterior (restriccion)
# o tomar la solucion del pago del dia anterior (ya que no puedo tomar el dia actual si eso pasara)

def juan_el_vago(pagos):
    k = len(pagos)

    np = [0] * k
    np[0] = pagos[0]
    np[1] = max(pagos[0], pagos[1])

    for i in range(2, k):
        
        np[i] = max(np[i-2] + pagos[i], np[i-1])

    print(np)
    return reconstruccion(pagos, np)

def reconstruccion(pagos, np):
    elecciones = []
    i = len(pagos) - 1
    while i >= 0:
        opt_ayer = np[i-1] if i > 0 else 0
        opt_anteayer = np[i-2] if i > 1 else 0
        valor_hoy = pagos[i]
        if valor_hoy + opt_anteayer >= opt_ayer:
            elecciones.append(i)
            i -= 2 
        else:
            i -= 1 
    elecciones.reverse()
    return elecciones

if __name__ == "__main__":

    pagos = [100, 20, 30, 70, 20]

    pago_obtenido = juan_el_vago(pagos)
    print(pago_obtenido) 
