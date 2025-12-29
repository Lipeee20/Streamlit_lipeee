import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import pytz
import os
from streamlit_autorefresh import st_autorefresh

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="LipWeb Dashboard",
    page_icon="📊",
    layout="wide"
)

# =========================
# AUTO REFRESH (JAM)
# =========================
st_autorefresh(interval=1000, key="clock")  # 1 detik

# =========================
# SIDEBAR - LOGO
# =========================
logo_path = "LipWeb/logo_kampus.png"
if os.path.exists(logo_path):
    st.sidebar.image(logo_path, width=150)
else:
    st.sidebar.warning("Logo kampus tidak ditemukan")

st.sidebar.title("🎓 LipWeb")
st.sidebar.caption("Dashboard Akademik Interaktif")

# =========================
# TENTANG SAYA
# =========================
NAMA = "Philip Day Hutasoit"
NIM = "4232401027"
PRODI = "Teknologi Rekayasa Pembangkit Energi"
KAMPUS = "Politeknik Negeri Batam"

st.sidebar.markdown("---")
st.sidebar.subheader("👤 Tentang Saya")
st.sidebar.markdown(f"""
**Nama** : {NAMA}  
**NIM** : {NIM}  
**Prodi** : {PRODI}  
**Kampus** : {KAMPUS}
""")

# =========================
# JAM ONLINE (WIB)
# =========================
st.sidebar.markdown("---")
st.sidebar.subheader("⏰ Jam Online")

wib = pytz.timezone("Asia/Jakarta")
now = datetime.now(wib).strftime("%H:%M:%S")

st.sidebar.write(f"🕒 {now} WIB")

# =========================
# TITLE
# =========================
st.title("📊 LipWeb – Dashboard Akademik Modern")

# =========================
# TEXT PARAGRAF
# =========================
st.text(
    "LipWeb adalah sebuah web dashboard interaktif berbasis Streamlit\n"
    "yang dirancang untuk menampilkan data akademik mahasiswa.\n\n"
    "Web ini menampilkan berbagai komponen penting seperti teks,\n"
    "potongan kode, tabel data, dan grafik interaktif berbasis Plotly."
)

st.caption("🚀 Dibangun menggunakan Python, Streamlit, Pandas, dan Plotly")

# =========================
# CODE (POTONGAN KODE)
# =========================
st.subheader("💻 Contoh Potongan Kode Streamlit")
st.code("""
import streamlit as st

st.title("Halo Streamlit")
st.write("Ini adalah contoh web sederhana")
""", language="python")

# =========================
# DATA MAHASISWA (20 SISWA)
# =========================
st.header("📋 Data Nilai Mahasiswa")

data = {
    "Nama": [
        "Andi","Budi","Citra","Dewi","Eka",
        "Fajar","Gina","Hadi","Indah","Joko",
        "Kiki","Lina","Mira","Nanda","Oki",
        "Putri","Rizki","Salsa","Tono","Yuni"
    ],
    "Mata Kuliah": [
        "Elektronika","Pemrograman","Sistem Digital","Robotika","AI",
        "Pemrograman","Jaringan","Robotika","AI","Elektronika",
        "Jaringan","Pemrograman","AI","Robotika","Sistem Digital",
        "Pemrograman","Elektronika","AI","Jaringan","Robotika"
    ],
    "Nilai": [
        85,90,78,88,92,
        87,80,89,91,76,
        84,90,88,79,86,
        93,81,90,85,87
    ]
}

df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)

# =========================
# GRAFIK BAR
# =========================
st.subheader("📊 Grafik Nilai Mahasiswa")
fig_bar = px.bar(
    df,
    x="Nama",
    y="Nilai",
    color="Mata Kuliah",
    title="Distribusi Nilai Mahasiswa"
)
st.plotly_chart(fig_bar, use_container_width=True)

# =========================
# GRAFIK PIE
# =========================
st.subheader("🥧 Komposisi Mata Kuliah")
fig_pie = px.pie(
    df,
    names="Mata Kuliah",
    title="Proporsi Mata Kuliah"
)
st.plotly_chart(fig_pie, use_container_width=True)

# =========================
# GRAFIK BOX
# =========================
st.subheader("📈 Sebaran Nilai")
fig_box = px.box(
    df,
    y="Nilai",
    title="Sebaran Nilai Mahasiswa"
)
st.plotly_chart(fig_box, use_container_width=True)

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("© 2025 LipWeb | Streamlit Academic Dashboard")
