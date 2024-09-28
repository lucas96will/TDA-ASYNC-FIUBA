# Programacion Dinamica II 
Saber programacion dinamica bien, te vuelve Messi 


Exploración implícita del espacio de posibles soluciones
Descomposición del problema en subproblemas que permitan construir las soluciones de problemas más grandes
Nos basamos en la intuición que nos da la Memorización para reconocer los sub-problemas y utilizarlos para construir la solución
Una vez que tenemos todas las soluciones memorizadas, el problema está resuelto
Nos ayuda evitando explorar un espacio exponencial de soluciones por fuerza bruta
De esa manera podemos reducir la complejidad temporal de nuestro algoritmo significativamente

# Intuición: cómo saber que podremos utilizar PD

1. Hay un número polinomial de subproblemas
2. La solución al problema original puede ser construido a partir de soluciones a subproblemas
3. Hay un orden natural de los subproblemas de menor a mayor. Los subproblemas “mayores” son resueltos mediante la composición de problemas “menores”
  a. La versión recursiva resuelve en formato Top-Down
  b. La versión iterativa es de un formato Bottom-Up, es la que preferimos a partir de ahora al resolver ejercicios
