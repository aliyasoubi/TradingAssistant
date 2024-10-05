import pandas as pd
import os
import yaml

# Load configuration from config.yaml
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Set the BASE_DIR and paths from config.yaml
BASE_DIR = config['BASE_DIR']
DATA_DIR = config['DATA_DIR']
PROCESSED_DATA_FILE = config['PROCESSED_DATA_FILE']
CONFIRMED_SIGNALS_FILE = config['CONFIRMED_SIGNALS_FILE']

# Function to load the processed data file
def load_processed_data():
    processed_data_path = os.path.join(BASE_DIR, DATA_DIR, PROCESSED_DATA_FILE)
    return pd.read_csv(processed_data_path)

# Function to save the confirmed signals data
def save_confirmed_signals(data):
    confirmed_signals_path = os.path.join(BASE_DIR, DATA_DIR, CONFIRMED_SIGNALS_FILE)
    data.to_csv(confirmed_signals_path, index=False)
    print(f"Buy/Sell signals confirmed and data saved at: {confirmed_signals_path}")

# Function to confirm signals (follows Single Responsibility Principle)
def confirm_signals(data):
    """
    Confirms buy/sell signals by combining multiple indicators.
    
    Parameters:
        data (pandas.DataFrame): Dataset with individual indicator signals.
    
    Returns:
        pandas.DataFrame: Dataset with confirmed buy/sell signals.
    """
    # Confirm Buy Signal: When RSI, MACD, and SMA signals align
    data['Confirmed_Buy_Signal'] = (
        (data['RSI_Buy_Signal'] == 1) &
        (data['MACD_Buy_Signal'] == 1) &
        (data['SMA_Buy_Signal'] == 1)
    ).astype(int)
    
    # Confirm Sell Signal: When RSI, MACD, and SMA signals align
    data['Confirmed_Sell_Signal'] = (
        (data['RSI_Sell_Signal'] == 1) &
        (data['MACD_Sell_Signal'] == 1) &
        (data['SMA_Sell_Signal'] == 1)
    ).astype(int)
    
    return data

if __name__ == "__main__":
    # Step 1: Load the processed data
    data = load_processed_data()

    # Step 2: Confirm buy/sell signals
    data = confirm_signals(data)

    # Step 3: Save confirmed signals data
    save_confirmed_signals(data)