#La libreria csv nos permite trabajar archivos separados por comas
import csv
#Esta libreria nos permite toar datos de un archivo y usarlos dentro de un programa
import copy

#Se crea el diccionario myVehicle
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

#Se crea unn ciclo for para imprimir cada una de las claves valor que hay dentro del diccionario
for key, value in myVehicle.items():
    print("{} : {}".format(key,value))
    
#Se crea la lsita myInventoryList
myInventoryList = []


#Se abre el arcivo car_fleet.csv y se guarda dentro de la variable csvFile
with open('car_fleet.csv') as csvFile:
    #Se lee el archivo csvReader donde su delimitador son las comas
    csvReader = csv.reader(csvFile, delimiter=',')  
    #Se crea la variable lineCount y se le asigna el valor de 0
    lineCount = 0  
    #Se lee cada una de las lineas, filas o renglones del archivo csvFile
    for row in csvReader:
        
        #Si el valor de las lineas es 0
        if lineCount == 0:
            #Se imprime el nombre de la columna
            print(f'Column names are: {", ".join(row)}')  
            #Si aumenta en uno, el valor de lineCode
            
            lineCount += 1  
            #Si el valor de la linea no es 0, imprime en cada una de las claves la posicion que fue separada por comas anteriormente 
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            #Se copia el valor de las variables dentro del diccionario myVehiculo 
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            #Se agrega a la lista un vehiculo
            myInventoryList.append(currentVehicle)  
            #Se aumenta en 1 el valor de lineCount
            lineCount += 1  
    #Se imprime el total de las lineas / renglones 
    print(f'Processed {lineCount} lines.')
    
    #Se crea un for para imprimir cada vehiculo de la lista 
    for myCarProperties in myInventoryList:
        #Se imprime los datos de cada vehiculo
        for key, value in myCarProperties.items():
            #Se imprime la llave valor y al final se imprime un separador 
            print("{} : {}".format(key,value))
            print("-----")