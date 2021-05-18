# 15. Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os números pares
# de 1 até N em ordem crescente.

num = int(input("Informe um numero: "))

for i in range(1, num, 1):
    if i % 2 != 0:
        print("\t", i)

'''
num = int(input("Informe um numero: "))
for i in range(1, num, 2):
    print("\t", i)
'''
