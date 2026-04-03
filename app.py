import streamlit as st
import pandas as pd
from streamlit_qrcode_scanner import qrcode_scanner

st.set_page_config(page_title="Sistema Anísio Carneiro", layout="wide")

st.title("🛡️ Controle de Presença Inteligente")
st.write("Aponte o crachá do aluno para a câmera")

# 1. Carregar o banco de dados que você já criou
try:
    df = pd.read_csv("alunos.csv")
except:
    st.error("Erro ao carregar alunos.csv. Verifique o arquivo no GitHub.")
    st.stop()

# 2. Componente de Leitura de QR Code
# Isso abrirá a câmera do seu tablet automaticamente
codigo_lido = qrcode_scanner(key='scanner')

if codigo_lido:
    st.audio("https://www.soundjay.com/buttons/beep-07a.mp3") # Feedback sonoro opcional
    
    # Converte o código lido para número (ID)
    try:
        id_aluno = int(codigo_lido)
        
        # 3. Processamento: Busca na lista
        if id_aluno in df['id'].values:
            nome_aluno = df.loc[df['id'] == id_aluno, 'nome'].values[0]
            st.success(f"✅ PRESENÇA REGISTRADA: {nome_aluno} (ID: {id_aluno})")
            
            # Aqui você poderia atualizar o CSV, mas para a DEMO, 
            # apenas mostrar que o sistema RECONHECEU o aluno já prova o conceito.
        else:
            st.warning(f"⚠️ ID {id_aluno} lido, mas não encontrado na lista de alunos.")
    except:
        st.error("Erro ao processar o código lido. Verifique se o QR Code contém apenas o número do ID.")

# 4. Análise de Dados (Demonstração da Busca Ativa)
st.divider()
st.subheader("📊 Painel de Controle - Busca Ativa")
st.write("Alunos com 2 ou mais faltas (Atenção prioritária):")

# Filtra e mostra quem precisa de atenção (quem tem faltas >= 2 no CSV)
lista_alerta = df[df['faltas'] >= 2]
st.warning(f"Existem {len(lista_alerta)} alunos em situação crítica.")
st.table(lista_alerta[['nome', 'email_responsavel', 'faltas']])