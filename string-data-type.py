# Creamos una variable myString y sentro de ella se guarda el texto "This is a string"
myString = "This is a string."
#Imprimimos el valor de la variable string 
print(myString)
#Imrpimimos el tipo de dato 
print(type(myString))
#Imprimimos el valor de la varible, un texto y finalmente el tipo de dato de la variable
print(myString + " is of the data type " + str(type(myString)))

#Creamos una variable y dentro de ella guardamos el valor de water 
firstString = "water"
#Creamos la variable secondstring y guardamos dentro de ella el valor de fall
secondString = "fall"
#Creamos la variable thirdstring y dentro de ella guardamos el valor concatenado (unido) de firs string
#y second string
thirdString = firstString + secondString

#Imprimimos el valor de la variable thirdstring 
print(thirdString)

#Creamos la variable name y usando la función input vamos a almacenar lo que escriba el usuario por 
#consola
name = input("What is your name? ")
#Imprimimos el valor de la variable name 
print(name)

#Cramos la variable color/animal y usando input vamos a almacenar lo que el usuario escriba 
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

#Para imprimir usando formas vamos a poner una llave por cada variable y el format va a poner el valor de las
#variables en el orden que las estamos usando 
print("{}, you like a {} {}!".format(name,color,animal))