# 🎓 StudentPerformance -- End-to-End Machine Learning Project

This repository contains a fully production-ready **End-to-End Machine
Learning system** that predicts **student academic performance** based
on demographic, socio-economic, and educational factors.

The project includes:\
✔ Automated ML pipeline (ingestion → transformation → training →
prediction)\
✔ Modular Python package (`src/`)\
✔ Streamlit/Flask-based web app\
✔ CI/CD workflow\
✔ Deployment setup using **Render**\
✔ Docker containerization

## 📂 Repository Structure

    StudentPerformance/
    ├── .github/workflows/
    │   └── main_studentperformance.yml
    ├── artifacts/
    ├── catboost_info/
    ├── notebook/
    │   └── Data ingestion.ipynb
    ├── src/
    │   ├── components/
    │   ├── pipeline/
    │   ├── utils.py
    │   ├── exception.py
    │   └── logger.py
    ├── templates/
    ├── static/
    ├── app.py
    ├── requirements.txt
    ├── render.yaml
    ├── Dockerfile
    ├── setup.py
    └── README.md

## 📘 Project Description

Dataset features: - gender\
- race_ethnicity\
- parental_level_of_education\
- lunch\
- test_preparation_course\
- math_score\
- reading_score\
- writing_score

## 🧠 Machine Learning Pipeline

1.  Data Ingestion\
2.  Data Transformation\
3.  Model Training\
4.  Model Prediction

## 🌐 Web Application

A Flask-based UI for predictions.

Run:

    python app.py

## 🚀 Deployment (Render)

Uses: - render.yaml\
- Dockerfile

## 🛠 Installation

    git clone your_repo
    cd studentperformance
    pip install -r requirements.txt

## 👨‍💻 Author

Venkatesh Samala
