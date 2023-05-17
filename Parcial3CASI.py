from functools import reduce

def matrizNN(matriz):
    def sumOddRows():
        sumatoriaFilasImpares = 0
        for i in range(len(matriz)):
            if i % 2 != 0:
                for j in range(len(matriz[i])):
                    sumatoriaFilasImpares += matriz[i][j]
        return sumatoriaFilasImpares
    
    def prodOddColumns():
        productoriaColumnasImpares = 1
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if j % 2 != 0:
                    productoriaColumnasImpares *= matriz[i][j]
        return productoriaColumnasImpares
    
    def pickOperator(operador):
        match operador:
            case "+":
                return sumOddRows()
            case "*":
                return prodOddColumns()
            case _:
                return None
    
    rows = sumOddRows()
    columns = prodOddColumns()
    return ("La diferencia entre la suma de las filas impares y la suma de las columnas impares es: ", rows - columns), pickOperator

matriz1 = [[1,2,3,4,5],
          [6,7,8,9,10],
          [11,12,13,14,15]]

matriz2 = [[3,7,1,9,0,15],
            [128,29,8,9,10,1777],
            [2,2,2,9999,15,4],
            [4,4,4,19,20],
            [5,5,5,5,5,5],
            [6,6,6,6,6,6],]

result1, funcionretornada1 = matrizNN(matriz1)
print(result1) #('La diferencia entre la suma de las filas impares y la suma de las columnas impares es: ', -84632)
print(funcionretornada1("+")) #40
print(funcionretornada1("*")) #84672

result2, funcionretornada2 = matrizNN(matriz2)
print(result2) #('La diferencia entre la suma de las filas impares y la suma de las columnas impares es: ', -71942190227883357952)
print(funcionretornada2("+")) #2048
print(funcionretornada2("*")) #71942190227883360000

#######################################################################################################################################

def compareStringLists(lista1, lista2):
    def comparewithFilter():
        result = list(filter(lambda elemento: elemento in lista1, lista2))
        if result == lista1:
            return True
        else:
            return False
    def comparewithReduce():
        result1 = reduce(lambda elemento1, elemento2: elemento1 + elemento2, lista1)
        result2 = reduce(lambda elemento1, elemento2: elemento1 + elemento2, lista2)
        if result1 == result2:
            return True
        else:
            return False
    return comparewithFilter(), comparewithReduce()
    
lista1 = ["hola", "como", "estas", "tu"]
lista2 = ["hola", "como", "estas", "tu"]

booleanofilter1, booleanoreduce1 = compareStringLists(lista1, lista2)

print(booleanofilter1) #True
print(booleanoreduce1) #True

lista3 = ["hola", "como", "estas", "tu"]
lista4 = ["aa", "co", "tas", "tu"]

booleanofilter2, booleanoreduce2 = compareStringLists(lista3, lista4)

print(booleanofilter2) #False
print(booleanoreduce2) #False
            
#######################################################################################################################################
#Implementación clásica
#PF LL
#Implementación clásica
Nil = None #representación clásica de None
def Cons(x, xs): #representación clásica de celda --> Node
  return (x,xs) #tupla --> inmutable

#helper para crear lista a base de celdas
def pflist(*xs):
  if(xs):
    return Cons(xs[0],pflist(*xs[1:]))
    #Cons(1,pflist((2,3)))
    #Cons(2,pflist((3)))
    #Cons(3,pflist(()))
    #Nil
  else:
    return Nil
  
#devuelve la cabeza de la celda
def head(xs):
  return xs[0]

#devuelve la cola de la celda
def tail(xs):
  return xs[1]

#define si la celda está vacía
def is_empty(xs):
  return xs is Nil

def checkConsecutives(xs, prevdata = 0):
    if (is_empty(xs)):
        return False
    else:
        if (prevdata == 0):
            return checkConsecutives(tail(xs), head(xs))
        else:
            if (head(xs) == prevdata + 1):
                return True
            else:
                return checkConsecutives(tail(xs), head(xs))
            
booleanoPersistente1 = checkConsecutives(pflist(1,2,4,6,8,10)) #True
booleanoPersistente2 = checkConsecutives(pflist(10,8,4,6,2)) #False
booleanoPersistente3 = checkConsecutives(pflist(2,7,9,4,5,10)) #True


print(booleanoPersistente1)
print(booleanoPersistente2)
print(booleanoPersistente3)
   
    