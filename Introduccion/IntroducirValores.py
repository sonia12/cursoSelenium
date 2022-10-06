# input = guarda datos en una variable

print ("cual es tu nombre")
nom = input()

print ("cual es tu apellido paterno")
ap = input()

print ("cual es tu apellido materno")
am = input ()

print ("dame el valor de a")
a= input()
a=int(a)

print ("dame el valor de b")
b= input()
b=int(b)

suma = a+b

print ("tu nombre es:  {}  {} {} " .format(nom, ap, am) )

print (" {} + {} = {}" .format(a,b,suma))