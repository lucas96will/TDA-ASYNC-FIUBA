def parte_entera_raiz(n):
    return _parte_entera_raiz(n, 0, n//2)

def _parte_entera_raiz(n, start, end):
    if start >= end:
        return end
    
    mitad = (start+end)//2
   
    print("start: ", start, " end: ", end, " mitad", mitad)

    if mitad**2 > n:
        return _parte_entera_raiz(n, start, mitad)
    elif mitad**2 <= n and end**2 > n:
        return _parte_entera_raiz(n, mitad, end-1)
    else:
        return _parte_entera_raiz(n, mitad+1, end)

if __name__ == "__main__":
    nro1 = 280
    nro2 = 24
    sq1 = parte_entera_raiz(nro1)
    sq2 = parte_entera_raiz(nro2)
    print(sq1)
    print(sq2)
    assert sq1 == 16
    assert sq2 == 4


