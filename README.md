# AI Trading Assistant for Short-Term Trading

## Overview
This project is an assistant program designed to help traders identify potential entry points for scalping and low-timeframe trading. The assistant uses multiple technical indicators like RSI, MACD, Simple Moving Averages (SMA), and Bollinger Bands to analyze market trends and provide confirmation signals for potential long or short positions.

Additionally, the assistant aims to help traders avoid emotional decision-making by providing a trade confirmation system based on data-driven signals from these indicators. The project focuses on 1-minute and 5-minute timeframes to match the fast pace of scalping strategies.

This tool is not a trading bot. Instead, it serves as an assistant to confirm trade ideas and provide suggestions based on the analysis of various indicators.

## Features
- **Technical Indicator Analysis**: Provides real-time analysis using key technical indicators such as RSI, MACD, Moving Averages, and Bollinger Bands.
- **Confirmation Signals**: Generates buy/sell suggestions based on a combination of indicators to assist in scalping strategies.
- **Customizable Timeframes**: Optimized for 1-minute to 15-minute trading intervals.
- **News Alerts (Upcoming)**: Future enhancements will include news alerts to inform traders of critical market events.
- **Risk Management**: Provides suggestions for stop-loss and take-profit levels to help manage risks.
## Project Structure
```plaintext
TradingAssistant/
│
├── data/                         # Stores raw and processed market data
│   ├── BTC-USD_data.csv           # Example data for Bitcoin
│   └── BTC-USD_processed_data.csv # Processed data with technical indicators
│
├── models/                       # Folder for saved machine learning models (if applicable)
│
├── notebooks/                    # Jupyter notebooks for analysis and experimentation
│   └── exploratory_analysis.ipynb # Exploratory data analysis and visualization
│
├── src/                          # Core Python scripts
│   ├── __init__.py               # Package initializer
│   ├── data_loader.py            # Download and preprocess market data
│   ├── feature_engineering.py    # Script to calculate technical indicators
│   ├── backtest.py               # Backtesting strategies using historical data
│   └── utils.py                  # Utility functions like configuration and logging
│
├── config.yaml                   # Configuration settings for assets, timeframes, etc.
├── .gitignore                    # Files and directories to ignore in version control
├── README.md                     # This file
└── requirements.txt              # Project dependencies

```

## Installation
To get started with this project, follow these steps:
1. Clone the repository:
    ```bash
    git clone https://github.com/aliyasoubi/TradingAssistant.git
    cd TradingAssistant
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
4. Install TA-Lib (if not included in requirements):
    ```bash
    pip install TA-Lib
    ```
## Configuration
Update the `config.yaml` file with the project base directory and other configurations.
    ```bash
     # Example config.yaml
    BASE_DIR: "C:/Users/YourName/Projects/TradingAssistant"
    TRADING_SYMBOL: "BTC-USD"
    INTERVAL: "1m"
    INDICATORS:
    - RSI
    - MACD
    - SMA_50
    - SMA_200
    - BollingerBands
    ```    
The configuration file allows you to:
- Change the trading symbol (e.g., BTC-USD, XAU-USD, etc.).
- Adjust the time intervals (e.g., 1-minute, 5-minute data).
- Specify which technical indicators to use.


## Usage
1. **Download Real-Time Data**: Run the `data_loader.py` script to download and preprocess historical data.
    ```bash
    py src/data_loader.py
    ```
    This script downloads the data and saves it to the data/ directory as a CSV file. You can modify the symbol (e.g., BTC-USD, AAPL) and the interval (1-minute, 5-minute) based on your preferences.

2. **Calculate Technical Indicators**: Generate and add technical indicators (e.g., RSI, MACD) to your data using the `feature_engineering.py` script:
    ```bash
    py src/feature_engineering.py
    ```
    This will add the indicators to the data and save the processed data as BTC-USD_processed_data.csv (or the asset you’re analyzing).
3. **Analyze the Data**: Test how your trading strategy performs on historical data:
    ```bash
    py src/backtest.py
    ```

4. **Run the Signal Generation and Confirmation**: After running the feature_engineering.py script to generate the indicator signals, run the signal_confirmation.py script to confirm the signals:

    ```bash
    py src/signal_confirmation.py
    ```
    This will output a CSV file (BTC-USD_confirmed_signals.csv) with final buy/sell confirmations based on the combined indicators.

## Future Phases
1. **Signal Generation & Trade Confirmation (Phase 2)**: The next phase will implement logic to generate buy/sell signals based on multiple indicators and provide a confidence score for potential trades.

2. **Real-Time Alerts (Phase 3)**: We plan to add real-time alerts to notify traders when a trade setup matches predefined conditions.
    ```
    This will add the indicators to the data and save the processed data as BTC-USD_processed_data.csv (or the asset you’re analyzing).
3. **News Monitoring and Sentiment Analysis (Phase 4)**: This phase will focus on monitoring market news and alerting the user of any important developments affecting the assets being traded.

## Branch Naming Convention
For easy collaboration and code tracking, follow these branch naming conventions:
- **feature/{feature-name}**: For new features or enhancements (e.g., feature/news-alerts).
- **bugfix/{bug-description}**: For fixing bugs (e.g., bugfix/fix-rsi-calculation).
- **hotfix/{urgent-fix}**: For urgent or critical fixes (e.g., hotfix/api-key-error).
- **test/{testing-branch}**: For testing purposes (e.g., test/indicator-combination).

## Contributing
Contributions are welcome! If you would like to contribute to the project, please submit a pull request or open an issue for discussion.

## License
This project is licensed under the MIT License.

## Additional Notes
- This program is meant for assisting traders in making more informed decisions based on technical analysis, and it is not a fully automated trading bot.
- Always backtest your strategies and validate the results in a simulated environment before applying them to live trades.
- The assistant is optimized for scalping and short-term trading but can be extended for other types of trading with some modifications.