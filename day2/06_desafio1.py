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
in_peso = float(input("Qual seu peso? "))
in_altura = float(input("Qual sua altura? "))

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
print(f"Considerando sua altura ({in_altura}) e seu peso ({in_peso}), atualmente seu imc é de ({imc}). Esse resultado é considerado como ({tipo_corpo}).")
