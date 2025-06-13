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

# db inicial
biblioteca = { # condição 1 do desafio
    "tiro/fps": [ # condição 2 do desafio
        {"titulo": "Counter-Strike", "ano": 1999, "plataforma": "PC"}, # condição 3 do desafio
        {"titulo": "Call of Duty: Mobile", "ano": 2019, "plataforma": "Mobile"}
        ],
    }
