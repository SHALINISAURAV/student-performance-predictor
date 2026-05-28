# Import required libraries
import joblib
from pathlib import Path

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# Import custom preprocessing functions
from data_preprocessing import load_data
from data_preprocessing import preprocess_data
from data_preprocessing import split_data


# MAIN EXECUTION
if __name__ == "__main__":

    # Get project root directory
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Dataset path
    data_path = BASE_DIR / 'data/raw/StudentsPerformance.csv'

    # Load dataset
    df = load_data(data_path)

    # Preprocess data
    X, y = preprocess_data(df)

    # Split dataset
    X_train, X_test, y_train, y_test = split_data(X, y)

    # Create Linear Regression model
    model = LinearRegression()

    # Train model
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    # Evaluate model
    mae = mean_absolute_error(y_test, predictions)

    mse = mean_squared_error(y_test, predictions)

    r2 = r2_score(y_test, predictions)

    # Print evaluation metrics
    print("Model Evaluation Results")
    print("-" * 30)

    print("MAE:", mae)

    print("MSE:", mse)

    print("R2 Score:", r2)

    # Create models directory if not exists
    models_dir = BASE_DIR / 'models'

    models_dir.mkdir(exist_ok=True)

    # Save trained model
    model_path = models_dir / 'model.pkl'

    joblib.dump(model, model_path)

    print("\\nModel saved successfully!")

    print(f"Model path: {model_path}")