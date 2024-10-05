import os
import pandas as pd
import talib as ta
import yaml

# Load configuration from config.yaml
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Fetch BASE_DIR from the loaded config
BASE_DIR = config['BASE_DIR']
DATA_DIR = config['DATA_DIR']
RAW_DATA_FILE = config['RAW_DATA_FILE']
PROCESSED_DATA_FILE = config['PROCESSED_DATA_FILE']

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
    
    # Add Bollinger Bands (20-period)
    data['upper_band'], data['middle_band'], data['lower_band'] = ta.BBANDS(data['Close'], timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    
    # Generate Signals
    data = generate_signals(data)
    
    # Drop rows with missing data (due to calculation windows)
    data.dropna(inplace=True)
    
    return data

def generate_signals(data):
    """
    Generates buy/sell signals based on technical indicators.
    
    Parameters:
        data (pandas.DataFrame): Dataset with technical indicators.
    
    Returns:
        pandas.DataFrame: Dataset with added buy/sell signal columns.
    """
    # RSI Buy/Sell Signal: Buy when RSI < 30 (oversold), Sell when RSI > 70 (overbought)
    data['RSI_Buy_Signal'] = (data['RSI'] < 30).astype(int)
    data['RSI_Sell_Signal'] = (data['RSI'] > 70).astype(int)
    
    # MACD Buy/Sell Signal: Buy when MACD crosses above MACD_signal, Sell when MACD crosses below
    data['MACD_Buy_Signal'] = ((data['MACD'] > data['MACD_signal']) & (data['MACD'].shift(1) <= data['MACD_signal'].shift(1))).astype(int)
    data['MACD_Sell_Signal'] = ((data['MACD'] < data['MACD_signal']) & (data['MACD'].shift(1) >= data['MACD_signal'].shift(1))).astype(int)
    
    # SMA Buy/Sell Signal: Buy when 50-SMA crosses above 200-SMA, Sell when 50-SMA crosses below 200-SMA
    data['SMA_Buy_Signal'] = ((data['SMA_50'] > data['SMA_200']) & (data['SMA_50'].shift(1) <= data['SMA_200'].shift(1))).astype(int)
    data['SMA_Sell_Signal'] = ((data['SMA_50'] < data['SMA_200']) & (data['SMA_50'].shift(1) >= data['SMA_200'].shift(1))).astype(int)
    
    return data

# Function to load the raw data file
def load_data():
    data_path = os.path.join(BASE_DIR, DATA_DIR, RAW_DATA_FILE)
    return pd.read_csv(data_path)

# Function to save the processed data with indicators
def save_data(data):
    processed_data_path = os.path.join(BASE_DIR, DATA_DIR, PROCESSED_DATA_FILE)
    data.to_csv(processed_data_path, index=False)
    print(f"Technical indicators added and data saved at: {processed_data_path}")

if __name__ == "__main__":

    # Step 1: Load raw data
    data = load_data()

    # Step 2: Add technical indicators
    data = add_indicators(data)

    # Step 3: Save processed data
    save_data(data)