import pandas as pd
import talib as ta


def add_indicators(data):
    data['RSI'] = ta.RSI(data['Close'], timeperiod=14)
    data['MACD'], data['MACD_signal'], _ = ta.MACD(data['Close'])
    return data


if __name__ == "__main__":
    data = pd.read_csv('../data/gold_data.csv')
    data = add_indicators(data)
    data.to_csv('../data/processed_data.csv', index=False)
    print("Technical indicators added.")
