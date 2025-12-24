import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Lipweb Dashboard",
    page_icon="🎓",
    layout="wide"
)

# =========================
# IDENTITAS MAHASISWA
# =========================
NAMA_KAMPUS = "Politeknik Negeri Batam"
NAMA_MAHASISWA = "Philip Day Hutasoit"
NIM = "4232401027"
PRODI = "Teknologi Rekaya Pembangkit Energi"
FAKULTAS = "Teknik Elekto"

# =========================
# BACKGROUND 3D GRADIENT
# =========================
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(
            -45deg,
            #020617,
            #0f172a,
            #1e293b,
            #020617
        );
        background-size: 400% 400%;
        animation: gradientBG 12s ease infinite;
    }

    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# SIDEBAR
# =========================
import os

logo_path = "logo_kampus.png"

if os.path.exists(logo_path):
    st.sidebar.image(logo_path, width=150)
else:
    st.sidebar.warning("Logo kampus tidak ditemukan")

st.sidebar.markdown(f"### 🎓 {NAMA_KAMPUS}")
st.sidebar.caption("Dashboard Akademik Mahasiswa")
st.sidebar.divider()

menu = st.sidebar.radio(
    "Navigasi",
    ["Dashboard", "Data Mahasiswa", "Visualisasi", "Tentang Saya"]
)

# =========================
# DATA MAHASISWA (20 ORANG)
# =========================
df = pd.DataFrame({
    "Nama": [
        "Andi", "Budi", "Citra", "Dewi", "Eko",
        "Fajar", "Gina", "Hadi", "Intan", "Joko",
        "Karin", "Lukman", "Maya", "Nanda", "Oki",
        "Putri", "Rizki", "Salsa", "Tono", "Vina"
    ],
    "Mata Kuliah": [
        "Elektronika", "Pemrograman", "Sistem Digital", "Robotika", "Elektronika",
        "Pemrograman", "Sistem Digital", "Robotika", "Elektronika", "Pemrograman",
        "Sistem Digital", "Robotika", "Elektronika", "Pemrograman", "Sistem Digital",
        "Robotika", "Elektronika", "Pemrograman", "Sistem Digital", "Robotika"
    ],
    "Nilai": [
        85, 90, 78, 88, 82,
        87, 80, 92, 76, 89,
        84, 91, 79, 86, 83,
        90, 88, 81, 77, 85
    ]
})

df["Status"] = df["Nilai"].apply(lambda x: "Lulus" if x >= 80 else "Tidak Lulus")
df["Ranking"] = df["Nilai"].rank(ascending=False, method="min").astype(int)

# =========================
# DASHBOARD
# =========================
if menu == "Dashboard":
    st.title("📊 Dashboard Akademik")
    st.caption("Monitoring data mahasiswa secara interaktif")

    col1, col2, col3 = st.columns(3)
    col1.metric("👥 Total Mahasiswa", len(df))
    col2.metric("✅ Lulus", (df["Status"] == "Lulus").sum())
    col3.metric("❌ Tidak Lulus", (df["Status"] == "Tidak Lulus").sum())

    st.subheader("🏆 5 Nilai Tertinggi")
    st.table(df.sort_values("Nilai", ascending=False).head(5))

# =========================
# DATA MAHASISWA
# =========================
elif menu == "Data Mahasiswa":
    st.title("📋 Data Mahasiswa")

    status = st.selectbox(
        "Filter Status Kelulusan",
        ["Semua", "Lulus", "Tidak Lulus"]
    )

    if status != "Semua":
        df_show = df[df["Status"] == status]
    else:
        df_show = df

    st.dataframe(df_show, use_container_width=True)

# =========================
# VISUALISASI
# =========================
elif menu == "Visualisasi":
    st.title("📈 Visualisasi Data Mahasiswa")

    col1, col2 = st.columns(2)

    with col1:
        fig_bar = px.bar(
            df,
            x="Nama",
            y="Nilai",
            color="Status",
            title="Grafik Nilai Mahasiswa"
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    with col2:
        fig_pie = px.pie(
            df,
            names="Status",
            title="Persentase Kelulusan"
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    fig_line = px.line(
        df.sort_values("Ranking"),
        x="Ranking",
        y="Nilai",
        markers=True,
        title="Tren Nilai Berdasarkan Ranking"
    )
    st.plotly_chart(fig_line, use_container_width=True)

# =========================
# TENTANG SAYA
# =========================
else:
    st.title("👤 Tentang Saya")

    st.markdown(
        f"""
        **Nama** : {"Philip Day Hutasoit"}  
        **NIM** : {"4232401027"}  
        **Program Studi** : {"Teknologi Rekaya Pembangkit Energi"}  
        **Fakultas** : {"Teknik Elekto"}  
        **Universitas** : {"Politeknik Negeri Batam"}
        """
    )

    st.divider()

    st.write(
        """
        Saya adalah mahasiswa yang sedang mempelajari
        pengembangan **aplikasi web dan visualisasi data**
        menggunakan Python.

        Aplikasi **Lipweb** ini dibuat sebagai project
        akademik untuk menampilkan data mahasiswa secara
        **interaktif, informatif, dan modern**.
        """
    )

    st.subheader("🎯 Tujuan Aplikasi")
    st.write(
        """
        - Menerapkan Streamlit dalam pengembangan web  
        - Menyajikan data akademik secara visual  
        - Meningkatkan pemahaman analisis data  
        """
    )

    st.subheader("🛠️ Teknologi")
    st.markdown(
        """
        - 🐍 Python  
        - 🌐 Streamlit  
        - 📊 Pandas  
        - 📈 Plotly  
        """
    )

    st.success(
        "Aplikasi ini dikembangkan untuk keperluan akademik "
        "dan siap dikembangkan lebih lanjut."
    )
