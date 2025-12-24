import streamlit as st
import pandas as pd
import time
import random

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Lipweb Pro Max",
    page_icon="🚀",
    layout="wide"
)

# =========================
# 3D ANIMATED BACKGROUND
# =========================
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(-45deg, #020617, #0f172a, #1e293b, #020617);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }

    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    h1, h2, h3 { color: #38bdf8; }
    p, span, div { color: #e5e7eb; }

    div[data-testid="metric-container"] {
        background-color: #020617;
        border: 1px solid #38bdf8;
        padding: 15px;
        border-radius: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# SESSION STATE
# =========================
if "login" not in st.session_state:
    st.session_state.login = False
    st.session_state.user = ""

# =========================
# LOGIN PAGE
# =========================
if not st.session_state.login:
    st.title("🔐 Login Lipweb Pro Max")
    st.caption("Silakan login untuk mengakses dashboard")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "123":
            st.session_state.login = True
            st.session_state.user = "Admin"
            st.success("Login berhasil sebagai Admin")
            st.rerun()
        elif username == "user" and password == "123":
            st.session_state.login = True
            st.session_state.user = "User"
            st.success("Login berhasil sebagai User")
            st.rerun()
        else:
            st.error("Username atau password salah")

    st.stop()

# =========================
# SIDEBAR
# =========================
st.sidebar.title("🚀 Lipweb Pro Max")
st.sidebar.write(f"👤 Login sebagai: **{st.session_state.user}**")

menu = st.sidebar.radio(
    "Menu",
    ["Dashboard", "Realtime Monitor", "Tentang"]
)

if st.sidebar.button("Logout"):
    st.session_state.login = False
    st.session_state.user = ""
    st.rerun()

# =========================
# DATA
# =========================
df = pd.DataFrame({
    "Nama": ["Andi", "Budi", "Citra", "Dewi"],
    "Nilai": [85, 90, 78, 88]
})

# =========================
# DASHBOARD
# =========================
if menu == "Dashboard":
    st.title("📊 Dashboard Akademik")

    st.dataframe(df, use_container_width=True)

    col1, col2, col3 = st.columns(3)
    col1.metric("Nilai Max", df["Nilai"].max())
    col2.metric("Nilai Min", df["Nilai"].min())
    col3.metric("Rata-rata", round(df["Nilai"].mean(), 2))

    fig = px.bar(df, x="Nama", y="Nilai", text="Nilai")
    st.bar_chart(df.set_index("Nama")["Nilai"])


# =========================
# REALTIME SIMULATION
# =========================
elif menu == "Realtime Monitor":
    st.title("📡 Realtime Monitoring Nilai")

    placeholder = st.empty()

    for i in range(20):
        df_rt = pd.DataFrame({
            "Waktu": list(range(i + 1)),
            "Nilai Rata-rata": [random.randint(70, 95) for _ in range(i + 1)]
        })

        fig_rt = px.line(
            df_rt,
            x="Waktu",
            y="Nilai Rata-rata",
            markers=True
        )

        placeholder.plotly_chart(fig_rt, use_container_width=True)
        time.sleep(0.7)

# =========================
# ABOUT
# =========================
else:
    st.title("ℹ️ Tentang Lipweb Pro Max")
    st.write(
        """
        **Lipweb Pro Max** adalah dashboard akademik interaktif
        berbasis **Streamlit** yang dilengkapi dengan:
        
        ✅ Login user  
        ✅ Session management  
        ✅ Realtime visualization  
        ✅ UI modern + animasi  
        
        Cocok untuk **tugas kuliah, demo, dan portofolio**.
        """
    )

st.caption("© 2025 Lipweb Pro Max • Level Up Dashboard 🚀")
