# Problema del cambio
Se tiene un sistema monetario (ejemplo, el nuestro). Se quiere dar "cambio" de una determinada cantidad de plata. Implementar un algoritmo que devuelva el cambio pedido, usando la mínima cantidad de monedas/billetes. 

Ej: 1, 10, 50, 100, 2000, 1000, 10000, 500, 20000

48372, cual es la menor cantidad de billetes 

Opciones
1. Uso la maxima cantidad de billetes de mas valor en cada momento, luego actualizando al nuevo valor
  . 2x20000, 4x2000, 1x200, 1x100, 1x50, 2x10, 2x1
  . O(nlogn + n)
  . No es optimo, depende de las denominaciones.

# Problemas con compras con inflacion
Tenemos unos productos dados por un arreglo R, donde R[i] nos dice el precio del producto. Cada día debemos comprar uno (y sólo uno) de los productos, pero vivimos en una era de inflación y los precios aumentan todo el tiempo. 
El precio del producto i el día j es R[i]j + 1 (j comenzando en 0). 
Implementar un algoritmo greedy que nos indique el precio mínimo al que podemos comprar todos los productos.

Soluciones
1. Regla greedy: Compramos lo mas caro primero

# Problema de la carga de combustible
Un camión debe viajar desde una ciudad a otra deteniéndose a cargar combustible para poder llegar a destino. El tanque de combustible le permite viajar hasta K kilómetros.
Las estaciones se encuentran distribuidas a lo largo de la ruta siendo di la distancia desde la estación i-1 a la estación i.
1. Implementar un algoritmo que decida en qué estaciones conviene detenerse a cargar combustible, de manera que se detenga la menor cantidad de veces posible.
2. Indicar y justificar la complejidad del algoritmo

Soluciones
1. regla greedy: cargo combustible si no llego a la siguiente parada
  i. Esta solucion es optima


