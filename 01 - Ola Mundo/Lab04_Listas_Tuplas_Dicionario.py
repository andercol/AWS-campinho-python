# Uso de listas, tuplas e dicionários

#Definição de uma lista

myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

#Acesso a uma lista pela posição

print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

#Alteração dos valores da lista

myFruitList[2] = "Orange"
print(myFruitList)

#Exercício 2: apresentação do tipo de dado tupla

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

#Acesso a uma tupla pela posição

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

#Exercício 3: apresentação do tipo de dado dicionário

myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

#Acesso a um dicionário pelo nome

print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])

