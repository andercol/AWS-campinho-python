
# 128- [PF] -Lab - Administração do sistema com Python

import os
import subprocess


def exec01():
    os.system("clear")
    print("\n Exercício 1: uso do os.system :\n")
    print("\n Listando arquivos do diretório com 'ls' :\n")

    os.system("ls")

    while True:
        try:
            print("\n")
            option2 = input("Digite 'm' para carregar o menu: ")
            if option2 == "m":
                menu();
            break
        except:
            print("Opção invalidada! Digite m para carregar o menu:")

def exec02():
    os.system("clear")
    print(" Exercício 3: uso do subprocess.run :\n")
    print("\n Listando arquivos do diretório com 'ls' :\n")

    subprocess.run(["ls"])

    while True:
        try:
            print("\n")
            option2 = input("Digite 'm' para carregar o menu: ")
            if option2 == "m":
                menu();
            break
        except:
            print("Opção invalidada! Digite m para carregar o menu:")


def exec03():
    os.system("clear")
    print(" Exercício 3: uso do subprocess.run com dois argumentos :\n")
    print("\n Listando arquivos de outro diretório com 'ls -l diretorio' :\n")

    subprocess.run(["ls","-l","../Lab01-06"])

    while True:
        try:
            print("\n")
            option2 = input("Digite 'm' para carregar o menu: ")
            if option2 == "m":
                menu();
            break
        except:
            print("Opção invalidada! Digite m para carregar o menu:")


def exec04():
    os.system("clear")
    print(" Exercício 4: uso do subprocess.run com três argumentos :\n")
    print("\n Listando arquivos de outro diretório com 'ls -l diretorio' :\n")

    subprocess.run(["ls","-l","../Lab01-06"])

    while True:
        try:
            print("\n")
            option2 = input("Digite 'm' para carregar o menu: ")
            if option2 == "m":
                menu();
            break
        except:
            print("Opção invalidada! Digite m para carregar o menu:")



def exec05():
    os.system("clear")
    print(" Exercício 5: recuperação de informações do sistema :\n")
    print("\n Recuperando informações do sistema com 'uname -a ' :\n")

    command="uname"
    commandArgument="-a"
    print(f'Gathering system information with command: {command} {commandArgument}')
    subprocess.run([command,commandArgument])

    while True:
        try:
            print("\n")
            option2 = input("Digite 'm' para carregar o menu: ")
            if option2 == "m":
                menu();
            break
        except:
            print("Opção invalidada! Digite m para carregar o menu:")



def exec06():
    os.system("clear")
    print(" Exercício 6: recuperação de informações sobre o espaço em disco :\n")
    print("\n Recuperando informações do disco com 'ps -x ' :\n")

    command="ps"
    commandArgument="-x"
    print(f'Gathering active process information with command: {command} {commandArgument}')
    subprocess.run([command,commandArgument])

    while True:
        try:
            print("\n")
            option2 = str(input("Digite 'm' para carregar o menu: "))
            if option2 == "m":
                menu();
            break
        except:
            print("Opção invalidada! Digite m para carregar o menu:")




def menu():
    os.system("clear")
    print("\n ---------- Selecione um exercicio: -----------\n")
    print(" Exercício 1: uso do os.system :\n")
    print(" Exercício 2: uso do subprocess.run :\n")
    print(" Exercício 3: uso do subprocess.run com dois argumentos :\n")
    print(" Exercício 4: uso do subprocess.run com três argumentos :\n")
    print(" Exercício 5: recuperação de informações do sistema :\n")
    print(" Exercício 6: recuperação de informações sobre o espaço em disco :\n")
    print(" Digite 0 para sair :\n")

    while True:
        try:
            option = int(input("\n Informa qual exercício quer executar de 1 à 6: "))
            break
        except:
            print("Opção invalidada! Digite um número entre 1 e 6:")



    match option:
        
        case 0:
            exit()
        case 1:
            exec01()
        case 2:
            exec02()
        case 3:
            exec03()
        case 4:
            exec04()    
        case 5:
            exec05()
        case 6:
            exec06()


if __name__ == "__main__":
    menu()



# A lista completa de argumentos de subprocess.run() é semelhante a esta:
    
'''
#subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, #check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)

'''