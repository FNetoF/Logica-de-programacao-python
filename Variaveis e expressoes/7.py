# 37. Faça um programa que leia o valor de um produto e imprima o valor com desconto,
# tendo em vista que o desconto foi de 12%

produto = float(input("Informe o valor do produto R$ "))

produto -= (produto * 0.12)

print("Produto R${:.2f}".format(produto))
