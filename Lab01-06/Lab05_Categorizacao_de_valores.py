
#Categorização de valores
"""Visão geral do laboratório

No Python, você pode misturar os tipos de uma lista. Neste laboratório, você criará uma lista com diferentes tipos e acessará os valores.

Neste laboratório, você vai:

    Usará tipos de dados numéricos
    Usará tipos de dados string
    Usará o tipo de dados lista
    Usará um loop for
    Usará a função print()
"""

#Exercício 1: criação de uma lista com tipos mistos

myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))