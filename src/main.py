import streamlit as st
import sys
import os

# Ajuste para o Python achar as suas pastas (core, io, algorithms)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa as funções com os nomes exatos que você criou
from src.io.leitor_json import carregar_grafo_do_json
from src.algorithms.dijkstra import calcular_rota_mais_rapida

# 1. Configuração da página Web
st.set_page_config(page_title="Expresso Catraca", page_icon="🚆", layout="centered")

# 2. Título e cabeçalho
st.title("🚆 Expresso Catraca")
st.markdown("Encontre a rota mais rápida na malha metroviária de São Paulo.")
st.divider()

# 3. Carregar o Grafo (O cache evita ler o JSON toda vez que clica num botão)
@st.cache_data
def carregar_dados():
    caminho_arquivo = os.path.join(os.path.dirname(__file__), '..', 'data', 'grafo_sp.json')
    grafo = carregar_grafo_do_json(caminho_arquivo)
    return grafo

grafo_obj = carregar_dados()

# Pegar a lista de todas as estações em ordem alfabética para o menu
lista_estacoes = sorted(list(grafo_obj.adjacencias.keys()))

# 4. Construção da Interface (Menus de seleção)
col1, col2 = st.columns(2)

with col1:
    origem = st.selectbox("📍 Estação de Origem:", lista_estacoes)

with col2:
    destino = st.selectbox("🎯 Estação de Destino:", lista_estacoes)

st.write("") # Espaçamento

# 5. O Botão Mágico
if st.button("Calcular Rota Mais Rápida 🚀", use_container_width=True):
    if origem == destino:
        st.warning("Você já está na estação de destino! Escolha uma rota diferente.")
    else:
        with st.spinner("Calculando a melhor rota..."):
            # Chama a SUA função com o nome certinho!
            tempo, trajeto = calcular_rota_mais_rapida(grafo_obj, origem, destino)
            
            if tempo == float('infinity'):
                st.error("Não foi possível encontrar uma rota entre essas estações.")
            else:
                st.success(f"**Tempo Estimado:** {tempo} minutos")
                st.info(f"**Trajeto:** {' ➔ '.join(trajeto)}")
                