###### Crie um jogo onde:
###### 1. O computador sorteia um número entre 1-100
###### 2. O usuário tem 7 tentativas para adivinhar
###### 3. A cada tentativa, o programa diz se o número é maior ou menor
###### 4. Ao acertar ou esgotar tentativas, mostra mensagem apropriada
###### # Dica:
###### #   import random
###### #   numero_secreto = random.randint(1, 100)

# Boas vindas ao jogo
print("Bem vindo ao jogo de adivinhação!")
print("Advinhe um número aleatório de 1 a 100.")

# Configurações
import random # Condição 1
numero_aleatorio = random.randint(1, 100)
try_count = 7 # Condição 2

while try_count > 0: # Condição 3
    try: # verifica validade do input
        in_numero = int(input("Digite um numero: "))
    except ValueError:
        print("Erro: Digite apenas números inteiros!")
        exit()
    if in_numero == numero_aleatorio:
        print("!!! Parabéns, você acertou o numero. !!!")
        break

    elif try_count > 1:
        try_count -= 1
        print("Que pena, você errou dessa vez.")
        print(f"Te restam {try_count} chance(s).")
        if in_numero > numero_aleatorio:
            print("Dica: que tal tentar um número menor?")
        else: print("Dica: que tal tentar um número maior?")
    else:
        print("Não foi dessa vez, mas você chegou perto.")
        print("Que tal tentar de novo? Experimente seguir a dica.")
        break
