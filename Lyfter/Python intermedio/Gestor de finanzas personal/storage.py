import json
import os

base_data_file = 'finanzas_data.json'

def storage_data(categories, transactions):
    data = {
        "categories": categories,
        "logic": [{"type": t.type, "category": t.category, "amount": t.amount} for t in transactions]
    }
    with open(base_data_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def load_data():
    if not os.path.exists(base_data_file):
        return [], []
    
    try:
        with open (base_data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            category = data.get("categories", [])
            from models import transaction
            transactions = [{"type": t.type, "category": t.category, "amount": t.amount} for t in data.get("Transactions", [])]
            return category, transaction
    except Exception:
        return [], []