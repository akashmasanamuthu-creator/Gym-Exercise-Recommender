# 🏋️ Gym Exercise Recommender

A Machine Learning web app that recommends personalized gym exercises based on your fitness preferences.

## 📌 Features
- Select Workout Type, Body Part, Equipment and Level
- Get Top 5 personalized exercise recommendations
- Built with KNN (Unsupervised Machine Learning)

## 🛠️ Tech Stack
- Python
- Scikit-learn (KNN)
- Pandas
- Streamlit
- Pickle

## 📂 Dataset
- Source: Kaggle - Mega Gym Dataset
- 2886 exercises across 17 body parts

## ⚙️ How to Run Locally
git clone https://github.com/yourusername/gym-recommender.git
cd gym-recommender
pip install -r requirements.txt
streamlit run app.py

## 🧠 How it Works
1. User selects fitness preferences
2. Input is encoded using Label Encoder
3. KNN finds 5 most similar exercises from dataset
4. Results displayed as an interactive Streamlit app

## 👨‍💻 Author
Akash Masanamuthu
