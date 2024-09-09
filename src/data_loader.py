import yfinance as yf
import pandas as pd


def download_data(symbol, start, end, interval):
    data = yf.download(symbol, start=start, end=end, interval=interval)
    return data


if __name__ == "__main__":
    # Example: Download 1-minute data for gold from 2023 to now
    data = download_data("GC=F", start="2023-01-01", end="2024-01-01", interval="1m")
    data.to_csv('../data/gold_data.csv')
    print("Data downloaded successfully.")
