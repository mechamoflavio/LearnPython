# Dados iniciais
biblioteca = {
    "fantasia": [
        {"titulo": "Harry Potter", "autor": "J.K. Rowling", "ano": 1997},
        {"titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien", "ano": 1954}
    ],
    "ficcao_cientifica": [
        {"titulo": "Duna", "autor": "Frank Herbert", "ano": 1965},
        {"titulo": "Fundação", "autor": "Isaac Asimov", "ano": 1951}
    ]
}

# Função para adicionar livro
def adicionar_livro():
    genero = input("Gênero do livro: ").lower()

    titulo = input("Título: ")
    autor = input("Autor: ")

    try:
        ano = int(input("Ano de publicação: "))
    except ValueError:
        print("Ano inválido! Use apenas números.")
        return

    novo_livro = (titulo, autor, ano)  # Usando tupla para dados imutáveis

    if genero not in biblioteca:
        biblioteca[genero] = []  # Cria novo gênero se não existir

    biblioteca[genero].append({
        "titulo": titulo,
        "autor": autor,
        "ano": ano
    })

    print(f"Livro '{titulo}' adicionado com sucesso ao gênero {genero}!")

# Função para buscar livros
def buscar_livros():
    termo = input("Buscar por (título/autor/gênero): ").lower()
    resultados = []

    for genero, livros in biblioteca.items():
        if termo in genero:
            resultados.extend(livros)

        for livro in livros:
            if termo in livro["titulo"].lower() or termo in livro["autor"].lower():
                resultados.append(livro)

    # Remove duplicatas usando set
    livros_unicos = {livro["titulo"]: livro for livro in resultados}.values()

    if not livros_unicos:
        print("Nenhum livro encontrado.")
        return

    print("\nResultados da busca:")
    for livro in livros_unicos:
        print(f"- {livro['titulo']} ({livro['autor']}, {livro['ano']})")

# Função principal
def main():
    while True:
        print("\n=== SISTEMA BIBLIOTECA ===")
        print("1. Adicionar livro")
        print("2. Buscar livros")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_livro()
        elif opcao == "2":
            buscar_livros()
        elif opcao == "3":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
