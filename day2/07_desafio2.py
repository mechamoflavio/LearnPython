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
print("Você terá 7 chances de acertar um numero aleatorio de 1 a 100")
print("Será que você consegue?")

# Condição 1
import random
numero_aleatorio = random.randint(1, 100)

# Debugging
print(f"numero_aleatorio = {numero_aleatorio}")
