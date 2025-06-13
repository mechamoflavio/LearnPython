# Criação
pessoa = {"nome": "Carlos", "idade": 35, "cidade": "Rio de Janeiro"}

# Acesso
nome = pessoa["nome"]  # "Carlos"
idade = pessoa.get("idade")  # 35 (mais seguro)

# Adição/Modificação
pessoa["email"] = "carlos@email.com"  # Adiciona novo campo
pessoa["idade"] = 36  # Atualiza valor existente

# Remoção
email = pessoa.pop("email")  # Remove e retorna o valor

# Verificação
if "cidade" in pessoa:
    print(pessoa["cidade"])

# Iteração
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
