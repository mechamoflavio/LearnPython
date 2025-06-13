#####
##### Desafio 01:
##### Crie um programa que:
##### 1. Pede peso (kg) e altura (m)
##### 2. Calcula o IMC (peso / altura²)
##### 3. Classifica:
#####   - < 18.5: Magreza
#####   - 18.5-24.9: Normal
#####   - 25-29.9: Sobrepeso
#####   - >=30: Obesidade
##### 4. Mostra resultado formatado
#####
###### Dica: Use condicionais aninhadas
#####

# Boas vindas
print("Bem vindo ao meu primeiro programa de calculo de IMC")

# Coleta de dados # condição 1
try:    # sugestão de correção está utilizando try pra verificação de entrada de dados
    in_peso = float(input("Qual seu peso? "))
    in_altura = float(input("Qual sua altura? "))

    if in_peso <= 0 or in_altura <= 0:
        print("Erro: Valores devem ser positivos!")
        exit()

except ValueError:
    print("Erro: Digite apenas números!")
    exit()

# Calculando o IMC # condição 2
imc = in_peso / (in_altura * in_altura)

# Classificando # condição 3
if imc < 18.5:
    tipo_corpo = "Magreza"
elif imc < 25:
    tipo_corpo = "Normal"
elif imc < 30:
    tipo_corpo = "Sobrepeso"
else:
    tipo_corpo = "Obesidade"

# Resultado # condição 4
# sugestão de correção: Formatar IMC com 2 casas decimais
print(f"Considerando sua altura ({in_altura:.2f}) e seu peso ({in_peso:.1f}), atualmente seu IMC é de {imc:.1f}. Esse resultado é considerado como {tipo_corpo}.")
