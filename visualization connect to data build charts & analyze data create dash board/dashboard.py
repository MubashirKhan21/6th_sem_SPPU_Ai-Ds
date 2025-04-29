import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# 📌 Load Titanic dataset from a public URL
DATA_URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
data = pd.read_csv(DATA_URL)

# ------------------ 🟢 STREAMLIT DASHBOARD START ------------------

# 📌 Set Power BI-like page layout
st.set_page_config(page_title="🚢 Titanic Analysis", layout="wide")

# 📌 Dashboard Header
st.markdown("<h1 style='text-align: center;'>🚢 Titanic Passenger Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Analyze survival rates and passenger demographics</h3>", unsafe_allow_html=True)

# --------------- 🟢 KPI METRICS (TOP ROW) -----------------
st.markdown("### 🚀 Key Statistics")

col1, col2, col3, col4 = st.columns(4)

# 📌 Display KPIs
with col1:
    st.metric(label="👥 Total Passengers", value=f"{len(data)}")

with col2:
    survived_count = data["Survived"].sum()
    st.metric(label="💚 Survived", value=f"{survived_count}")

with col3:
    avg_fare = round(data["Fare"].mean(), 2)
    st.metric(label="💰 Avg Fare", value=f"${avg_fare}")

with col4:
    avg_age = round(data["Age"].mean(), 1)
    st.metric(label="📊 Avg Age", value=f"{avg_age} yrs")

# --------------- 🟢 VISUALIZATION GRID (MIDDLE ROW) -----------------
st.markdown("### 📊 Data Visualizations")

row1_col1, row1_col2 = st.columns(2)

# 📌 Bar Chart - Survival Count
with row1_col1:
    st.markdown("#### 📌 Survival Count")
    fig, ax = plt.subplots()
    data["Survived"].value_counts().plot(kind="bar", color=["red", "green"], ax=ax)
    plt.xlabel("Survival (0 = No, 1 = Yes)")
    plt.ylabel("Count")
    st.pyplot(fig)

# 📌 Histogram - Age Distribution
with row1_col2:
    st.markdown("#### 📌 Age Distribution of Passengers")
    fig, ax = plt.subplots()
    sns.histplot(data["Age"].dropna(), bins=20, kde=True, ax=ax)
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    st.pyplot(fig)

# --------------- 🟢 INTERACTIVE SCATTER PLOT (FULL WIDTH) -----------------
st.markdown("### 🔍 Passenger Insights")

fig = px.scatter(data, x="Age", y="Fare", color="Survived",
                 title="Fare Paid vs Age",
                 labels={"Fare": "Fare Paid", "Age": "Passenger Age"},
                 width=900, height=500)
st.plotly_chart(fig, use_container_width=True)

# --------------- 🟢 FILTERED DATA TABLE (BOTTOM ROW) -----------------
st.markdown("### 🎯 Filter & Explore Data")

pclass_filter = st.selectbox("🔍 Select Passenger Class", sorted(data["Pclass"].unique()))
filtered_data = data[data["Pclass"] == pclass_filter]
st.dataframe(filtered_data)

# ------------------ 🟢 STREAMLIT DASHBOARD END ------------------
