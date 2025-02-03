# Cereals Price Prediction
Welcome to the Cereal Price Prediction Dashboard! This interactive web app lets you explore the historical and predicted prices of major cereals in France. Using advanced machine learning models, we forecast the future prices of crops like wheat, oats, rapeseed, sunflower, and corn.

### Features
- **Explore Historical Prices:** View detailed data of past prices for cereals (up to 30 years of history).
- **Forecast Future Prices:** See predictions of cereal prices for the next 5 to 30 years, including confidence intervals.
- **Interactive Interface:** Choose the cereals and the time period for which you want to see the price trends.
- **Data-Driven Insights:** All predictions are powered by machine learning models (Prophet) based on FAOSTAT data.

### How to use
1. **Visit the Dashboard:** Access the app through the following link: https://cereals-dashboard-258413365847.europe-west1.run.app
2. **Select Your Cereal:** Choose one of the available cereals (wheat, oats, rapeseed, sunflower, corn).
3. **Adjust the Time Period:** Use the slider to pick a historical period (5 to 30 years) and visualize the price trends.
4. **See the Future:** Click to generate price forecasts and view predicted values with confidence intervals.

### Technologies used
- **Prophet:** Time series forecasting library by Facebook, used to generate price predictions.
- **Streamlit:** Framework to create interactive web apps with Python.
- **Google Cloud Platform:** Used for hosting and serving the app through Cloud Run, with data storage in Google Cloud Storage.

### How it works
1. **Data Collection:** The app fetches historical price data from FAOSTAT (Food and Agriculture Organization).
2. **Model Training:** Machine learning models are trained using historical data to predict future prices.
3. **Forecasting:** The trained models generate price forecasts for different cereals.
4. **Visualization:** Streamlit is used to display the data and predictions in an interactive format.
