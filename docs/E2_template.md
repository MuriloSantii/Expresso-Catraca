# E2 — Design Técnico, Arquitetura e Backlog

> **Disciplina:** Teoria dos Grafos  
> **Prazo:** 13 de abril de 2026  
> **Peso:** 20% da nota final  

---

## Identificação do Grupo

| Campo | Preenchimento |
|-------|---------------|
| Nome do projeto | Expresso Catraca |
| Integrante 1 | Guilherme da Macena Andrade — 38093057 |
| Integrante 2 | Murilo Santiago de Carvalho — 37616391 |
| Integrante 3 | Pedro Henrique Nepomoceno dos Santos — 38537958 |

---

## 1. Algoritmos Escolhidos

### 1.1 Algoritmo Principal

| Campo | Resposta |
|-------|----------|
| Nome do algoritmo | Algoritmo de Dijkstra |
| Categoria | Busca em Grafos / Algoritmo Guloso |
| Complexidade de tempo | $O(E \log V)$ (usando Fila de Prioridade/Min-Heap) |
| Complexidade de espaço | $O(V)$ |
| Problema que resolve | Encontrar o caminho mais rápido (menor peso) entre uma estação de origem e uma estação de destino na malha metroviária. |

**Por que este algoritmo foi escolhido?**
O Dijkstra é o padrão ouro para cálculo de caminhos mínimos de fonte única em grafos cujas arestas possuem pesos não negativos. No domínio do Expresso Catraca (transporte público), os pesos das arestas representam o tempo de viagem em minutos, que nunca assumirá valores negativos. Ele garante matematicamente a rota mais rápida considerando as baldeações e integrações.

**Alternativa descartada e motivo:**

| Algoritmo alternativo | Motivo da exclusão |
|----------------------|-------------------|
| Busca em Largura (BFS) | Foi descartado pois o BFS clássico assume que todas as arestas possuem peso uniforme (custo 1). No metrô real, o tempo entre estações varia drasticamente (ex: Sé->Liberdade leva 2 min, Braz Cubas->Tatuapé leva 45 min), o que tornaria as rotas do BFS ineficientes na vida real. |

**Limitações no contexto do problema:**
O algoritmo é incapaz de processar arestas com pesos negativos (o que não afeta nosso modelo físico). Além disso, sua complexidade pode aumentar em grafos excessivamente densos, limitação que é mitigada pela esparsidade natural das redes de trilhos de metrô (onde cada estação se conecta apenas a 2 ou 3 outras no máximo).

**Referência bibliográfica:**
> CORMEN, T. H. et al. Algoritmos: teoria e prática. 3. ed. Rio de Janeiro: Elsevier, 2012.

---

### 1.2 Algoritmo Adicional *(se houver)*

| Campo | Resposta |
|-------|----------|
| Nome do algoritmo | Heurística do Vizinho Mais Próximo |
| Categoria | Heurística / Algoritmo Guloso |
| Complexidade de tempo | $O(V^2)$ (no pior caso por iteração) |
| Complexidade de espaço | $O(V)$ |

**Justificativa:**
Este algoritmo complementa o projeto para resolver a dor principal do usuário: o roteamento de múltiplas entregas (uma variação do Problema do Caixeiro Viajante - TSP). Usar força bruta para calcular todas as combinações de rotas paralisaria o sistema. A heurística iterativa (que aciona o Dijkstra a cada passo para encontrar a próxima parada mais próxima) fornece uma solução altamente otimizada em frações de segundo, ideal para a experiência do usuário no terminal.

**Referência bibliográfica:**
> GAREY, M. R.; JOHNSON, D. S. Computers and Intractability: A Guide to the Theory of NP-Completeness. New York: W. H. Freeman and Company, 1979.

---

## 2. Arquitetura em Camadas

> ![Diagrama de arquitetura](./docs/arquitetura_e2.png)
> *(Lembre-se de salvar um print genérico ou esquema simples de blocos na pasta docs com este nome).*

### Descrição das camadas

| Camada | Responsabilidade | Artefatos principais |
|--------|-----------------|----------------------|
| Apresentação (UI/CLI) | Interação direta com o vendedor logístico via terminal de linha de comando. Coleta origens e destinos. | `main.py` (Módulo CLI) |
| Aplicação (Service) | Orquestra as regras de negócio: valida se as estações existem no mapa e aciona o motor de rotas. | `orquestrador.py` |
| Domínio (Core) | Contém as estruturas de dados puras (Grafo em listas de adjacência) e executa a lógica matemática (Dijkstra/TSP). | `grafos.py` |
| Infraestrutura (I/O) | Responsável por ler o arquivo da malha do metrô do disco e carregá-lo para a memória. | `leitor_json.py`, `grafo_sp.json` |

---

## 3. Estrutura de Diretórios

```text
expresso-catraca/
├── docs/
│   ├── README.md
│   ├── E1_template.md
│   ├── E2_template.md
│   └── arquitetura_e2.png
├── src/
│   ├── core/
│   │   └── grafos.py         # Lógica do Dijkstra e Caixeiro Viajante
│   ├── application/
│   │   └── orquestrador.py   # Validação e orquestração
│   ├── io/
│   │   └── file_reader.py    # Leitura do dataset
│   └── main.py               # Interface Interativa de Terminal (CLI)
├── tests/
│   ├── test_grafos.py
│   └── test_leitura.py
├── data/
│   └── grafo_sp.json         # Dataset com a malha do metrô
└── requirements.txt