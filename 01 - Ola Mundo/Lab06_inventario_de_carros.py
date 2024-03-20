#Uso dos tipos de dados compostos

"""
Visão geral do laboratório

Um tipo de dado composto é todo tipo de dado que seja formado por tipos de dados primitivos. Se você gosta de comida, pode visualizar um tipo de dado composto como um turducken, que é um prato que consiste em um frango dentro de um pato dentro de um peru. Neste laboratório, você criará um tipo de dado que consiste em uma string que está em um dicionário, o qual está em uma lista.

Neste laboratório, você vai:

    Usará tipos de dados numéricos
    Usará tipos de dados string
    Usará o tipo de dados dicionário
    Usará o tipo de dados lista
    Usará um loop for
    Usará a função print()
    Usará a declaração if
    Usará a declaração else
    Usará a declaração import
"""

#Criação dos dados de um inventário de carros

"""vin,make,model,year,range,topSpeed,zeroSixty,mileage
TMX20122,AnyCompany Motors, Coupe, 2012, 335, 155, 4.1, 50000
TM320163,AnyCompany Motors, Sedan, 2016, 240, 140, 5.2, 20000
TMX20121,AnyCompany Motors, SUV, 2012, 295, 155, 4.7, 100000
TMX20204,AnyCompany Motors, Truck, 2020, 300, 155, 3.5, 0"""

#Criação de um programa de inventário de carros

import csv
import copy

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

for key, value in myVehicle.items():
    print("{} : {}".format(key,value))

myInventoryList = []

#Cópia do arquivo CSV para a memória

with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0  
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')
    
    currentVehicle = copy.deepcopy(myVehicle)
    
    #Exibição do inventário de carros
    
    for myCarProperties in myInventoryList:
        for key, value in myCarProperties.items():
            print("{} : {}".format(key,value))
            print("-----")
        
        