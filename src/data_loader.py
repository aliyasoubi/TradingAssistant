import yfinance as yf
import pandas as pd
import os


def download_data(symbol, start, end, interval):
    """
    Downloads historical data from Yahoo Finance using yfinance.
    
    Parameters:
        symbol (str): The trading symbol (e.g., "GC=F" for Gold Futures).
        start (str): Start date in "YYYY-MM-DD" format.
        end (str): End date in "YYYY-MM-DD" format.
        interval (str): Data interval (e.g., '1m' for 1-minute data).
    
    Returns:
        pandas.DataFrame: The downloaded data.
    """
    print(f"Downloading data for {symbol} from {start} to {end} with interval {interval}...")
    data = yf.download(symbol, start=start, end=end, interval=interval)
    return data

def save_data(data, file_path):
    """
    Saves the data to a CSV file.
    
    Parameters:
        data (pandas.DataFrame): The data to save.
        file_path (str): The file path for saving the CSV.
    """
    data.to_csv(file_path)
    print(f"Data saved to {file_path}")

if __name__ == "__main__":
    # Set parameters for the download
    symbol = "GC=F"  # Gold Futures symbol on Yahoo Finance
    start_date = "2024-08-01"  # Start date
    end_date = "2024-09-28"    # End date
    interval = "15m"  # 1-minute interval data

    # Download the data
    data = download_data(symbol, start=start_date, end=end_date, interval=interval)

    # Define file path for saving the data
    file_path = os.path.join('C:\\Users\\Ali\\Projects\\TradingAssistant\\data', 'gold_data.csv')

    # Save the data to CSV
    save_data(data, file_path)