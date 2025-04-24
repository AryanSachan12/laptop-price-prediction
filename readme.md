# 💻 Laptop Price Prediction App

This is a Streamlit-based web application that predicts the **price of laptops** based on their specifications. The prediction model is built using a **Ridge Regression** algorithm trained on a cleaned and feature-engineered dataset.

---

## 🚀 Features

- 🔍 Predict laptop prices using specs like CPU, RAM, GPU, screen resolution, etc.
- 📊 Cleaned and preprocessed dataset with feature extraction and transformation
- 🎛️ User-friendly interface for inputting laptop configurations
- 🧠 Model pipeline built using **scikit-learn**
- 📈 Exploratory Data Analysis (EDA) using `seaborn` and `matplotlib`

---

## 📦 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend / ML**: Python, Pandas, NumPy, Scikit-learn
- **Visualization**: Seaborn, Matplotlib

---

## 📁 Project Structure

```
laptop-price-prediction/
│
├── app.py                    # Main Streamlit app
├── model.pkl
├── model_training.ipynb
├── dataset/
│   └── laptop_data.csv           # Original dataset
│   └── cleaned_laptop_data.csv   # Cleaned dataset
├── requirements.txt          # Python dependencies
└── README.md                 # Project description
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git https://github.com/AryanSachan12/laptop-price-prediction
cd laptop-price-prediction
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

### 3. Install dependencies

```bash
pip install --upgrade pip
sudo apt-get install python3-distutils  # Fix for distutils error if needed
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

---

## 📊 Sample Input Fields

- Brand
- RAM (GB)
- Operating System
- Weight (kg)
- Touchscreen (Yes/No)
- Screen Resolution
- CPU Type
- GPU Brand
- HDD/SSD size

---

## 🧠 Model Details

- Model: Ridge Regression
- Evaluation: R² score, RMSE
- Trained on ~1300 laptop entries after cleaning and feature engineering

---

## 🤝 Contribution

Feel free to fork the repo, suggest features, or raise issues. PRs are welcome!

---

## 📃 License

MIT License © 2025 [Your Name]

---

## 🌐 Live Demo (Optional)

🔗 [Deployed on Streamlit Cloud](https://aryansachan12-laptop-price-prediction-app-zjjerp.streamlit.app/)
