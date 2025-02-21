import pandas as pd

# Example test cases
test_cases = [
    {"filename": "case_1.pdf", "text": "The petition is allowed. The plaintiff wins.", "actual_outcome": 1},
    {"filename": "case_2.pdf", "text": "The appeal is rejected. The case is dismissed.", "actual_outcome": 0},
    {"filename": "case_3.pdf", "text": "Matter remanded back to the lower court.", "actual_outcome": None},
    {"filename": "case_4.pdf", "text": "The respondent is liable for damages.", "actual_outcome": 1},
    {"filename": "case_5.pdf", "text": "Petition dismissed. Costs imposed on petitioner.", "actual_outcome": 0},
]

# Convert to DataFrame
df = pd.DataFrame(test_cases)

# Save to CSV
df.to_csv("data/test_cases.csv", index=False)

print("✅ Sample test_cases.csv created in data/")
