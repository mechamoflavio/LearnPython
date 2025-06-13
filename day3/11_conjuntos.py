# Criação
numeros = {1, 2, 3, 3, 4}  # {1, 2, 3, 4}

# Adição
numeros.add(5)

# Remoção
numeros.remove(3)

# Operações de conjunto
pares = {2, 4, 6, 8}
impares = {1, 3, 5, 7}

uniao = pares | impares  # {1,2,3,4,5,6,7,8}
intersecao = pares & {4, 5}  # {4}
diferenca = pares - {2, 8}  # {4,6}
