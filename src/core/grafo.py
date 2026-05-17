# src/core/grafo.py

class Grafo:
    def __init__(self):
        
        self.adjacencias = {}

    def adicionar_vertice(self, vertice):
        """Adiciona uma nova estação ao mapa, se ela ainda não existir."""
        if vertice not in self.adjacencias:
            self.adjacencias[vertice] = {}

    def adicionar_aresta(self, origem, destino, peso):
        """Cria uma conexão (trilho) entre duas estações com o tempo de viagem (peso)."""
    
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        
        self.adjacencias[origem][destino] = peso

    def consultar_adjacencia(self, vertice):
        """Retorna todos os vizinhos de uma estação e o tempo até eles."""
        return self.adjacencias.get(vertice, {})