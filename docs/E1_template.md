# E1 — Proposta e Definição do Projeto

> **Disciplina:** Teoria dos Grafos  
> **Prazo:** 19 de março de 2026  
> **Peso:** 10% da nota final  

---

## Identificação do Grupo

| Campo | Preenchimento |
|-------|---------------|
| Nome do projeto | Expresso Catraca |
| Integrante 1 | Guilherme da Macena Andrade — 38093057 |
| Integrante 2 | Murilo Santiago de Carvalho — 37616391 |
| Integrante 3 | Pedro Henrique Nepomoceno dos Santos — 38537958 |

---

## 1. Contexto e Motivação

Em grandes centros urbanos, vendedores e entregadores que utilizam o transporte público precisam visitar vários pontos da cidade ao longo do dia. No caso do metrô, apesar de existir uma malha organizada de estações e linhas, escolher manualmente a melhor sequência de paradas pode ser difícil, principalmente quando há várias entregas em regiões diferentes. Uma escolha ruim pode aumentar o tempo de deslocamento, gerar atrasos e reduzir a produtividade do profissional.

Esse problema é relevante porque a malha do metrô possui conexões, baldeações e tempos diferentes entre estações. Além disso, trocar de linha pode acrescentar alguns minutos ao percurso, o que influencia diretamente na escolha da melhor rota. Por isso, apenas cadastrar estações em listas ou tabelas não é suficiente para resolver o problema de forma eficiente. É necessário representar as relações entre estações e calcular caminhos considerando custos.

A Teoria dos Grafos permite modelar esse cenário de maneira natural. Cada estação ou ponto de uma linha pode ser representado como um vértice, enquanto os trilhos e conexões entre estações podem ser representados como arestas. Os pesos das arestas indicam o tempo estimado de deslocamento. Assim, o sistema pode aplicar algoritmos de caminho mínimo e heurísticas de roteirização para sugerir uma ordem de entrega mais eficiente.

---

## 2. Objetivo Geral

O sistema deve calcular uma rota eficiente para um vendedor realizar várias entregas usando a malha do metrô, indicando a melhor ordem das paradas e o tempo total estimado de deslocamento.

---

## 3. Objetivos Específicos

- [ ] Modelar a malha do metrô como um grafo, representando estações como vértices e conexões como arestas.
- [ ] Implementar o Algoritmo de Dijkstra para calcular o menor tempo de deslocamento entre duas estações.
- [ ] Considerar pesos nas arestas, como tempo entre estações e tempo adicional de baldeação.
- [ ] Implementar uma heurística, como o Vizinho Mais Próximo, para definir a ordem das entregas.
- [ ] Exibir no terminal a sequência sugerida de estações, os caminhos calculados e o tempo total estimado.

---

## 4. Público-Alvo / Caso de Uso Principal

O sistema seria utilizado por um vendedor ou entregador que precisa realizar várias entregas em locais próximos a estações de metrô. Por exemplo, um vendedor inicia o dia na estação Luz e precisa passar por cinco ou seis estações diferentes para realizar entregas. Em vez de decidir manualmente a ordem das visitas, ele informa as estações no sistema, que calcula uma sequência eficiente de paradas e mostra o tempo total estimado para o trajeto.

---

## 5. Justificativa Técnica — Por que Grafos?

A modelagem em grafos é adequada porque a malha do metrô já possui uma estrutura de rede. As estações representam os vértices, e as ligações entre estações representam as arestas. Como o deslocamento entre duas estações possui um tempo estimado, o grafo será ponderado, permitindo que os algoritmos considerem o custo de cada trecho.

Além disso, o problema envolve encontrar caminhos mínimos entre estações e organizar múltiplas paradas de entrega. Para o cálculo do menor caminho entre dois pontos, será utilizado o Algoritmo de Dijkstra, que pertence à categoria de algoritmos gulosos de caminho mínimo em grafos ponderados. Para definir a ordem das entregas, será usada uma heurística relacionada ao Problema do Caixeiro Viajante, como o Vizinho Mais Próximo.

A representação por lista de adjacência é uma boa escolha porque a malha do metrô não é um grafo completo; cada estação se conecta apenas a algumas estações vizinhas. Dessa forma, a lista de adjacência economiza espaço e facilita a execução dos algoritmos. A complexidade de tempo do Dijkstra, usando fila de prioridade, é O((V + E) log V), em que V representa o número de vértices e E o número de arestas. A complexidade de espaço da representação é O(V + E).

---

## 6. Tipo de Grafo

| Característica | Escolha | Justificativa breve |
|----------------|---------|---------------------|
| Dirigido ou não-dirigido | Não-dirigido | Em geral, o metrô permite deslocamento nos dois sentidos entre estações conectadas. |
| Ponderado ou não-ponderado | Ponderado | Cada aresta terá um peso representando o tempo estimado em minutos entre estações ou em baldeações. |
| Conectado / bipartido / geral | Conectado e geral | A malha principal do metrô permite alcançar diferentes estações por meio de conexões, mas não segue uma estrutura bipartida. |
| Representação interna pretendida | Lista de adjacência | É mais eficiente para uma malha onde cada estação se conecta a poucas estações vizinhas. |

---

## 7. Diagrama Conceitual

```text
                 [Luz - Azul]
                      |
                  3 min
                      |
                 [Sé - Azul]
                      |
        Baldeação: 4 min
                      |
              [Sé - Vermelha]
                /           \
            5 min           6 min
              /               \
     [República]          [Brás]
          |
        7 min
          |
     [Pinheiros]
```

**Legenda:** Cada estação ou estação-linha é representada por um vértice. As conexões entre estações são arestas ponderadas pelo tempo médio de deslocamento. A baldeação é representada como uma aresta especial com peso adicional, simulando o tempo gasto para trocar de linha.

---

## Checklist de Entrega

Antes de submeter, confirme:

- [x] Texto entre 300 e 600 palavras (seções 1 a 5)
- [ ] Todos os campos da tabela de identificação preenchidos
- [x] Tipo de grafo especificado com justificativa
- [x] Diagrama presente e referenciado no texto
- [ ] Arquivo nomeado como `E1_NomeGrupo_Grafos.docx` (versão Word) ou PR aberto (versão GitHub)

---

*Teoria dos Grafos — Profa. Dra. Andréa Ono Sakai*

