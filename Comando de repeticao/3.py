# 10. Faça um programa que calcule e mostre a soma dos 50 primeiros números pares

i = 0
soma = 0

while i <= 100:
    if i % 2 == 0:
        soma += i
    i += 1
print(soma)
