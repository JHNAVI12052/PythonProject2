import yfinance as yf
data = yf.download("INFY.NS", start="2020-01-01", end="2025-06-30", auto_adjust=False)

data.to_csv("data/infosys.csv")

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import os

df = pd.read_csv("infosys.csv", parse_dates=["Date"])

# Remove nulls
df.dropna(inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Reset index
df.reset_index(drop=True, inplace=True)
