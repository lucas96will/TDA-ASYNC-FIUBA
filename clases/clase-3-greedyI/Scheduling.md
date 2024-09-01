# Problema
Tengo un aula / sala donde quiero dar charlas. Las charlas tienen horario de inicio y fin.
Quiero usar la sala para dar la mayor cantidad de charlas.

Charla:
 1. Inicio, fin, ya estan definidas.

Ideas:
 1. Ordenar las charlas de menor a mayor, tomar la de menor en cada momento
  i. La duracion deberia ser mas corta de la duracion disponible para acomodar
  ii. No deberia solaparse con otras charlas 
  iii. ordenar, tomar.
  iv. No es optimo, solo toma la charla mas corta en vez de la optima (mayor cantidad de charlas)
 2. Tomar todos las charlas, ordenarlas segun el numero de solapamientos
  i. tomar la charla mas corta
  ii. actualizar los solapamientos 
  iii. repetir i, ii hasta que se termine
 3. Tomar las que terminan primero
  i. Es optima
  ii. optimizacion -> que no se pise con otra charla 
  iii. O(nlogn)



