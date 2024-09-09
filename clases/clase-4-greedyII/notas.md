# Algoritmos Greedy II 

Repaso: Un algoritmo greedy es un algoritmo que en cada momento se busca el estado optimo local

## Problema de la mochila
Tenemos una mochila con una capacidad W (peso, volumen). Hay elementos a guardar. Cada elemento tiene un peso y un valor. Queremos maximizar el valor de lo que nos llevamos sin pasarnos de la capacidad.
No se puede resolver de manera greedy este problema, solo con una aproximacion se puede.

## Problema de la mochila 2

Ahora supongamos que no es necesario poner "todo un elemento" sino que podemos poner proporciones. 
¿Ahora un algoritmo greedy sería óptimo?

## Problema de scheduling 2 

Ahora tenemos tareas con un deadline (fecha límite) di y una duración ti, pero pueden hacerse en cualquier momento, siempre que se hagan antes del deadline. Si se hacen después del deadline, incurrimos en una latencia. 
Para este problema, buscamos minimizar la latencia máxima en el que las tareas se ejecuten. Es decir, si definimos que una tarea i empieza en si, entonces termina en fi = si + ti, y su latencia es li = fi - di (si fi > di, sino 0). 

Propuesta: ordenar por deadline (solucion optima)

### Demostracion por inversiones

## Problema de Optimal Caching

Problema de Caché: podemos tener hasta k elementos de memoria bien a mano, el resto tendríamos que ir a RAM. Hay que decidir qué guardamos en la memoria caché. 
Tenemos un conjunto de datos U en memoria general (n en total), una memoria caché de k < n elementos. Tenemos una secuencia de pedidos de datos di. Si di está en la caché, accedemos muy rápido. Si no está → cache miss + ahora la tenemos que traer a la caché (y si la caché está llena, tenemos que evictear un dato previo). Queremos minimizar la cantidad de caché misses. 

 ## Problema de coloreo de intervalos

Contamos con un conjunto de “n” charlas. Cada una tiene hora de inicio y de finalización. Contamos también con un número “k” de salas donde se pueden llevar a cabo  (plot twist).
Se pide un algoritmo greedy que obtenga una asignación (lista de asignaciones para cada sala) que permita llevar a cabo TODAS las actividades, si es posible. 
Además se pide que la asignación use la menor cantidad de salas posible. 

Basicamente la idea es buscar por la menor hora de inicio, si ya esta ocupoada la sala buscar otra.
Esto da la solucion optima, el resultado muestra que se llenan las salas con reuniones.
En el ejercicio de la clase anterior se buscaba maximizar la cantidad de charlas en una sola sala por ejemplo,
pero en este lo que se busca es minimizar el tiempo entre charlas (creo)

## Ejercicio submarios de examen

Se tiene una matriz donde en cada celda hay submarinos, o no, y se quiere poner faros para iluminarlos a todos.
Implementar un algoritmo Greedy que dé la cantidad mínima de faros que se necesitan para que todos los submarinos queden iluminados, siendo que cada faro ilumina su celda y además todas las adyacentes (incluyendo las diagonales), y las directamente adyacentes a éstas (es decir, un “radio de 2 celdas”).
Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado da siempre la solución óptima?

No hay algoritmo greedy de solucion optima. Entre las opciones greedy esta tomar los faros que mas submarinos iluminen

## Problema generacion de grafos

Dado una lista de n números naturales, implementar un algoritmo en tiempo polinomial que cree un grafo de n nodos cuyos grados sean los indicados por esa lista. G debe ser simple y si bucles. 

Un algoritmo greedy puede ser por cada nodo, agregar las aristas a aquellos nodos con mas grado y descontarles 1, no entendi bien la idea
Tambien se hablo de que en el tiempo los nodos con mas grado iban a tener mas grado y los de menos, menos.

## Problema de los empleados

Una empresa tiene n empleados, y k proyectos posibles a realizar. Cada proyecto debe ser realizado por unos empleados en particular, y cada empleado puede realizar a lo sumo dos trabajos en total, en el tiempo que se tiene destinado para realizar todos los proyectos (suponer que podrían trabajar en ambos en simultáneo).
Por lo tanto, puede no ser posible realizar todos los proyectos. Implementar un algoritmo greedy que permita determinar los proyectos a realizar, de forma de maximizar las ganancias (cada proyecto da una ganancia distinta).
Primero resolvamos en caso que cada proyecto tenga un único empleado como alternativa.
Luego, que cada proyecto tenga varias alternativas (necesita de un empleado para que se encargue). 
Luego, que cada proyecto tenga que usar a todos los empleados que tiene en el listado. 

No hay algoritmo greedy con solucion optima, dado que la familia a la que pertenece este problema es parecido al de los pesos y valor

## Problema materias compatibles


Se tiene una lista de materias que deben ser cursadas en el mismo cuatrimestre, cada materia está representada con una lista de cursos (horarios) posibles a cursar (debe elegirse un horario por cada materia). Cada materia puede tener varios cursos.
Implementar un algoritmo greedy que devuelva un listado de cursos de forma que se pueda cursar un curso por cada materia (sin que se solapen, etc). Considerar que existe una función son_compatibles(curso_1, curso_2) que dados dos cursos devuelve un valor booleano que indica si se pueden cursar al mismo tiempo.

Parecido al de submarinos (creo yo), no hay algoritmo greedy con solucion optima

Generalmente creo que este tipo de problemas que los algoritmos greedy no tienen solucion optima, se debe a que no hay condicion 
al estado optimo local que tenga en cuenta las posibles combinaciones entre optimo local y no optimo local, por ejemplo no se sabe 
si para alcanzar la solucion optima se debe tomar primero una solucion no optima local y luego si (recordar submarinos), ya en ese caso
no es greedy el algoritmo, y se debe tener en cuenta otra condicion, que puede seguir resultando en una solucion no optima.
Esto ya entra en el terreno de backtracking o fuerza bruta, lo de las posibles combinaciones.


