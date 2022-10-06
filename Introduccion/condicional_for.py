#for--> ciclo de repeticion
'''
for x in range(100):
    print("sonia" + str (x))

colores= ["rojo","amarillo","verde"]

for vcol in colores:
    print(vcol)

nombreC = "Sonia Caceres Aramayo"

for vn in nombreC:
    print(vn)


# imprime del rango de 10 al 20
for x in range(10,20):
    print(x)

# incrementa en 5 del rango de 1 al 100
for x in range(1,100,5):
    print(x)
'''
# cuando el numero sea >= 75 rompe
'''
for x in range(1,100,7):
    if(x>=75):
        break
    print(x)
'''

for num in range(1,11):
    if(num==3 or num ==6 or num==9):
        continue # --> buscas el condicionante y continua (la condicionante eliminala)
    print(num)