# 12. Faça um programa que leia um numero inteiro N e imprima todos os números naturais
# de 0 até N em ordem decresente

num = int(input("Informe um número: "))

i = num
while i >= 0:
    print("\t", i)
    i -= 1
