import pandas as pd

def label_data(data):
    """
    Labels the data based on whether the next period's closing price is higher than the current period's.
    
    Parameters:
        data (pandas.DataFrame): The dataset with technical indicators.
    
    Returns:
        pandas.DataFrame: The dataset with a new 'Target' column (1 for upward movement, 0 for downward).
    """
    # Shift the 'Close' column to compare the next period's price with the current period's price
    data['Target'] = (data['Close'].shift(-1) > data['Close']).astype(int)
    
    # Remove the last row as it doesn't have a next period to compare
    data = data.iloc[:-1]
    
    return data

if __name__ == "__main__":
    # Load the data with indicators from the previous step
    data = pd.read_csv('C:\\Users\\Ali\\Projects\\TradingAssistant\\data\\processed_data.csv')
    
    # Label the data with the price direction (up = 1, down = 0)
    data = label_data(data)
    
    # Save the labeled data
    data.to_csv('C:\\Users\\Ali\\Projects\\TradingAssistant\\data\\labeled_data.csv', index=False)
    print("Data labeled and saved as labeled_data.csv")
