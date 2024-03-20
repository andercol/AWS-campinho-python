#Exercício 1: apresentação do tipo de dado string

myString = "This is a string."
print(myString)

print(type(myString))

print(myString + " is of the data type " + str(type(myString)))

#Exercício 2: uso da concatenação de strings

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

#Exercício 3: uso de strings de entrada

name = input("What is your name? ")

print(name)

#Exercício 4: formatação de strings de saída

color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

print("{}, you like a {} {}!".format(name,color,animal))

