def factorial_numero(n):
    r = 1
    for i in range(1, n+1):
        r *= i
    return(r)


def lista_pares(l1):
#   [1, 2, 3, 4, 5, 6, 7, 8, 9]
    l_pares = []
    l_impares = []
    for i in (l1): 
        if i%2 == 0:
            l_pares.append(i)
        else:
            l_impares.append(i)
    return l_pares

def numero_primo(n):
    for i in range(2, n):
        if n%i == 0:
            return False
        else:
            return True

def numero_par(n):
        if n%2 == 0:
            return True
        else:
            return False
    
def suma_lista_igual(list1, list2):
    r1 = 0
    r2 = 0
    for i in (list1):
        r1 += i
    for j in (list2):
        r2 += j
        if r1 == r2:
            return True
    return False

def palindromo(p):
    p1 = p[::-1]
    if p1 == p:
        return True
    else:
        return False



        


