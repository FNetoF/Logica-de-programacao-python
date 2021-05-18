# 30. Leia um valor em real e a contação do dólar. Em seguida, imprima o valor correspondente em dolares.

real = float(input("Informe o valor em (Real) R$ "))
cotacao_dolar = float(input("Informe a cotação do dolar do dia $ "))

dolar = real / cotacao_dolar

print("Total $ %.2f" % dolar)
