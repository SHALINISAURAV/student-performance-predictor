# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from pathlib import Path


def load_data(path):
    """
    Load dataset from CSV file
    """

    df = pd.read_csv(path)

    return df


# Function for preprocessing data
def preprocess_data(df):
    """
    Preprocess dataset:
    - Encode categorical variables
    - Split features and target
    """

    # Create copy
    df = df.copy()

    # Encode categorical columns
    label_encoder = LabelEncoder()

    categorical_columns = df.select_dtypes(include='object').columns

    for col in categorical_columns:
        df[col] = label_encoder.fit_transform(df[col])

    # Features
    X = df.drop('math score', axis=1)

    # Target variable
    y = df['math score']

    return X, y


# Function to split dataset
def split_data(X, y):
    """
    Split data into train and test sets
    """

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    return X_train, X_test, y_train, y_test


# Run preprocessing directly
if __name__ == "__main__":

    # Get project root directory
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Correct dataset path
    data_path = BASE_DIR / 'data/raw/StudentsPerformance.csv'

    # Load dataset
    df = load_data(data_path)

    # Preprocess data
    X, y = preprocess_data(df)

    # Split dataset
    X_train, X_test, y_train, y_test = split_data(X, y)

    # Print dataset shapes
    print("X_train shape:", X_train.shape)
    print("X_test shape:", X_test.shape)

    print("Preprocessing completed successfully!")