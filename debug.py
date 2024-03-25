# Peça ao usuário um valor e confirme se o valor fornecido é maior que 0

def checkvalue(valuetocheck):
    assert (type(valuetocheck) is int), "Insiraum número."
    assert (valuetocheck > 0), "O valor deveser maiorque 0"
    if valuetocheck> 4:
        print("Valor maiorque 4")
        
var = int(input("Insira um número maiorque 0:"))

checkvalue(var)
