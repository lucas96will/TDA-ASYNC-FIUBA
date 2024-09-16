# Backtracking como tecnica de disenio

Backtracking != fuerza brutq

La fuerza bruta prueba todas las decisiones mientras que backtracking no continua sobre un caso que sabe que no tiene solucion (poda).

## Receta de BT 
1. Si ya encontre una solucion, la devuelvo y termino
2. avanzo si puedo
3. Pruebo si la solcion parcial es valida
  1. Si no lo es, retrocedo y vuelvo a 2)
  2. Si lo es, llamo recursivamente y vuelvo a 1)
4. Si llegue hasta aca, ya probe con todo y no encontre una solucion 
(no valido para todos los casos, pero el esquema suele ser parecido)

## Ejercicio sudoku
Calcular las alternativas que tiene cada casillero para poner un numero -> es la poda 



