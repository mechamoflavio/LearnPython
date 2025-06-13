# Criação
frutas = ["maçã", "banana", "laranja"]

# Acesso
primeira = frutas[0]  # "maçã"

# Modificação
frutas[1] = "kiwi"  # ["maçã", "kiwi", "laranja"]

# Adição
frutas.append("uva")  # Adiciona no final
frutas.insert(1, "abacaxi")  # Insere na posição 1

# Remoção
frutas.pop()  # Remove o último
frutas.remove("kiwi")  # Remove pelo valor

# Ordenação
frutas.sort()  # Ordem alfabética
frutas.reverse()  # Inverte a ordem

# Compreensão de listas (avançado)
quadrados = [x**2 for x in range(10)]  # [0, 1, 4, 9, ..., 81]
