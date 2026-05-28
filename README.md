# Student Performance Predictor

## Overview

This project predicts student math scores using Machine Learning techniques based on student-related features such as reading score, writing score, parental education, lunch type, and test preparation course.

The project includes:

* Data preprocessing
* Model training
* Model evaluation
* Prediction pipeline
* Streamlit web application

---

## Features

* Data preprocessing using Pandas
* Label encoding for categorical features
* Linear Regression model
* Streamlit interactive frontend
* Student performance categorization
* Model saving using Joblib

---

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib

---

## Project Structure

```text
student-performance-predictor/
│
├── data/
│   └── raw/
│       └── StudentsPerformance.csv
│
├── src/
│   ├── data_preprocessing.py
│   ├── train.py
│   ├── predict.py
│   └── utils.py
│
├── app/
│   └── app.py
│
├── models/
│   └── model.pkl
│
├── notebooks/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone repository:

```bash
git clone YOUR_GITHUB_REPO_LINK
```

Move into project folder:

```bash
cd student-performance-predictor
```

Create virtual environment:

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\\Scripts\\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Train Model

Run model training:

```bash
python src/train.py
```

---

## Run Streamlit App

```bash
streamlit run app/app.py
```

---

## Model Evaluation Metrics

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* R2 Score

---

## Future Improvements

* Random Forest Regressor
* XGBoost Regressor
* Hyperparameter tuning
* Better UI/UX
* Docker deployment
* MLflow integration
* FastAPI backend
* Feature importance visualization

---

## Learning Outcomes

This project helped in understanding:

* End-to-end Machine Learning workflow
* Data preprocessing
* Feature engineering
* Model training and evaluation
* Streamlit deployment
* GitHub workflow
* Project structuring

---

## Author

Shalini Saurav
