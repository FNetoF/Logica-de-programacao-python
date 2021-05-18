'''
36. Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser
paga ao vendedor. Para calcular a comissão, considere a tabela abaixo:
________________________________________________________________________________________
|Venda mensal                                             | Comissão                   |
|_________________________________________________________|____________________________|
|menor que R$ 20.000.00                                   | R$ 400.00 + 14% das vendas |
|menor que R$ 40.000.00 e maior ou igual a R$ 20.000.00   | R$ 500.00 + 14% das vendas |
|menor que R$ 60.000.00 e maior ou igual a R$ 40.000.00   | R$ 550.00 + 14% das vendas |
|Menor que R$ 80.000.00 e maior ou igual a R$ 60.000.00   | R$ 600.00 + 14% das vendas |
|Menor que R$ 100.000.00  e maior ou igual a R$ 80.000.00 | R$ 650.00 + 14% das vendas |
|Maior ou igual a R$ 100.000.00                           | R$ 700.00 + 16% das vendas |
|_________________________________________________________|____________________________|
'''

venda = float(input("O valor da venda R$ "))

if venda <= 20000.00:
    venda *= 0.14
    venda += 400
elif venda >= 20000.01 and venda <= 40000:
    venda *= 0.14
    venda += 500
elif venda >= 40000.01 and venda <= 60000:
    venda *= 0.14
    venda += 550
elif venda >= 60000.01 and venda <= 80000:
    venda *= 0.14
    venda += 600
elif venda >= 80000.01 and venda <= 100000:
    venda *= 0.14
    venda += 650
elif venda >= 100000.01:
    venda *= 0.16
    venda += 700

print("Comissao R$%.2f\n" % venda)
