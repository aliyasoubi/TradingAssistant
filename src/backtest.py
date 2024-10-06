import os
import backtrader as bt
import pandas as pd
import yaml

# Load configuration from config.yaml
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)


# Set the BASE_DIR and paths from config.yaml
BASE_DIR = config['BASE_DIR']
DATA_DIR = config['DATA_DIR']
CONFIRMED_SIGNALS_FILE = config['CONFIRMED_SIGNALS_FILE']

# Extend PandasData to include custom columns
class CustomPandasData(bt.feeds.PandasData):
    # Define the custom columns in the dataset
    lines = ('Confirmed_Buy_Signal', 'Confirmed_Sell_Signal',)
    
    # Define the Pandas columns that will map to the Backtrader lines
    params = (
        ('Confirmed_Buy_Signal', -1),  # Default to -1 if not found
        ('Confirmed_Sell_Signal', -1), # Default to -1 if not found
    )

class SignalStrategy(bt.Strategy):
    """
    Backtrader strategy to execute trades based on confirmed buy/sell signals.
    """
    def __init__(self):
        # Reference the custom buy/sell signals from the data feed
        self.buy_signal = self.data.Confirmed_Buy_Signal
        self.sell_signal = self.data.Confirmed_Sell_Signal

    def next(self):
        # Execute Buy Order if Buy Signal is triggered
        if self.buy_signal[0] == 1 and not self.position:
            self.buy(size=1)  # Buy 1 unit
            print(f"Buy at {self.data.close[0]}")

        # Execute Sell Order if Sell Signal is triggered
        elif self.sell_signal[0] == 1 and self.position:
            self.sell(size=1)  # Sell 1 unit
            print(f"Sell at {self.data.close[0]}")

# Function to run the backtest
def run_backtest():
    # Load historical data with confirmed signals
    confirmed_signals_path = os.path.join(BASE_DIR, DATA_DIR, CONFIRMED_SIGNALS_FILE)
    data = pd.read_csv(confirmed_signals_path, index_col='Datetime', parse_dates=True)

    # Convert the data to Backtrader's CustomPandasData Feed
    data_feed = CustomPandasData(dataname=data)

    # Initialize Backtrader engine
    cerebro = bt.Cerebro()

    # Add strategy to engine
    cerebro.addstrategy(SignalStrategy)

    # Add the data feed to the engine
    cerebro.adddata(data_feed)

    # Set initial capital
    cerebro.broker.setcash(10000)

    # Set fixed commission (for more realistic backtesting)
    cerebro.broker.setcommission(commission=0.001)

    # Print starting portfolio value
    print(f"Starting Portfolio Value: {cerebro.broker.getvalue()}")

    # Run the backtest
    cerebro.run()

    # Print ending portfolio value
    print(f"Ending Portfolio Value: {cerebro.broker.getvalue()}")

    # Plot the results
    cerebro.plot()

if __name__ == "__main__":
    run_backtest()