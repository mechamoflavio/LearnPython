###### Desafio1.py
######
###### Crie um sistema para gerenciar sua coleção de jogos:
###### 1. Use dicionário com gêneros como chaves                        ok
###### 2. Cada gênero contém uma lista de jogos                         ok
###### 3. Cada jogo é um dicionário com: título, ano, plataforma        ok
###### 4. Implemente funções para:
######    - Adicionar jogo                                              ok
######    - Listar jogos por plataforma                                 ok
######    - Buscar jogos por título                                     iniciado
######    - Mostrar estatísticas (total de jogos, jogos por gênero)     aguardando
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
    plataforma = input("Plataforma: ")
    try: ano = int(input("Ano de lançamento: "))
    except ValueError:
        print("Ano invalido! Use apenas numeros.")
        return

    novo_jogo = (titulo, plataforma, ano) # tupla de dados

    if genero not in db_jogos: # verifica genero na database e cria se não existir
        db_jogos[genero] = []

    db_jogos[genero].append({ # adiciona os dados coletados
        "titulo": titulo,
        "plataforma": plataforma,
        "ano": ano
        })

    print(f"Jogo '{titulo}' adicionado com sucesso no genero {genero}!")

# condição 4.2: função listar jogos por plataforma
def f_listar_platf():
    platf_unicas = set(jogo["plataforma"]
                       for lista_jogos in db_jogos.values()
                       for jogo in lista_jogos)
    print(f"\nPlataformas cadastradas: {platf_unicas}")

# condição 4.3: função buscar jogos por titulo
def f_buscar_titulo():

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
