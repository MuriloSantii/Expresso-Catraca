# src/main.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.io.leitor_json import carregar_grafo_do_json
from src.algorithms.dijkstra import calcular_rota_mais_rapida

def main():
    print("\n" + "="*50)
    print("🚆 EXPRESSO CATRACA - INICIALIZANDO MVP 🚆")
    print("="*50)

    # 1. Camada I/O: Carrega os dados do mapa a partir do JSON
    caminho_dados = os.path.join('data', 'grafo_sp.json')
    print(f"📂 Carregando mapa de: {caminho_dados}...")
    
    mapa_metro = carregar_grafo_do_json(caminho_dados)
    
    if not mapa_metro:
         print("❌ Falha ao carregar o mapa. Verifique se o arquivo existe.")
         return
         
    print("✅ Mapa carregado na memória com sucesso!\n")

    # 2. Tela de Entrada (UI/CLI)
    print("--- NOVA ROTA ---")
    origem = input("📍 Digite a estação de origem (ex: Sé): ").strip()
    destino = input("🎯 Digite a estação de destino (ex: Luz): ").strip()

    print("\n⚙️  Calculando a rota mais rápida...\n")

    # 3. Camada Core/Algorithms: Executa o Dijkstra
    tempo, rota = calcular_rota_mais_rapida(mapa_metro, origem, destino)

    # 4. Tela de Resultado (UI/CLI)
    if tempo == float('infinity'):
        print("❌ Não foi possível encontrar uma rota. Verifique o nome das estações.")
    else:
        print(f"==========================================")
        print(f"📦 EXPRESSO CATRACA - RECIBO DE ROTA 📦")
        print(f"==========================================")
        print(f"📍 Origem:  {origem}")
        print(f"🎯 Destino: {destino}")
        print(f"⏱️ Tempo Estimado: {tempo} minutos")
        print(f"🛤️ Trajeto: {' -> '.join(rota)}")
        print(f"==========================================\n")


if __name__ == "__main__":
    main()