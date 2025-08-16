import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing

# Load and prepare the data
df = pd.read_csv("Nat_Gas.csv")
df["Dates"] = pd.to_datetime(df["Dates"])
df.set_index("Dates", inplace=True)
df = df.asfreq("M")  # ensures consistent monthly frequency

# Plot original data
plt.figure(figsize=(10,5))
plt.plot(df.index, df["Prices"], marker='o', color='steelblue')
plt.title("Natural Gas Monthly Prices")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.grid(True)
plt.show()

# Create daily interpolated prices
daily_prices = df.resample("D").interpolate("time")

# Build forecasting model
model = ExponentialSmoothing(df["Prices"], trend="add", seasonal="add", seasonal_periods=12)
fit = model.fit()

# Forecast 12 months ahead
future_months = pd.date_range(df.index[-1] + pd.DateOffset(months=1), periods=12, freq="M")
forecast = fit.forecast(len(future_months))
forecast_df = pd.Series(forecast.values, index=future_months)
forecast_daily = forecast_df.resample("D").interpolate("time")

# Merge historical + forecasted daily prices
full_daily = pd.concat([daily_prices, forecast_daily])

def estimate_price(input_date):
    date = pd.to_datetime(input_date)
    if date in full_daily.index:
        return round(full_daily.loc[date], 2)
    else:
        return "⚠️ Date out of range. Try a date between 2020-10-31 and 2025-09-30."

# Example calls
print("Estimated Price on 2023-08-15:", estimate_price("2023-08-15"))
print("Estimated Price on 2025-06-10:", estimate_price("2025-06-10"))
