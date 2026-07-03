import json
import os
from models import Transaction

DIRECTORIO_SCRIPT = os.path.dirname(os.path.abspath(__file__))
base_data_file = os.path.join(DIRECTORIO_SCRIPT, 'finanzas_data.json')

def storage_data(categories, transactions):
    data = {
        "categories": categories,
        "transactions": [
            {
                "title": t.title, 
                "type": t.type, 
                "category": t.category, 
                "amount": t.amount
            } 
            for t in transactions
        ]
    }
    with open(base_data_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def load_data():
    if not os.path.exists(base_data_file):
        return [], []
    
    try:
        with open(base_data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            loaded_categories = data.get("categories", [])
            raw_transactions = data.get("transactions", [])
            
            loaded_transactions = []
            for t in raw_transactions:
                title = t.get("title", "Sin título")
                t_type = t.get("type", "Expense")
                category = t.get("category", "")
                amount = t.get("amount", 0.0)
                

                obj_transaction = Transaction(t_type, category, amount, title)
                loaded_transactions.append(obj_transaction)
                
            return loaded_categories, loaded_transactions
    
    except json.JSONDecodeError as jde:
        print(f"[ERROR CRÍTICO] El archivo '{base_data_file}' está corrupto o mal formateado.")
        print(f"Detalle técnico del JSON: {jde}")
        print("La aplicación iniciará vacía para proteger la ejecución, pero se sugiere revisar el archivo.")
        return [], []
        
    except PermissionError:
        print(f"[ERROR DE SISTEMA] No se tienen permisos de lectura para el archivo '{base_data_file}'.")
        return [], []
        
    except Exception as e:
        print(f"[ERROR INESPERADO] Ocurrió un problema imprevisto al cargar los datos: {type(e).__name__} - {e}")
        return [], []       