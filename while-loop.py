#Importamos una libreria al principio del codigo
import random
# Un ciclo while es un bucle que va a recorrer hasta que no se cumple la condicion
#Se escrib la variable numero y se le pide al usuario que escriba el numero 0
numero = input ('escriba el numero 0')
numero = int (numero)

#Se verifica que lo que haya en la variable numero sea menor a 10
while numero < 10:
    # Se incrementa el valor de numero 
    numero = numero + 1
    #Si numero es menor que 10 se imprime su valor 
    print (numero)
    
#Vamos a construir una tabla de multiplicar 
numero = input ('escriba el numero:')
numero = int (numero)

#Se verifica que lo que haya en la variable numero sea menor a 10
multiplicador = 0
while multiplicador < 10:
    #Multiplicador 
    
    # Se incrementa el valor de multiplicador
    multiplicador = multiplicador + 1
    multiplicacion = numero * multiplicador
    
    
    #Si numero es menor que 10 se imprime su valor 
    #print (numero, '*', multiplicador, ' ', multiplicacion)
    print (f"{numero} * {multiplicador} = {multiplicacion}")
    
#-----------------------LABORATORIO--------------------
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#La libreria random genera numoerso aleatorios desde un numero inicial a un numero final
number = random.randint(1,10)

#Se crea la variable isguessright y se guarda un valor booleano False
isGuessRight = False

#Mientras la variable Iguessright sea diferente de verdaddero se ejecuta el codigo 
while isGuessRight != True:
    #se crea la variable guess y se guarda dentro lo que escriba el usuario
    guess = input("Guess a number between 1 and 10: ")
    #Mientras el valor de la variable guess sea un entero exactamente igual al valor de la variable number
    if int(guess) == number:
        #Imprime que ganamos
        print("You guessed {}. That is correct! You win!".format(guess))
        #La variable Iguess se pasa a verdadero para terminar el ciclo whuile
        isGuessRight = True
    #Si la variable guess no es exactamente a la variable IguessRigth imprime 
    else:
        #Intentalo de nuevo 
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))