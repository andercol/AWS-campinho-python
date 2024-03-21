
# Python3.6  
# Coding: utf-8 
# 122- [PF] -Lab - Calculando a carga líquida de insulina usando listas e loops Python
'''
    No módulo Controle de Fluxo, você aprendeu as declarações if-else, os loops while, as listas e os loops for. Agora, você usará o que aprendeu no aplicativo real da insulina humana.
    Aqui você usará lists, loops for and while, e matemática básica para calcular a carga líquida da insulina de pH 0 a pH 14.
    Neste laboratório, você vai:
    Criar um dicionário de valores de pKa (que indicam a força de um ácido) que será usado nos cálculos da carga líquida
    Usar o método de count() para obter uma contagem de aminoácidos
    Usar um loop while para calcular a carga líquida da insulina de pH 0 a pH 14
'''
# Store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  
# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin

pKR = {'y':10.07, 'c':8.18, 'k':10.53, 'h':6.00, 'r':12.48, 'd':3.65, 'e':4.25}

float(insulin.count("y"))

seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})


print(pKR, "\n")

print("\n", seqCount)

pH = 0

while(pH <= 14):
    netCharge = (
    +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    for x in ['k','h','r']}.values()))
    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    for x in ['y','c','d','e']}.values())))
    print('{0:.2f}'.format(pH), netCharge)
    pH += 1

