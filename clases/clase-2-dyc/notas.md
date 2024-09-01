# Tecnicas de disenio

## Repaso de Division y conquista

Tecnica de disenio en la que:
  1. Dividimos el problema en subproblemas
  2. Resolvemos cada subproblema recursivamente
  3. Combinamos las soluciones a cada problema.

Siempre se utiliza la ecuacion de recurrencia que representa el algoritmo que representa al algoritmo, para analizarlo.

### Ejemplo de Algoritmos
  1. Busqueda binaria (fundamentos)
  2. Mergesort y Quicksort
  3. Otros algoritmos de dificultad similar

Generalmente muchos se parecen a estos algoritmos, en su estructura. Puede variar lo especifico.

  4. Arboles

# Teorema Maestro

T(n) = A T(n/B) + O(n^C)

A: llamados a la ecuacion recursiva
B: Divisiones o particiones con las que trabaja el llamado a la funcion
C: Complejidad de agrupar las divisiones

  1. log_B(A) > C -> T(n) = O(n^C)
  2. log_B(A) = C -> T(n) = O(n^c * log_B(n))
  3. log_B(A) < C -> T(n) = O(n^log_B(A))

## Condiciones para aplicar Teorema Maestro
  1. A es natural
  2. B es real mayor a 1, y es constante (siempre el mismo)
  3. El caso base es constante

# Teorema Maestro General

T(n) = A T(n/B) + f(n)

A,B lo mismo de antes, f(n) siendo el costo de partir y juntar los resultados

f(n) = O(n^c), C < log_B(A) -> T(n) = 0(n^log_B(A))
f(n) = 0(n^c * log^k(n)), c = log_B(A) -> t(n) = 0(n^c log^(k+1)(n))
f(n) = omega(n^c), c > log_B(A), Af(n/B) <= kf(n)(k < 1, n grande) -> t(n) = 0(f(n))

# Problema 1. Multiplicacion de numeros muy grandes

Cuando multiplicamos dos enteros de largos m y n, Como es el algoritmo? Cuanto tiempo consume?

solucion primaria
Calculamos productos parciales de cada digito, vamos multiplicando por la base (10) y luego sumamos
Agarramos cada m digito y lo multiplicamos contra los n igitos, y luego sumamos los n resultados parciales O(mxn)
O(nxm) algoritmo de multiplicacion de primaria

solucion tda
1234 x 56
1. Escribimos la multiplicacion como si estuvieramos trabajando en base 2 y separamos primera mitad y segunda mitad
    i. x = x1 * 2^(n/2) + x0
    ii. 12 x 10^2 + 34 = 1234
2. y*x = (x1 * 2^(n/2) + x0) * (y1 * 2^(n/2) + y0)
    i. = x1y1 * 2^n + (xiy0 + x0y1) * 2^n/2 + x0y0
3. Hay cuatro multiplicaciones de las subpartes
4. T(n) = 4 T(n/2) + O(n) -> O(n^2)

Pero si podriamos usar 3 expresiones en vez de 4, podriamos mejorar la Complejidad. -> Ver karatsuba-offman

# Problema 2: Obtener extremo de un poligono

Tenemos n vertices V= (v0, ..., vn) dispuestos en sentido antihorario

Para que sirve? Ejemplo, teoria de juegos, para representaciones de imagenes, para algoritmos geometricos
Un algoritmo sencillo: Buscar el maximo, lineal

Un algoritmo mejor: 
Condiciones para aplicacion 
  1. Tiene que ser convexo
  2. Para todo segmento L el poligono sea monotonico
  3. Que no lo corte mas de 2 veces 
  4. Equivalente a que los angulos interiores <= 180 grad 

Seguimiento:
  1. El maximo esta entre A y B 
  2. Hay un punto C entre A y B 
  3. Comparo la proyeccion del vector A al siguiente punto, C al siguiente punto 
  4. Me quedo con el tramo que se encuentra mas arriba en la proyeccion, puede ser A, C o B, C 
    i. Esto se hace comparando direcciones A y C
      a. Si son iguales, comparamos posiciones
      b. Si no son iguales, nos quedamos con el tramo que empieza con el vector que va para arriba 

Algoritmo: 
Empezamos con A = 0, B = n - 1, C = n/2 
Si tenemos 2 vertices, comparemos a mano 
Aplicamos la logica de partir 
Como partimos a la mitad, nos quedamos con una sola, y luego solo comparo -> simil busqueda binaria -> O(log n)

# Problema 3: Buscando puntos mas cercanos en 2 dimensiones

Algoritmo sencillo: ver todas las distancias -> O(n^2) 

Resolviendo con DyC
Asumimos que ningun par de puntos tienen misma coordenada x e y 
Si fuera en una sola dimension -> O(n log n) usando Mergesort

En 2 dimensiones:
Buscamos la pareja mas cercana del lado izquierdo, luego del otro lado derecho 
luego en tiempo lineal buscar los mas cercanos, mergesort -> O(n log n) 

Luego divido en areas de distancia d/2, comparo cada punto (max 15 numero magico), resolviendo linealmente el problema

El caso base es cuando tengo 2 o 3 elementos. Con 2 elementos devuelvo, con 3 elementos comparo, con 4 o mas hago el resto de dividir etc

# Multiplicaciones de matrices

Generalmente las primeras ideas cuestan O(n^3)

Algoritmo de Strassen
En vez de hacer 8 llamados recursivos, hacemos 7. Haciendo algo similar a Karatsuba-Offman para multiplicar numeros grandes.
T(n) = 7T(n/2) + O(1) -> ~= O(n^2.8)

# Problema FFT - Transformada rapida de Fourier
problema: tenemos dos vector A y B y queremos obtener la convolucion entre ambos.

Aplicaciones:
  1. Procesamiento de seniales
  2. Procesamientos de habla
  3. Procesamiento de Imagenes (redes neuronales de convolucion)
  4. Machine learning sobre grafos (redes convoluciones sobre grafos)

convolucion: La convolucion de dos funciones pasa a una multiplicacion, en el dominio de la transformada de fourier.
En el mundo discreto es sencillo multiplicar dos matrices
Se puede obtener un algoritmo que resuelve el problema en O(nlogn)

F(f*g) = F{f} * F{g}

Aplicaciones de la TDF
  1. Realizar la convolucion eficientemente
  2. Trabajar en el dominio de las frecuencias, en vez del tiempo -> si queremos analizar las frecuencias que aparecen una senial, filtrar, etc

FFT KT 5.6 

# Problema 4, conteo de inversiones, importante
Tengo un conjunto de n elementos + 2 arreglos / listas ordenados por diferentes criterios (A y B)
-> Dar una medida de semejanza entre dichas listas

Version 1:
  . Nombramos los elementos de A con 1,2...n y B como correspondiente a eso 

Concepto de inversiones
Dos elementos estan invertidos si bi > bj (con i < j) -> O(n^2)
[2, 4, 1, 3, 5] -> 3 inversiones 

Version mergesort:
  1. Cada vez que intercambio al lado derecho, le pregunto cuantos elementos quedan de esa parte y eso es el nro de inversiones

            (6, 8, 7, 2, 1, 5, 3, 4)
        (6, 8, 7, 2)                                (1, 5, 3, 4) -> (1,2,3,4,5,6,7,8) 6+4+3+3+3 = 19 inversiones
    (6, 8)     (7, 2) -> (2,6,7,8)4             (1, 5)       (3, 4) -> (1,3,4,5)2
(6, 8)->(6,8)0 (7,2)->(2,7)1      

Complejidad: O(nlogn) igual a mergesort
