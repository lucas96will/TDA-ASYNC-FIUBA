def sche_recursivo(inicio, fin, valor, p, j):
   if j == 0:
       return 0
   return max(valor[j] + sche_recursivo(inicio, fin, valor, p, p[j]),
              sche_recursivo(inicio, fin, valor, p, j-1))

def sche_memorioso(inicio, fin, valor, p, j):
   M_CHE = [None] * j
   return sche_rec_memorioso(inicio, fin, valor, p, j, M_CHE)

def sche_rec_memorioso(inicio, fin, valor, p, j, M_CHE):
   if j == 0:
       return 0
   if M_CHE[j-1] == None:
       M_CHE[n-1] = sche_rec_memorioso(inicio, fin, valor, p, j-1, M_CHE)
   if M_CHE[p[j]] == None:
       M_CHE[n-2] = sche_rec_memorioso(inicio, fin, valor, p, p[j], M_CHE)
   return max(valor[j]+M_CHE[p[j]], M_CHE[j-1])

def sche_dinamico(n, p, valor):
   if n == 0:
       return 0
   M_SCHE = [0] * (n + 1)
   M_SCHE[0] = 0
   for j in range (1, n + 1):
       M_SCHE[j] = max(valor[j] + M_SCHE[p[j]], M_SCHE[j-1])
   return M_SCHE[n]


# Ordenar por tiempo de fin: O(n log n)
# Obtener p[i]: O(log n) → obtener p: O(n log n)
# El cálculo de M_SCHE: O(n)
# Total: O(n log n)


def sche_solucion(M_SCHE, valor, p, j, solucion):
   if j == 0:
       return solucion
   if valor[j]+M_SCHE[p[j]] >= M_SCHE[j-1]:
       solucion.append(j)
       return sche_solucion(M_SCHE, valor, p, p[j], solucion)
   else:
       return sche_solucion(M_SCHE, valor, p, j-1, solucion)



