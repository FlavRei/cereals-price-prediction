import streamlit as st
import plotly.express as px
import pandas as pd
from utils import gcs_data
import os

USE_GCS = os.getenv("USE_GCS", "false").lower() == "true"
BUCKET_NAME = os.getenv("GCS_BUCKET_NAME", "cereals-data-bucket")

st.title("Cereals Price Prediction")

cereal_files = {
    "Wheat": {
        "history": "data/raw/wheat_france_prices.csv",
        "forecast": "data/clean/wheat_france_forecast_clean.csv"
    },
    "Oats": {
        "history": "data/raw/oats_france_prices.csv",
        "forecast": "data/clean/oats_france_forecast_clean.csv"
    },
    "Rapeseed": {
        "history": "data/raw/rapeseed_france_prices.csv",
        "forecast": "data/clean/rapeseed_france_forecast_clean.csv"
    },
    "Sunflower": {
        "history": "data/raw/sunflower_france_prices.csv",
        "forecast": "data/clean/sunflower_france_forecast_clean.csv"
    },
    "Corn": {
        "history": "data/raw/corn_france_prices.csv",
        "forecast": "data/clean/corn_france_forecast_clean.csv"
    },
}

selected_cereal = st.selectbox("Select a cereal", list(cereal_files.keys()))

try:
    if USE_GCS:
        history_path = f"raw/{cereal_files[selected_cereal]['history'].split('/')[-1]}"
        forecast_path = f"clean/{cereal_files[selected_cereal]['forecast'].split('/')[-1]}"
        df_history = gcs_data.load_csv_from_gcs(BUCKET_NAME, history_path)
        df_forecast = gcs_data.load_csv_from_gcs(BUCKET_NAME, forecast_path)
    else:
        history_path = cereal_files[selected_cereal]['history']
        forecast_path = cereal_files[selected_cereal]['forecast']
        df_history = pd.read_csv(history_path)
        df_forecast = pd.read_csv(forecast_path)
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

historical_options = [5, 10, 15, 20, 25, 30]
selected_hist_years = st.selectbox("Number of historical years to display", historical_options)

max_hist_year = df_history['Year'].max()
min_year_to_show = max_hist_year - selected_hist_years + 1
df_history_filtered = df_history[df_history['Year'] >= min_year_to_show]

fig1 = px.line(
    df_history_filtered,
    x='Year',
    y='Value',
    title=f"Historical price of {selected_cereal} in France (USD/t) (last {selected_hist_years} years)"
)
st.plotly_chart(fig1)

forecast_options = [5, 10, 15, 20, 25, 30]
selected_forecast_years = st.selectbox("Number of forecast years to display", forecast_options)

df_forecast_sorted = df_forecast.sort_values(by='Year')
df_forecast_filtered = df_forecast_sorted.head(selected_forecast_years)

fig2 = px.line(
    df_forecast_filtered,
    x='Year',
    y='Predicted Value',
    title=f"Forecasted price of {selected_cereal} (USD/t) (next {selected_forecast_years} years)"
)

fig2.add_scatter(
    x=df_forecast_filtered['Year'],
    y=df_forecast_filtered['Predicted Value Upper'],
    mode='lines',
    name='Upper',
    line=dict(dash='dash', color='violet')
)

fig2.add_scatter(
    x=df_forecast_filtered['Year'],
    y=df_forecast_filtered['Predicted Value Lower'],
    mode='lines',
    name='Lower',
    line=dict(dash='dash', color='pink')
)

st.plotly_chart(fig2)
