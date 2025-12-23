import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# TITLE
# =========================
st.title("🌐 Lipweb")

# =========================
# HEADER & SUBHEADER
# =========================
st.header("Dashboard Informasi")
st.subheader("Contoh Web Page Menggunakan Streamlit")

# =========================
# TEXT / PARAGRAPH
# =========================
st.text(
    "Lipweb adalah contoh web sederhana yang dibuat\n"
    "menggunakan Streamlit. Web ini menampilkan\n"
    "berbagai komponen dasar seperti teks, kode,\n"
    "tabel data, dan grafik interaktif."
)

# =========================
# CAPTION
# =========================
st.caption("Lipweb – Contoh dashboard Streamlit untuk pembelajaran")

# =========================
# CODE (Potongan Kode)
# =========================
st.subheader("Contoh Potongan Kode Python")
st.code("""
import streamlit as st

st.title("Lipweb")
st.write("Web sederhana menggunakan Streamlit")
""", language="python")

# =========================
# DATA DISPLAY (TABEL)
# =========================
st.header("Data Nilai Mahasiswa")

data = {
    "Nama": ["Andi", "Budi", "Citra", "Dewi"],
    "Mata Kuliah": ["Elektronika", "Pemrograman", "Sistem Digital", "Robotika"],
    "Nilai": [85, 90, 78, 88]
}

df = pd.DataFrame(data)

st.subheader("Tabel Data")
st.dataframe(df)

# =========================
# DATA DISPLAY (CHART)
# =========================
st.header("Grafik Nilai Mahasiswa")

fig = px.bar(
    df,
    x="Nama",
    y="Nilai",
    color="Mata Kuliah",
    title="Grafik Nilai Mahasiswa"
)

st.plotly_chart(fig, use_container_width=True)
