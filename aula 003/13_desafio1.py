###### Desafio1.py
######
###### Crie um sistema para gerenciar sua coleção de jogos:
###### 1. Use dicionário com gêneros como chaves                        ok (checked)
###### 2. Cada gênero contém uma lista de jogos                         ok (checked)
###### 3. Cada jogo é um dicionário com: título, ano, plataforma        ok (checked)
###### 4. Implemente funções para:
######    - Adicionar jogo                                              ok (need testing)
######    - Listar jogos por plataforma                                 ok (need testing)
######    - Buscar jogos por título                                     ok (need testing)
######    - Mostrar estatísticas (total de jogos, jogos por gênero)     ok (need testing)
######

# Database inicial de jogos
db_jogos = {
    "Tiro/FPS": [
        {"titulo": "Counter-Strike", "ano": 1999, "plataforma": "PC"},
        {"titulo": "Call of Duty: Mobile", "ano": 2019, "plataforma": "Mobile"}
    ],
    "RPG": [
        {"titulo": "World of Warcraft", "ano": 2004, "plataforma": "PC"},
        {"titulo": "Priston Tale", "ano": 2001, "plataforma": "PC"},
        {"titulo": "Brawl Stars", "ano": 2017, "plataforma": "Mobile"}
    ],
    "Corrida": [
        {"titulo": "Need for Speed: Underground", "ano": 2003, "plataforma": "PC"},
        {"titulo": "Real Racing 3", "ano": 2013, "plataforma": "Mobile"}
    ]
}

def f_add_jogo():
    """Adiciona um novo jogo ao inventário"""
    genero = input("Gênero do jogo: ").title()  # Usar title() para padronizar
    titulo = input("Título: ")

    try:
        ano = int(input("Ano de lançamento: "))
    except ValueError:
        print("Ano inválido! Use apenas números.")
        return

    plataforma = input("Plataforma: ")

    # Verifica se o gênero já existe, senão cria
    if genero not in db_jogos:
        db_jogos[genero] = []

    # Verifica se o jogo já existe
    for jogo in db_jogos[genero]:
        if jogo["titulo"].lower() == titulo.lower() and jogo["plataforma"].lower() == plataforma.lower():
            print("Este jogo já está cadastrado neste gênero!")
            return

    # Adiciona o novo jogo
    db_jogos[genero].append({
        "titulo": titulo,
        "ano": ano,
        "plataforma": plataforma
    })

    print(f"\n✅ Jogo '{titulo}' adicionado com sucesso ao gênero {genero}!")
    print(f"   Ano: {ano} | Plataforma: {plataforma}")

def f_listar_por_plataforma():
    """Lista todos os jogos agrupados por plataforma"""
    # Cria um dicionário para agrupar por plataforma
    jogos_por_plataforma = {}

    for genero, jogos in db_jogos.items():
        for jogo in jogos:
            plataforma = jogo["plataforma"]
            if plataforma not in jogos_por_plataforma:
                jogos_por_plataforma[plataforma] = []
            jogos_por_plataforma[plataforma].append(jogo)

    # Mostra os resultados
    if not jogos_por_plataforma:
        print("Nenhum jogo cadastrado!")
        return

    print("\n=== JOGOS POR PLATAFORMA ===")
    for plataforma, jogos in jogos_por_plataforma.items():
        print(f"\n🔧 {plataforma.upper()}:")
        for jogo in jogos:
            print(f"  - {jogo['titulo']} ({jogo['ano']}) - {list(db_jogos.keys())[[i for i, lista in enumerate(db_jogos.values()) if jogo in lista][0]]}")

def f_buscar_jogo():
    """Busca jogos por título, plataforma ou gênero"""
    termo = input("\nBuscar por (título, plataforma ou gênero): ").lower()
    resultados = []

    for genero, jogos in db_jogos.items():
        # Busca por gênero
        if termo in genero.lower():
            resultados.extend(jogos)

        for jogo in jogos:
            # Busca por título
            if termo in jogo["titulo"].lower():
                resultados.append(jogo)

            # Busca por plataforma
            if termo in jogo["plataforma"].lower():
                resultados.append(jogo)

    # Remove duplicatas usando conjunto
    jogos_unicos = []
    titulos_vistos = set()
    for jogo in resultados:
        if jogo["titulo"] not in titulos_vistos:
            titulos_vistos.add(jogo["titulo"])
            jogos_unicos.append(jogo)

    # Mostra resultados
    if not jogos_unicos:
        print("\n🔍 Nenhum jogo encontrado!")
        return

    print(f"\n🔍 Resultados da busca ({len(jogos_unicos)} encontrados):")
    for jogo in jogos_unicos:
        # Encontra o gênero do jogo
        genero_jogo = [g for g, jogos in db_jogos.items() if jogo in jogos][0]
        print(f"  - {jogo['titulo']} ({jogo['ano']}) | {jogo['plataforma']} | {genero_jogo}")

def f_estatisticas():
    """Mostra estatísticas da coleção"""
    total_jogos = sum(len(jogos) for jogos in db_jogos.values())

    print("\n📊 ESTATÍSTICAS DA COLEÇÃO")
    print(f"Total de jogos: {total_jogos}")
    print("\nJogos por gênero:")
    for genero, jogos in db_jogos.items():
        print(f"  - {genero}: {len(jogos)} jogos")

    # Jogos por plataforma
    plataformas = {}
    for jogos in db_jogos.values():
        for jogo in jogos:
            plataforma = jogo["plataforma"]
            plataformas[plataforma] = plataformas.get(plataforma, 0) + 1

    print("\nJogos por plataforma:")
    for plataforma, quantidade in plataformas.items():
        print(f"  - {plataforma}: {quantidade} jogos")

def main():
    while True:
        print("\n" + "="*40)
        print("🎮 SISTEMA DE INVENTÁRIO DE JOGOS")
        print("="*40)
        print("1. Adicionar jogo")
        print("2. Listar jogos por plataforma")
        print("3. Buscar jogos")
        print("4. Estatísticas")
        print("5. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            f_add_jogo()
        elif opcao == "2":
            f_listar_por_plataforma()
        elif opcao == "3":
            f_buscar_jogo()
        elif opcao == "4":
            f_estatisticas()
        elif opcao == "5":
            print("\nAté logo! Obrigado por usar o sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
