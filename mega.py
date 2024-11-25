import streamlit as st
import random

# Configuração da página
st.set_page_config(page_title="Gerar Números", layout="centered")

# Título
st.title("Gerar Números")

# Entrada: quantidade de listas
quantidade_listas = st.number_input(
    "Quantas listas você deseja gerar?", 
    min_value=1, 
    max_value=100, 
    value=1, 
    step=1
)

# Botão para gerar os números
if st.button("Gerar Listas"):
    st.subheader("Listas Geradas:")
    
    # Gerar as listas
    for i in range(quantidade_listas):
        numeros = random.sample(range(1, 61), 6)  # Gera 6 números únicos entre 1 e 60
        st.write(f"Lista {i+1}: {sorted(numeros)}") # Ordena a lista
st.write('Se Deus é por nois, quem será contra nois?')


