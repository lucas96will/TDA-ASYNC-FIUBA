# Dada una escalera, y sabiendo que tenemos la capacidad de 
# subir escalones de a 1 o 2 pasos, encontrar cuántas formas 
# diferentes hay de subir la escalera.


# Dada una escalera, y sabiendo que tenemos la capacidad de subir escalones de a 1 o 2 pasos, 
# encontrar cuántas formas diferentes hay de subir la escalera.
# Para una escalera nivel 0: 1 sola forma, quedarme estático = 1 forma
# Para una escalera nivel 1: dar 1 paso simple = 1 forma
# Para una escalera nivel 2: dar 2 pasos simples, o dar 1 paso doble = 2 formas
# Para una escalera nivel n: ?


# E(N) = E(N-1) + E(N-2)


# Dada una escalera, y sabiendo que tenemos la capacidad de subir escalones de a 1 o 2 o 3 pasos,
# encontrar cuántas formas diferentes hay de subir la escalera.


# Dada una escalera, y sabiendo que tenemos la capacidad de subir escalones de a 1 o 2 o 3 pasos, encontrar cuántas formas diferentes hay de subir la escalera.
# Para una escalera nivel 0: 1 sola forma, quedarme estático = 1 forma
# Para una escalera nivel 1: dar 1 paso simple = 1 forma
# Para una escalera nivel 2: dar 2 pasos simples, o dar 1 paso doble = 2 formas
# Para una escalera nivel 3: dar 3 pasos simples, dar 1 simple y 1 doble, dar 1 doble y 1 simple, o dar 1 paso triple = 4 formas
# Para una escalera nivel n: ?

E(N) = E(N-1) + E(N-2) + E(N-3)
