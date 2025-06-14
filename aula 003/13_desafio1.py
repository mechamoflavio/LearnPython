###### Desafio1.py
######
###### Crie um sistema para gerenciar sua coleção de jogos:
###### 1. Use dicionário com gêneros como chaves
###### 2. Cada gênero contém uma lista de jogos
###### 3. Cada jogo é um dicionário com: título, ano, plataforma
###### 4. Implemente funções para:
######    - Adicionar jogo
######    - Listar jogos por plataforma
######    - Buscar jogos por título
######    - Mostrar estatísticas (total de jogos, jogos por gênero)
######

# database inicial
biblioteca = { # condição 1: dicionario
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
