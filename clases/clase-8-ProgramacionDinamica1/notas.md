# Disclaimer
1. Este es posiblemente el tema mas dificil de la materia -> vamos a ir lento
2. Esperamos que en algun momento les caiga la ficha y vean la matrix
3. Tema de entrevistas en lugares groso
4. Pregunten apenas diga algo que los haga pensar

# Programacion dinamica
Es una tecnica de programacion, tal como:
  - Division y conquista
  - Algoritmos Greedy
  - Backtracking

Es una gran herramienta para casos donde no podemos recurrir a otras tecnicas (y para tipicos problemas de entrevistas de trabajo)

## Problematica introductoria

Numero (entrada) -> Metodo/algoritmo para sumarle 5 a un numero -> numero + 5 (salida)

Usar el procedimiento cuesta tiempo. No sabemos cosas raras como factorizar
  - Opcione 1: consultar el procedimiento 7 veces para sumar 5 veces y luego usarlo para sumar 9 veces 5 
  Cuantas veces tendria que usar el procedimiento?

  - Enfoque final: Uso el procedimiento 7 veces para hallar 7*5, anoto el resultado y basandome en el resultado al problema 
  al problema peque;o usare el procedimiento para sumar 5 dos veces mas 
Consultamos resultados de problemas mas peque;os -> no fuimos redundantes 

Moraleja: Capaz y puedo recordar las soluciones -al mismo problema- "mas chicas" para usarlas para el problema mas grande 
Problemas con problemas mas peque;os?

# Ejemplo con Fibonacci
  [fibonacci.py]
# Afrontar los problemas de PD 
- Top down 
  - Desde el caso general hasta el caso base
- Bottom Up 
  - Desde el caso base hasta el caso general

# Memoization o Memorizacion
La técnica de guardar los resultados previamente calculados se llama Memoization
En este caso nos permitió pasar de un tiempo de ejecución exponencial a uno polinomial (particularmente, proporcional al número de Fibonacci a calcular)

Por que preferimos la forma iterativa (bottom up) a la recursiva (top down)?
1. Es mucho mas facil de entender que pasa cuando
2. Como consecuencia de lo anterior, mucho mas facil calcular la complejidad
3. Este tipo de resoluciones suelen ser mas faciles de resolver de forma inductiva que recursiva
4. Es mas facil cometer errores o pensarlo de una forma rebuscada en la version recursiva 
5. Nos estructura mucho más cómo pensar la solución → primero la ecuación de recurrencia, después programar (este último paso, siendo extremadamente sencillo)
6. Se pueden aplicar optimizaciones de memoria fácilmente.

# Problema de scheduling
Tengo un aula/sala donde quiero dar charlas. Las charlas tienen horario de inicio y fin.
Quiero utilizar el aula para dar la mayor cantidad de charlas.

# Problema de shceduling con pesos
Tengo un aula/sala donde quiero dar charlas. Las charlas tienen horario de inicio y fin,
y un peso asociado al valor de cada charla. Quiero utilizar el aula para maximizar la
sumatoria de pesos de las charlas dadas. 

El algoritmo greedy que ordena por orden de fin, no es optimo 
Pero nos da una forma interesante de acercarse al problema

n = 0 ninguna charla ok 
n = 1 agarro una charla ok 
n = 2 
  - si se superponen, la de mayor valor 
  - si no se superponen, las dos
n = 3 
  - que ninguna se cruce 
  - permutaciones

En PD al ordenar por hora de finalizacion, podemos tomar la primera charla, resolver ese 
al tomar la segunda charla, decidir que tenemos que hacer y eliminar el superposicionamiento con las charlas anteriores 
(es decir, la primera en este caso) -> si no se superpone elegir. Si se superpone, elegir la de mayor valor.

Nos quedamos con la suposicion de que sabemos las soluciones de problemas mas peque;os, llamemosle OPT 
La ultima charla en particular puede o no pertenecer a la solucion 
Si no damos la charla, entonces el problema mas peque;o puede excluir esta charla 
Si damos esa charla, entonces el problema mas peque;o debe excluir todas las charlas 
  que terminen despues del comienzo de esta charla 
De estas dos opciones deberíamos siempre seleccionar aquella que maximice la sumatoria de los pesos

OPT(j) = max (dar la charla Vj + OPT(P(j)), no dar la charla OPT(j-1)) 

La PD:
- Es una exploracion implicita del espacio de posibles soluciones (no vuelvo a explorar las soluciones ya conocidas)
- Descomposicion del problema en subproblemas que permitan construir las soluciones de problemas mas grandes 
- Nos basamos en la intuicion que nos da la Memorizacion para reconocer los sub-problemas y utilizarlos 
para construir la solucion 
- Una vez que tenemos todas las soluciones memorizadas, el problema esta resuelto 
- Nos ayuda evitando explorar un espacio exponencial de soluciones por fuerza bruta
- De esa manera podemos reducir la complejidad temporal de nuestro algoritmo significativamente

Intuicion: Como saber que podremos utilizar PD 
1. Hay un numero polinomial de subproblemas 
2. La solucion al problema original puede ser construido a partir de soluciones a subproblemas
3. Hay un orden natural de los subproblemas de menor a mayor. Los subprolemas mayores son resueltos
mediante la composicion de problemas menores
  - La versión recursiva resuelve en formato Top-Down
  - La versión iterativa es de un formato Bottom-Up, es la que preferimos a partir de ahora al resolver ejercicios

## Como encontrar la solucion usando PD 
Necesitamos
○ La forma que tienen los subproblemas
○ La forma en que dichos subproblemas se componen para solucionar subproblemas más grandes
¿Cómo se encuentran?
¿En qué pensamos primero?


