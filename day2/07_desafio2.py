###### Crie um jogo onde:
###### 1. O computador sorteia um número entre 1-100
###### 2. O usuário tem 7 tentativas para adivinhar
###### 3. A cada tentativa, o programa diz se o número é maior ou menor
###### 4. Ao acertar ou esgotar tentativas, mostra mensagem apropriada
###### # Dica:
###### #   import random
###### #   numero_secreto = random.randint(1, 100)

# Versão final após correções e sugestões da IA

print("=== Jogo de Adivinhação ===")
print("Tente adivinhar o número entre 1 e 100. Você tem 7 tentativas!")

# Configurações
import random
numero_secreto = random.randint(1, 100)
tentativas_restantes = 7

while tentativas_restantes > 0:
    print(f"\nTentativas restantes: {tentativas_restantes}")

    try:
        palpite = int(input("Digite seu palpite: "))

        # Validação do intervalo
        if palpite < 1 or palpite > 100:
            print("Por favor, digite um número entre 1 e 100!")
            continue

    except ValueError:
        print("Erro: Digite apenas números inteiros!")
        continue

    # Verificação do palpite
    if palpite == numero_secreto:
        print(f"🎉 Parabéns! Você acertou em {8 - tentativas_restantes} tentativas!")
        break

    tentativas_restantes -= 1

    # Feedback e dicas
    if palpite > numero_secreto:
        print("Dica: Tente um número MENOR")
    else:
        print("Dica: Tente um número MAIOR")

    # Mensagem final se acabarem as tentativas
    if tentativas_restantes == 0:
        print(f"\n😢 Fim de jogo! O número era {numero_secreto}.")
        print("Tente novamente - você consegue!")
