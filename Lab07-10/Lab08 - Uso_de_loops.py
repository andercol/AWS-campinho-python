
# 115- [PF] -Lab - Loops 
'''Um loop é um segmento de código que se repete. Apresentaremos a você dois tipos de loops: o loop while e o loop for.'''

print("\n --------------- Exercício 1: uso de loop while ---------------")

'''Um loop while faz uma seção do código se repetir até que uma determinada condição seja atendida. Neste exercício, você criará um script Python que pede ao usuário para adivinhar corretamente um número.'''

print("\n Welcome to Guess the Number! \n")
print("\n The rules are sample. I will think of a number, and you will try to guess it. \n")

import random

number = random.randint(1,10)

isGuessRight = False

while isGuessRight != True:
    guess = input("\n Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("\n You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("\n You guessed {}. Sorry, that isn't it. Try again.".format(guess))
        print("\n")



print("\n --------------- Exercício 2: Escrita do loop for ---------------")

'''No Python, é possível criar uma funcionalidade avançada com poucas palavras. Esse recurso faz do Python uma linguagem relativamente fácil de escrever em comparação com outras linguagens de programação, mas também pode dificultar a leitura do código. Nesta atividade, você usará a declaração for, mas também passará um tempo analisando-a depois de executá-la.'''

print("\n Count to 10!")

for x in range (0,11):
    print(x)
    