#se usa para comparar --> el valor de un numero es igual a otro.
# = con el igual asignas valor
# == con esto comparas

a= 10
b= 8
c= 23

print (" son iguales " + str(a==b))
print (" a es mayor que b " + str(a>b))
print (" a es menor que b " + str(a<b))
print (" a es menor que b" + str(a<=b))


# operadores logicos and or

print ("si a es menor que b y a es menor que c: " + str(a<b and a<c) )

# comparando con la funcion or --> con una de las dos que cumpla mandara verdad

print ("si a es menor que b y a es menor que c: " + str(a<b or a<c) )

