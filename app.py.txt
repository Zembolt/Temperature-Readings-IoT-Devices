import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(
    page_title="Meu Aplicativo Streamlit",
    page_icon="📊",
    layout="wide"
)

# Título e descrição
st.title("Meu Aplicativo Streamlit de Exemplo")
st.markdown("Este é um exemplo básico de um aplicativo Streamlit rodando em Docker.")

# Sidebar
st.sidebar.header("Configurações")
num_points = st.sidebar.slider("Número de pontos", 10, 1000, 100)
chart_type = st.sidebar.selectbox("Tipo de gráfico", ["Linha", "Dispersão", "Histograma"])

# Gerando dados aleatórios
def generate_data(n):
    dates = pd.date_range(start="2024-01-01", periods=n)
    values = np.cumsum(np.random.randn(n))
    df = pd.DataFrame({"Data": dates, "Valor": values})
    return df

data = generate_data(num_points)

# Exibindo os dados
st.subheader("Dados Gerados")
st.dataframe(data)

# Download dos dados
csv = data.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download dos dados como CSV",
    data=csv,
    file_name="dados.csv",
    mime="text/csv"
)

# Visualização dos dados
st.subheader("Visualização dos Dados")
col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(10, 6))
    
    if chart_type == "Linha":
        ax.plot(data["Data"], data["Valor"])
        st.write("Gráfico de Linha")
    elif chart_type == "Dispersão":
        ax.scatter(data["Data"], data["Valor"])
        st.write("Gráfico de Dispersão")
    else:
        ax.hist(data["Valor"], bins=20)
        st.write("Histograma")
    
    ax.set_xlabel("Data")
    ax.set_ylabel("Valor")
    ax.grid(True)
    fig.autofmt_xdate()
    
    st.pyplot(fig)

with col2:
    st.subheader("Estatísticas")
    st.write({
        "Média": data["Valor"].mean(),
        "Mediana": data["Valor"].median(),
        "Desvio Padrão": data["Valor"].std(),
        "Mínimo": data["Valor"].min(),
        "Máximo": data["Valor"].max()
    })
    
    st.subheader("Valores Recentes")
    st.dataframe(data.tail(5))

# Widget interativo
st.subheader("Adicionar Novo Ponto")
new_value = st.number_input("Novo valor:", value=0.0, step=0.1)

if st.button("Adicionar"):
    new_data = pd.DataFrame({
        "Data": [pd.Timestamp.now()],
        "Valor": [new_value]
    })
    st.session_state.data = pd.concat([data, new_data]) if "data" in st.session_state else new_data
    st.success("Valor adicionado com sucesso!")
    if "data" in st.session_state:
        st.write("Último ponto adicionado:")
        st.dataframe(st.session_state.data.tail(1))
