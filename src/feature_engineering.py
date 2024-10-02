import os
import pandas as pd
import talib as ta
import yaml

# Load configuration from config.yaml
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Fetch BASE_DIR from the loaded config
BASE_DIR = config['BASE_DIR']

def add_indicators(data):
    """
    Adds technical indicators (RSI, MACD, SMA) to the dataset.
    
    Parameters:
        data (pandas.DataFrame): The dataset with columns like 'Open', 'High', 'Low', 'Close', 'Volume'.
    
    Returns:
        pandas.DataFrame: The dataset with added technical indicators.
    """
    # Add RSI
    data['RSI'] = ta.RSI(data['Close'], timeperiod=14)
    
    # Add MACD
    data['MACD'], data['MACD_signal'], _ = ta.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    
    # Add Simple Moving Averages
    data['SMA_50'] = ta.SMA(data['Close'], timeperiod=50)
    data['SMA_200'] = ta.SMA(data['Close'], timeperiod=200)
    
    # Drop rows with missing values due to indicator calculations
    data.dropna(inplace=True)
    
    return data

if __name__ == "__main__":

    # Construct the path to the raw gold data using BASE_DIR
    data_path = os.path.join(BASE_DIR, 'data', 'gold_data.csv')

    # Load the raw gold data
    data = pd.read_csv(data_path)
    
    # Add technical indicators
    data = add_indicators(data)
    
    # Construct the path to save the processed data
    processed = os.path.join(BASE_DIR, 'data', 'processed.csv')
    
    # Save the processed data with indicators
    data.to_csv(processed, index=False)
    print("Technical indicators added and data saved as processed_data.csv")
