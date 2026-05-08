import pytest
from desafio_rpg import (
    saudacao_heroi,
    heroi_vivo,
    calcular_dano,
    descricao_classe,
    tem_item,
    calcular_nivel,
    usar_pocao,
    resultado_batalha,
    total_loja,
    ficha_heroi,
)

# ─────────────────────────────────────────────
#  Desafio 1 - Saudação do herói
# ─────────────────────────────────────────────
def test_saudacao_com_nome():
    assert saudacao_heroi("Arthur") == "Saudações, Arthur! Que comecem as aventuras!"

def test_saudacao_outro_nome():
    assert saudacao_heroi("Zelda") == "Saudações, Zelda! Que comecem as aventuras!"


# ─────────────────────────────────────────────
#  Desafio 2 - Herói está vivo?
# ─────────────────────────────────────────────
def test_heroi_vivo_com_hp_positivo():
    assert heroi_vivo(50) is True

def test_heroi_morto_com_hp_zero():
    assert heroi_vivo(0) is False

def test_heroi_morto_com_hp_negativo():
    assert heroi_vivo(-10) is False


# ─────────────────────────────────────────────
#  Desafio 3 - Calcular dano
# ─────────────────────────────────────────────
def test_dano_simples():
    assert calcular_dano(10, 2) == 20

def test_dano_com_multiplicador_um():
    assert calcular_dano(15, 1) == 15

def test_dano_com_multiplicador_fracionado():
    assert calcular_dano(10, 1.5) == 15.0


# ─────────────────────────────────────────────
#  Desafio 4 - Tipo de personagem
# ─────────────────────────────────────────────
def test_classe_guerreiro():
    assert descricao_classe("guerreiro") == "Especialista em combate corpo a corpo"

def test_classe_mago():
    assert descricao_classe("mago") == "Mestre das artes arcanas"

def test_classe_arqueiro():
    assert descricao_classe("arqueiro") == "Preciso como uma flecha"

def test_classe_desconhecida():
    assert descricao_classe("bardo") == "Classe desconhecida"


# ─────────────────────────────────────────────
#  Desafio 5 - Verificar inventário
# ─────────────────────────────────────────────
def test_item_presente_no_inventario():
    assert tem_item(["espada", "escudo", "poção"], "escudo") is True

def test_item_ausente_no_inventario():
    assert tem_item(["espada", "escudo", "poção"], "arco") is False

def test_inventario_vazio():
    assert tem_item([], "espada") is False

def test_tem_gatos():
    assert tem_item(["Sirius", "Luke", "Bastet"], "Sirius") is True 
    

# ─────────────────────────────────────────────
#  Desafio 6 - Calcular nível
# ─────────────────────────────────────────────
def test_nivel_com_xp_zero():
    assert calcular_nivel(0) == 1

def test_nivel_com_exatamente_100_xp():
    assert calcular_nivel(100) == 2

def test_nivel_com_xp_intermediario():
    assert calcular_nivel(350) == 4

def test_nivel_com_xp_alto():
    assert calcular_nivel(999) == 10


# ─────────────────────────────────────────────
#  Desafio 7 - Usar poção de cura
# ─────────────────────────────────────────────
def test_pocao_sem_ultrapassar_maximo():
    assert usar_pocao(50, 20, 100) == 70

def test_pocao_limitada_ao_maximo():
    assert usar_pocao(80, 30, 100) == 100

def test_pocao_com_hp_exatamente_no_maximo():
    assert usar_pocao(100, 10, 100) == 100


# ─────────────────────────────────────────────
#  Desafio 8 - Resultado da batalha
# ─────────────────────────────────────────────
def test_batalha_segundo_vence():
    assert resultado_batalha("Aragorn", 15, "Sauron", 20) == "Sauron"

def test_batalha_primeiro_vence():
    assert resultado_batalha("Gandalf", 25, "Orc", 10) == "Gandalf"

def test_batalha_empate():
    assert resultado_batalha("Herói A", 15, "Herói B", 15) == "Empate!"


# ─────────────────────────────────────────────
#  Desafio 9 - Total da loja
# ─────────────────────────────────────────────
def test_total_sem_desconto():
    assert total_loja([10, 20, 30], 0) == 60

def test_total_com_desconto_10_porcento():
    assert total_loja([10, 20, 30], 10) == 54.0

def test_total_com_lista_unitaria():
    assert total_loja([100], 25) == 75.0

def test_total_loja_sem_passar_desconto():
    assert total_loja([10, 10, 10]) == 30


# ─────────────────────────────────────────────
#  Desafio 10 - Ficha do herói
# ─────────────────────────────────────────────
def test_ficha_heroi_completa():
    heroi = {"nome": "Arthur", "classe": "guerreiro", "hp": 100, "xp": 250}
    esperado = "=== Ficha do Herói ===\nNome: Arthur\nClasse: guerreiro\nHP: 100\nNível: 3"
    assert ficha_heroi(heroi) == esperado

def test_ficha_heroi_nivel_1():
    heroi = {"nome": "Novato", "classe": "mago", "hp": 60, "xp": 0}
    esperado = "=== Ficha do Herói ===\nNome: Novato\nClasse: mago\nHP: 60\nNível: 1"
    assert ficha_heroi(heroi) == esperado
