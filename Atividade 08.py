# Imagine que você está em uma viagem para os Estados Unidos e precisa converter o valor em reais para dólares. Crie um programa que receba o valor em reais e a taxa de câmbio atual, e exiba o valor equivalente em dólares.

real = float(input("Digite o valor em reais"))
dolar = float(input("Digite o valor do cambio do dolar"))

valorConvertido = real/dolar

print(f"Seu valor é $ {valorConvertido}")