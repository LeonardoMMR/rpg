# ============================================================
#  DESAFIO RPG - Complete as funções abaixo!
#  Cada função tem uma descrição dizendo o que ela deve fazer.
#  Quando todas as funções estiverem certas, todos os testes
#  vão passar. Boa aventura! ⚔️🛡️
# ============================================================

# Desafio 1 - Saudação do herói
# Crie uma saudação para o herói.
# Exemplo: saudacao_heroi("Arthur") → "Saudações, Arthur! Que comecem as aventuras!"
def saudacao_heroi(nome):
    return f"Saudações, {nome}! Que comecem as aventuras!"

# Desafio 2 - Herói está vivo?
# Retorne True se os pontos de vida (hp) forem maiores que 0, senão False.
# Exemplo: heroi_vivo(50) → True
#          heroi_vivo(0)  → False
def heroi_vivo(hp):
    if hp > 0:
        return True
    else:
        return False

# Desafio 3 - Calcular dano
# Um guerreiro causa dano = forca * multiplicador.
# Exemplo: calcular_dano(10, 2) → 20
def calcular_dano(forca, multiplicador):
    return forca * multiplicador

# Desafio 4 - Tipo de personagem
# Retorne a descrição da classe do personagem:
#   "guerreiro" → "Especialista em combate corpo a corpo"
#   "mago"      → "Mestre das artes arcanas"
#   "arqueiro"  → "Preciso como uma flecha"
# Para qualquer outro valor, retorne "Classe desconhecida"
def descricao_classe(classe):
    if(classe == "guerreiro"):
        return "Especialista em combate corpo a corpo"
    elif(classe == "mago"):
        return "Mestre das artes arcanas"
    elif(classe == "arqueiro"):
        return "Preciso como uma flecha"
    else:
        return "Classe desconhecida"

# Desafio 5 - Verificar inventário
# Retorne True se o item estiver na lista inventario, senão False.
# Exemplo: tem_item(["espada", "escudo", "poção"], "escudo") → True
def tem_item(inventario, item):
    if item in inventario:
        return True
    else:
        return False

# Desafio 6 - Calcular nível
# O herói sobe de nível a cada 100 pontos de experiência (xp).
# Nível mínimo é 1 (mesmo com xp = 0).
# Exemplo: calcular_nivel(0)   → 1
#          calcular_nivel(100) → 2
#          calcular_nivel(350) → 4
def calcular_nivel(xp): 
    x = xp / 100 + 1
    if x % 100 + 1 != 0:
        while x % 100 + 1 != 0:
            x += -0.01
    else:
        x = x
    return x

    

# Desafio 7 - Usar poção de cura
# Aplica cura ao herói. O HP não pode ultrapassar o hp_maximo.
# Exemplo: usar_pocao(80, 30, 100) → 100  (80+30=110, mas máximo é 100)
#          usar_pocao(50, 20, 100) → 70
def usar_pocao(hp_atual, cura, hp_maximo):
    pass
    

# Desafio 8 - Resultado da batalha
# Dois heróis batalham. Quem tiver mais forca vence.
# Retorne o nome do vencedor ou "Empate!" se a força for igual.
# Exemplo: resultado_batalha("Aragorn", 15, "Sauron", 20) → "Sauron"
def resultado_batalha(nome1, forca1, nome2, forca2):
    pass


# Desafio 9 - Total da loja
# Dada uma lista de preços (números), retorne o valor total.
# Aplique um desconto percentual se desconto > 0.
# Exemplo: total_loja([10, 20, 30], 0)  → 60
#          total_loja([10, 20, 30], 10) → 54.0  (10% de desconto)
def total_loja(precos, desconto=0):
    pass


# Desafio 10 - Ficha do herói
# Dado um dicionário com as chaves "nome", "classe", "hp" e "xp",
# monte e retorne a ficha completa como texto.
# O nível deve ser calculado pelo xp (use a função calcular_nivel!).
# Formato exato:
# "=== Ficha do Herói ===\nNome: Arthur\nClasse: guerreiro\nHP: 100\nNível: 3"
def ficha_heroi(heroi):
    pass
