import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from utils.data_loader import load_data
import joblib
from simulation import run_monte_carlo_simulation

st.set_page_config(page_title="FIFA WC 2026 Predictor", layout="wide")

st.title("FIFA World Cup 2026 AI Predictor")
st.markdown("ML Project")

matches, teams, editions = load_data()

# Sidebar
team_options = sorted(teams['team'].unique())
selected_team = st.sidebar.selectbox("Select Team", team_options, index=team_options.index("") if "" in team_options else 0)

# Prediction Page
st.header("Match Predictor")
col1, col2 = st.columns(2)
with col1:
    team_a = st.selectbox("Team A", team_options, key="ta")
with col2:
    team_b = st.selectbox("Team B", team_options, key="tb", index=1)

if st.button("Predict Match"):
    # Placeholder
    st.success(f"{team_a} vs {team_b}: High chance for strong teams!")
    st.progress(0.45)

# Simulation
st.header("Tournament Simulation")
if st.button("Run 1000 Simulations"):
    results = run_monte_carlo_simulation(focus_team=selected_team)
    st.bar_chart(pd.DataFrame.from_dict(results, orient='index'))

# EDA example

st.markdown("### Egypt's Path to Glory")
st.info("With current form, Egypt has strong potential ")
