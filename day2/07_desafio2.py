###### Crie um jogo onde:
###### 1. O computador sorteia um número entre 1-100
###### 2. O usuário tem 7 tentativas para adivinhar
###### 3. A cada tentativa, o programa diz se o número é maior ou menor
###### 4. Ao acertar ou esgotar tentativas, mostra mensagem apropriada
###### # Dica:
###### #   import random
###### #   numero_secreto = random.randint(1, 100)

print("Bem vindo ao jogo de adivinhação!")  # Boas vindas ao jogo
print("Você terá 7 chances de acertar um numero aleatorio de 1 a 100")
print("Será que você consegue?")

import random   # Condição 1
numero_aleatorio = random.randint(1, 100)

tentativas = 7  # Condição 2

try: # verificação se dados de entrada é valido
    in_numero = int(input("Digite um numero de 1 a 100: "))
except ValueError: # em caso de erro na entrada de dados
    print("Erro: Digite apenas números inteiros!")
    exit()

# Debugging
print(f"numero_aleatorio = {numero_aleatorio}")
print(f"numero digitado = {in_numero}")
