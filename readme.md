# 🗡️ Desafio RPG — Python para aventureiros iniciantes

Bem-vindo, jovem aventureiro! Aqui você vai resolver **10 missões de código** usando Python.
Cada missão tem um teste que vai verificar se você acertou. Quando todos os testes passarem, você completou a quest! ⚔️🏆

---

## 📁 Arquivos do projeto

| Arquivo | O que é |
|---|---|
| `desafio_rpg.py` | **Aqui você escreve seu código!** |
| `test_desafio_rpg.py` | Os testes automáticos (não precisa mexer) |
| `requirements.txt` | Lista de ferramentas necessárias |
| `README.md` | Este guia |

---

## ⚙️ Como configurar o ambiente

### 1. Instale as dependências

Abra o terminal na pasta do projeto e rode:

```bash
pip install -r requirements.txt
```

### 2. Rode os testes

```bash
pytest test_desafio_rpg.py -v
```

A flag `-v` mostra o nome de cada teste. Você vai ver algo assim:

```
PASSED  test_saudacao_com_nome        ✅
FAILED  test_heroi_vivo_com_hp_positivo  ❌
```

### 3. Rodar um teste específico

Se quiser testar só um desafio de cada vez:

```bash
pytest test_desafio_rpg.py -v -k "saudacao"
```

Troque `"saudacao"` pelo nome do desafio que quiser testar.

---



## 💡 Dicas para resolver os desafios

### Dicas gerais

- Leia **com calma** o comentário de cada função — ele explica o que você deve fazer e dá exemplos.
- Sempre **teste um desafio de cada vez** para não se perder.
- Se travar, tente escrever o código no papel antes de digitar.
- Errar faz parte! Os testes existem para te ajudar a achar o erro, não para te julgar 😄

### Dicas por desafio

| # | Dica |
|---|---|
| 1 | Use f-string: `f"Olá, {nome}!"` |
| 2 | Compare `hp` com `0` usando `>` |
| 3 | Multiplicação em Python usa `*` |
| 4 | Use `if`, `elif` e `else` para cada classe |
| 5 | O operador `in` verifica se algo está em uma lista: `"espada" in inventario` |
| 6 | Divida `xp` por `100` e some `1`. Pesquise sobre divisão inteira `//` |
| 7 | Use a função `min()` para não ultrapassar o máximo |
| 8 | Compare as forças com `>` e use `if`/`elif`/`else` |
| 9 | Use `sum()` para somar uma lista. Para o desconto: `total * (1 - desconto/100)` |
| 10 | Use f-string com várias linhas e chame `calcular_nivel(heroi["xp"])` |

### Como usar f-strings

```python
nome = "Arthur"
hp = 100
mensagem = f"Herói: {nome}, HP: {hp}"
# resultado: "Herói: Arthur, HP: 100"
```

### Como acessar um dicionário

```python
heroi = {"nome": "Arthur", "classe": "guerreiro"}
print(heroi["nome"])    # Arthur
print(heroi["classe"])  # guerreiro
```

---

## 🏅 Ordem sugerida

Resolva os desafios **em ordem** — eles ficam gradualmente mais difíceis e o Desafio 10 usa uma função que você criou antes!

```
Desafio 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10  🏆
```

Boa sorte, aventureiro! 🐉
