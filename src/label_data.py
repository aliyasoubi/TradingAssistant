import os
import pandas as pd
import yaml

# Load configuration from config.yaml
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Fetch BASE_DIR from the loaded config
BASE_DIR = config['BASE_DIR']

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
    processed_path = os.path.join(BASE_DIR, 'data', 'processed_data.csv')
    
    # Load the labeled data
    data = pd.read_csv(processed_path)
    
    # Label the data with the price direction (up = 1, down = 0)
    data = label_data(data)
    
    labeled_path = os.path.join(BASE_DIR, 'data', 'labeled_data.csv')
    # Save the labeled data
    data.to_csv(labeled_path, index=False)
    print("Data labeled and saved as labeled_data.csv")
