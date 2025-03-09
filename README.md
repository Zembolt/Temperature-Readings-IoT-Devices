# Temperature-Readings-IoT-Devices
estudos para analisar diferentes temperaturas ao dia
# Pipeline - IOT

## Descrição do Projeto
Este projeto implementa um pipeline de dados para processar e armazenar leituras de temperatura de dispositivos IoT em um banco de dados PostgreSQL, utilizando Docker. A solução também inclui um dashboard interativo criado com Streamlit, que visualiza insights como a média de temperatura por dispositivo, leituras por hora e temperaturas máximas e mínimas por dia.

O fluxo de trabalho do projeto envolve:
- Processar um arquivo CSV (`IOT-temp.csv`) com leituras de temperatura de dispositivos IoT.
- Armazenar os dados em um banco de dados PostgreSQL usando SQLAlchemy.
- Criar visualizações dinâmicas dos dados via Streamlit.

---

## Como Configurar o Ambiente

### Pré-requisitos:
- Python 3.8
- Docker
- Conta no GitHub e Kaggle

### Passos para configurar o ambiente:

1. Clone o repositório:
    ```bash
    git clone https://github.com/DOliveiira/pipeline-IOT
    cd repositorio
    ```

2. Crie e ative um ambiente virtual Python:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate      # Windows
    ```

3. Instale as dependências necessárias:
    ```bash
    pip install pandas psycopg2-binary sqlalchemy streamlit plotly
    ```

4. Configure o banco de dados PostgreSQL com Docker:

    Inicie o contêiner PostgreSQL:
    ```bash
    docker run --name postgres-iot -e POSTGRES_PASSWORD=sua_senha -p 5432:5432 -d postgres
    ```

5. Carregue os dados CSV para o banco de dados:

    Execute o script de processamento:
    ```bash
    python pipeline.py
    ```

6. Execute o dashboard Streamlit:
    ```bash
    streamlit run dashboard.py
    ```

---

## Explicação das Views SQL

### 1. `avg_temp_por_Min_Max `
- **Descrição**: Esta view calcula a média de temperatura.
- **Insight**: Permite identificar quais dias estão reportando temperaturas consistentemente mais altas ou mais baixas.
    ```sql
   CREATE TABLE temperature_readings (
    id TEXT PRIMARY KEY,
    room_id TEXT NOT NULL,
    noted_date TIMESTAMP NOT NULL,
    temp INTEGER NOT NULL,
    location TEXT CHECK (location IN ('In', 'Out'))
);
    

## Capturas de Tela do Dashboard
Grafico em colunas
![image](https://github.com/user-attachments/assets/e31298b0-3757-491d-b018-3ac62376891d)

Grafico em Linha
![image](https://github.com/user-attachments/assets/34b86a24-26b3-4aca-b56b-5287af9014fe)

Grafico por Diperção
![image](https://github.com/user-attachments/assets/b53cd58d-8d83-4775-9501-1048e633063a)

---
Postgres Data base
![image](https://github.com/user-attachments/assets/a8a7e88e-c18e-4462-aea5-41298fb4d8bc)

![image](https://github.com/user-attachments/assets/d2668ecb-0fae-4848-8c3f-85b8f3ecfc03)

![image](https://github.com/user-attachments/assets/a14982f0-3001-472b-a7ac-26c45e196844)

SQL Editor
![image](https://github.com/user-attachments/assets/cde64a73-ad01-4e17-8fed-e00e81d14919)

----
Capturas de Telas Docker 

![image](https://github.com/user-attachments/assets/96abcd5a-6590-4d90-b66f-75d2989f0655)



