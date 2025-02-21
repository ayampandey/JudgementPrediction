# import os

# pdf_folder = "data/pdfs/"
#
# for file in os.listdir(pdf_folder):
#     file_path = os.path.join(pdf_folder, file)
#     if os.path.getsize(file_path) == 0:
#         print(f"Empty file detected: {file}")

# import fitz  # PyMuPDF
# import os
# import pandas as pd
#
# pdf_folder = "data/pdfs/"
# output_csv = "data/judgment_texts.csv"
# log_file = "data/skipped_files.txt"
#
# pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
#
# data = []
# skipped_files[]
#
# for pdf_file in pdf_files:
#     pdf_path = os.path.join(pdf_folder, pdf_file)
#
#     # Skip empty files
#     if os.path.getsize(pdf_path) == 0:
#         print(f"Skipping empty file: {pdf_file}")
#         continue
#
#     try:
#         with fitz.open(pdf_path) as doc:
#             text = ""
#             for page in doc:
#                 text += page.get_text("text")
#
#             data.append({"filename": pdf_file, "text": text})
#
#     except Exception as e:
#         print(f"Error reading {pdf_file}: {e}")
#
# df = pd.DataFrame(data)
# df.to_csv(output_csv, index=False)
#
# print(f"Extracted text from {len(df)} valid PDFs and saved to {output_csv}")

import fitz  # PyMuPDF
import os
import pandas as pd

# File paths
pdf_folder = "data/pdfs/"
output_csv = "data/judgment_texts.csv"
log_file = "data/skipped_files.txt"

# Get all PDF files
pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]

data = []
skipped_files = []  # List to store skipped file names

for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_folder, pdf_file)

    # Skip empty files
    if os.path.getsize(pdf_path) == 0:
        print(f"Skipping empty file: {pdf_file}")
        skipped_files.append(f"{pdf_file} - Empty File")
        continue

    try:
        with fitz.open(pdf_path) as doc:
            text = ""
            for page in doc:
                text += page.get_text("text")

            # Check if extracted text is empty (likely a scanned image)
            if not text.strip():
                print(f"Skipping scanned PDF (no text): {pdf_file}")
                skipped_files.append(f"{pdf_file} - Scanned Image")
                continue

            # Save extracted text
            data.append({"filename": pdf_file, "text": text})

    except Exception as e:
        print(f"Error reading {pdf_file}: {e}")
        skipped_files.append(f"{pdf_file} - Error: {e}")

# Save extracted data to CSV
df = pd.DataFrame(data)
df.to_csv(output_csv, index=False)

# Save skipped files log
with open(log_file, "w") as log:
    for skipped in skipped_files:
        log.write(skipped + "\n")

print(f"✅ Extracted text from {len(df)} valid PDFs and saved to {output_csv}")
print(f"🚀 Skipped {len(skipped_files)} files. Log saved in {log_file}")

