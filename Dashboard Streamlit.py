Dashboard Streamlit 
----
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Configuração do banco de dados
DB_URL = "postgresql+pg8000://postgres:sua_senha@localhost:5432/postgres"
engine = create_engine(DB_URL)

st.title("Dashboard de Temperaturas IoT")

# Média de temperatura por dispositivo
st.subheader("Média de Temperatura por Dispositivo")
query = "SELECT device_id, AVG(temperature) AS avg_temp FROM temperature_data GROUP BY device_id;"
df = pd.read_sql(query, engine)
st.bar_chart(df.set_index("device_id"))

# Leituras por hora
st.subheader("Leituras por Hora")
query = "SELECT DATE_TRUNC('hour', timestamp) AS hora, COUNT(*) AS contagem FROM temperature_data GROUP BY hora;"
df = pd.read_sql(query, engine)
st.line_chart(df.set_index("hora"))

# Temperaturas máximas e mínimas por dia
st.subheader("Temperaturas Máximas e Mínimas por Dia")
query = "SELECT DATE(timestamp) AS data, MAX(temperature) AS temp_max, MIN(temperature) AS temp_min FROM temperature_data GROUP BY data;"
df = pd.read_sql(query, engine)
st.area_chart(df.set_index("data"))
