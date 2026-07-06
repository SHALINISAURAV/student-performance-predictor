<div align="center">

# 🎓 Student Performance Predictor

### *Turning academic data points into early warnings and real support.*

An end-to-end Machine Learning project that predicts student math performance using academic and demographic features — helping schools spot at-risk students before it's too late.

<br>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<br>

[**🚀 Live Demo**](https://your-streamlit-app-link.streamlit.app) &nbsp;•&nbsp; [**📁 GitHub Repository**](#) &nbsp;•&nbsp; [**📊 EDA Notebook**](notebooks/eda.ipynb)

</div>

<br>

---

## 📚 Table of Contents

- [Project Overview](#-project-overview)
- [Problem Definition](#1️⃣-problem-definition)
- [Business Understanding](#2️⃣-business-understanding)
- [ML Problem Type](#3️⃣-ml-problem-type)
- [Tech Stack](#4️⃣-tech-stack)
- [Recommended Dataset](#5️⃣-recommended-dataset)
- [Project Architecture](#6️⃣-final-project-architecture)
- [Exploratory Data Analysis](#7️⃣-exploratory-data-analysis-eda)
- [Sample EDA Graphs](#8️⃣-sample-eda-graphs)
- [Data Preprocessing](#9️⃣-data-preprocessing)
- [Model Building](#-model-building)
- [Model Evaluation](#-model-evaluation)
- [Streamlit Web Application](#-streamlit-web-application)
- [Live Deployment](#-live-deployment)
- [Installation Guide](#-installation-guide)
- [Run Model Training](#-run-model-training)
- [Run Streamlit App](#-run-streamlit-app)
- [Future Improvements](#-future-improvements)
- [Learning Outcomes](#-learning-outcomes)
- [Screenshots](#-screenshots)
- [Author](#-author)

---

## 📌 Project Overview

The **Student Performance Predictor** is an end-to-end Machine Learning project that predicts student math performance using academic and demographic features such as reading score, writing score, parental education level, lunch type, and test preparation course.

Behind every number in a gradebook is a story — a student who needed more support, a preparation course that made the difference, a pattern nobody noticed until it was too late. This project turns those scattered signals into a single, actionable prediction, so intervention can happen *before* the final exam instead of after.

This project demonstrates the complete ML workflow including:

- 🧹 Data preprocessing
- 🔍 Exploratory Data Analysis (EDA)
- 🛠️ Feature engineering
- 🤖 Model training
- 📊 Model evaluation
- 🔮 Prediction pipeline
- 🌐 Streamlit deployment
- 🗂️ GitHub version control

---

## 1️⃣ Problem Definition

### 🧩 Problem Statement

Students often struggle to identify whether they are academically at risk **before** final examinations — by the time performance dips are obvious, opportunities for intervention have often already passed.

Educational institutions and teachers require an intelligent system that can:

- 📊 Analyze student-related factors
- 🔮 Predict academic performance
- 🚨 Identify low-performing students early
- 🤝 Enable proactive academic support

The goal of this project is to build a Machine Learning model that predicts student math scores using features like:

| Feature | Description |
|---|---|
| 📖 Reading Score | Marks scored in reading |
| ✍️ Writing Score | Marks scored in writing |
| 🧑 Gender | Student gender |
| 🎓 Parental Education | Parent's education level |
| 🍽️ Lunch Type | Standard / free-reduced lunch |
| 📚 Test Preparation Course | Completed or not |
| 🌍 Race/Ethnicity | Demographic group |

---

## 2️⃣ Business Understanding

### 💡 Why This Project Matters

This project can help:

- 🏫 **Schools** identify academically weak students early
- 👩‍🏫 **Teachers** provide targeted, individualized support
- 👨‍👩‍👧 **Parents** monitor student progress proactively
- 💻 **Educational platforms** personalize learning strategies at scale

### 🌍 Real-World Applications

- 🚨 Student risk analysis
- 📈 Academic performance monitoring
- 🎯 Personalized education systems
- 📊 Educational analytics dashboards

> *A model that predicts a score is useful. A model that predicts a score early enough to change it is transformative.*

---

## 3️⃣ ML Problem Type

### ✅ Regression Problem

Because the target variable — **Math Score** — is a continuous numerical value, this is framed as a **regression** problem rather than classification.

The model predicts an **exact numerical score**, not just a category like "pass/fail."

#### Example

| Input Features | Predicted Math Score |
|---|---|
| Reading = 70, Writing = 75 | **72.4** |
| Reading = 45, Writing = 50 | **48.1** |
| Reading = 90, Writing = 88 | **89.3** |

---

## 4️⃣ Tech Stack

### 🔹 Core Technologies

| Category | Tools |
|---|---|
| **Language** | Python |
| **Data Handling** | Pandas, NumPy |
| **Machine Learning** | Scikit-learn |
| **Visualization** | Matplotlib, Seaborn |
| **Model Persistence** | Joblib |

### 🔹 Deployment

- 🌐 Streamlit

### 🔹 Version Control

- 🗂️ Git
- 🐙 GitHub

---

## 5️⃣ Recommended Dataset

### 📊 Student Performance Dataset

**Source:** Kaggle Student Performance Dataset

The dataset contains:

- 👤 Demographic information
- 📚 Academic scores
- 🎓 Education-related attributes

### Main Features

| Feature | Description |
|---|---|
| `gender` | Student gender |
| `race/ethnicity` | Student group |
| `parental level of education` | Parent education level |
| `lunch` | Lunch type |
| `test preparation course` | Preparation status |
| `reading score` | Reading marks |
| `writing score` | Writing marks |
| `math score` | 🎯 Target variable |

---

## 6️⃣ Final Project Architecture

```text
student-performance-predictor/
│
├── screenshots/
│   ├── Correlation Heatmap.png
│   ├── Math Score Distribution.png
│   ├── Boxplot of Scores.png
│   └── app_ui.png
│
├── data/
│   └── raw/
│       └── StudentsPerformance.csv
│
├── notebooks/
│   └── eda.ipynb
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
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 7️⃣ Exploratory Data Analysis (EDA)

EDA was performed to:

- 📊 Understand data distribution
- 🔍 Identify patterns
- 🔗 Analyze feature relationships
- 🚨 Detect outliers
- 🧮 Study correlations

### 📈 Visualizations Used

**Distribution Plots**
- Math score distribution
- Reading score distribution
- Writing score distribution

**Correlation Heatmap** — used to analyze feature relationships

**Boxplots** — used to identify score spread and outliers

**Countplots** — used for categorical feature analysis

---

## 8️⃣ Sample EDA Graphs

### 📊 Correlation Heatmap

![Correlation Heatmap](./screenshots/screenshots%20Correlation%20Heatmap.png)

*Reveals how strongly reading and writing scores correlate with math performance — a key insight driving feature selection.*

---

### 📈 Math Score Distribution

![Math Score Distribution](./screenshots/screenshots%20Math%20Score%20Distribution.png)

*Shows the overall spread of math scores across the student population.*

---

### 📉 Boxplot Analysis

![Boxplot Analysis](./screenshots/screenshots%20Boxplot%20of%20Scores.png)

*Highlights score spread and flags potential outliers across subjects.*

---

## 9️⃣ Data Preprocessing

The following preprocessing steps were applied:

- 🏷️ Handling categorical variables
- 🔢 Label Encoding
- 🎯 Feature selection
- ✂️ Train-test splitting

### Train-Test Split

| Split | Percentage |
|---|---|
| 🏋️ Training Data | 80% |
| 🧪 Testing Data | 20% |

---

## 🔟 Model Building

### 🤖 Model Used: Linear Regression

Linear Regression was used as the baseline model for predicting student scores — chosen for its interpretability, speed, and effectiveness as a first benchmark before exploring more complex models.

---

## 1️⃣1️⃣ Model Evaluation

The model was evaluated using:

- 📏 Mean Absolute Error (MAE)
- 📐 Mean Squared Error (MSE)
- 📊 R² Score

### Evaluation Metrics

| Metric | Purpose |
|---|---|
| **MAE** | Average prediction error |
| **MSE** | Squared prediction error (penalizes larger errors) |
| **R² Score** | Overall model accuracy / goodness of fit |

---

## 1️⃣2️⃣ Streamlit Web Application

An interactive Streamlit web app was built where users can:

- ✍️ Enter student details
- 🔮 Predict math score
- 🏷️ View performance category

### Features

- 🎨 User-friendly UI
- ⚡ Real-time prediction
- 🏷️ Performance categorization (e.g., At Risk / Average / High Performer)

---

## 1️⃣3️⃣ Live Deployment

### 🚀 Streamlit Deployment Link

```text
https://your-streamlit-app-link.streamlit.app
```

> 🔧 Replace this placeholder with your actual deployed Streamlit app URL once live.

---

## 1️⃣4️⃣ Installation Guide

### Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### Move Into Project Folder

```bash
cd student-performance-predictor
```

### Create Virtual Environment

**Mac/Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 1️⃣5️⃣ Run Model Training

```bash
python src/train.py
```

---

## 1️⃣6️⃣ Run Streamlit App

```bash
streamlit run app/app.py
```

---

## 1️⃣7️⃣ Future Improvements

- [ ] 🌲 Random Forest Regressor
- [ ] ⚡ XGBoost Regressor
- [ ] 🎛️ Hyperparameter tuning
- [ ] 🎨 Better UI/UX
- [ ] 📊 Model comparison dashboard
- [ ] 🔍 Feature importance visualization
- [ ] 📦 MLflow integration
- [ ] 🐳 Docker deployment
- [ ] ⚙️ FastAPI backend
- [ ] 🔄 CI/CD pipeline

---

## 1️⃣8️⃣ Learning Outcomes

This project helped in understanding:

- 🔄 End-to-end Machine Learning workflow
- 🔍 EDA and visualization
- 🧹 Data preprocessing
- 🛠️ Feature engineering
- 📈 Regression modeling
- 📊 Model evaluation
- 🌐 Streamlit deployment
- 🗂️ GitHub workflow
- 🏗️ ML project structuring

---

## 1️⃣9️⃣ Screenshots

### 🖥️ Streamlit App UI

![Streamlit App UI](./screenshots/screenshots%20app%20ui.png)

---

## 2️⃣0️⃣ Author

<div align="center">

### 👩‍💻 Shalini Saurav

**BTech CSE (Data Science) Student**

Passionate about:

🤖 Artificial Intelligence &nbsp;•&nbsp; 📊 Machine Learning &nbsp;•&nbsp; 🔬 Data Science &nbsp;•&nbsp; ✨ Generative AI &nbsp;•&nbsp; 🚀 Entrepreneurship

</div>

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star on GitHub!

*Every star helps more students benefit from proactive academic support.*

</div>

