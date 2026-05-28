# Import required libraries
import joblib
import pandas as pd

from pathlib import Path


# Get project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Correct model path
model_path = BASE_DIR / 'models/model.pkl'

# Load trained model
model = joblib.load(model_path)


def predict_score(input_data):
    """
    Predict student score
    """

    # Convert input into DataFrame
    input_df = pd.DataFrame([input_data])

    # Predict score
    prediction = model.predict(input_df)

    # Return predicted value
    return prediction[0]


# Test prediction directly
if __name__ == "__main__":

    sample_data = {
        'gender': 0,
        'race/ethnicity': 2,
        'parental level of education': 1,
        'lunch': 0,
        'test preparation course': 1,
        'reading score': 72,
        'writing score': 74
    }

    predicted_score = predict_score(sample_data)

    print("Predicted Math Score:", predicted_score)