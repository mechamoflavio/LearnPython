numero = int(input("Digite um número inteiro: "))

# Verificação de sinal
if numero > 0:
    sinal = "positivo"
elif numero < 0:
    sinal = "negativo"
else:
    sinal = "zero"

# Verificação de paridade e aplicação de condicionais na mesma sintaxe
paridade = "par" if numero % 2 == 0 else "ímpar"

# A divisão utilizando % traz como resultado a "sobra" da divisão
# Ex: 10 % 2 = 0
# Ex: 10 % 3 = 1

# Verificação de múltiplo de 5
multiplo_5 = "é" if numero % 5 == 0 else "não é"

print(f"O número {numero} é {sinal}, {paridade} e {multiplo_5} múltiplo de 5.")
