# main.py
import yaml
from src import data_loader, model, trade_bot


def load_config():
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)
    return config


def main():
    config = load_config()

    # Load and preprocess data
    data = data_loader.load_data(config['trading']['symbol'], config['trading']['time_interval'])

    # Train or load model
    trained_model = model.train_model(data)

    # Run the trading bot
    trade_bot.run(trained_model, config)


if __name__ == "__main__":
    main()
