#se va a crear un validador para saber si podemos o no podemos entrar a una party, es importante agregar que
#para poder entrar a la fiesta, debe ser mayor de edad
#El usuario deberá ingresar su edad
edad = int (input("Escribe tu edad:"))

# edad = int (edad) 

#vamos a preguntar si la edad es mayor o igua a 18 años
if edad >= 18:
    #imprime que lo deje entrar
    print ('Puedes entrar compadre')
else:
    #si no se cumple la condicion imprime que no puede entrar
    print('No puede entrar')
    
# ahora se va a validar si la persona es mayor de edad y ademas tiene mas de 600 pesos
#se crea la variable edad y en ella se guarda lo que escriba el usauro 

print ('----------------------')
edad = int (input('Escribe tu edad'))
dinero = int (input('Escribe tu presupuesto'))

if edad >= 18:
    if dinero >= 600 :
        print ('Lo deja entrar')
    else:
        #como no tiene dinero no puede entrar
        print('dale pa fuera mi loco')
else:
    #como no tiede la edad no puede entra
    print ('no puedes entrar por la edad')
    
    



edad = int (input('Escribe tu edad'))
dinero = int (input('Escribe tu presupuesto'))

if edad >= 18 and dinero >= 600:
    
        print ('Lo deja entrar')
    
else:
    #como no tiede la edad no puede entra
    print ('no puedes entrar por la edad')


#-----------------------------------------
#condicional con multiples comparaciones
dinero = input ('Escriba el dinero con el que cuenta')
dinero = int (dinero)

if dinero < 100:
    print ('le compro unas galletas')
elif dinero >= 100 and dinero <= 200:
    print ('le compro unos chocolates')
elif dinero > 200 and dinero <= 300:
    print ('Le compro unas 300 picafresas')
else:
    print ('Le compro un peluche')
    
    
#----------------------LABORATORIO--------------------
userReply = input("Do you need to ship a package? (Enter yes or no) ")
#Si lo que escribe el usuario es exactamente igua a yes
if userReply == "yes":
    #Imprime que puede ayudar
    print("We can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")
    
    
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")