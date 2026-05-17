
grafo_sp = {
    'Sé': {'Liberdade': 2, 'São Bento': 2, 'Anhangabaú': 2, 'Brás': 5},
    'Liberdade': {'Sé': 2},
    'São Bento': {'Sé': 2, 'Luz': 3},
    'Anhangabaú': {'Sé': 2, 'República': 2},
    'República': {'Anhangabaú': 2, 'Luz': 3},
    'Luz': {'São Bento': 3, 'República': 3, 'Brás': 4},
    # Expandindo para a Linha 11-Coral (tempos aproximados)
    'Brás': {'Sé': 5, 'Luz': 4, 'Tatuapé': 6},
    'Tatuapé': {'Brás': 6, 'Braz Cubas': 45}, 
    'Braz Cubas': {'Tatuapé': 45, 'Estudantes': 5},
    'Estudantes': {'Braz Cubas': 5}
}


estacao_atual = 'Sé'

print(f"--- Você está na estação {estacao_atual} ---")
print("Opções de viagem direta:")

for estacao_vizinha, tempo in grafo_sp[estacao_atual].items():
  import heapq 


grafo_sp = {
    'Sé': {'Liberdade': 2, 'São Bento': 2, 'Anhangabaú': 2},
    'Liberdade': {'Sé': 2},
    'São Bento': {'Sé': 2, 'Luz': 3},
    'Anhangabaú': {'Sé': 2, 'República': 2},
    'República': {'Anhangabaú': 2, 'Luz': 3},
    'Luz': {'São Bento': 3, 'República': 3}
}


def calcular_rota_mais_rapida(grafo, origem, destino):
    
    tempos = {estacao: float('infinity') for estacao in grafo}
    tempos[origem] = 0 
    
    
    estacao_anterior = {estacao: None for estacao in grafo}
    
   
    fila = [(0, origem)]
    
    while fila:
        tempo_atual, estacao_atual = heapq.heappop(fila)
        
       
        if estacao_atual == destino:
            break
            
        
        for vizinho, tempo_viagem in grafo[estacao_atual].items():
            tempo_total = tempo_atual + tempo_viagem
            
            
            if tempo_total < tempos[vizinho]:
                tempos[vizinho] = tempo_total
                estacao_anterior[vizinho] = estacao_atual
                heapq.heappush(fila, (tempo_total, vizinho))
                
   
    rota = []
    estacao_trilha = destino
    while estacao_trilha is not None:
        rota.insert(0, estacao_trilha) 
        estacao_trilha = estacao_anterior[estacao_trilha]
        
    return tempos[destino], rota


partida = 'Liberdade'
chegada = 'Luz'

tempo_final, caminho_final = calcular_rota_mais_rapida(grafo_sp, partida, chegada)

#print(f"\n--- ROTEAMENTO EXPRESSO CATRACA ---")#
#print(f"Origem: {partida}")#
#print(f"Destino: {chegada}")#
#print(f"Tempo total estimado: {tempo_final} minutos")#
#print(f"Rota a seguir: {' -> '.join(caminho_final)}\n")#


def roteamento_multiplas_paradas(grafo, origem, destinos):
    estacao_atual = origem
    entregas_pendentes = destinos.copy() 
    
    tempo_total_jornada = 0
    ordem_de_visita = []
    rota_completa = [origem] 
    
    # Enquanto houver pacotes para entregar na lista...
    while entregas_pendentes:
        melhor_tempo = float('infinity')
        proxima_parada = None
        caminho_ate_proxima = []
        
        
        for destino_candidato in entregas_pendentes:
            tempo, caminho = calcular_rota_mais_rapida(grafo, estacao_atual, destino_candidato)
            
            
            if tempo < melhor_tempo:
                melhor_tempo = tempo
                proxima_parada = destino_candidato
                caminho_ate_proxima = caminho
                
        
        tempo_total_jornada += melhor_tempo
        ordem_de_visita.append(proxima_parada)
        
        
        rota_completa.extend(caminho_ate_proxima[1:])
        
        
        estacao_atual = proxima_parada
        
        
        entregas_pendentes.remove(proxima_parada)
        
    return tempo_total_jornada, ordem_de_visita, rota_completa


print("\n" + "="*50)
print("🚆 BEM-VINDO AO EXPRESSO CATRACA 🚆")
print("="*50)


while True:
    partida_vendedor = input("📍 Digite a sua estação de partida: ").strip()
    if partida_vendedor in grafo_sp:
        break
    print("❌ Estação não encontrada no mapa. Tente novamente (ex: Sé, Luz, Braz Cubas).")


while True:
    try:
        qtd_entregas = int(input("\n📦 Quantas entregas você fará hoje? "))
        if qtd_entregas > 0:
            break
        print("❌ Digite um número maior que zero.")
    except ValueError:
        print("❌ Por favor, digite apenas números inteiros.")


lista_entregas = []
for i in range(qtd_entregas):
    while True:
        destino = input(f"🎯 Digite a estação da entrega {i+1}: ").strip()
        if destino in grafo_sp:
            if destino == partida_vendedor or destino in lista_entregas:
                 print("❌ Você já está nessa estação ou já adicionou ela na lista.")
            else:
                 lista_entregas.append(destino)
                 break
        else:
            print("❌ Estação não encontrada. Tente novamente.")


print("\n⚙️  Calculando a rota mais otimizada... aguarde.")

tempo_final, ordem, trajeto = roteamento_multiplas_paradas(grafo_sp, partida_vendedor, lista_entregas)


print(f"\n==========================================")
print(f"📦 EXPRESSO CATRACA - ROTA DE ENTREGAS 📦")
print(f"==========================================")
print(f"📍 Ponto de Partida: {partida_vendedor}")
print(f"🎯 Entregas a fazer: {', '.join(lista_entregas)}\n")
print(f"✅ Ordem ideal calculada: {' -> '.join(ordem)}")
print(f"⏱️ Tempo total da jornada: {tempo_final} minutos")
print(f"🛤️ Trajeto passo a passo: {' -> '.join(trajeto)}")
print(f"==========================================\n")