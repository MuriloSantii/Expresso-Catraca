# tests/test_algoritmos.py
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.grafo import Grafo
from src.algorithms.dijkstra import calcular_rota_mais_rapida

def test_caso_base():
    """Testa um caminho simples onde A -> B -> C é mais rápido que A -> C direto."""
    grafo = Grafo()
    grafo.adicionar_aresta('A', 'B', 2)
    grafo.adicionar_aresta('B', 'C', 3)
    grafo.adicionar_aresta('A', 'C', 10)
    
    tempo, rota = calcular_rota_mais_rapida(grafo, 'A', 'C')
    
    assert tempo == 5
    assert rota == ['A', 'B', 'C']

def test_grafo_vazio():
    """Testa como o sistema reage se pedirmos uma rota de uma estação que não existe."""
    grafo = Grafo()
    tempo, rota = calcular_rota_mais_rapida(grafo, 'Sé', 'Luz')
    
    assert tempo == float('infinity')
    assert rota == []

def test_grafo_completo():
    """Testa um mapa onde todo mundo tem um trilho direto para todo mundo."""
    grafo = Grafo()
    grafo.adicionar_aresta('A', 'B', 1)
    grafo.adicionar_aresta('A', 'C', 1)
    grafo.adicionar_aresta('B', 'C', 1)
    
    tempo, rota = calcular_rota_mais_rapida(grafo, 'A', 'C')
    
    assert tempo == 1
    assert rota == ['A', 'C']