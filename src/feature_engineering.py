import pandas as pd
import talib as ta

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
    # Load the raw gold data from Phase 1
    data = pd.read_csv('C:\\Users\\Ali\\Projects\\TradingAssistant\\data\\gold_data.csv')
    
    # Add technical indicators
    data = add_indicators(data)
    
    # Save the processed data with indicators
    data.to_csv('C:\\Users\\Ali\\Projects\\TradingAssistant\\data\\processed_data.csv', index=False)
    print("Technical indicators added and data saved as processed_data.csv")
