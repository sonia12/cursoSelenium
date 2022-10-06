'''
#funcion sin parametro (vacio)
def saludo():
    print("hola  bienvenido ")
    print("saludos desde python ")
    a=20
    b=30
    c=a+b
    print("la suma es: {} + {} = {} " .format(a,b,c) )

print("esto es una funcion: ")
saludo()


# funcion con parametros

def saludar():
    print(" hola a todos")
def suma(a,b):
    c=a+b
    print(" la suma es: {} + {} = {}" .format(a,b,c))
saludar()
suma(6,5)


def saludar():
    print(" hola a todos")
def suma(a,b):
    a=input("dame a: ")
    a= int(a)
    b=input("dame b: ")
    b= int(b)
    c=a+b
    print(" la suma es: {} + {} = {}" .format(a,b,c))

saludar()
suma(6,5)



#
def datos (nom, ap, am):
    print ("hola mi nombre es: {} {} {}" .format(nom,ap,am) )
datos("sonia", "caceres", "aramayo")
datos ("emma", "tola", "caceres")
#'''

#funcion args --> tiene n valores

def suma(*args):
    resultado=0
    for n in args:
        resultado= resultado +n
    print("el resultado es : " + str(resultado))

suma(5,7)



