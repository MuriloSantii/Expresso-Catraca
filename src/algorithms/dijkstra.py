# src/algorithms/dijkstra.py
import heapq

def calcular_rota_mais_rapida(grafo_obj, origem, destino):
    """
    Calcula o caminho mais rápido usando Dijkstra.
    Complexidade de Tempo: O(E log V)
    Complexidade de Espaço: O(V)
    """
    
    if origem not in grafo_obj.adjacencias:
        return float('infinity'), []

    
    tempos = {estacao: float('infinity') for estacao in grafo_obj.adjacencias}
    tempos[origem] = 0 
    
    
    estacao_anterior = {estacao: None for estacao in grafo_obj.adjacencias}
    
    fila = [(0, origem)]
    
    
    while fila:
        tempo_atual, estacao_atual = heapq.heappop(fila)
        
        if estacao_atual == destino:
            break
            
        
        vizinhos = grafo_obj.consultar_adjacencia(estacao_atual)
        
        for vizinho, tempo_viagem in vizinhos.items():
            tempo_total = tempo_atual + tempo_viagem
            
            if tempo_total < tempos.get(vizinho, float('infinity')):
                tempos[vizinho] = tempo_total
                estacao_anterior[vizinho] = estacao_atual
                heapq.heappush(fila, (tempo_total, vizinho))
                
    
    if tempos.get(destino, float('infinity')) == float('infinity'):
         return float('infinity'), []
         
    
    rota = []
    estacao_trilha = destino
    while estacao_trilha is not None:
        rota.insert(0, estacao_trilha) 
        estacao_trilha = estacao_anterior.get(estacao_trilha)
        
    return tempos[destino], rota