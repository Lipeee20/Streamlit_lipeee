# =====================================================
# MY COLLECTION DASHBOARD - ENTERPRISE (FULL UPGRADED)
# Plotly Only | Clear Charts | Professional Insight
# =====================================================

import pandas as pd
import streamlit as st
import plotly.express as px
from babel.numbers import format_currency

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="My Collection Dashboard",
    page_icon="📊",
    layout="wide"
)

px.defaults.template = "plotly_dark"

# =====================================================
# HEADER
# =====================================================
st.title("📊 My Collection Dashboard")
st.caption("Interactive Sales & Customer Analytics")
st.markdown("---")

# =========================================================
# DARK MODE + ENTERPRISE THEME
# =========================================================
st.markdown("""
<style>
:root {
--primary: #1f77b4;
--background: #0e1117;
--secondary-bg: #161b22;
--text-color: #e6edf3;
}
html, body, [class*="css"] {
background-color: var(--background) !important;
color: var(--text-color) !important;
}
section[data-testid="stSidebar"] {
background-color: var(--secondary-bg) !important;
padding-top: 200px;
}
[data-testid="stMetric"] {
background: linear-gradient(135deg, #1f77b4, #0d3b66);
padding: 20px;
border-radius: 16px;
color: white;
}
[data-testid="stMetric"] div {
font-size: 28px;
font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# FUNCTIONS
# =====================================================
def create_daily_orders_df(df):
    df = df.copy()
    df.set_index("order_date", inplace=True)
    return (
        df.resample("D")
        .agg(order_count=("order_id", "nunique"), revenue=("total_price", "sum"))
        .reset_index()
    )

def create_rfm_df(df):
    rfm = (
        df.groupby("customer_id")
        .agg(
            last_order=("order_date", "max"),
            frequency=("order_id", "nunique"),
            monetary=("total_price", "sum")
        )
        .reset_index()
    )

    recent = df["order_date"].max()
    rfm["recency"] = (recent - rfm["last_order"]).dt.days

    return rfm


# =====================================================
# LOAD DATA
# =====================================================
all_df = pd.read_csv("all_data.csv")
for col in ["order_date", "delivery_date"]:
    all_df[col] = pd.to_datetime(all_df[col])
all_df.sort_values("order_date", inplace=True)

# =====================================================
# SIDEBAR FILTER
# =====================================================
with st.sidebar:
    st.image("https://raw.githubusercontent.com/mhvvn/dashboard_streamlit/refs/heads/main/img/tshirt.png", width=90)
    st.markdown("## 🔎 Filter")
    start_date, end_date = st.date_input(
        "Rentang Waktu",
        value=[all_df.order_date.min(), all_df.order_date.max()]
    )
    show_raw = st.checkbox("Tampilkan Data Mentah")

main_df = all_df[(all_df.order_date >= pd.to_datetime(start_date)) &
                 (all_df.order_date <= pd.to_datetime(end_date))]

# =====================================================
# DERIVED DATA
# =====================================================
daily_orders_df = create_daily_orders_df(main_df)
product_df = main_df.groupby("product_name").quantity_x.sum().reset_index()
bygender_df = main_df.groupby("gender").customer_id.nunique().reset_index(name="customer_count")
byage_df = main_df.groupby("age_group").customer_id.nunique().reset_index(name="customer_count")
bystate_df = main_df.groupby("state").customer_id.nunique().reset_index(name="customer_count")

# RFM DF (INI YANG KURANG)
rfm_df = create_rfm_df(main_df)



# =====================================================
# KPI
# =====================================================
st.subheader("📌 Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Orders", daily_orders_df.order_count.sum())
col2.metric("Revenue", format_currency(daily_orders_df.revenue.sum(), "AUD", locale="es_CO"))
col3.metric("AOV", format_currency(daily_orders_df.revenue.sum()/daily_orders_df.order_count.sum(), "AUD", locale="es_CO"))
col4.metric("Customers", main_df.customer_id.nunique())

st.markdown("---")

# =====================================================
# DAILY TREND (UPGRADED)
# =====================================================
st.subheader("📈 Daily Orders & Revenue")
fig = px.line(
    daily_orders_df,
    x="order_date",
    y=["order_count", "revenue"],
    markers=True,
    title="Daily Orders & Revenue Trend"
)
fig.update_layout(
    hovermode="x unified",
    xaxis=dict(rangeslider=dict(visible=True), type="date")
)
st.plotly_chart(fig, use_container_width=True)

# =====================================================
# PRODUCT PERFORMANCE
# =====================================================
st.subheader("🏆 Top Products")
fig = px.bar(
    product_df.sort_values("quantity_x", ascending=False).head(10),
    x="quantity_x",
    y="product_name",
    orientation="h",
    text="quantity_x",
    color="quantity_x",
    title="Top 10 Best Products"
)
fig.update_traces(textposition="outside")
fig.update_layout(yaxis=dict(categoryorder="total ascending"))
st.plotly_chart(fig, use_container_width=True)

# =====================================================
# CUSTOMER DEMOGRAPHICS
# =====================================================
st.subheader("👥 Customer Demographics")
col1, col2 = st.columns(2)
with col1:
    fig = px.pie(bygender_df, names="gender", values="customer_count", hole=0.45,
                 title="Customer by Gender")
    fig.update_traces(textinfo="percent+label")
    st.plotly_chart(fig, use_container_width=True)
with col2:
    fig = px.bar(byage_df, x="age_group", y="customer_count", text="customer_count",
                 title="Customer by Age Group")
    fig.update_traces(textposition="outside")
    st.plotly_chart(fig, use_container_width=True)

fig = px.bar(
    bystate_df.sort_values("customer_count", ascending=False).head(10),
    y="state",
    x="customer_count",
    orientation="h",
    color="customer_count",
    title="Top 10 Customer by State"
)
st.plotly_chart(fig, use_container_width=True)

# =====================================================
# RFM ANALYSIS
# =====================================================
st.subheader("💎 Top Customers (RFM)")

median_monetary = rfm_df["monetary"].median()

fig = px.bar(
    rfm_df.sort_values("monetary", ascending=False).head(10),
    x="customer_id",
    y="monetary",
    color="monetary",
    title="Top Customers by Monetary"
)

fig.add_hline(
    y=median_monetary,
    line_dash="dash",
    annotation_text="Median"
)

st.plotly_chart(fig, use_container_width=True)

# =====================================================
# RAW DATA
# =====================================================
if show_raw:
    st.subheader("📄 Raw Data")
    st.dataframe(main_df)

st.markdown("---")
st.caption("© 2025 My Collection Dashboard")
