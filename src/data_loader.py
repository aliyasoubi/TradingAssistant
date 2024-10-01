import yfinance as yf
import pandas as pd
import os
import yaml

def load_config(config_file):
    """
    Loads configuration parameters from a YAML file.
    
    Parameters:
        config_file (str): Path to the config.yaml file.
    
    Returns:
        dict: Configuration dictionary containing data parameters and file paths.
    """
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config

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
    # Load configuration from the config.yaml file
    config = load_config("config.yaml")

    # Set parameters for the download
    symbol = config['data_params']['symbol']
    start_date = config['data_params']['start_date']
    end_date = config['data_params']['end_date']
    interval = config['data_params']['interval']

    # Download the data
    data = download_data(symbol, start=start_date, end=end_date, interval=interval)

    # Get the file path from config and save the data to CSV
    file_path = config['file_params']['save_path']
    save_data(data, file_path)
