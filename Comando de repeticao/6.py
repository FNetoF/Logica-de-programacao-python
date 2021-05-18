# 13. Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares
# de 0 até N em ordem crescente.

num = int(input("Informe um valor: "))

for i in range(1, num, 1):
    if i % 2 == 0:
        print("\t", i)

'''
for i in range(0, num, 2):
    print("\t", i)
'''
