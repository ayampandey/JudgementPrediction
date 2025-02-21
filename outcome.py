import pandas as pd
from sklearn.utils import resample
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os

# ✅ Load the dataset
df = pd.read_csv("data/labeled_judgments.csv")

# ✅ Drop NaN rows (cases with unknown outcomes)
df = df.dropna(subset=["outcome"])

# ✅ Convert outcome to integer
df["outcome"] = df["outcome"].astype(int)

# ✅ Clean text (ensure text column is string)
df["clean_text"] = df["text"].astype(str)

# ✅ Define TF-IDF vectorizer
tfidf = TfidfVectorizer(max_features=5000)

# ✅ Balance Data (Oversample plaintiff wins)
df_majority = df[df["outcome"] == 0]  # Defendant wins (0)
df_minority = df[df["outcome"] == 1]  # Plaintiff wins (1)

df_minority_upsampled = resample(df_minority,
                                 replace=True,
                                 n_samples=len(df_majority),
                                 random_state=42)

df_balanced = pd.concat([df_majority, df_minority_upsampled]).sample(frac=1, random_state=42)

# ✅ TF-IDF transformation
X_balanced = tfidf.fit_transform(df_balanced["clean_text"])
y_balanced = df_balanced["outcome"]

# ✅ Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_balanced, y_balanced, test_size=0.2, random_state=42)

# ✅ Train Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# ✅ Predict & Evaluate
y_pred = rf_model.predict(X_test)

print("✅ New Model Accuracy:", accuracy_score(y_test, y_pred))
print("🔍 Updated Classification Report:\n", classification_report(y_test, y_pred))

# ✅ Save model & vectorizer
os.makedirs("models", exist_ok=True)
pickle.dump(rf_model, open("models/outcome_classifier.pkl", "wb"))
pickle.dump(tfidf, open("models/tfidf_vectorizer.pkl", "wb"))

print("🚀 Improved Model & vectorizer saved successfully!")
