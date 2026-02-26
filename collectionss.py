#Para crear una lista se usa []
#Creamos la lista myFruitlist dentro de ella guardamos las siguientes frutas "apple", "banana", "cherry"
myFruitList = ["apple", "banana", "cherry"]
#Imrprimimos la lista
print(myFruitList)
#Imprimimos el tipo de dato que es myFruit
print(type(myFruitList))

#Imprimimos el vaor que esta en la primera posición de la lsita (aple)
print(myFruitList[0])
#Imprimimos el vaor que esta en la primera posición de la lsita (banana)
print(myFruitList[1])
#Imprimimos el vaor que esta en la primera posición de la lsita (Cherry)
print(myFruitList[2])

#Vamos a cambiar el valor de la lista en la posición 2 que antes era cherry y ahora es orange
myFruitList[2] = "orange"

#Imrpimimos la lista con el cambio 
print(myFruitList)
print ("-------------")

#Creamos una tupla llamada myFinalAnswer 
myFinalAnswerTuple = ("apple", "banana", "pineapple")
#Imprimimos la tupla completa
print(myFinalAnswerTuple)
#Imprimimos el tipo de dato de la tupla 
print(type(myFinalAnswerTuple))

#Imprimimos cada una de las posiciones de la tupla
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

print ("-------------")
# Para crear un diccionario se utilizan {} y dentro de ellas se va a crear una clave y un valor. La clave y el valor van separados por : y luego de cada clave:valor se separa del siguiente usando ,
# Creamos el diccionario myFavoriteFruitDictionary con las siguientes claves "Akua", "Saanvi", "Paulo" y sus correspondientes valores "apple", "banana", "pineapple"

myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

#Imprimimos cada valor de cada clave comenzando por Akua, despues Saanvi y finalmente Paulo
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])