###### Desafio1.py
######
###### Crie um sistema para gerenciar sua coleção de jogos:
###### 1. Use dicionário com gêneros como chaves                        ok
###### 2. Cada gênero contém uma lista de jogos                         ok
###### 3. Cada jogo é um dicionário com: título, ano, plataforma        ok
###### 4. Implemente funções para:
######    - Adicionar jogo
######    - Listar jogos por plataforma
######    - Buscar jogos por título
######    - Mostrar estatísticas (total de jogos, jogos por gênero)
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

# função adicionar jogo
def add_jogo():
    genero = input("Gênero do jogo: ").lower()

    titulo = input("Titulo: ")
    plataforma = input("Plataforma: ")

    try:
        ano = int(input("Ano de lançamento: "))
    except ValueError:
        print("Ano invalido! Use apenas numeros.")
        return

    novo_jogo = (titulo, plataforma, ano) # tupla de dados

    if genero not in db_jogos:
        db_jogos[genero] = []

