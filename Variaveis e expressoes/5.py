'''
7. Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
A fórmula de conversão é: C = 5.0*(F-32.0)/9.0, sendo C a temperatura em Celsius e
F a temperatura em Fahrenheit.
'''

temp_fahrenheit = float(input("Informe a temperatura em graus Fahrenheit: "))

c = 5.0 * (temp_fahrenheit - 32.0) / 9.0

print("Temperatura em graus Celsius é %.2f" % c)
