import os
import pandas as pd
import backtrader as bt
import joblib
import yaml
from datetime import datetime

# Load configuration from config.yaml
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Fetch BASE_DIR from the loaded config
BASE_DIR = config['BASE_DIR']

# Define the path to the model and data files
model_path = os.path.join(BASE_DIR, 'models', 'random_forest_model.pkl')
data_path = os.path.join(BASE_DIR, 'data', 'labeled_data.csv')


class MLStrategy(bt.Strategy):
    """
    Backtrader strategy that uses a pre-trained machine learning model 
    to predict market direction and execute trades based on those predictions.
    """
    def __init__(self):
        # Load the pre-trained model
        self.model = joblib.load(model_path)
        
        # Initialize technical indicators (RSI, MACD, SMA)
        self.rsi = bt.indicators.RelativeStrengthIndex(self.data.close, period=14)
        self.macd = bt.indicators.MACD(self.data.close)
        self.sma_50 = bt.indicators.SimpleMovingAverage(self.data.close, period=50)
        self.sma_200 = bt.indicators.SimpleMovingAverage(self.data.close, period=200)

    def next(self):
        # Get the current data (for the last candle/period)
        close = self.data.close[0]
        rsi = self.rsi[0]
        macd = self.macd.macd[0]
        macd_signal = self.macd.signal[0]
        sma_50 = self.sma_50[0]
        sma_200 = self.sma_200[0]
        
        # Create a feature set based on current market data
        current_features = [[rsi, macd, macd_signal, sma_50, sma_200]]

        # Use the trained model to predict the next move (up or down)
        prediction = self.model.predict(current_features)[0]

        # Trading logic based on the model's prediction
        if prediction == 1 and not self.position:  # Buy signal
            self.buy(size=1)
            print(f"Buy at {close}")
        elif prediction == 0 and self.position:  # Sell signal
            self.sell(size=1)
            print(f"Sell at {close}")


if __name__ == "__main__":
    # Load historical data
    data = pd.read_csv(data_path, index_col='Datetime', parse_dates=True)
    
    # Backtrader data feed
    data_feed = bt.feeds.PandasData(dataname=data)
    
    # Initialize Backtrader engine
    cerebro = bt.Cerebro()
    
    # Add strategy
    cerebro.addstrategy(MLStrategy)
    
    # Add data to the engine
    cerebro.adddata(data_feed)
    
    # Set initial cash for backtesting
    cerebro.broker.setcash(10000)
    
    # Run the backtest
    print("Starting Portfolio Value: %.2f" % cerebro.broker.getvalue())
    cerebro.run()
    print("Ending Portfolio Value: %.2f" % cerebro.broker.getvalue())
    
    # Plot the results
    cerebro.plot()