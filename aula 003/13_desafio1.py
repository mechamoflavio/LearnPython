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
######    - Mostrar estatísticas (total de jogos, jogos por gênero)     iniciado
######

# database inicial de jogos
db_jogos = { # condição 1: dicionario
    "Tiro/FPS": [ # condição 2: genero e lista
        {"titulo": "Counter-Strike", "ano": 1999, "plataforma": "PC"}, # condição 3: titulo, ano, plataforma
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

# condição 4.1: função adicionar jogo
def f_add_jogo():
    genero = input("Gênero do jogo: ").lower() # coleta dados (genero, titulo, plataforma, ano)
    titulo = input("Titulo: ")
    try: ano = int(input("Ano de lançamento: "))
    except ValueError:
        print("Ano invalido! Use apenas numeros.")
        return
    plataforma = input("Plataforma: ")

    novo_jogo = (titulo, ano, plataforma) # tupla de dados

    if genero not in db_jogos: # verifica genero na database e cria se não existir
        db_jogos[genero] = []

    db_jogos[genero].append({ # adiciona os dados coletados
        "titulo": titulo,
        "ano": ano,
        "plataforma": plataforma
        })

    print(f"Jogo '{titulo}' adicionado com sucesso no genero {genero}! \nAno: {ano} ~ Plataforma: {plataforma}")

# condição 4.2: função listar jogos por plataforma
def f_listar_platf():
    platf_unicas = set(jogo["plataforma"]
                       for lista_jogos in db_jogos.values()
                       for jogo in lista_jogos)
    print(f"\nPlataformas cadastradas: {platf_unicas}")

# condição 4.3: função buscar jogos por titulo ou categoria
def f_buscar_jogo():
    termo = input("\nBuscar por 'jogo' ou 'plataforma': ").lower()
    resultados = []
    for plataforma, jogos in db_jogos.items():
        if termo in plataforma:
            resultados.extend(jogos)
        for jogo in jogos:
            if termo in jogo["titulo"].lower():
                resultados.append(jogo)
    jogos_unicos = {jogo["titulo"]: jogo for jogo in resultados}.values() # remove resultados duplicados
    if not jogos_unicos:
        print("Nenhum jogo encontrado.")
        return
    print("\nResultados da busca:")
    for jogo in jogos_unicos:
        print(f"- {jogo['titulo]']} ({jogo['ano']}, {jogo['plataforma']})")

# condição 4.4: estatísticas (total jogos e jogos por genero) e frontend

###################################
###### debugging ##################
###################################

# Usando set() para valores únicos
platf_unicas = set(jogo["plataforma"]
                   for lista_jogos in db_jogos.values() # Itera nas listas de jogos
                   for jogo in lista_jogos)             # Itera nos jogos de cada lista
print(f"\nPlataformas cadastradas: {platf_unicas}") # Saída: {'PC', 'Mobile'}

# Extrair TODAS as plataformas (incluindo repetições)
list_platf = [jogo["plataforma"]
              for lista_jogos in db_jogos.values()  # Itera nas listas de jogos
              for jogo in lista_jogos]              # Itera nos jogos de cada lista
print(list_platf) # Saída: ['PC', 'Mobile', 'PC', 'PC', 'Mobile', 'PC', 'Mobile']
