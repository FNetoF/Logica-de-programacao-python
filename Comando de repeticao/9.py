# 26. Faça um algoritmo que encontra o primeiro múltiplo de 11, 13 ou 17 após um número dado

num = int(input("Informe um numero: "))

for i in range(1, num, 1):
    if i % 11 == 0 or i % 13 == 0 or i % 17 == 0:
        print(i)
