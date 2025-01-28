import pandas as pd
from prophet import Prophet
import pickle
import os

def train_prophet_model(csv_path, model_output_path):
    """
    Reads a CSV containing price history (e.g. annual)
    and trains a Prophet model.
    """
    df = pd.read_csv(csv_path)
    df_prophet = pd.DataFrame()
    df_prophet['ds'] = pd.to_datetime(df['Year'], format='%Y')
    df_prophet['y'] = df['Value'] 

    model = Prophet(
        yearly_seasonality=True,
        weekly_seasonality=False,
        daily_seasonality=False
    )

    model.fit(df_prophet)

    with open(model_output_path, "wb") as f:
        pickle.dump(model, f)
    print(f"Prophet model trained and saved in {model_output_path}")

if __name__ == "__main__":
    os.makedirs("models", exist_ok=True)

    input_wheat_csv = "data/raw/wheat_france_prices.csv" 
    output_wheat_model = "models/prophet_wheat.pkl"
    train_prophet_model(input_wheat_csv, output_wheat_model)

    input_oats_csv = "data/raw/oats_france_prices.csv"
    output_oats_model = "models/prophet_oats.pkl"
    train_prophet_model(input_oats_csv, output_oats_model)

    input_rapeseed_csv = "data/raw/rapeseed_france_prices.csv"
    output_rapeseed_model = "models/prophet_rapeseed.pkl"
    train_prophet_model(input_rapeseed_csv, output_rapeseed_model)

    input_sunflower_csv = "data/raw/sunflower_france_prices.csv"
    output_sunflower_model = "models/prophet_sunflower.pkl"
    train_prophet_model(input_sunflower_csv, output_sunflower_model)

    input_corn_csv = "data/raw/corn_france_prices.csv"
    output_corn_model = "models/prophet_corn.pkl"
    train_prophet_model(input_corn_csv, output_corn_model)
