# src/io/leitor_json.py
import json
from src.core.grafo import Grafo

def carregar_grafo_do_json(caminho_arquivo):
    """Abre o arquivo JSON e transforma os dados em um objeto da classe Grafo."""
    grafo_sp = Grafo()
    
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            
            
            for origem, destinos in dados.items():
                grafo_sp.adicionar_vertice(origem)
                for destino, peso in destinos.items():
                    grafo_sp.adicionar_aresta(origem, destino, peso)
                    
        return grafo_sp
    
    except FileNotFoundError:
        print(f"❌ Erro: O arquivo {caminho_arquivo} não foi encontrado.")
        return None