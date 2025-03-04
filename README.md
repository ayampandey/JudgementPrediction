# 🏛️ AI-Powered Judgment Prediction System

This project is an AI-based **Judgment Prediction System** that analyzes legal case documents and predicts the **outcome** (whether the plaintiff or defendant will win). It utilizes **Natural Language Processing (NLP)** and **Machine Learning** techniques for classification.

---

## 🚀 Features
- 📄 **Extracts text** from PDF court judgments.
- 🧠 **Predicts case outcomes** using a trained ML model.
- 📊 **Uses NLP techniques** for text processing.
- 🌐 **Flask-based API** for easy integration.

---

## 🛠️ Tech Stack
- **Python** (NLP & ML)
- **Flask** (API Backend)
- **scikit-learn** (Model Training)
- **spaCy** (Text Processing)
- **TfidfVectorizer** (Feature Extraction)
- **Jupyter Notebook** (Model Development)
- **Git & GitHub** (Version Control)

---

## 📥 Dataset Download
Due to GitHub file size limitations, the **dataset and processed files** are stored externally.

📂 **Download `data.zip` (5GB)** 👉 https://www.kaggle.com/datasets/vangap/indian-supreme-court-judgments

After downloading:
1. Extract `data.zip`
2. Place the extracted `data/` folder inside the project directory.

---

## 🔧 Installation Guide
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/ayampandey/JudgementPrediction.git
cd JudgementPrediction
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies



### 4️⃣ Run the Flask API
```sh
python app.py
```

---

## 📡 API Endpoints
| Method | Endpoint       | Description               |
|--------|---------------|---------------------------|
| POST   | `/predict`    | Upload a PDF and predict outcome |

#### Example Usage:
```python
import requests

url = "http://127.0.0.1:5000/predict"
files = {"file": open("sample_judgment.pdf", "rb")}
response = requests.post(url, files=files)
print(response.json())
```

---

## 🛠️ Project Structure
```
JudgementPrediction/
│-- app.py                   # Flask API
│-- model.pkl                 # Trained ML model
│-- extract_text.py           # PDF text extraction script
│-- data/                     # Contains court judgment texts (Not included in repo)
│-- static/                   # Frontend assets (if applicable)
│-- templates/                # HTML Templates (if applicable)
│-- README.md                 # Project Documentation
```

---

## 🏗️ Future Enhancements
- ✅ Improve model accuracy with **BERT** or **Transformer-based models**.
- ✅ Expand dataset with **more diverse judgments**.
- ✅ Implement a **web UI** for easier access.

---

