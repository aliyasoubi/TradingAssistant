import os
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

def load_data():
    """
    Loads the labeled dataset for training the model.
    
    Returns:
        X (pandas.DataFrame): The feature matrix with technical indicators.
        y (pandas.Series): The target labels (0 for down, 1 for up).
    """
    data = pd.read_csv('C:\\Users\\Ali\\Projects\\TradingAssistant\\data\\labeled_data.csv')
    features = ['RSI', 'MACD', 'MACD_signal', 'SMA_50', 'SMA_200']
    X = data[features]
    y = data['Target']
    return X, y

def train_model(X, y):
    """
    Trains a Random Forest Classifier model on the dataset.
    
    Parameters:
        X (pandas.DataFrame): Feature matrix.
        y (pandas.Series): Target labels.
    
    Returns:
        model: Trained Random Forest model.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print(classification_report(y_test, y_pred))

    # Create the models directory if it doesn't exist
    model_dir = 'C:\\Users\\Ali\\Projects\\TradingAssistant\\models'
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    # Save the model
    model_path = os.path.join(model_dir, 'random_forest_model.pkl')
    joblib.dump(model, model_path)
    print(f"Model saved as {model_path}")

    return model

if __name__ == "__main__":
    X, y = load_data()
    train_model(X, y)
