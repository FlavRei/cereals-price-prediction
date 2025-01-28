import streamlit as st
import pandas as pd
import plotly.express as px

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

history_path = cereal_files[selected_cereal]["history"]
forecast_path = cereal_files[selected_cereal]["forecast"]

try:
    df_history = pd.read_csv(history_path)
    df_forecast = pd.read_csv(forecast_path)
except FileNotFoundError as e:
    st.error(f"File not found : {e}")
    st.stop()

fig1 = px.line(
    df_history,
    x='Year',
    y='Value',
    title=f"Historical price of {selected_cereal} in France (USD/t)"
)
st.plotly_chart(fig1)

fig2 = px.line(
    df_forecast,
    x='Year',
    y='Predicted Value',
    title=f"Forecasted price of {selected_cereal} (USD/t)"
)

fig2.add_scatter(
    x=df_forecast['Year'],
    y=df_forecast['Predicted Value Lower'],
    mode='lines',
    name='Lower',
    line=dict(dash='dash', color='pink')
)

fig2.add_scatter(
    x=df_forecast['Year'],
    y=df_forecast['Predicted Value Upper'],
    mode='lines',
    name='Upper',
    line=dict(dash='dash', color='violet')
)

st.plotly_chart(fig2)
