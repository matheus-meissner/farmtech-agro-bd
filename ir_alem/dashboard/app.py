import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="FarmTech Solutions – Dashboard de Irrigação", layout="wide")

# 1. descobrir onde está a raiz do projeto (sobe 2 pastas: ir_alem/dashboard -> ir_alem -> raiz)
BASE_DIR = Path(__file__).resolve().parents[2]
csv_path = BASE_DIR / "banco" / "Sensores_Fazenda.csv"

# 2. tentar ler o CSV
def carregar_csv(caminho: Path) -> pd.DataFrame:
    # tenta com vírgula
    try:
        df = pd.read_csv(caminho)
    except Exception:
        # tenta com ;
        df = pd.read_csv(caminho, sep=";")
    return df

df = carregar_csv(csv_path)

# 3. normalizar nomes das colunas
#    - tira espaços
#    - deixa tudo maiúsculo
df.columns = [col.strip().upper() for col in df.columns]

# 4. checar se as colunas que a gente precisa existem
colunas_esperadas = ["UMID", "PH", "N", "P", "K", "CHUVA", "BOMBA", "TEMPERATURA"]
faltando = [c for c in colunas_esperadas if c not in df.columns]

if faltando:
    st.error(f"As seguintes colunas não foram encontradas no CSV: {', '.join(faltando)}")
    st.write("Colunas encontradas no arquivo:", list(df.columns))
    st.stop()

# 5. ordenar por alguma coisa se quiser (não é obrigatório)
# se não tiver timestamp, vamos só pegar a última linha
ultima = df.tail(1).iloc[0]

# 6. título
st.title("🌱 FarmTech Solutions – Dashboard de Irrigação")
st.caption("Dados coletados na Fase 2 (simulação no Wokwi) e carregados no Oracle.")

# 7. métricas principais
col1, col2, col3, col4 = st.columns(4)

col1.metric("Umidade (%)", f"{ultima['UMID']:.1f}")
col2.metric("pH (simulado)", f"{ultima['PH']:.2f}")
col3.metric("Chuva", "Sim" if str(ultima["CHUVA"]).lower() == "true" else "Não")
col4.metric("Bomba", "Ligada 💧" if str(ultima["BOMBA"]).lower() == "true" else "Desligada ⛔")

st.divider()

# 8. gráficos / tabela
left, right = st.columns([2, 1])

with left:
    st.subheader("Histórico de umidade")
    st.line_chart(df["UMID"])

with right:
    st.subheader("Registros brutos")
    st.dataframe(df)

st.caption(f"📁 Arquivo usado: `{csv_path}`")
