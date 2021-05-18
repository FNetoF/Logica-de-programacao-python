# 2. Leia um numero fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada
# do número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.

import math

num = int(input("Informe un numero: "))

if num >= 0:
    raiz = math.sqrt(num)
    print("\nA raiz quadrada de", num, "é", raiz)
else:
    print("\nNúmero inválido")
