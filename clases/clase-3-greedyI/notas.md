# Algoritmos que ya sabemos
  1. Dijkstra
  2. Prim
  3. Kruskal

# Que es un algoritmo greedy

. Se aplica una regla sencilla que nos permite obtener el optimo local a mi estado actual
. La aplicacion iterativa de esa regla, esperando que nos lleve al optimo general (la mejor solucion)

Algoritmo greedy: Sucesion de optimos locales -> optimo global

## Ventajas y desventajas
- No siempre dan el resultado optimo
- Demostrar que dan el resultado optimo es dificil
+ Son intuitivos de pensar. Son faciles de entender
+ Suelen funcionar rapido
+ Para problemas complejos pueden ser buenas aproximaciones

## Dijkstra
No es optimo, porque pueden aparecer pesos negativos
Es greedy porque en cada momento, en el estado actual (elemento que estan en el heap) se consigue el elemento de peso menor entre todos al origen y ese es el elemento siguiente a considerar y ese valor no puede cambiar. Por eso es que si hay elementos con peso negativo, el resultado ya no es optimo.
