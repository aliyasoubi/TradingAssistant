import os
import pandas as pd
import joblib
import yaml
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load configuration from config.yaml
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Fetch BASE_DIR from the loaded config
BASE_DIR = config['BASE_DIR']

def load_data():
    """
    Loads the labeled dataset for training the model.
    
    Returns:
        X (pandas.DataFrame): The feature matrix with technical indicators.
        y (pandas.Series): The target labels (0 for down, 1 for up).
    """
    # Construct the relative path to the labeled data file
    data_path = os.path.join(BASE_DIR, 'data', 'labeled_data.csv')
    
    # Load the labeled data
    data = pd.read_csv(data_path)
    
    # Define the features (technical indicators) and the target (price direction)
    features = ['RSI', 'MACD', 'MACD_signal', 'SMA_50', 'SMA_200']
    X = data[features]  # Feature matrix
    y = data['Target']  # Target labels (0 or 1)
    
    return X, y

def train_model(X, y):
    """
    Trains a Random Forest Classifier model on the dataset.
    
    Parameters:
        X (pandas.DataFrame): Feature matrix (technical indicators).
        y (pandas.Series): Target labels (0 for down, 1 for up).
    
    Returns:
        model: Trained Random Forest model.
    """
    # Split the data into training and test sets (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the Random Forest Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)
    
    # Evaluate the model's performance
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print(classification_report(y_test, y_pred))

    # Create the models directory if it doesn't exist
    model_dir = os.path.join(BASE_DIR, 'models')
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    # Save the model
    model_path = os.path.join(model_dir, 'random_forest_model.pkl')
    joblib.dump(model, model_path)
    print(f"Model saved as {model_path}")

    return model

if __name__ == "__main__":
    # Load the data with features and labels
    X, y = load_data()
    
    # Train the model
    train_model(X, y)