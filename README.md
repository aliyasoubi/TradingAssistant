# AI Trading Assistant for Short-Term Trading

## Overview
This project is an AI-powered trading assistant designed to help predict short-term market movements (1-15 minute intervals) in gold (XAU/USD) or other financial assets. It leverages machine learning and technical analysis to improve trading decisions, providing both real-time predictions and automated trading capabilities. The AI model is trained on historical data using popular technical indicators like RSI, MACD, and Moving Averages.

The project includes features for backtesting strategies, real-time trade execution via broker APIs, and dynamic risk management to maximize win rate and manage losses effectively.

## Features
- **Real-time Price Predictions**: Utilizes machine learning to predict short-term price movements based on historical and live market data.
- **Technical Indicator Analysis**: Supports indicators like RSI, MACD, Bollinger Bands, Moving Averages, and more.
- **Automated Trade Execution**: Integrates with broker APIs (like Alpaca) for automated trading decisions.
- **Backtesting**: Includes the ability to backtest strategies on historical data to evaluate their performance before going live.
- **Risk Management**: Offers dynamic stop-loss and take-profit strategies.
## Project Structure
```plaintext
ai_trading_assistant/
│
├── data/                         # Directory to store datasets, historical data
│   ├── gold_data.csv              # Example dataset for gold prices
│   └── processed_data.csv         # Processed data for training
│
├── models/                       # Trained AI models (saved models)
│   ├── model.pkl                  # Trained ML model saved here
│   └── scaler.pkl                 # Scaler for data normalization
│
├── notebooks/                    # Jupyter notebooks for testing and experimenting
│   └── exploratory_analysis.ipynb # Initial analysis of data
│
├── src/                          # Core Python scripts for data processing, ML model, etc.
│   ├── __init__.py               # Package initializer
│   ├── data_loader.py            # Script to load and preprocess data
│   ├── feature_engineering.py    # Feature generation (technical indicators)
│   ├── model.py                  # Model training and prediction
│   ├── backtest.py               # Backtesting the strategy
│   ├── trade_bot.py              # Real-time trading using broker API
│   └── utils.py                  # Utility functions (logging, configuration loading)
│
├── tests/                        # Unit tests for project components
│   ├── test_data_loader.py       # Test cases for data loader
│   └── test_model.py             # Test cases for model
│
├── .gitignore                    # Files to ignore in version control (e.g., virtualenv, data files)
├── README.md                     # Project documentation (this file)
├── requirements.txt              # Python dependencies
├── config.yaml                   # Configuration file for customizable settings
└── main.py                       # Main script to run the trading assistant
```

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ai_trading_assistant.git
    cd ai_trading_assistant
    ```

2. Set up a virtual environment (recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. **Preprocess Data**: Run the `data_loader.py` script to download and preprocess historical data.
    ```bash
    python src/data_loader.py
    ```

2. **Train the Model**: Train the machine learning model using the prepared dataset.
    ```bash
    python src/model.py
    ```

3. **Backtest the Strategy**: Test the performance of the trading strategy.
    ```bash
    python src/backtest.py
    ```

4. **Start Real-Time Trading**: Launch the AI trading bot for live trading.
    ```bash
    python main.py
    ```

## Configuration
Modify the `config.yaml` file to change parameters such as API keys, trading symbol, or model settings.

## Contributing
Feel free to submit issues or pull requests if you'd like to contribute!

## License
This project is licensed under the MIT License.
