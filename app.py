import os
import pickle
import fitz  # PyMuPDF for PDF text extraction
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS

# ✅ Initialize Flask App
app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# ✅ Load Model & Vectorizer
model_path = "models/outcome_classifier.pkl"
vectorizer_path = "models/tfidf_vectorizer.pkl"

if not os.path.exists(model_path) or not os.path.exists(vectorizer_path):
    raise FileNotFoundError("❌ Model or Vectorizer missing! Train the model first.")

model = pickle.load(open(model_path, "rb"))
vectorizer = pickle.load(open(vectorizer_path, "rb"))

# ✅ Function to Extract Text from PDFs
def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text("text") + "\n"
    except Exception as e:
        print(f"⚠️ Error reading {pdf_path}: {e}")
    return text.strip()

# ✅ API Endpoint for Prediction
@app.route("/predict", methods=["POST"])
def predict():
    print("📩 Received Request Headers:", request.headers)
    print("📂 Received Request Files:", request.files)  # Debugging Line

    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    pdf_file = request.files["file"]
    if pdf_file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    # Save and process file
    temp_pdf_path = "temp_uploaded.pdf"
    pdf_file.save(temp_pdf_path)

    extracted_text = extract_text_from_pdf(temp_pdf_path)
    os.remove(temp_pdf_path)  # Clean up

    if not extracted_text:
        return jsonify({"error": "No text extracted from PDF"}), 400

    text_vector = vectorizer.transform([extracted_text])
    prediction = model.predict(text_vector)[0]
    result = "Plaintiff Wins ✅" if prediction == 1 else "Defendant Wins ❌"

    return jsonify({"prediction": result})

# ✅ Run the API
if __name__ == "__main__":
    app.run(debug=True, port=5000)
