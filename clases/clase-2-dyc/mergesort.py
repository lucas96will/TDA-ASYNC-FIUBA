def mergesort(arr):
    if len(arr) <= 1:
        return arr
    medio = len(arr) / 2
    izq = mergesort(arr[:medio])
    der = mergesort(arr[medio:])
    return intercalar_ordenado(izq, der)

# T(n) = 2T(n/2) + O(n)
# Ojo que en python las slices son copias, en golang no lo son.
