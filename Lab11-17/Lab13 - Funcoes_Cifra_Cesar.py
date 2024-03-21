
# Python3.6  
# Coding: utf-8 

# 124- [PF] -Lab - Use funções para implementar uma cifra de César 

'''Na programação, uma função é uma seção nomeada de um programa que executa uma tarefa específica. Python tem funções internas, como print(), que são fornecidas pela linguagem. Além disso, você pode usar funções fornecidas por outros desenvolvedores pela declaração import. Por exemplo, é possível usar import math se você quiser usar a função math.floor(). No Python, você pode criar suas próprias funções, que são chamadas de funções definidas pelo usuário.
Para continuar a discussão sobre funções definidas pelo usuário, você escreverá um programa que implementa uma cifra de César, que é um método simples de criptografia. A cifra de César pega as letras de uma mensagem e desloca cada uma ao longo do alfabeto um certo número de posições.
Neste laboratório, você vai:

    Criar funções definidas pelo usuário
    Usar várias funções para implementar um programa de criptografia com a cifra de César
'''


def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount

def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)


def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')


runCaesarCipherProgram()
