
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Panel de Trading Colombia", layout="wide")

st.title("🎯 Mi Panel de Control de Señales")
st.write("Datos actualizados desde Google Colab")

# Intentar leer el archivo de señales que ya tienes en GitHub
try:
    # Leemos la hoja de señales de tu archivo Excel
    df = pd.read_excel("estrategia_reversion_a_media_resultados.xlsx", sheet_name="Señales_Continuidad")

    st.subheader("🚀 Últimas Señales Detectadas")
    st.dataframe(df.style.highlight_max(axis=0, color='#2e7d32')) # Resalta datos importantes

except Exception as e:
    st.error(f"Todavía no puedo leer el archivo Excel: {e}")
    st.info("Asegúrate de que el nombre del archivo sea exacto.")
