import pickle
import os

def forecast_future_prices(model_path, periods=21):
    """
    Loads a saved Prophet model, forecasts 'periods' years into the future.
    """
    with open(model_path, "rb") as f:
        model = pickle.load(f)

    future = model.make_future_dataframe(periods=periods, freq='Y') 
    forecast = model.predict(future)
    return forecast

if __name__ == "__main__":
    os.makedirs("data/forecast", exist_ok=True)

    wheat_forecast_df = forecast_future_prices("models/prophet_wheat.pkl")
    print("Wheat forecast saved to data/forecast/wheat_france_forecast.csv")
    wheat_forecast_df.to_csv("data/forecast/wheat_france_forecast.csv", index=False)

    oats_forecast_df = forecast_future_prices("models/prophet_oats.pkl")
    print("Oats forecast saved to data/forecast/oats_france_forecast.csv")
    oats_forecast_df.to_csv("data/forecast/oats_france_forecast.csv", index=False)

    rapeseed_forecast_df = forecast_future_prices("models/prophet_rapeseed.pkl")
    print("Rapeseed forecast saved to data/forecast/rapeseed_france_forecast.csv")
    rapeseed_forecast_df.to_csv("data/forecast/rapeseed_france_forecast.csv", index=False)

    sunflower_forecast_df = forecast_future_prices("models/prophet_sunflower.pkl")
    print("Sunflower forecast saved to data/forecast/sunflower_france_forecast.csv")
    sunflower_forecast_df.to_csv("data/forecast/sunflower_france_forecast.csv", index=False)

    corn_forecast_df = forecast_future_prices("models/prophet_corn.pkl")
    print("Corn forecast saved to data/forecast/corn_france_forecast.csv")
    corn_forecast_df.to_csv("data/forecast/corn_france_forecast.csv", index=False)


