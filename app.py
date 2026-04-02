import streamlit as st
import pandas as pd
from datetime import datetime

# Configuração da Página
st.title("Controle de Presença - E.E. Prof. Anísio Carneiro") [cite: 9, 17]
st.subheader("Captura de QR Code e Busca Ativa") [cite: 43]

# Carregar Banco de Dados
df = pd.read_csv("alunos.csv")

# Interface de Captura
input_id = st.text_input("Aponte o leitor ou digite o ID do Aluno:")

if st.button("Registrar Presença"):
    if input_id:
        # Lógica de Processamento: Encontra o aluno e atualiza data
        agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        idx = df.index[df['ID'] == int(input_id)]
        
        if not idx.empty:
            df.at[idx[0], 'Ultima_Presenca'] = agora
            df.at[idx[0], 'Faltas'] = 0  # Zera faltas ao aparecer
            df.to_csv("alunos.csv", index=False)
            st.success(f"Presença confirmada para: {df.at[idx[0], 'Nome']}")
        else:
            st.error("Aluno não encontrado.")

# Seção de Busca Ativa (Análise de Dados)
st.divider()
st.write("### Alunos com Alerta de Busca Ativa (2+ Faltas)") [cite: 9]
alertas = df[df['Faltas'] >= 2]
st.table(alertas[['Nome', 'Faltas', 'Contato_Responsavel']])