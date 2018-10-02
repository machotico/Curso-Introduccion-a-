# Tema Hileras
mensaje = input("Digite culquier mensaje: ")

print (mensaje)

#len() -> encontrar el largo de un string

print(len(mensaje))

print (mensaje[0])                #Obtenemos el primer caracter de una hilera

print (mensaje [len(mensaje)-1])  #Obtenemos el ultimo caracter de una hilera

#Concatenacion de hileras

hilera = "Hilera Inical"

#Concatenacion simple

print (hilera + " mas otra hilera")
print (hilera)

#Concatenacion modificando la variable

hilera += ". Esta es la nueva hilera"
print (hilera)

#Inyectando Texto
apellido = "Guevara"
otra_hilera = "Hola {}{}! Como esta?".format("Luis ", apellido) # Un par de corchetes por cada elemento
print(otra_hilera)

print (otra_hilera [3:8])

print (otra_hilera [:8])

print (otra_hilera [3:])