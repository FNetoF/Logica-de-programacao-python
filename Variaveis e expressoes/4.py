'''
6. Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
A fórmula de conversão é: F = C*(9.0/5.0)+32.0, sendo F a temperatura em Fahrenheit e
C a temperatura em Celsius.
'''

temp_celsius = float(input("Informe a temperatura em graus Celsius: "))

f = temp_celsius * (9.0 / 5.0) + 32.0

print("Temperatura em graus Fahrenheit é %.2f" % f)
