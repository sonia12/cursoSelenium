lenguajes= ["php","java","python", "javascript"]

print ("lenguaje seleccionado: " + lenguajes [2])
lenguajes[2]= "django"                          # le esta cambiando python a django
print ("lenguaje " + lenguajes[2])
print (lenguajes)

# para añadir
lenguajes.append("visual")

print (lenguajes)

# remover uno de la lista

lenguajes.remove("java")
print (lenguajes)