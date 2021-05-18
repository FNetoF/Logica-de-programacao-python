# 25. Faça um programa que some todos os números naturais abaixo de 1000 que são mútiplos de 3 ou 5.

for i in range(1, 1000, 1):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
