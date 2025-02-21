import os
import pandas as pd
import pickle
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Define file paths
test_file = "data/test_cases.csv"
output_file = "data/test_predictions.csv"
model_file = "models/outcome_classifier.pkl"
vectorizer_file = "models/tfidf_vectorizer.pkl"

# ✅ Check if required files exist
if not os.path.exists(test_file):
    print(f"❌ Test dataset not found: {test_file}")
    exit()

if not os.path.exists(model_file) or not os.path.exists(vectorizer_file):
    print("❌ Model or vectorizer missing! Train the model first.")
    exit()

# ✅ Load test dataset
test_df = pd.read_csv(test_file)

# ✅ Load trained model & vectorizer
model = pickle.load(open(model_file, "rb"))
vectorizer = pickle.load(open(vectorizer_file, "rb"))

# ✅ Ensure 'text' column exists
if "text" not in test_df.columns:
    print("❌ 'text' column missing in test_cases.csv. Check file format.")
    exit()

# Convert judgment texts into feature vectors
test_df["text"] = test_df["text"].astype(str).fillna("")
test_vectors = vectorizer.transform(test_df["text"])

# ✅ Predict outcomes
test_df["predicted_outcome"] = model.predict(test_vectors)
test_df["predicted_label"] = test_df["predicted_outcome"].apply(
    lambda x: "Plaintiff Wins ✅" if x == 1 else "Defendant Wins ❌"
)

# ✅ Save predictions
test_df.to_csv(output_file, index=False)
print(f"✅ Predictions saved to {output_file}")

# ✅ Display sample results
print(test_df[["filename", "predicted_label"]].head(10))

# ✅ If actual outcomes exist, clean NaN values before accuracy calculation
if "actual_outcome" in test_df.columns:
    test_df = test_df.dropna(subset=["actual_outcome"])  # Remove NaN rows
    test_df["actual_outcome"] = test_df["actual_outcome"].astype(int)
    test_df["predicted_outcome"] = test_df["predicted_outcome"].astype(int)

    accuracy = accuracy_score(test_df["actual_outcome"], test_df["predicted_outcome"])
    print(f"\n✅ Model Accuracy on Real Cases: {accuracy:.4f}")

    print("\n🔍 Classification Report:")
    print(classification_report(test_df["actual_outcome"], test_df["predicted_outcome"]))

    print("\n📊 Confusion Matrix:")
    print(confusion_matrix(test_df["actual_outcome"], test_df["predicted_outcome"]))
else:
    print("\n⚠️ No actual outcomes provided. Skipping accuracy check.")