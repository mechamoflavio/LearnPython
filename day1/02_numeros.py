# Meu segundo programa baseado no desafio 1 (dia 1 parte 3)
#
# Crie um programa que:
# 1. Pede dois números ao usuário
# 2. Calcula: soma, subtração, multiplicação e divisão
# 3. Mostra os resultados formatados

# Exemplo de saída:
# "Soma: 15, Subtração: 5, Multiplicação: 50, Divisão: 2.0"


primeiro_numero = int(input("Olá, diga 1 numero inteiro: "))
segundo_numero = int(input("agora diga um 2 numero inteiro: "))


soma = primeiro_numero + segundo_numero
subtração = primeiro_numero - segundo_numero
multiplicação = primeiro_numero * segundo_numero
divisão = primeiro_numero / segundo_numero


print(f"Aqui estão os resultados para os numeros {primeiro_numero} e {segundo_numero}")
print(f"{primeiro_numero}+{segundo_numero}={soma}")
print(f"{primeiro_numero}-{segundo_numero}={subtração}")
print(f"{primeiro_numero}*{segundo_numero}={multiplicação}")
print(f"{primeiro_numero}/{segundo_numero}={divisão}")
