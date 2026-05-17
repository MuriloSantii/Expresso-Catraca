# E3 — MVP: Núcleo Funcional com Primeiras Telas

> **Disciplina:** Teoria dos Grafos  
> **Prazo:** 10 de maio de 2026  
> **Peso:** 25% da nota final  

---

## Identificação do Grupo

| Campo | Preenchimento |
|-------|---------------|
| Nome do projeto | Expresso Catraca |
| Repositório GitHub | https://github.com/MuriloSantii/expresso-catraca |
| Integrante 1 | Murilo Santiago — RA: [SEU RA AQUI] |
| Integrante 2 | [Nome do Colega 1 ou remover] — RA |
| Integrante 3 *(se houver)* | [Nome do Colega 2 ou remover] — RA |

---

## 1. Como Executar o MVP

**Pré-requisitos:**
```bash
# Python 3.10+ instalado no sistema.
```

**Instalação:**
```bash
# Clone o repositório
git clone [https://github.com/MuriloSantii/expresso-catraca.git](https://github.com/MuriloSantii/expresso-catraca.git)
cd expresso-catraca
```

**Execução:**
```bash
# Comando para rodar o MVP no terminal
python src/main.py
```

**Saída esperada:**
```text
==================================================
🚆 EXPRESSO CATRACA - INICIALIZANDO MVP 🚆
==================================================
📂 Carregando mapa de: data\grafo_sp.json...
✅ Mapa carregado na memória com sucesso!

--- NOVA ROTA ---
📍 Digite a estação de origem (ex: Sé): Sé
🎯 Digite a estação de destino (ex: Luz): Luz

⚙️  Calculando a rota mais rápida...

==========================================
📦 EXPRESSO CATRACA - RECIBO DE ROTA 📦
==========================================
📍 Origem:  Sé
🎯 Destino: Luz
⏱️ Tempo Estimado: 5 minutos
🛤️ Trajeto: Sé -> São Bento -> Luz
==========================================
```

---

## 2. Algoritmo Implementado

| Campo | Resposta |
|-------|----------|
| Nome do algoritmo | Algoritmo de Dijkstra |
| Arquivo de implementação | `src/algorithms/dijkstra.py` |
| Complexidade de tempo | $O(E \log V)$ |
| Complexidade de espaço | $O(V)$ |

**Trecho do código com comentário de Big-O:**

```python
    # O(V) - Cria a tabela de tempos com infinito
    tempos = {estacao: float('infinity') for estacao in grafo_obj.adjacencias}
    tempos[origem] = 0 
    
    # O(V) - Guarda a trilha de volta
    estacao_anterior = {estacao: None for estacao in grafo_obj.adjacencias}
    
    fila = [(0, origem)]
    
    # O(E log V) - Loop principal processando as arestas com Min-Heap
    while fila:
        tempo_atual, estacao_atual = heapq.heappop(fila)
```

---

## 3. Estrutura do Repositório

```text
expresso-catraca/
├── data/
│   └── grafo_sp.json
├── docs/
│   ├── E2_Template.md
│   └── E3_Template.md
├── src/
│   ├── core/
│   │   └── grafo.py
│   ├── algorithms/
│   │   └── dijkstra.py
│   ├── io/
│   │   └── leitor_json.py
│   └── main.py
└── tests/
    └── test_algoritmos.py
```

**Desvios em relação ao E2**: Sem desvios. Estrutura fiel à arquitetura em camadas projetada.

---

## 4. Telas do MVP

### Tela de Entrada / Resultado CLI

![Tela do Terminal](./docs/assets/mvp_terminal.png)

*Descrição:* Interface de linha de comando operando em fluxo contínuo. Demonstra a injeção do JSON e a execução do roteamento com sucesso. *(Nota: Guarde o print do terminal rodando o sistema na pasta docs/assets)*.

---

## 5. Testes Unitários

| Algoritmo | Caso de teste | Status | Comando para executar |
|-----------|--------------|--------|----------------------|
| Dijkstra | Caso base | ✅ | `python -m pytest tests/` |
| Dijkstra | Grafo vazio | ✅ | `python -m pytest tests/` |
| Dijkstra | Grafo completo | ✅ | `python -m pytest tests/` |

**Como rodar todos os testes:**
```bash
python -m pytest tests/
```

**Resultado atual:**
```text
tests\test_algoritmos.py ...                                             [100%]
============================== 3 passed in 0.03s ==============================
```

---

## 6. Histórico de Commits

| Hash (7 chars) | Mensagem | Autor |
|----------------|----------|-------|
| a7240ee | `feat: entrega completa do MVP (E3) com rotas, testes e documentação` | Murilo |

---

## 7. O que está funcionando / O que ainda falta

| Funcionalidade | Status | Observação |
|---------------|--------|------------|
| Classe do grafo | ✅ Completo | Operações de vértices e arestas isoladas. |
| Algoritmo principal | ✅ Completo | Dijkstra com fila de prioridade implementado. |
| Leitura de arquivo | ✅ Completo | Leitor converte dicionários JSON nativamente. |
| Tela de entrada | ✅ Completo | Coleta via CLI. |
| Tela de resultado | ✅ Completo | Output de console padronizado em recibo. |
| Testes unitários | ✅ Completo | Casos base, conexões nulas e malhas totais testados. |

---