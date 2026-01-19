import os
import json
import re

RAW_TEXT_DIR = "data/raw_text"
CLAUSE_DIR = "data/processed/clauses"

os.makedirs(CLAUSE_DIR, exist_ok=True)

def split_into_clauses(text):
    # naive split on periods + line breaks
    raw_clauses = re.split(r"\.\s+|\n", text)
    clauses = [c.strip() for c in raw_clauses if len(c.strip()) > 40]
    return clauses

for filename in os.listdir(RAW_TEXT_DIR):
    if not filename.endswith(".txt"):
        continue

    file_path = os.path.join(RAW_TEXT_DIR, filename)

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    clauses = split_into_clauses(text)

    clause_data = []
    for i, clause in enumerate(clauses, start=1):
        clause_data.append({
            "contract_id": filename.replace(".txt", ""),
            "clause_id": i,
            "clause_text": clause
        })

    output_name = filename.replace(".txt", "_clauses.json")
    output_path = os.path.join(CLAUSE_DIR, output_name)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(clause_data, f, indent=2)

    print(f"✅ Clauses created: {output_name}")
