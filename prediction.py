import pickle
import pandas as pd

# Load saved model & vectorizer
model = pickle.load(open("models/outcome_classifier.pkl", "rb"))
vectorizer = pickle.load(open("models/tfidf_vectorizer.pkl", "rb"))


# Function to predict outcome
def predict_outcome(judgment_text):
    # Transform text using the saved vectorizer
    text_vector = vectorizer.transform([judgment_text])

    # Predict using the trained model
    prediction = model.predict(text_vector)[0]

    # Convert output to readable format
    outcome_label = "Plaintiff Wins ✅" if prediction == 1 else "Defendant Wins ❌"

    return outcome_label


# Example usage
new_text = "The appeal is granted and the petitioner shall be entitled to relief."
prediction = predict_outcome(new_text)

print(f"Predicted Outcome: {prediction}")
