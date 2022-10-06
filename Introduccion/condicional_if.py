
a= 80
b= 80
c= 80

if(a>b):
    print("El mayor es: " + str (a))
else:
    print("el mayor es: " + str(b))

nom = " Sonia"
if (nom==" Sonia"):
    print("tu nombre es: " + nom)

if (a!=b):
    print("{} es diferente que {}".format(a,b))
else:
    print("{} es igual a {}".format(a,b))

# elif--> condicionamos algo mas

if (a>b and a>c):
    print ("el mayor es: " +str(a))
elif (b>a and b>c):
    print(" el mayor es: " + str (b))
elif(c>a and c>b):
    print("el mayor es: " + str (c))
else:
    print("son iguales")

if(a<b or a>c):
    print("{} < {} o {} > {}" .format(a,b,a,c))