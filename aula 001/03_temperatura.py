#Esse é o terceiro arquivo em python, seguindo o desafio numero 2 (dia 1 parte 3)
#
# Crie um conversor de Celsius para Fahrenheit
# Fórmula: F = (C × 9/5) + 32
# O programa deve:
# 1. Pedir a temperatura em Celsius
# 2. Converter para Fahrenheit
# 3. Mostrar o resultado com 1 casa decimal

# Exemplo:
# "25°C = 77.0°F"


temperatura = int(input("Qual a temperatura em Celsius? "))
convertido = (temperatura*9/5)+32
print(f"O valor de {temperatura} em Celsius convertido para Fahrenheit fica igual a {convertido}")
